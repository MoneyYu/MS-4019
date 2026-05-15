# Demo 檔案類型與用途說明

> 為什麼 MS-4019 國泰課程要產出 14 Word + 10 Excel + 10 PPT 共 34 個檔？每種檔案的策略意圖是什麼？
> 本文件供未來類似 demo 設計流程參考。

---

## 🎯 設計總原則

每個 Demo 檔都對應「**至少一個 M365 Copilot Agent 的消化點**」：

| Agent | 最擅長處理的檔案類型 | 為什麼 |
|---|---|---|
| **Researcher Agent** | Word（敘事、報告、備忘錄） | 跨多份文字內容做「整合 + 摘要 + 對比」 |
| **Analyst Agent** | Excel（純資料表格） | 數值計算、敏感度、繪圖、樞紐 |
| **M365 Copilot**（標準） | PPT（半成品 / 完整版） | 改寫版面、生成新頁、補上預留區塊 |
| **SharePoint Agent / Copilot Chat Agent** | 三種混合（OneDrive + SharePoint） | 跨來源整合，模擬「真實工作助理」 |

> **若沒有對應 Agent 消化點的檔案 = 不產出**。例如本案沒做 PDF（不是任何 Agent 的最佳輸入格式）。

---

## 📝 Word 檔案（14 份）— Researcher Agent 的主要素材

### 1. Researcher 素材（深度報告 / 競品研究 / 新規評估）

| 場景 | 檔案 | 為什麼是 Researcher 的菜 |
|---|---|---|
| S1 | S1_長照保單競品分析報告.docx | 5 家競品 SWOT、市場數據需整合外部資料 |
| S1 | S1_新版長照商品精算備忘錄.docx | 精算假設 + 風險警示需與業界對比 |
| S2 | S2_2026Q3全球市場展望.docx | Fed/ECB/BOJ 觀點需即時更新 |
| S3 | S3_IFRS17_ICS2_影響評估備忘錄.docx | IFRS17 第二年度影響涉及多份法規 |
| S3 | S3_AML風險評估Q1報告.docx | 新興 AML 樣態需網路 + 內部資料整合 |
| S4 | S4_全球Fintech同業比較研究.docx | DBS / JPM / UBS 案例需更新 |
| S5 | S5_2025TCFD揭露報告草稿.docx | TCFD 揭露涉及同業 benchmark |
| S5 | S5_2050淨零路徑研究.docx | 高碳產業曝險 + 路徑分析 |

**特徵**：
- 結構：背景 → 數據 → 對比 → 結論 → **Researcher Agent 待整合題目**（明確列出網路 + OneDrive 整合點）
- 必含「💡【此處待補：請用 Copilot 補上 X】」紅色標記，課程現場 demo 用 Copilot 補
- 引用具體數字、人名、日期，模擬真實工作報告

### 2. Analyst 素材（數據導向但敘事呈現）

| 場景 | 檔案 | 為什麼是 Analyst 的菜 |
|---|---|---|
| S2 | S2_高資產客戶組合複核範本.docx | 表格 + 績效歸因，Analyst 容易延伸 |
| S4 | S4_集團NPS客戶旅程2026Q1.docx | 八階段 NPS 矩陣，Analyst 容易拆解 |

**特徵**：含明確的「Analyst Agent 待計算題目」段落。

### 3. 業務文件（給 Copilot 一般用）

| 場景 | 檔案 | 用途 |
|---|---|---|
| S1 | S1_安心久久商品企劃書.docx | 完整商品提案，Copilot 改寫摘要 |
| S3 | S3_2026Q1法遵執行摘要.docx | Q1 法遵執行報告 |
| S4 | S4_2026-2028數位轉型藍圖.docx | 三年策略文件 |
| 跨 | CDO月會逐字稿_五大專案統合報告.docx | 跨場景整合素材 |

**特徵**：完整的工作文件，Copilot 可做「重寫」、「摘要」、「翻譯」等基本任務。

### Word 檔的 demo 戰術

1. **直接給 Researcher**：把 Word 檔丟給 Researcher Agent，配合一個整合性 Prompt
2. **多檔交叉**：3-5 份 Word 同時餵 Agent，看「跨文件整合能力」
3. **網路 + 內部混合**：Prompt 中明確要求 Researcher「整合 OneDrive 中 X.docx 與公開網路最新 X 資料」

