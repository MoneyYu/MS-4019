# MS-4019 國泰金控 Demo Data Seeder

> **課程**：MS-4019 Transform your everyday business processes with agents
> **客戶**：國泰金控（含人壽 / 世華銀行 / 投信 / 證券）
> **日期**：2026 年 5 月 15 日（五）
> **目的**：在 M365 tenant 注入 6 個跨子公司 demo 場景，預埋 Researcher / Analyst Agent 可消化的素材，並預建 3 個 SharePoint Sites 給 SharePoint Agent demo 使用

---

## ⚠️ Demo 帳號鐵律：admin@moneyyu.com

**全程只用 admin@moneyyu.com 登入**。所有 demo 操作（M365 Copilot、SharePoint、OneDrive、Teams、Outlook、Calendar、建立 Agent）一律從這個帳號出發。

| 動作 | 用哪個帳號？ |
|---|---|
| 講師現場 demo 登入 M365 | **admin@moneyyu.com** |
| 開啟 OneDrive、Outlook、Calendar、Teams、SharePoint | **admin@moneyyu.com** |
| 在 Copilot Chat 跑 Researcher / Analyst Agent | **admin@moneyyu.com** |
| 建立 SharePoint Agent / Copilot Chat Agent | **admin@moneyyu.com**（admin 是 site owner，自然有權限）|
| 寄出新 email、發 Teams 訊息（demo 過程） | **admin@moneyyu.com** |
| 分享 Agent 給其他角色 | **僅展示 UI，不實際送出** |

> ⚠️ **絕對不要**在 demo 步驟書中寫「請用 ChristieC 帳號登入...」之類的指令 — 講師沒有那些帳號的密碼。
>
> ✅ **正確寫法**：「我（admin）正在協助 Christie 準備...」 — 角色僅出現在 prompt 內容，不影響登入。
>
> 完整解釋見 [01_Demo檔案類型與用途說明.md](01_Demo檔案類型與用途說明.md) 「帳號使用鐵律」段。

---

## 📦 內容物總覽

| 類別 | 數量 | 位置 |
|---|---|---|
| Demo 檔案（Word） | 14 | `DEMO-FILE/` |
| Demo 檔案（Excel） | 10 | `DEMO-FILE/`（5 純表格 + 5 預製分析）|
| Demo 檔案（PPT） | 10 | `DEMO-FILE/`（5 完整 + 5 半成品）|
| Email Threads | 5 | `seed-data/scenarios/cathay-ms4019/emails.json` |
| Teams Channels | 1 team + 5 channels | `seed-data/scenarios/cathay-ms4019/teams-messages.json` |
| Calendar Events | 10 | `seed-data/scenarios/cathay-ms4019/calendar-events.json` |
| Meeting Group Chats | 5 | `seed-data/scenarios/cathay-ms4019/meeting-chats.json` |
| **SharePoint Sites（NEW）** | **3 個** | `seed-data/scenarios/cathay-ms4019/sharepoint-sites.json` |
| **SharePoint Lists** | **9 個（每 site 3 個）** | 同上 |
| **SharePoint List Items** | **~92 條** | 同上 |
| **總計 demo 檔案** | **34** | |

---

## 🎯 6 個 Demo 場景

| # | 場景 | 主角（故事設定）| MS-4019 模組 |
|---|---|---|---|
| 1 | 國泰人壽 — 長照新商品開發 | Christie + Lidia + Irvin | M2 Researcher / Analyst |
| 2 | 國泰世華 + 投信 — 財富管理 | Joni + Isaiah + Lidia | M2 Researcher / Analyst |
| 3 | 國泰金控 — 法遵與風險管理 | Johanna + Irvin + Lidia | **M3b** SharePoint Agent |
| 4 | 跨子公司 — 數位轉型 PMO | Christie + Isaiah + Lidia | **M3b** SharePoint Agent |
| 5 | 國泰金控 + 投信 — 永續金融 ESG | Joni + Johanna + Lidia | M4 Share & Use |
| **6** | **集團專案查詢助理** | **admin（PMO 視角）** | **M3a Copilot Chat Agent Builder 🆕** |

