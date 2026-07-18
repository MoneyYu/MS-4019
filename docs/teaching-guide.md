<!--
本檔為講師備課用的「原創整理」，非 Microsoft 官方教材，亦非逐字轉載官方講師手冊/講者備忘/測驗解答。
所有外部連結請以 README.md 的「Links」與「Videos」為準（已逐一驗證）。
DEMO/ 內的封裝屬歷史交付範例，僅供示範參考，非官方課程內容。
-->

# MS-4019 備課指南（講師用）

> **MS-4019-A：Transform your everyday business processes with agents** — 教商務使用者用**無程式**方式，在 **Microsoft 365 Copilot Chat** 與 **SharePoint** 建立、管理、分享與使用 agent。
> 對象：一般商務使用者（無需寫程式）｜等級：Beginner｜時長：1 天｜完訓：**Achievement Code（無 Applied Skills 憑證、無認證考試）**
> 內容 as-of：2026-07（每次開課前請對照 MCT Download Center 的 **Change Log** 複查是否改版）
>
> ⚠️ **產品版本落差提醒**：本課投影片約為 2026 年初版本，而 Microsoft 365 Copilot／SharePoint agent 更新頻繁。**已知變更**：自 **2026/6 起，SharePoint agent 不再需要核准流程**，且**已支援將 Lists 與 Site Pages（ASPX）納入知識來源**。授課前請一律以 README「Links」中的**當前官方文件**為準，並實機確認 UI 與功能。

---

## 0. 課程速覽

- 全課只有**一條 Learning Path**（與課名同名），底下 **4 個內容模組** + 課程導論/複習/結論。
- **只有 M2、M3 有動手 Lab**；M1、M4 以影片與討論為主，無獨立 Lab。
- 採 **BYOS（Bring Your Own Subscription）**：學員用**自己的** Microsoft 365 Copilot 訂閱做 Lab，沒有虛構租戶。
- 課程投影片內嵌 **3 支官方短片**（M1、M3、M4 各一），每支後面都接一張討論投影片。

| 模組 | 主題 | 有無 Lab | 內嵌影片 | 建議時間 |
|---|---|:---:|:---:|:---:|
| 導論 | 課程/講師/學員介紹、對象與先決條件 | — | — | 30 分 |
| **M1** | Get started with agents（agent 是什麼、存取與授權、效益、IT 治理） | 無 | 有 | 60 分 |
| **M2** | Explore prebuilt agents（Analyst/Researcher/Prompt Coach/Idea Coach/Writing Coach） | 3 個 | — | 90 分 |
| **M3** | Build and manage an agent（Agent Builder 與 SharePoint 工具、測試/管理） | 2 個 | 有 | 120 分 |
| **M4** | Share and use agents（分享、Teams、互動） | 無 | 有 | 45 分 |
| 複習 | Learning Path 複習討論（投影片段落，非 Learn 模組） | — | — | 15 分 |
| 結論 | 回顧、成就兌換、後續課程 | — | — | 10 分 |

> 以上為投影片講授時間的估計，**不含**在課堂上做 Module Assessment 題目的時間；請依學員背景彈性調整。

---

## 1. 開課前檢查清單（Pre-class）

**講師自身準備**
- [ ] 讀過 4 個 Learn 模組全部單元，特別留意「新增/變更」項（對照 Change Log）。
- [ ] **親自跑過全部 5 個 Lab**（M2×3、M3×2），記下容易卡住的地方。
- [ ] 看過 3 支內嵌影片，準備好每支的 2–3 個引導討論問題。
- [ ] 檢視 Module Assessment 題目，能說明為何某答案正確（學員可能提出質疑）。

**環境與帳號（提醒學員）**
- [ ] 每位學員需有可用的 **Microsoft 365 Copilot** 存取權（BYOS）。
- [ ] 瀏覽器建議 **Microsoft Edge**；Copilot 入口 `https://m365.cloud.microsoft`。
- [ ] M3 SharePoint agent Lab：有自己的 SharePoint 站台最佳；**沒有站台者可用課程提供的 Fabrikam 模擬環境**。
- [ ] 提醒資料隱私：Researcher／Agent choice Lab 會用到**學員自己的** Outlook/OneDrive/Teams 資料，請勿使用機敏內容。