---

## 📊 Excel 檔案（10 份）— Analyst Agent 的雙軌策略

**10 份 Excel = 5 純資料表 + 5 預製分析 Dashboard**，這是刻意的雙軌設計。

### 軌道 A：純資料表（5 份） — 給 Analyst 自由發揮

| 場景 | 檔案 | 內容 |
|---|---|---|
| S1 | S1_長照精算原始資料.xlsx | 失能/失智發生率、三檔保費 |
| S2 | S2_全球市場原始資料.xlsx | 12 月區域指數、5 客戶組合明細 |
| S3 | S3_風險原始資料KRI_STR.xlsx | 12 KRI × 6 月、30 件 STR |
| S4 | S4_通路NPS月度原始.xlsx | 4 子公司 × 多通路 12 月 |
| S5 | S5_組合碳足跡原始資料.xlsx | 18 持股、6 同業 ESG |

**特徵**：
- 扁平資料表（無 chart、無 pivot、無計算公式）
- 每個欄位清楚命名，符合 Analyst Agent 偏好
- 行數適中（10-30 行），不要太多以免處理超時
- **demo 重點**：讓 Analyst 現場「跑出洞察」，戲劇感強

### 軌道 B：預製分析 Dashboard（5 份） — 模擬「現有日常工作」

| 場景 | 檔案 | 內容 |
|---|---|---|
| S1 | S1_長照競品Dashboard.xlsx | CP 值對比、保費 vs 給付 chart |
| S2 | S2_組合績效Dashboard.xlsx | 績效歸因、風險指標、月度趨勢 |
| S3 | S3_風險指標Dashboard.xlsx | KRI 熱圖、壓力測試、24 月 ICS 趨勢 |
| S4 | S4_數位轉型KPI_Dashboard.xlsx | 三年路徑、NPS 旅程、ROI |
| S5 | S5_ESG淨零Dashboard.xlsx | 淨零路徑、TCFD 對比、高碳曝險 |

**特徵**：
- 含預製 BarChart / LineChart、KPI 摘要表、條件格式
- 模擬「員工已經整理好的常用 dashboard」
- **demo 重點**：讓 Analyst Agent **基於既有分析做進階洞察**

### Excel 雙軌的教學價值

| 學員看到 | 學到的事 |
|---|---|
| 軌道 A → Analyst Agent → 產出洞察 | Agent 取代「資料分析師花 1 天做歸因」 |
| 軌道 B → Analyst Agent → 進階解讀 | Agent 不取代既有 Dashboard，而是延伸 |
| 兩軌同時看 | 真實工作中**先有 Dashboard 再用 Agent 深挖**才是常態 |

---

## 📽️ PPT 檔案（10 份）— Copilot 升級半成品的雙軌策略

**10 份 PPT = 5 完整版 + 5 半成品**，這是另一個雙軌設計。

### 軌道 A：完整版（5 份） — 「目標長相」

| 場景 | 檔案 | 頁數 | 用途 |
|---|---|---|---|
| S1 | S1_安心久久商品提案_完整版.pptx | 8 頁 | 商審會 |
| S2 | S2_2026Q3市場展望_完整版.pptx | 7 頁 | 客戶月報 |
| S3 | S3_風險法遵董事會月報_完整版.pptx | 7 頁 | 董事會 |
| S4 | S4_數位轉型藍圖_完整版.pptx | 7 頁 | Steering Committee |
| S5 | S5_2025TCFD揭露報告_完整版.pptx | 8 頁 | 永續委員會 |

**特徵**：
- 標題頁、章節頁、內容頁、表格頁俱全
- 國泰金控品牌色（深綠 #006633 + 金 #CC9933）
- 章節分明，模擬 PMO 已產出的最終提報

### 軌道 B：半成品（5 份） — 「Copilot 升級的素材」

每場景對應一份，內容刻意保留：
- 標題頁完整 + 章節分頁完整（讓視覺一致性看得出來）
- 內容頁只有重點 1-2 條 + **「💡【此處待補：請用 Copilot 補上 X】」標記**
- 紅色字體 + 圓角光綠背景 placeholder 框