> 場景 6 是 MS-4019 Module 3 前半（**官方份量最重的單元**）的對應 demo。

詳細 demo 步驟請見：

- [00_MS4019_整體授課流程.md](00_MS4019_整體授課流程.md)
- [01_Demo檔案類型與用途說明.md](01_Demo檔案類型與用途說明.md)
- [場景一_長照新商品開發_Demo步驟.md](場景一_長照新商品開發_Demo步驟.md)
- [場景二_財富管理投資建議_Demo步驟.md](場景二_財富管理投資建議_Demo步驟.md)
- [場景三_法遵與風險管理_Demo步驟.md](場景三_法遵與風險管理_Demo步驟.md)
- [場景四_跨子公司數位轉型_Demo步驟.md](場景四_跨子公司數位轉型_Demo步驟.md)
- [場景五_永續金融ESG_Demo步驟.md](場景五_永續金融ESG_Demo步驟.md)
- [場景六_AgentBuilder_Demo步驟.md](場景六_AgentBuilder_Demo步驟.md) 🆕

---

## 👥 角色映射（沿用金融事業處 6 帳號）

| Cathay 身份 | UPN | 顯示名稱 | Title |
|---|---|---|---|
| 國泰金控 數位金融長 (CDO) | LidiaH@moneyyu.com | Lidia Holloway | 數位金融長 (CDO) |
| 國泰人壽 商品企劃協理 | ChristieC@moneyyu.com | Christie Cline | 商品企劃協理 |
| 國泰金控 風險管理副理 | IrvinS@moneyyu.com | Irvin Sayers | 風險管理副理 |
| 國泰世華 資深系統架構師 | IsaiahL@moneyyu.com | Isaiah Langer | 資深系統架構師 |
| 國泰金控 法遵稽核經理 | JohannaL@moneyyu.com | Johanna Lorenz | 法遵稽核經理 |
| 國泰投信 量化分析師 | JoniS@moneyyu.com | Joni Sherman | 量化分析師 |
| **觀察者 / Demo 操作帳號** | **admin@moneyyu.com** | **MOD Administrator** | **—** |

> 上述 6 個角色僅作 seed 資料的「故事人物」（寄信者、會議 organizer、Teams message author）；**所有 demo 操作一律用 admin** 登入。

---

## 🏛️ SharePoint 資產地圖

執行 `run.ps1` 後，admin@moneyyu.com 在 SharePoint 會看到 **4 個 site**：

| # | Site | 用途 | 內容 | 來源 Phase |
|---|---|---|---|---|
| 1 | 國泰集團 — MS-4019 Demo | 即時溝通 | Teams team site + 5 channels | Phase 4 |
| 2 | 國泰金控 — 法令遵循處 | 場景三 SharePoint Agent 知識庫 | 7 docs + 3 lists × 30 items | **Phase 7** |
| 3 | 國泰集團 — 數位轉型 PMO | 場景四 SharePoint Agent 知識庫 | 7 docs + 3 lists × 29 items | **Phase 7** |
| 4 | 國泰金控 — 永續金融委員會 | 場景五 SharePoint Agent 知識庫 | 6 docs + 3 lists × 33 items | **Phase 7** |

> **設計理念**：Teams team site = 即時對話現場；3 SharePoint sites = 部門定稿知識庫。對應真實企業中**通訊頻道與知識資產分離**的工作型態。
>
> 場景六 Copilot Chat Agent 同時連 OneDrive + 3 個 SharePoint sites + Web Search，呈現「跨來源」價值。

### Site 預建內容詳情

#### 🏛️ 國泰金控 — 法令遵循處（cathay-compliance）