**UI／地區漂移提醒（很容易變）**
- Agent 在 Copilot 導覽列的位置、Agent Store 分類（「Built by Microsoft」）可能隨版本調整；找不到時走 **All agents → Agent Store**。
- Agent Builder 的 **Describe 頁籤**並非所有地區/語言都支援；不支援時改用 **Configure 頁籤**（功能完整）。
- prebuilt agent（如 Analyst/Researcher）的可用性依授權與推出進度而定，開課前一天再確認一次。

---

## 2. 逐模組教學重點

### M1 — Get started with agents（60 分）

**核心訊息**：agent 是嵌在 Copilot Chat／SharePoint 裡的 AI 助理；商務使用者自己就能建，但**資料治理是組織的責任**。

**必講談話點**
- **兩種入口的差異**（見 §3 授權速查）：Copilot Chat（人人可用、Web grounding、免額外費用）vs 完整 Microsoft 365 Copilot（授權、可存取工作資料/tenant Graph grounding）。
- **要讓 agent 讀「工作資料」的兩條路**：指派 M365 Copilot 授權，或為 Copilot Chat 使用者啟用**隨用隨付（Copilot Credits）**。
- **SharePoint agent 權限**：需 **Edit 以上**權限才能「建立」；只有 Read 權限者只能「使用」被分享的 agent；外部使用者預設視為 site visitor。
- **效益**（用一兩個例子帶過即可）：簡化例行工作、更好的搜尋、協作、個人化、安全/合規監控。
- **IT 治理**：政策、風險、存取控管、資料管理、稽核 — 強調「使用者建 agent、組織訂規則」。

**影片（M1）**：`Microsoft 365 Copilot | SharePoint agents`（README Videos 表內）。放完接討論投影片：問學員「這支片裡哪個情境最貼近你們的工作？」

**課堂互動**：討論投影片「Using agents in your organization」— 讓學員各舉一個可自動化的流程（10–15 分，討論熱烈就多給時間）。

**常見提問**
- 「Copilot Chat 免費版能不能建 agent？」→ 能，但只用 Web grounding；要讀公司資料需授權或 PAYG。
- 「agent 會不會看到我沒權限的檔案？」→ 不會，agent 一律**沿用既有權限**。

---

### M2 — Explore prebuilt agents（90 分，含 3 Lab）

**核心訊息**：prebuilt agent 開箱即用、不需設定，用自然語言就能操作。本模組重點在「**何時用哪一個**」。

**五個 agent 速查**（詳見 §4）：Analyst（資料分析、可跑 Python）、Researcher（深度研究、附引用、回應偏長）、Prompt Coach（改寫提示）、Idea Coach（腦力激盪）、Writing Coach（專業寫作）。

**Lab 檢查點與疑難排解**

| Lab | 目標 | 時間 | 常見卡點 / 回復 |
|---|---|:---:|---|
| L1 Analyst | 用 Analyst 分析 **Project Nexus 問卷**試算表 | ~15–20 分 | 需先下載官方範例 xlsx；Analyst 會**跑數個 Python 步驟**，請學員耐心等聚合結果；回應間可能有大片空白（已知顯示問題，往上捲即可看到結果）。 |
| L2 Researcher | 用 Researcher 跨 Outlook/OneDrive/Teams 彙整**自己的**資料 | ~20 分 | 複雜查詢**耗時較久**、回應常長達 8–10 頁 → **提醒學員追問「請摘要成重點」**。用自己資料，避免機敏內容。 |
| L3 Agent choice | 自選一個（非 Analyst/Researcher）prebuilt agent 解決近 90 天的實際工作 | ~15–20 分 | 鼓勵多試幾個 agent；此 Lab 目的在「看見 agent 的廣度」。 |

**示範建議**：可搭配 `DEMO/20260515-Cathy/`（財富管理、法遵、ESG 情境）或 `DEMO/20250909-MOMO/` 的範例檔展示 Analyst/Researcher（**這些為歷史示範素材，非官方教材，請視租戶現況調整**）。

---

### M3 — Build and manage an agent（120 分，含 2 Lab）

**核心訊息**：不用寫程式就能建 agent；**兩種建置工具、能力不同**，這是本模組最重要的觀念。

