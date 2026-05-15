# 場景六：Copilot Chat Agent Builder — 集團專案查詢助理 Demo 步驟

> **MS-4019 對應**：**Module 3a（Build and manage an agent — Copilot Chat 部分，官方份量最重的單元）**
> **時長**：30 分鐘
> **操作帳號**：⚠️ **admin@moneyyu.com**（唯一登入帳號，全程不切換）
> **核心對比**：與場景三、四、五的 SharePoint Agent 形成「Copilot Chat Agent vs SharePoint Agent」教學對照

---

## 場景背景（30 秒講師開場）

> 「admin 是國泰金控數位金融處的 demo 操作者。今天你（admin）同時要追蹤集團 5 個專案：
>
> 1. 長照新商品『安心久久』（Christie 主導）
> 2. 2026 Q3 投資觀點月報（Joni 主導）
> 3. 金管會 4/22 三大新規應變（Johanna 主導）
> 4. 2026-2028 數位轉型藍圖（Christie + Isaiah）
> 5. 2025 TCFD 揭露報告（Joni + Johanna）
>
> 這 5 個專案的素材**散落在 OneDrive、3 個 SharePoint Site、5 個 Teams Channel 與多封 email**。
>
> 我們先試問內建的 Researcher Agent — 一次只能查一個主題。但如果你想要「**一句話跨 5 專案**」的查詢能力，就需要**自己建一個 Custom Agent**。
>
> 這就是 MS-4019 Module 3a 的核心：**業務人員 no-code 在 Copilot Chat 內建立 Agent**。」

---

## Demo 5 步驟（30 min）

### Step 1（3 min）：開場 — 為什麼需要 Custom Agent

操作帳號：**admin@moneyyu.com**（已登入 M365）

打開 M365 Copilot Chat（`microsoft365.com/chat`），先試問內建 Researcher Agent：

```
請整合 OneDrive Cathay-MS4019/ 中所有 5 場景的資料，告訴我本週每個專案的進度與風險。
```

**預期觀察**：
- Researcher Agent 會盡力整合，但因為是「通用研究員」，不一定知道我們的場景結構（S1-S5）
- 回覆品質可能不一致，每次問還要重新解釋背景

**講師金句**：
> 「Researcher 是萬能但不專屬。如果同一個查詢你**每週都要做**，就值得建一個**屬於你的 Agent**。」

---

### Step 2（7 min）：建立 Agent — Agent Builder UI 操作

> 📌 **UI 註記**：以下操作以 2026 年 5 月 Agent Builder 介面為準。若 UI 微調，操作意圖 = 在 Copilot Chat 範圍建立 Custom Agent，含 Name / Description / Instructions / Starter Prompts / Knowledge。

#### 2.1 進入 Agent Builder

在 Copilot Chat 左側 Agent 面板找到 `+ Create agent`（或 `+ New agent`），開啟 Agent Builder。

#### 2.2 填入基本資訊

| 欄位 | 內容 |
|---|---|
| **Name** | `國泰集團 專案查詢助理` |
| **Description** | `跨 5 場景的集團專案 PMO 智能助理 — 整合 OneDrive、SharePoint、公開網路` |
| **Icon** | 上傳國泰金控 logo（或保留預設）|

#### 2.3 Instructions（複製貼上）

```
你是國泰金控集團的「專案查詢助理」，協助 admin（數位金融處 demo 操作者）追蹤 5 個專案：

1. S1 國泰人壽 — 長照新商品開發（Christie Cline 主導）
2. S2 國泰世華+投信 — 財富管理投資建議（Joni Sherman + Isaiah Langer 主導）
3. S3 國泰金控 — 法令遵循處（Johanna Lorenz + Irvin Sayers 主導）
4. S4 跨子公司 — 數位轉型 PMO（Christie + Isaiah + Lidia 主導）
5. S5 國泰金控+投信 — 永續金融 ESG（Joni + Johanna 主導）

當被問到任一個專案時，請依序：

【步驟 1】識別場景：從問題判斷屬於 S1-S5 哪個場景
【步驟 2】摘要：本週進度 / 本週風險 / 本週決策（每項 1-2 句）
【步驟 3】跨專案連結：找出與其他專案相關的資訊（如「金管會 4/22 新規同時影響 S1 與 S5」）
【步驟 4】下一步行動：提出 1 個明確、可執行的下一步建議

格式：
- 開頭給「TL;DR」3 句話
- 中間用表格或 bullet point
- 結尾「建議下一步」一句話

語氣：精準、戰略性、避免技術術語（業務人員可懂）。
若資料不足或不確定，請明確標示「待補」與資料來源建議。
```

#### 2.4 Starter Prompts（5 個對應 5 場景）

```
1. 長照新商品『安心久久』本週狀態？商審會準備到哪？
2. Q3 投資觀點月報的關鍵爭議是什麼？我作為 admin 該關注什麼？
3. 金管會 4/22 三大新規影響評估 — 哪個專案最緊急？
4. 2026-2028 數位轉型藍圖董事會提報需要我留意什麼？
5. 2025 TCFD 揭露報告 6/30 公布前還有什麼風險？
```