- **Members**：admin（owner）+ Compliance、Risk、CDO
- **文件庫**：S3 系列 7 檔（與 OneDrive 雙存）
- **3 Lists**：
  - 法規異動追蹤（10 條，含 4/22 三大新規 + 過往歷史）
  - 稽核發現追蹤（10 條，含 2 重大 + 8 一般/改進）
  - AML STR 摘要（10 條，跨 4 子公司）

#### 🚀 國泰集團 — 數位轉型 PMO（cathay-digital-pmo）

- **Members**：admin（owner）+ Product、Architect、CDO、Risk
- **文件庫**：S4 系列 7 檔（與 OneDrive 雙存）
- **3 Lists**：
  - 專案 RAID Log（12 條，含 Goldman Marcus 失敗教訓 3 條）
  - 五大支柱 KPI 追蹤（7 條）
  - 跨子公司里程碑（10 條）

#### 🌱 國泰金控 — 永續金融委員會（cathay-esg）

- **Members**：admin（owner）+ Quant、Compliance、Risk、CDO
- **文件庫**：S5 系列 6 檔（與 OneDrive 雙存）
- **3 Lists**：
  - 氣候風險登記簿（5 條）
  - 投融資組合碳足跡監控（18 持股，含 ESG ETF）
  - 永續商品 / 綠色金融追蹤（10 條）

---

## 🔐 App Permission 必備清單（重要）

執行 `run.ps1` 需要 Azure App registration 已授權以下 Application permissions：

| Permission | Phase | 用途 |
|---|---|---|
| User.Read.All | 1 | 解析 user UPN → id |
| User.ReadWrite.All | 1 | 更新 JobTitle / Department |
| Mail.Send / Mail.ReadWrite | 3 | 發送 email thread |
| Calendars.ReadWrite | 5 | 建立 calendar events |
| Files.ReadWrite.All | 2、7 | OneDrive + SharePoint drive 上傳 |
| **Group.ReadWrite.All** | 4、**7** | 建立 Teams team + **M365 Group / SharePoint Site** |
| Teamwork.Migrate.All | 4、6 | Teams Migration API（歷史訊息）|
| ChannelMessage.Send / ReadWrite.All | 4 | Teams channel messages |
| Chat.Create / ReadWrite.All / ChatMessage.Send | 6 | Meeting group chats |
| **Sites.Manage.All** 🆕 | **7** | **建立 SharePoint List + Columns** |
| **Sites.ReadWrite.All** 🆕 | **7** | **建立 List Items（Phase 7 NEW）** |

> ⚠️ **Phase 7 是新增的 SharePoint 注入**，需驗證 `Sites.Manage.All` 與 `Sites.ReadWrite.All` 是否已授權。
>
> 若試跑 Phase 7 出現 401/403，請到 Azure Portal → App registrations → 對應 App → API permissions → Add permission → Microsoft Graph → Application permissions，加上述兩個權限並 Grant admin consent。

---

## 🚀 執行步驟

### 第一次設定（已完成）

```powershell
# 安裝 Python 依賴
pip install python-docx openpyxl python-pptx
```

### 步驟 A：產生 Demo 檔案（一次性，已完成）

```powershell
cd 20260515-Cathy
python create_word_files.py    # → 14 個 .docx
python create_excel_files.py   # → 10 個 .xlsx
python create_pptx_files.py    # → 10 個 .pptx
```

### 步驟 B：注入 M365 資料（**5/15 課前 4-24 小時執行**）

**重要**：在外部 PowerShell 執行（**非 VS Code Terminal**），以避免互動問題：

```powershell
cd 20260515-Cathy\seed-data\scenarios\cathay-ms4019
.\run.ps1
```

`run.ps1` 預設使用 `cathay-financial` industry profile，依序執行 7 個 phase：

```
Phase 0: Connect — App token
Phase 1: Update user profiles (cathay-financial)
Phase 2: Upload files to OneDrive
Phase 3: Seed Outlook email threads
Phase 4: Seed Teams channels + messages (Migration API)
Phase 5: Seed calendar events (dayOffset 對齊執行日)
Phase 6: Seed meeting group chats (Migration API)
Phase 7: Seed SharePoint Sites (M365 Group + Doc Library + 3 Lists × items per site) 🆕
```