**必講談話點**
- **兩種工具**（見 §3 對比）：Copilot Chat 內的 **Agent Builder**（Copilot Studio 輕量版）vs **SharePoint 內建的 Copilot agent 工具**。
- **Agent Builder 的兩個頁籤**：**Describe**（用對話式自然語言，系統幫你產生指令；受地區/語言限制）vs **Configure**（手動逐欄設定，最完整）。兩者同步。
- **agent 元件**：圖示（.png，≤1MB）、名稱、描述、指令、**能力（Code interpreter／Image generator — 只有 Agent Builder 有，SharePoint 工具沒有）**、知識來源、建議提示。
- **SharePoint 工具的限制**：三個頁籤（Overview／Sources／Behavior）、無「能力」區、不能套模板、**不會像 Agent Builder 一樣跟你對話微調**（指令要一次寫清楚）、建議提示最多 3 個。

**影片（M3）**：`One-click AI Agents`（README Videos 03-02）。接討論投影片：問「建 SharePoint agent 時哪個功能最吸引你？」

**Lab 檢查點與疑難排解**

| Lab | 目標 | 時間 | 常見卡點 / 回復 |
|---|---|:---:|---|
| L1 Copilot Chat agent | 用 Agent Builder 建一個**自己感興趣**的 agent | ~25 分 | 無標準答案，鼓勵學員自訂主題；提醒**建完要測試**，再回頭調指令/知識來源/建議提示。 |
| L2 SharePoint agent | 用 SharePoint 工具建 agent | ~25 分 | **無 SharePoint 站台者→用 Fabrikam 模擬環境**（步驟相同）；強調指令要一次寫清楚。 |

**示範建議**：`DEMO/20260515-Cathy/場景六_AgentBuilder_Demo步驟.md` 可作為 Agent Builder 的完整示範腳本（歷史素材，請先自行走過一次）。

---

### M4 — Share and use agents（45 分）

**核心訊息**：建好的 agent 可分享給更多人，但**分享 agent ≠ 自動分享底層資料的權限**。

**必講談話點**
- **Copilot Chat 分享三選項**：組織內任何人／指定使用者（建議用**安全性群組**）／僅自己（預設）。
- **SharePoint 分享（注意：2026/6 起已變更）**：**不再需要核准流程**；具 **Edit** 權限的站台成員即可建立／編輯／分享 agent（`.agent` 檔），站台擁有者可為站台指定**主要 agent**。（投影片仍呈現舊的「站台擁有者/管理員核准」流程，授課時請說明已變更。）
- **重點觀念**：被分享者只能取用**他自己有權限**的知識來源；分享 agent 時**權限不會自動調整**，可能要另外調整資源的分享設定。被分享者**不能編輯** agent；agent 編輯後需**重新分享**對方才看得到最新版。
- **Teams**：用分享連結把 agent 帶進群組/頻道，以 **@提及** 互動。
- **互動重點**：agent 只用**你有權限且被列為來源**的內容回答；hub site 會連動其關聯站台；聊天記錄**僅自己可見**、可重新命名/刪除。（投影片說「不支援 Lists／Site Pages」，但**當前產品已支援**將 Lists 與 Site Pages（ASPX）納入來源——以官方文件為準。）

**影片（M4）**：`Leading engineering firm Amey keeps employees safer with SharePoint agents`（README Videos 04-02；課程投影片以「A real-life use case of using agents in SharePoint」呈現）。接討論投影片。

---

### 複習 + 結論（25 分）
- Learning Path 複習（投影片段落，**非 Learn 模組**）：快速回顧四模組重點。
- 結論：提醒兌換 **Achievement**、填問卷、介紹後續課程（見 §7）。

---

## 3. 授權 / 存取 / grounding 速查

| 面向 | Microsoft 365 Copilot **Chat**（內建/免費） | **完整** Microsoft 365 Copilot（授權） |
|---|---|---|
| 誰能用 | 具合格 M365/O365 授權者 | 已指派 Copilot 授權者 |
| grounding | **Web grounding**（透過 Bing 的公開資料） | 額外加 **Work grounding**（tenant Microsoft Graph：SharePoint/OneDrive/Teams） |
| 建 agent | 可（僅 Web grounding 免費） | 可（含存取工作資料） |
| 讀「工作資料」的 agent | 需**隨用隨付（Copilot Credits）** | 授權已內含、grounded 回應**不另計費** |
| 適用情境 | 建立「用 AI 的習慣」、起步 | 深度整合組織資料的完整體驗 |