### PPT 雙軌的 demo 戰術

```
第 1 步：先打開「半成品」.pptx 給學員看 — 啊，這份才寫 50%
第 2 步：用 Copilot 升級每一頁（基於 OneDrive 中的 Word + Excel）
第 3 步：對比「升級後」vs「完整版」 — 戲劇性差異
第 4 步：講師結語：5 分鐘把半成品變成 80% 完成度，剩下 20% 由你定稿
```

> **設計鐵律**：半成品**不是「空白」**，而是「**架構完整但內容缺失**」。完全空白會讓學員覺得 AI 太依賴。架構先做好才能把 Agent 限縮在「補內容」這個明確職責。

---

## 🔄 三種檔案 + SharePoint 的協作關係

```
                        ┌─────────────────────────────────────┐
                        │   admin@moneyyu.com                  │
                        │   (唯一的 Demo 操作帳號)             │
                        └──────────────┬───────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            │                                                      │
            ▼                                                      ▼
  ┌─────────────────────────┐                          ┌─────────────────────────┐
  │   OneDrive               │                          │   SharePoint Sites       │
  │   Cathay-MS4019/         │                          │   3 部門知識庫           │
  │   (扁平 + 5 子資料夾)    │                          │   (S3/S4/S5 雙存)        │
  │   34 檔（個人草稿）      │                          │   + 9 lists × ~92 items  │
  └────────┬────────────────┘                          └────────┬────────────────┘
           │                                                    │
           ▼                                                    ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │   📝 Word     📊 Excel     📽️ PPT                              │
  │   14 份       10 份         10 份                                │
  │   (敘事)      (5純+5預製)   (5完整+5半)                          │
  └────────┬───────────┬───────────┬───────────────────────────────┘
           │           │           │
           ▼           ▼           ▼
  ┌─────────────┬─────────────┬─────────────┐
  │ Researcher  │  Analyst    │  Copilot    │
  │ (整合/摘要) │  (計算/繪圖)│  (升級/改寫)│
  └──────┬──────┴──────┬──────┴──────┬──────┘
         │             │             │
         └─────────────┼─────────────┘
                       ▼
       ┌─────────────────────────────────────┐
       │  SharePoint Agent /                  │
       │  Copilot Chat Agent Builder          │
       │  (跨來源整合的「Demo 高潮」)        │
       └─────────────────────────────────────┘
```

---

## 📋 設計檢查清單（未來類似流程）

設計新場景時，逐項檢查：

- [ ] 每場景至少 **2 份 Word**（其中 1 份是 Researcher 素材、1 份是工作文件）
- [ ] 每場景至少 **2 份 Excel**（1 份純表格給 Analyst、1 份預製分析做 benchmark）
- [ ] 每場景至少 **2 份 PPT**（1 份完整版做目標、1 份半成品做升級舞台）
- [ ] 每份 Word 含「Researcher / Analyst Agent 待整合題目」段落
- [ ] 每份 Word/PPT 含至少 1 個「💡【此處待補】」紅色標記
- [ ] Excel 純表格 < 30 行 / 預製 Dashboard 必含 1-2 個 chart
- [ ] PPT 半成品**不是空白**，而是架構完整但內容缺失
- [ ] 檔名前綴使用 `S1_` ~ `S5_` 做場景分組
- [ ] 完整版 / 半成品命名一致：`{場景名}_完整版.pptx` / `{場景名}_半成品.pptx`
- [ ] 部門共用知識資產要建 SharePoint Site（含 doc library + lists）

---

## ⚠️ 帳號使用鐵律（重要）

| 動作 | 用哪個帳號？ |
|---|---|
| 講師現場 demo 登入 M365 | **admin@moneyyu.com** |
| 開啟 OneDrive、Outlook、Calendar、Teams、SharePoint | **admin@moneyyu.com** |
| 在 Copilot Chat 跑 Researcher / Analyst Agent | **admin@moneyyu.com** |
| 建立 SharePoint Agent 或 Copilot Chat Agent | **admin@moneyyu.com**（admin 是 owner，自然有權限）|
| 寄出新 email、發 Teams 訊息（demo 過程） | **admin@moneyyu.com** |
| Email/Teams 訊息中的 fromRole（角色）| 由 seed JSON 控制，**真實寄送人是各角色 UPN**，但 admin 都會 CC 看得到 |