預計耗時：12-20 分鐘（Phase 7 約佔 5-8 分鐘，含 site provisioning 等待）。完成後等待 4-24 小時讓 Copilot 完成索引。

---

## ✅ 執行後驗證

用 `admin@moneyyu.com` 登入 M365，逐一檢查：

| 項目 | 預期 | 位置 |
|---|---|---|
| Outlook | 5 個 email thread（含 admin CC） | Inbox |
| Calendar | 10 個 events（執行日 -7 ~ +3） | Calendar |
| Teams | 「國泰集團 — MS-4019 Demo」team + 5 channels | Teams |
| Chat | 5 個 meeting group chat（多用戶頭像） | Chat |
| OneDrive | `Cathay-MS4019/` 下含 6 個子資料夾共 34 檔 | admin 的 OneDrive |
| **SharePoint** | **4 個 site（1 Teams + 3 預建）** | **SharePoint Home** |
| SharePoint sites | 各有 6-7 docs + 3 lists + items | 各 site 主頁 |
| 6 帳號 JobTitle | 已切換為國泰子公司身份 | 各使用者 profile |

---

## 🔄 重跑機制

### 為什麼需要重跑？

`calendar-events.json` 與 `meeting-chats.json` 中的時間軸是用 `dayOffset` 表示（相對於執行當日的偏移）。**每次執行 `run.ps1` 都會用「當下日期」重新計算**，因此：

- ✅ Calendar 與 Meeting Chat **每次重跑時間都會自動對齊** 到執行日 -7 ~ +3
- ⚠️ Email、Teams 訊息**會重複建立**（首次後再執行會出現重複）
- ✅ **Phase 7 SharePoint 全 idempotent** — 重跑會跳過已存在的 site / list / item，不會重複

### 課前重跑建議

5/15 上課當天前一日（5/14）執行：

```powershell
cd 20260515-Cathy\seed-data\scenarios\cathay-ms4019
.\run.ps1
```

如需先清理舊資料：

1. **手動清理**：在 admin@moneyyu.com 帳號中手動刪除 5/14 之前的舊事件
2. **接受重複**：如時間緊迫可接受 email/teams 重複（不影響課程演示）
3. **SharePoint**：不需清理（idempotent）

### 多場景共存

本 demo 會建立新的 team「國泰集團 — MS-4019 Demo」與 3 個新 SharePoint site，與既有的 AB730 / MS4018 共存無衝突（不同 displayName / mailNickname）。但 6 個帳號的 JobTitle/Department 會被覆寫為國泰身份，如需切回 MS4018 請執行：

```powershell
cd MS4018-Tmnewa\seed-data\scenarios\tokiomarine-ms4018
.\run.ps1 -Industry financial
```

---

## 📂 檔案結構

```
20260515-Cathy/
├── README.md                              # 本檔
├── 00_MS4019_整體授課流程.md
├── 01_Demo檔案類型與用途說明.md            # NEW
├── 場景一_長照新商品開發_Demo步驟.md
├── 場景二_財富管理投資建議_Demo步驟.md
├── 場景三_法遵與風險管理_Demo步驟.md
├── 場景四_跨子公司數位轉型_Demo步驟.md
├── 場景五_永續金融ESG_Demo步驟.md
├── 場景六_AgentBuilder_Demo步驟.md          # NEW
├── create_word_files.py                   # 14 docx 生成
├── create_excel_files.py                  # 10 xlsx 生成
├── create_pptx_files.py                   # 10 pptx 生成
├── DEMO-FILE/                             # 34 個檔案（扁平）
└── seed-data/
    ├── engine/                            # 8 支 PowerShell 引擎
    │   ├── Connect-GraphApp.ps1
    │   ├── Invoke-SeedCalendar.ps1
    │   ├── Invoke-SeedEmails.ps1
    │   ├── Invoke-SeedMeetingChats.ps1
    │   ├── Invoke-SeedTeamsChannel.ps1
    │   ├── Invoke-SeedUserProfiles.ps1
    │   ├── Invoke-UploadFiles.ps1         # 支援子資料夾
    │   └── Invoke-SeedSharePoint.ps1      # NEW
    └── scenarios/cathay-ms4019/
        ├── config.json                    # ⚠️ 含 secret，已 gitignore
        ├── run.ps1                        # 一鍵執行 7 phase
        ├── user-profiles.json             # cathay-financial industry
        ├── files-manifest.json            # 34 檔對應 OneDrive 路徑（含 subfolder）
        ├── emails.json                    # 5 thread
        ├── teams-messages.json            # 1 team + 5 channel
        ├── calendar-events.json           # 10 events
        ├── meeting-chats.json             # 5 group chat
        └── sharepoint-sites.json          # NEW — 3 sites + 9 lists + items
```

