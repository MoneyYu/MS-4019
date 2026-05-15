# 場景四：跨子公司 — 數位轉型 Demo 步驟

> **MS-4019 對應**：**Module 3b（Build and manage an agent — SharePoint Agent for PMO）**
> **時長**：30 分鐘（含 SharePoint Agent 建立）
> **主角（故事設定）**：Christie Cline（PMO）+ Isaiah Langer（IT 架構師）+ Lidia Holloway（CDO）
> **操作帳號**：⚠️ **admin@moneyyu.com**（全程唯一登入帳號，不切換；Christie/Isaiah/Lidia 僅為 **故事中的角色背景**，不是登入帳號）
> **SharePoint Site**：`國泰集團 — 數位轉型 PMO`（由 Phase 7 預建）

---

## 場景背景（30 秒講師開場）

> 「下週 Steering Committee（董事長親自主持），Lidia 要對董事會提報 2026-2028 三年數位轉型藍圖，總投資 53.7 億。
>
> 董事會會問三個尖銳問題：
> 1. 跟 DBS、JPMorgan、UBS 比，我們落後幾年？
> 2. 53.7 億 ROI 怎麼交代？
> 3. 客戶端有感的改變是什麼？
>
> 這三題分別需要：**最新 Fintech 同業研究**（Researcher）、**ROI 與 NPS 數據分析**（Analyst）、**跨子公司專案狀態整合**（SharePoint Agent）。」

---

## Demo 5 步驟

### Step 1：Researcher Agent — 升級 Fintech 同業 benchmark（7 min）

切換到 **Researcher Agent**：

```
我（admin）正在協助 Christie Cline（PMO 主導者）下週 Steering Committee 要對董事會提報數位轉型藍圖，董事會會問「跟 DBS、JPMorgan、UBS 比，我們落後幾年」。

請整合以下資訊：
1. OneDrive 中 S4_全球Fintech同業比較研究.docx 的九家公司比較
2. 公開網路最新（2026 Q1-Q2）資料：
   - DBS 4/2026 公布的「DBS Joi」客戶 GenAI 助理上線細節
   - JPMorgan 5/2026 IndexGPT 開放 RIA 使用的範圍
   - UBS 3/2026 hybrid advisor model 的營收影響
   - Goldman Marcus 收掉的最新檢討（為什麼失敗）

最後給董事會一段 200 字摘要，包含：
- 本集團整體落後 DBS / JPM 共幾年
- 雲端化、客戶 GenAI、Open API 三項落差量化
- 哪兩塊是「最該全力衝」的優先級
- 從 Goldman Marcus 失敗學到的三個教訓
```

**預期成果**：Researcher 整合 Word + 公開最新案例，呼應 Email thread 中 Isaiah 提到「整體落後 2-4 年」的結論。

---

### Step 2：Analyst Agent — NPS 旅程痛點分析（7 min）

切換到 **Analyst Agent**，附上 `S4_通路NPS月度原始.xlsx` + `S4_數位轉型KPI_Dashboard.xlsx`：

```
請基於這兩個檔案：

1. 從「通路月度使用」分頁，找出 4 個子公司中 NPS 最低的子公司 + 通路組合
2. 計算近 12 個月 NPS 趨勢，找出進步最大與退步最大的兩個子公司
3. 重點分析：把資料按「年齡層」與「子公司」交叉，找出國泰人壽 55 歲以上客戶 NPS 表現
4. 計算「保全旅程數位化」投資 1.8 億可帶來的具體效益（NPS 提升、年省工時、客戶流失減少）

最後產出：
- 一個「金句級」結論：適合放在 PPT 第 5 頁的 1 句話
- 一段 100 字的「給董事會的 NPS 改善承諾」
```

**預期成果**：Analyst 跑出 55+ 客戶變更 NPS 28（最低）這個關鍵痛點，呼應 Email thread 中 Christie 的發現。

---

### Step 3：用 Copilot 升級半成品 PPT（6 min）

打開 `S4_數位轉型藍圖_半成品.pptx`：

```
這是 5/17 Steering Committee 提報，請依序：

1. 第 1 頁三年策略目標：補上三年具體里程碑與投資金額（53.7 億 = 13.5 + 17.9 + 22.3）
2. 第 2 頁五大支柱 KPI：用「數位轉型KPI_Dashboard.xlsx」產出三年路徑表
3. 第 3 頁客戶旅程 NPS：用 Analyst Agent 剛才的「保全旅程」金句結論
4. 第 4 頁 Fintech benchmark：用 Researcher Agent 剛才的最新案例
5. 第 5 頁 ROI：計算三年累積投資、效益、淨現值（NPV）
6. **新增第 6 頁**：「Goldman Marcus 失敗教訓 — 我們要避開的三個坑」
```

---

### Step 4：建立『數位轉型 PMO』SharePoint Agent（8 min — Module 3b 主軸）

> **這是本場景的精華 — 跨子公司專案狀態整合**
>
> 📌 **UI 註記**：以下操作以 2026 年 5 月 SharePoint 介面為準。若 UI 微調，操作意圖 = **在 SharePoint 文件庫範圍內建立 Custom Agent**，含 Name / Description / Instructions / Knowledge。

#### 4.1 打開預建的 SharePoint Site（Phase 7 已建好）