#### 2.5 Knowledge Sources

勾選以下三類來源（**這是場景六的 demo 重點 — 跨來源整合**）：

| 來源類型 | 具體內容 |
|---|---|
| **OneDrive Files** | `Cathay-MS4019/` 全部 6 子資料夾（34 個檔）|
| **SharePoint Sites** | `國泰金控 — 法令遵循處`、`國泰集團 — 數位轉型 PMO`、`國泰金控 — 永續金融委員會`（共 3 sites，由 Phase 7 預建）|
| **Web Search** | ✅ 啟用（讓 Agent 可整合金管會、Fed、TCFD 等公開最新資訊）|

#### 2.6 Save（**不要 Publish，先個人測試**）

按 `Save` → 左側 Agent 面板會出現「國泰集團 專案查詢助理」。

---

### Step 3（10 min）：跨 5 場景試問 + 觀察跨場景連結能力

#### 3.1 點 Starter Prompt 5 試跑

點擊 Starter Prompt 5「2025 TCFD 揭露報告 6/30 公布前還有什麼風險？」

**預期成果（觀察重點）**：
- ✅ TL;DR 3 句話
- ✅ 引用 OneDrive 中 `S5_2025TCFD揭露報告草稿.docx` 的具體段落
- ✅ 引用 SharePoint「國泰金控 — 永續金融委員會」中的氣候風險登記簿（5 條）
- ✅ Web Search 可能補上 ISSB IFRS S2 最新進展
- ✅ 結尾「建議下一步」明確可執行

#### 3.2 進階問：跨場景連結

```
請列出本週 5 個專案中『金管會 4/22 三大新規』的具體影響：
- 哪個專案最緊急（按合規時程）
- 哪些專案彼此相關（如 S1 ESG 附約 ↔ S5 TCFD 揭露）
- admin 應該優先關注哪一件？
```

**預期成果**：
- 找出 S1 長照新商品的 ESG 附約受外匯規範影響（合規 9/1）
- 找出 S5 TCFD 受永續揭露準則 2.0 影響（合規 2027/3）
- 找出 S4 集團 AI 應用受 AI 治理指引影響（12/1）
- 排出優先順序：**S1 最緊急**（9 月 → 距今 4 個月）

#### 3.3 與內建 Researcher Agent 對比

切回內建 Researcher Agent，問同樣問題。對比兩者：

| 維度 | 內建 Researcher | 集團專案查詢助理 |
|---|---|---|
| 對「S1-S5 場景」結構的認知 | ❌ 不知道 | ✅ 已內化 |
| 知識源範圍 | 只 OneDrive | OneDrive + 3 SharePoint + Web |
| 回覆格式 | 不固定 | 固定 TL;DR + 表 + 行動 |
| 跨場景連結能力 | 弱 | 強 |

**講師金句**：
> 「Researcher 給的是『資訊』，Custom Agent 給的是『**符合你工作流程的洞察**』。差別在 Custom Instructions。」

---

### Step 4（5 min）：分享給團隊（**只展示 UI，不實際送出**）

> ⚠️ **demo 注意**：分享步驟僅展示 UI 流程，**不真的送出**（admin 一個帳號看完整流程，避免實際打擾其他角色信箱）。

#### 4.1 點 `Share` 按鈕

打開分享面板，向學員展示三個分享選項：

| 選項 | 說明 |
|---|---|
| **Specific people** | 加 LidiaH / ChristieC / IsaiahL 等成員（個別授權） |
| **Anyone in your organization** | 全集團 admin@moneyyu.com 員工皆可使用 |
| **Copy link** | 產生分享連結 |

#### 4.2 演示 Web Search 開關差異

回到 Agent 編輯頁，**關閉 Web Search**，重問同一題（「TCFD 公布前風險」）：

**預期觀察**：
- 沒有 Web Search 時，回答只能基於 OneDrive + SharePoint 內已知資料
- ISSB IFRS S2 最新進展、同業最新揭露不會出現
- 適合「**內部敏感資料、避免外部洩露**」的場景

**講師金句**：
> 「金管會 4/22 AI 治理新規要求『**透明度** + **可解釋性**』。Web Search 開關決定 Agent 引用範圍，是治理的第一道控制。」

#### 4.3 重新打開 Web Search

`Save` 收尾。

---

### Step 5（5 min）：對比 SharePoint Agent + 結語

#### 5.1 與場景三/四/五的 SharePoint Agent 對比

打開場景三的 SharePoint Site（`國泰金控 — 法令遵循處`），展示「Add Agent」入口：