---

## 🔐 機密資訊

`seed-data/scenarios/cathay-ms4019/config.json` 包含 Azure App Client Secret，已被 `.gitignore`（透過 `**/scenarios/*/config.json` 規則）。**不可 commit**。

---

## 🔗 相關文件

- 主 SKILL：`.github/skills/m365-demo-data-seeding/SKILL.md`
- 工作區指南：根目錄 `AGENTS.md`
- AB730 / MS4018 已驗證的 Engine 細節參見 [memory: ab730-conventions.md](#)

---

## 🛟 故障排除

| 症狀 | 可能原因 | 解法 |
|---|---|---|
| Phase 0 連線失敗 401 | clientSecret 過期 | 在 Azure Portal 重新產生並更新 config.json |
| Phase 2 OneDrive 上傳失敗 | DEMO-FILE 缺檔 | 重跑 3 支 Python 腳本 |
| Phase 4 Teams Migration 卡住 | 既有 team displayName 衝突 | 先在 admin@moneyyu.com 手動刪除既有 team |
| **Teams / SharePoint site 在 admin 帳號看不到** | **資源已從先前 run 存在，engine 不會 retro-fit admin** | **跑 SKILL 「Post-Run Verification」段的 PowerShell 補上 admin 為 owner+member**（見 `.github/skills/m365-demo-data-seeding/SKILL.md`）|
| Phase 6 Chat 未顯示頭像 | createdDateTime 過舊 | dayOffset 計算 OK，重跑即可 |
| **Phase 7 401/403** | **缺 `Sites.Manage.All` / `Sites.ReadWrite.All`** | **Azure Portal 加 permission + Grant admin consent**|
| Phase 7 site provisioning timeout | M365 Group 建好但 SharePoint 慢 | 等 1 小時後重跑（idempotent 不會重建）|
| Calendar 顯示 UTC 時區 | events.json 未指定 timezone | 已預設 Asia/Taipei，無需處理 |

---

## 📝 已知限制

- **Teams 訊息會重複**：再執行 `run.ps1` 不會清舊訊息，會新建另一個 team
- **Email 會重複**：再執行會增加新郵件，不會更新
- **Calendar / Chat dayOffset 會重新對齊**：這是 feature，不是 bug
- **SharePoint 全 idempotent**：重跑會跳過既有，不重複
- **PPT 圖表渲染**：python-pptx 不直接生圖表，預製分析的圖表在 Excel 中（Copilot 在 PPT demo 時會即時生成）

## 🆕 OneDrive 子資料夾支援

`Invoke-UploadFiles.ps1` 已支援多層子資料夾，使用 `subfolder` 欄位將檔案分群。詳見 [files-manifest.json](seed-data/scenarios/cathay-ms4019/files-manifest.json)。

```jsonc
// 方式 1：localName 內嵌路徑
{ "localName": "S1/file.docx" }

// 方式 2（本案採用）：本地扁平、OneDrive 分群
{ "localName": "file.docx", "subfolder": "S1_國泰人壽_長照新商品" }
```