> ⚠️ **絕對不要**：在 demo 步驟書裡寫「請用 ChristieC 帳號登入...」或「切換到 IsaiahL 帳號...」之類的指令，**這在現場無法操作**（講師不會有那些帳號的密碼）。
>
> ✅ **正確寫法**：「我（admin）正在協助 Christie 準備商審會，請整合我這週收到的長照郵件」 — 角色僅出現在 prompt 內容中，不影響登入帳號。

---

## 🎬 場景與 demo 模組對應（最終 6 場景）

| 場景 | MS-4019 模組 | 主要 Agent | 核心檔案類型 |
|---|---|---|---|
| 1 長照新商品 | M2 | Researcher + Analyst | Word + Excel + PPT |
| 2 財富管理 | M2 | Researcher + Analyst（含跨子公司串接）| Word + Excel + PPT |
| 3 法遵與風險 | **M3b**（SharePoint Agent） | SharePoint Agent + Researcher | Word + Excel + PPT + SharePoint Site #1 |
| 4 數位轉型 | **M3b**（SharePoint Agent） | SharePoint Agent + Analyst | Word + Excel + PPT + SharePoint Site #2 |
| 5 永續金融 ESG | M4（Share & Use） | SharePoint Agent + 多角色視角 | Word + Excel + PPT + SharePoint Site #3 |
| **6 集團專案查詢助理** | **M3a（Copilot Chat Agent Builder）** | **Copilot Chat Agent**（NEW） | **無新檔案，跨 5 場景整合** |

> 場景 6 是 MS-4019 Module 3 前半（**官方份量更大的單元**）的對應 demo，與場景 3、4、5 的 SharePoint Agent 形成「**Copilot Chat Agent vs SharePoint Agent**」的關鍵對比。

---

## 🏛️ SharePoint 資產地圖

執行 `run.ps1` 後，admin@moneyyu.com 在 SharePoint 會看到 **4 個 site**：

| # | Site | 用途 | 來源 Phase |
|---|---|---|---|
| 1 | 國泰集團 — MS-4019 Demo（Teams team site） | 即時溝通（5 channels 對應 5 場景討論） | Phase 4 |
| 2 | 國泰金控 — 法令遵循處（cathay-compliance） | 場景三 SharePoint Agent 知識庫 | **Phase 7** |
| 3 | 國泰集團 — 數位轉型 PMO（cathay-digital-pmo） | 場景四 SharePoint Agent 知識庫 | **Phase 7** |
| 4 | 國泰金控 — 永續金融委員會（cathay-esg） | 場景五 SharePoint Agent 知識庫 | **Phase 7** |

> **設計理念**：Teams team site 是「即時對話現場」；3 個 SharePoint sites 是「部門定稿知識庫」。這對應真實企業中**通訊頻道與知識資產分離**的工作型態。

---

## 📂 檔案分布總覽

```
本機 DEMO-FILE/                       (扁平 34 檔，由 Python 生成)
        ↓ Phase 2 上傳
OneDrive Cathay-MS4019/                (5 子資料夾，admin 個人視角)
        ↓ Phase 7 雙存到 SharePoint（S3/S4/S5 共 20 檔）
SharePoint 3 sites                     (部門知識庫 + 9 lists × ~92 items)
```

### 雙存的設計理由

1. 模擬真實工作 — 個人草稿在 OneDrive、定稿移到部門 SharePoint
2. 場景六 Copilot Chat Agent 同時連 OneDrive + 3 SharePoint，呈現「跨來源」價值
3. files-manifest.json 不變動，sharepoint-sites.json 用 sourceFilename 共用 DEMO-FILE

---

## 🔗 相關文件

- 整體授課流程：[00_MS4019_整體授課流程.md](00_MS4019_整體授課流程.md)
- Demo 步驟書：場景一 ~ 場景六 .md
- README：[README.md](README.md)
- AB730 / MS4018 工作區慣例：[memory: ab730-conventions.md](#)