| 維度 | Copilot Chat Agent（場景六）| SharePoint Agent（場景三/四/五）|
|---|---|---|
| **建立位置** | Copilot Chat 左側 + | SharePoint 文件庫頂端 + Add agent |
| **知識源** | 自選（OneDrive / SP / Connector / Web）| 自動 = 該文件庫 + 自選擴充 |
| **Starter Prompts** | 必填（教學員寫好 prompt）| 自動生成 |
| **適合場景** | **跨來源、流程化、業務用** | **文件集中、團隊共用、知識庫式** |
| **分享機制** | 與特定人員 / 群組 / 組織 | 文件庫繼承權限 |
| **官方時長** | 36 min（Module 3a，**份量更大**）| 26 min（Module 3b）|

#### 5.2 結語

> 「**MS-4019 Module 3 教給你兩種能力**：
>
> - **Copilot Chat Agent**（場景六）→ **跨來源、流程化、業務用**（適合 PMO、跨子公司整合）
> - **SharePoint Agent**（場景三/四/五）→ **文件集中、團隊共用**（適合法遵知識庫、PMO 文件、ESG 揭露）
>
> 哪個適合你？取決於你的**問題**、**資料分布**、**團隊範圍**。
>
> 兩者都是 no-code，業務人員自己就能建。**這是這次課程最重要的解放**。」

---

## 學員 Q&A 提示

| 學員可能問 | 講師可回答 |
|---|---|
| Copilot Chat Agent 與 Copilot Studio Agent 有何差異？ | Agent Builder 完全 no-code、限制較多（不能串外部 API、不能在 Teams Chat 內呼叫）；Copilot Studio 可串 API + Actions，但需要更多技術 |
| 不能在 Teams Chat 內使用是什麼意思？ | Copilot Chat Agent 只能在 microsoft365.com/chat、office.com/chat、Teams 桌面/網頁版「Copilot」面板中呼叫，**不能在群組對話框直接 @ 它** |
| 多人共用同一個 Agent 怎麼計價？ | 使用 Agent 的人都需要 M365 Copilot license，**Agent 本身不計價**（包含在 license 內） |
| 金管會 AI 治理新規對 Custom Agent 的要求？ | 三條：(1) 知識源透明（誰建、引用什麼）；(2) 人類覆核（決策權在使用者）；(3) 可解釋性（Custom Instructions 開放查看） |
| Agent 答錯怎麼辦？ | 使用者責任 — 必審核、必驗證；Agent 是輔助不是決策。可在 Custom Instructions 強制要求「不確定處明確標示」 |
| 換 tenant 能搬遷 Agent 嗎？ | 目前 Agent Builder 沒有 export，但 Custom Instructions / Starter Prompts 可手動複製到新環境 |
| Web Search 引用的「最新資料」可信嗎？ | Agent 會標出處，但金融重大決策**必須人工 verify**（特別是法規、市場數據） |

---

## Knowledge Sources 對應預埋資料

### OneDrive `Cathay-MS4019/` 子資料夾（5 + 1 = 6）

| 子資料夾 | 對應場景 | 檔案數 |
|---|---|---|
| `S1_國泰人壽_長照新商品` | S1 | 7 |
| `S2_世華投信_財富管理` | S2 | 6 |
| `S3_金控_法遵與風險` | S3 | 7 |
| `S4_跨子公司_數位轉型` | S4 | 7 |
| `S5_金控投信_永續金融ESG` | S5 | 6 |
| `_跨場景共用` | 跨 | 1 |

### SharePoint Sites（3 個，由 Phase 7 預建）

| Site | 對應場景 | 文件 + Lists |
|---|---|---|
| `國泰金控 — 法令遵循處` | S3 | 7 docs + 3 lists（法規異動 / 稽核發現 / AML STR）|
| `國泰集團 — 數位轉型 PMO` | S4 | 7 docs + 3 lists（RAID Log / 五大支柱 KPI / 跨子公司里程碑）|
| `國泰金控 — 永續金融委員會` | S5 | 6 docs + 3 lists（氣候風險 / 碳足跡 / 永續商品）|

### Web Search

啟用後可查詢：金管會、保險局、銀行局公開資訊；Fed、ECB、BOJ 政策利率；TCFD / ISSB 最新框架；同業（玉山金、富邦金、中信金）公開揭露等。

---

## 場景六的教學亮點

1. **三層知識整合**：OneDrive（個人）+ SharePoint（部門）+ Web（公開）— **這是其他 5 場景做不到的**
2. **Custom Instructions 注入企業文化**：「TL;DR + 表 + 行動」格式、不確定要標示 — 這就是「Agent 屬於你」
3. **Starter Prompts 教學員怎麼用**：5 個 prompt 等於「使用手冊」內建在 Agent 裡
4. **Web Search 開關 = 治理第一道控制**：呼應金管會 4/22 AI 治理新規
5. **與 SharePoint Agent 對比**：MS-4019 Module 3 兩半，業務人員可自選

---

## 場景六與其他場景的關係

```
場景六（Module 3a）= 跨 5 場景的「PMO 整合查詢」
    ↓
依賴：5 場景的 OneDrive + Phase 7 預建的 3 SharePoint sites
    ↓
受惠：admin 可一句話跨專案，省去手動跑 5 個地方
    ↓
延伸：學員可學會自己建立屬於自己角色的 Agent
```
