# MS-4019 Repository — Copilot Instructions

Reference repo for the Microsoft training course **MS-4019: Transform your everyday business processes with agents**. It holds course-landing material plus self-contained, dated **demo packages** (Python file generators + PowerShell Microsoft Graph seeders + Markdown step-by-step scripts). There is no application code, no test suite, and no linter — content correctness is verified by running the generators/seeders against an M365 tenant.

Documentation, prompts, file names, and console output are written in **Traditional Chinese (zh-TW)**. Match that language when editing or adding scenario / step / Demo material; only this `copilot-instructions.md` and engine code/comments are in English.

## Repository layout

- `README.md` — public course landing page (links, training key, video catalogue). Edits here are user-facing.
- `DEMO/<YYYYMMDD>-<Customer>/` — one folder per delivered class. Each is a self-contained, fully reproducible demo package. Treat folders other than the one you've been asked about as **frozen historical deliverables** — do not refactor across them.
  - `20250909-MOMO/` — Momoshop demo (single `DEMO-SCRIPT.md`, two sample `.xls/.xlsx` files).
  - `20260515-Cathy/` — **Cathay Financial Holdings** package; the active and most elaborate one. See "Cathay package conventions" below.
- `DEMO/Prompt Guides/` — flat list of M365 Copilot agent names referenced from the scripts.
- `.github/skills/` — committed skill packs available to the cloud agent: `git-commit` (Conventional Commits) and `github-issues` (issue management via `gh api` + GitHub MCP). Read `SKILL.md` before using them.
- `.vscode/mcp.json` — wires up two MCP servers: `github` and `microsoft-learn` (`https://learn.microsoft.com/api/mcp`). Use the Microsoft Learn MCP for any course-content lookups.
- `.gitignore` — currently only covers Terraform artefacts (see "Secrets" below for an important caveat).

## Cathay package conventions (`DEMO/20260515-Cathy/`)

This is where most active work happens. It bundles four artefact families:

1. **Markdown scripts** — `00_…整體授課流程.md`, `01_…檔案類型與用途說明.md`, `場景一_…` … `場景六_…`, plus the package `README.md`. These are the source of truth for demo flow; keep them in sync when you change generated files or seed JSON.
2. **Demo file generators** — three Python scripts produce 34 files into the local `DEMO-FILE/` directory:
   - `create_word_files.py` → 14 `.docx`
   - `create_excel_files.py` → 10 `.xlsx` (deliberately split: 5 raw tables + 5 pre-built dashboards)
   - `create_pptx_files.py` → 10 `.pptx` (5 完整版 + 5 半成品 with `💡【此處待補：請用 Copilot 補上 X】` placeholders)
   - Re-run the relevant script after edits; outputs are not committed except via the seeder.
3. **Graph seed data** — JSON under `seed-data/scenarios/cathay-ms4019/` (`emails.json`, `teams-messages.json`, `calendar-events.json`, `meeting-chats.json`, `sharepoint-sites.json`, `files-manifest.json`, `user-profiles.json`).
4. **Reusable PowerShell engines** — `seed-data/engine/Invoke-Seed*.ps1` and `Connect-GraphApp.ps1`. Engines are scenario-agnostic: they take a `-ConfigPath` and a data-file path and are dot-sourced from `run.ps1`. Any new seeding capability belongs as a new `Invoke-Seed*.ps1` engine plus a phase block in `run.ps1`, not inline in the scenario script.

### File-naming pattern

Scenario assets are prefixed `S1_` … `S5_` for Modules 2/3b scenarios and routed into matching OneDrive subfolders via `files-manifest.json`. New scenario files **must** keep the `S<N>_<topic>.<ext>` prefix and be added to both the relevant Python generator and `files-manifest.json` (with either `subfolder` field or path-prefixed `localName`).

### Account discipline (鐵律)