> 組織可**混合**：部分人給完整授權、部分人用 PAYG；Copilot Credits 只在對租戶資料做 grounding 檢索時消耗。

**SharePoint agent 權限速查**：Edit↑＝可建可用；Read＝只能用被分享的；外部使用者預設為 visitor（除非被加為 member 或被指派授權）。

---

## 4. Prebuilt agents「何時用哪個」

| Agent | 一句話 | 最適用 | 講師提醒 |
|---|---|---|---|
| **Analyst** | 分析並視覺化你的工作資料 | 試算表/報表分析、找趨勢、產生圖表 | 支援執行 Python 程式碼（Code interpreter）、可跨檔關聯、尊重權限 |
| **Researcher** | 深度、有引用的研究彙整 | 跨來源找事實/趨勢、彙整長文件 | 多步驟深度推理、附來源引用；回應可能很長 → 追問「摘要重點」 |
| **Prompt Coach** | 幫你把提示寫得更好 | 提示改寫、疑難排解 | 適合剛上手 Copilot 的學員 |
| **Idea Coach** | 想法的 sounding board | 腦力激盪、壓力測試提案 | 會挑戰/擴展你的想法，不只說好 |
| **Writing Coach** | 專業寫作潤飾 | email/報告/簡報的清晰度與語氣 | 可依受眾調整風格 |

---

## 5. 對應現有 DEMO 素材（皆為歷史交付範例，非官方教材）

| DEMO 封裝 | 內容 | 可對應模組 |
|---|---|---|
| `DEMO/20260515-Cathy/`（國泰金控） | 六大情境（長照商品、財富管理、法遵風險、跨子公司轉型、ESG、**AgentBuilder**）+ Word/Excel/PPTX 產生器 + 完整授課流程 | M2（Analyst/Researcher 情境）、**M3（場景六 AgentBuilder）** |
| `DEMO/20250909-MOMO/`（Momoshop） | 講師版 PPTX、學員 Lab 指南、逐分流程、範例報表 | M2、M3 綜合示範 |
| `DEMO/Prompt Guides/` | Researcher、Analyst、Idea Coach、Writing/Career Coach、Word/Excel/PPT 的 Copilot 提示指南 | M2、M3 |

> 使用前請自行走過一次，並依當前租戶與 UI 現況調整；勿當成標準答案照本宣科。

---

## 6. 常見問題與踩雷（Q&A）

- **Q：學員沒有 Copilot 授權怎麼辦？** BYOS 是本課前提；無授權者無法完成多數 Lab，可改為觀摩講師示範。
- **Q：找不到 Analyst/Researcher agent？** 走 All agents → Agent Store →「Built by Microsoft」；部分 agent 依授權/推出進度而定。
- **Q：Describe 頁籤不見了？** 該地區/語言可能未支援，改用 Configure 頁籤（功能完整）。
- **Q：分享 agent 後對方看不到資料？** 分享 agent 不會自動給資料權限；需另行調整知識來源（檔案/資料夾/站台）的分享設定；建議用安全性群組。
- **Q：改了 agent 對方還是舊的？** 編輯後要**重新分享**才會更新；含 SharePoint 檔案/資料夾為來源時，重新分享給同一群組以保持一致。
- **踩雷：Researcher 回應太長**淹沒學員 → 一律教「追問摘要」。
- **踩雷：SharePoint 工具不對話** → 指令要一次寫完整，別期待它像 Agent Builder 會建議。

---

## 7. 延伸與後續課程

- 後續學習路徑（結論投影片建議）：**MS-4004**（Copilot 使用情境）、**MS-4017**（管理與擴充 Copilot）、**MS-4018**（用 Copilot 起草/分析/簡報）。（投影片另提及 MS-4007 使用者導入，但其 Learn 課程頁目前無法解析，故 README 未收錄。）
- 概念與服務的權威參考連結，一律以 **`README.md` 的 Links / Videos 區塊**為準（已逐一驗證、僅收官方連結）。