操作帳號：**admin@moneyyu.com**

打開 SharePoint，找到 **「國泰集團 — 數位轉型 PMO」**（alias: `cathay-digital-pmo`）。

> 💡 這個 site **不需要從零建立** — Phase 7 已預建好，內含：
> - **文件庫**：7 份 S4 系列文件（與 OneDrive 雙存）
> - **3 個 List**：專案 RAID Log（12 條，含 Goldman Marcus 失敗教訓 3 條）、五大支柱 KPI 追蹤（7 條）、跨子公司里程碑（10 條）
>
> 「Goldman Marcus 失敗教訓」已預先寫進 RAID-002~004，這就是 Agent 之後會自動引用的「企業記憶」素材。

#### 4.2 建立 SharePoint Agent（學員觀摩 + 動手）

在 site 文件庫頂端右上角，點選 **`+ Add an agent`** → 選擇 **Custom agent**：

| 欄位 | 內容 |
|---|---|
| **Agent Name** | `國泰集團 數位轉型 PMO Agent` |
| **Description** | 整合四子公司數位轉型專案狀態、跨子公司資源協調、Steering Committee 提報生成 |
| **Knowledge Sources** | 自動 = 整個 `國泰集團 — 數位轉型 PMO` site（7 docs + 3 lists）|
| **Capabilities** | ✅ 啟用 Web Search（讓 Agent 可整合 DBS / JPM 最新案例）|

**Custom Instructions**（複製貼上）：

```
你是國泰金控集團 PMO 的智能助理，協助 Christie（PMO 主導）、Isaiah（IT 架構師）、Lidia（CDO）。

當被詢問時，請依序：

1. 查閱「專案 RAID Log」List 找出相關 Risk / Issue / Dependency
2. 查閱「五大支柱 KPI 追蹤」List 確認進度數據
3. 查閱「跨子公司里程碑」List 對齊時程
4. 跨子公司影響盤點：明確指出人壽 / 世華 / 投信 / 證券四個子公司各自的角色
5. ROI 試算：必引用具體投資金額與效益
6. 風險與失敗教訓：必引用 Goldman Marcus、UBS、DBS 案例

格式：
- 答覆開頭給「TL;DR」摘要 3 句話
- 中間用表格呈現
- 結尾給董事會 / Steering Committee 友善的「行動建議」

語氣：戰略性、可執行、避免技術術語（董事會友善）。

特別重要：每次回覆都要引用 RAID Log 中 Goldman Marcus 失敗教訓（RAID-002~004）至少一條，提醒「我們不要重蹈覆轍」。
```

按 **Save**（先個人測試，**不 Publish 不 Share**）。

#### 4.3 試問 Agent

```
本集團 2026 年數位轉型最關鍵的三件事是什麼？哪個子公司負責？投資多少？預計什麼時候看到客戶端有感的改變？
```

**預期成果**：PMO Agent 整合：
- 「跨子公司里程碑」List：MS-001（世華 cutover）、MS-002（Copilot 部署）、MS-008（SSO）
- 「五大支柱 KPI 追蹤」List：雲端化 32%→55%、MAU 495→620、NPS 57→60
- 「專案 RAID Log」中的 Goldman Marcus 教訓
- SharePoint 文件中的 Fintech benchmark
- 給出 TL;DR + 表格 + 行動建議

---

### Step 5：對比與結語（2 min）

**講師結語**：
> 「過去 Christie 每月要花 1 整週整合四子公司專案狀態 + 對齊 Lidia + 寫 Steering Committee 提報。
>
> 建立 PMO Agent 後，**月會前 1 小時隨時可問 Agent 取得最新狀態**。
>
> 對 Lidia 來說更關鍵的：**Goldman Marcus 失敗教訓被『硬塞進 Agent 的記憶』**，每次對話都會自動提醒，避免我們重蹈覆轍。
>
> 這是 MS-4019 Module 3 的進階：**Custom Instructions 不只給格式，還能注入企業文化與失敗經驗**。」

---

## 學員 Q&A 提示

| 學員可能問 | 講師可回答 |
|---|---|
| 53.7 億是不是真的能達到 ROI 146%？ | Agent 跑出來的是基於現有資料的預估，董事會仍要審慎審查 |
| 跨子公司資料能放在同一 SharePoint 嗎？ | 可以，但要設權限隔離，符合金控法第 43 條 |
| Agent 會不會洩漏單一子公司的機密？ | SharePoint 的權限設定會繼承，Agent 不會繞過 |
| 為什麼非要用 Agent，每月會議不就解決？ | Agent 讓「問狀態」隨時可問，不必等月會 |

---

## Researcher / Analyst / SharePoint Agent 對應預埋資料

| Agent | 預埋資料 |
|---|---|
| **Researcher** | `S4_2026-2028數位轉型藍圖.docx`、`S4_全球Fintech同業比較研究.docx` |
| **Analyst** | `S4_通路NPS月度原始.xlsx`、`S4_數位轉型KPI_Dashboard.xlsx`、`S4_集團NPS客戶旅程2026Q1.docx` |
| **SharePoint Agent**（建立用） | 上述全部 + 四子公司 RAID Log |
| **Copilot** | 3 封跨子公司 email + Teams S4 channel 4 個討論 |