All demo flows assume **only `admin@moneyyu.com` is ever used to log in**. Persona names (`ChristieC@moneyyu.com`, `LidiaH@…`, `IrvinS@…`, `IsaiahL@…`, `JohannaL@…`, `JoniS@…`) appear only as **story characters in prompt text** — never as login instructions. When writing new scenario steps, phrase them as "我（admin）正在協助 Christie 準備…", never "請用 Christie 帳號登入…". The role→UPN map lives in `seed-data/scenarios/cathay-ms4019/config.json` under `roles`.

### Branding

Cathay assets use deep green `#006633` (`CATHAY_GREEN`) + gold `#CC9933` (`CATHAY_GOLD`), font **Microsoft JhengHei**. Helpers `set_cell_shading`, `styled_table`, `add_title` in `create_word_files.py` already enforce this — reuse them rather than open-coding new styling.

### Idempotency contract for the seeder

`run.ps1` executes 7 phases in order. The idempotency model differs per phase and must be preserved:

- **Phase 1 (user profiles)** — overwrites JobTitle/Department.
- **Phase 2 (OneDrive upload)**, **Phase 7 (SharePoint sites/lists/items)** — fully idempotent; safe to rerun.
- **Phase 3 (emails)**, **Phase 4 (Teams messages)** — **not idempotent**; reruns create duplicates / a new team. Document this whenever you add a similar phase.
- **Phase 5 (calendar)**, **Phase 6 (meeting chats)** — re-anchored to "today" via `dayOffset` on every run; this is intentional ("course-day rebasing"). Time fields in JSON should stay relative offsets, not absolute timestamps.

If you add a phase, follow the existing `Invoke-SeedSharePoint.ps1` pattern: GET-filter-then-POST per entity, App-only Graph permissions, and clearly state required scopes in the script header.

## Build, run, and verify

There are no unit tests or linters in this repo. The "build" is regenerating files; the "test" is running the seeder against the demo tenant.

**Python deps (one-time):**

```powershell
pip install python-docx openpyxl python-pptx
```

**Regenerate demo files (run individually after edits):**

```powershell
cd DEMO\20260515-Cathy
python create_word_files.py     # → DEMO-FILE\*.docx
python create_excel_files.py    # → DEMO-FILE\*.xlsx
python create_pptx_files.py     # → DEMO-FILE\*.pptx
```

There is no "single test"; to verify just one scenario, regenerate and inspect only its `S<N>_*` outputs in `DEMO-FILE/`.

**Run the M365 seeder (must be outside VS Code Terminal — use a standalone PowerShell window):**

```powershell
cd DEMO\20260515-Cathy\seed-data\scenarios\cathay-ms4019
.\run.ps1                              # default: -Industry cathay-financial
```

To test a single phase, dot-source the engine directly with the same args `run.ps1` uses, e.g.:

```powershell
. ..\..\engine\Connect-GraphApp.ps1 -ConfigPath .\config.json
. ..\..\engine\Invoke-SeedSharePoint.ps1 -ConfigPath .\config.json -SharePointPath .\sharepoint-sites.json
```

Required Microsoft Graph **Application** permissions are listed in the package `README.md` under "App Permission 必備清單" and in each engine's header comment. Phase 7 specifically needs `Sites.Manage.All` + `Sites.ReadWrite.All`.

## Secrets — important

`DEMO/20260515-Cathy/seed-data/scenarios/cathay-ms4019/config.json` holds the Azure App `clientSecret`. The package `README.md` states this is gitignored "via `**/scenarios/*/config.json`", but **`.gitignore` does not actually contain that rule** — only Terraform paths are ignored. The file happens to be untracked today; a careless `git add .` would commit the secret. Before staging anything inside `seed-data/scenarios/`, either add the missing rule to `.gitignore` or stage paths explicitly. Never commit `config.json`, and never echo `clientSecret` in PR descriptions or commit messages.

## Commit style

Use the `git-commit` skill (`.github/skills/git-commit/SKILL.md`) — Conventional Commits with type/scope/body, imperative mood, ≤72-char subject. Recent history shows mixed styles; new commits should follow the skill. Typical scopes seen here would be `cathay`, `seeder`, `docs`, `readme`.
