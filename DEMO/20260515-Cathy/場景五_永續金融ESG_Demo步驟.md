# 場景五：國泰金控 + 投信 — 永續金融 ESG Demo 步驟

> **MS-4019 對應**：Module 4（Share and use agents — 跨團隊協作）
> **時長**：30 分鐘
> **主角（故事設定）**：Joni Sherman（量化分析師 / 國泰投信）+ Johanna Lorenz（法遵稽核經理）
> **協作（故事設定）**：Lidia Holloway（CDO）、Irvin Sayers（風險）
> **操作帳號**：⚠️ **admin@moneyyu.com**（全程唯一登入帳號，不切換；Joni/Johanna/Lidia/Irvin 僅為 **故事中的角色背景**，不是登入帳號）

---

## 場景背景（30 秒講師開場）

> 「2025 TCFD 揭露報告 6/30 要對外公布，永續金融委員會 5/12 已審查通過初稿。但這份報告涉及：
> - **投信**：18 個高碳/低碳持股的碳足跡計算
> - **法遵**：金管會永續金融揭露 2.0 合規性確認
> - **風險**：氣候風險矩陣（颱風 / 海平面 / 政策 / 技術 / 訴訟五類）
> - **CDO**：對外揭露的策略訊息掌控
>
> 這四方都需要『同一份資料的不同視角』。Module 4 的精髓就是：**Agent 不只給個人用，還要能在團隊間分享、跨部門協作**。」

---

## Demo 5 步驟

### Step 1：Researcher Agent — TCFD 同業 benchmark 升級（6 min）

切換到 **Researcher Agent**：

```
我（admin）正在協助 Joni Sherman（國泰投信）與 Johanna Lorenz（國泰金控法遵）準備 2025 TCFD 揭露報告。
請整合以下資訊，產出「同業 TCFD 揭露品質對比」最新版：

1. OneDrive 中：
   - S5_2025TCFD揭露報告草稿.docx 的同業比較表
   - S5_2050淨零路徑研究.docx
   - S5_組合碳足跡原始資料.xlsx 的「同業 ESG 揭露」分頁

2. 公開網路最新資料（2025-2026 上半年）：
   - 玉山金、富邦金、中信金 2024 TCFD 報告（CSR 報告書）
   - ISSB IFRS S2 與 TCFD 的對應關係（2026 年最新）
   - SBTi 在金融業的最新驗證家數
   - 金管會 4/22 公布的永續金融揭露準則 2.0 條文細節

最後給永續金融委員會一段 200 字摘要，包含：
- 本公司 TCFD 88 分在四大金控中的排名
- 與排名第 1 的玉山金（89 分）差距在哪
- 有哪些揭露項目我們可以在 6/30 公布前快速補強
```

**預期成果**：Researcher 整合 Word + Excel + 公開最新資料，找出 6/30 前可改善的揭露項目。

---

### Step 2：Analyst Agent — 18 持股碳足跡與淨零路徑（8 min）

切換到 **Analyst Agent**，附上 `S5_組合碳足跡原始資料.xlsx` + `S5_ESG淨零Dashboard.xlsx`：

```
請基於這兩個檔案：

1. 從「持股碳足跡明細」分頁分析 18 個持股：
   - 碳排前 5 大、排放強度（tCO2e/百萬美元投資）前 5 大
   - 高碳產業（電力、石化、水泥、鋼鐵）合計曝險與 WACI
   - ESG 評分 BBB 以下的持股清單

2. 從「淨零路徑」分頁：
   - 計算 2030 中期目標 -38% 的可行性（路徑斜率 vs 實際歷史減速度）
   - 哪一個產業（電力/石化/水泥/鋼鐵）最有可能拖慢進度
   - 2030-2040 那段路徑可信度評估

3. 找出三個「可立即減持以優化 WACI」的持股建議

最後產出：
- 一個適合放在 TCFD 報告附錄的「Top 5 / Bottom 5」摘要表
- 一段 100 字的「2050 淨零承諾的關鍵假設」陳述（用情境分析語氣）
```

**預期成果**：Analyst 跑出明確的 Top 5 / Bottom 5、找出水泥/鋼鐵是最大瓶頸（呼應 Joni email 中的「最不確定」）。

---

### Step 3：用 Copilot 升級半成品 PPT（5 min）

打開 `S5_2025TCFD揭露報告_半成品.pptx`：

```
這是永續金融委員會提報，請依序：

1. 第 1 頁治理：整合 TCFD 揭露草稿第一節，產出三條重點
2. 第 2 頁策略：補上四大子公司各自策略行動（金控 / 人壽 / 世華 / 投信）
3. 第 3 頁風險管理矩陣：用 2050 淨零路徑研究.docx 整合五大氣候風險（注意：颱風要升級為「高」、訴訟升「中」）
4. 第 4 頁關鍵指標表：用 Analyst Agent 剛才的 5 大指標進度
5. 第 5 頁同業 benchmark：用 Researcher Agent 剛才的最新比較

注意：必使用「情境分析」語氣（1.5°C / 2°C / 延誤轉型三 case）
```

---

### Step 4：建立『ESG 揭露專案』SharePoint Agent + 跨團隊分享（10 min — Module 4 主軸）

> **本場景精華 — Module 4：Share and Use Agents**
>
> 📌 **UI 註記**：以下操作以 2026 年 5 月 SharePoint 介面為準。若 UI 微調，操作意圖 = **在 SharePoint 文件庫範圍內建立 Custom Agent，並分享給多個視角的使用者**。

#### 4.1 打開預建的 SharePoint Site（Phase 7 已建好）

操作帳號：**admin@moneyyu.com**

打開 SharePoint，找到 **「國泰金控 — 永續金融委員會」**（alias: `cathay-esg`）。

> 💡 這個 site **不需要從零建立** — Phase 7 已預建好，內含：
> - **文件庫**：6 份 S5 系列文件（與 OneDrive 雙存）
> - **3 個 List**：氣候風險登記簿（5 條）、投融資組合碳足跡監控（18 持股）、永續商品/綠色金融追蹤（10 條）
>
> Site members 已設定為 admin（owner）+ Quant、Compliance、Risk、CDO（協作者）。

#### 4.2 建立 Agent（學員觀摩 + 動手）

在 site 文件庫頂端右上角，點選 **`+ Add an agent`** → 選擇 **Custom agent**：

| 欄位 | 內容 |
|---|---|
| **Agent Name** | `國泰 ESG 揭露專案 Agent` |
| **Description** | 整合 TCFD 揭露需求，提供投信 / 法遵 / 風險 / CDO 四方協作介面 |
| **Knowledge Sources** | 自動 = 整個 `國泰金控 — 永續金融委員會` site（6 docs + 3 lists）|
| **Capabilities** | ✅ 啟用 Web Search |

**Custom Instructions**（複製貼上）：

```
你是國泰金控永續金融委員會的智能助理，協助 Joni Sherman（投信量化）、Johanna Lorenz（法遵）、Irvin Sayers（風險）、Lidia Holloway（CDO）。

四個角色詢問同一份報告時，請依不同視角回應：

【投信視角】（Joni）：聚焦持股碳足跡、淨零路徑、ESG 評分 — 引用「投融資組合碳足跡監控」List
【法遵視角】（Johanna）：聚焦金管會揭露準則合規、與 ISSB IFRS S2 對應、可能被環團攻擊的項目
【風險視角】（Irvin）：聚焦氣候風險矩陣、實體 vs 轉型、壓力測試 — 引用「氣候風險登記簿」List
【CDO 視角】（Lidia）：聚焦對外揭露的策略訊息、董事會友善摘要、四大金控比較

格式：
- 必先確認使用者是誰（如沒明說，問一句）
- 給該角色「最關心的 3 件事」
- 必引用具體文件名稱與 List 項目編號（出處可追蹤）
- 必標示「不確定」之處（特別是 2030-2040 路徑）

語氣：學術嚴謹（給投信）、保守精準（給法遵）、量化導向（給風險）、戰略簡潔（給 CDO）。
```

#### 4.3 分享給 Site Members（**僅展示 UI，不實際送出**）

> ⚠️ **注意**：分享步驟僅展示 UI 流程，**不真的送出**（admin 一個帳號示範 Module 4 的「Share & Use」概念，避免實際打擾其他角色信箱）。

點選 **Share** 按鈕，向學員說明：
- 此 Agent 已在「國泰金控 — 永續金融委員會」site，**權限自動繼承** site members（Joni、Johanna、Irvin、Lidia）
- 若要進一步加人，可「Add specific people」或「Anyone in your organization」

按 **Cancel** 不送出，回到 Agent。

#### 4.4 同一個問題、四個視角試問

學員可以坐在 admin 帳號前，扮演四個角色提問同樣問題（**這是 Module 4「Share & Use」的重點 — 同一個 Agent，不同視角**）：

```
我是 Joni（投信）。2025 TCFD 揭露報告中「水泥產業曝險偏高」這件事我該怎麼處理？
```

```
我是 Johanna（法遵）。2025 TCFD 揭露報告中「水泥產業曝險偏高」這件事我該怎麼處理？
```

```
我是 Irvin（風險）。2025 TCFD 揭露報告中「水泥產業曝險偏高」這件事我該怎麼處理？
```

```
我是 Lidia（CDO）。2025 TCFD 揭露報告中「水泥產業曝險偏高」這件事我該怎麼處理？
```

> ⚠️ 注意：這裡的「我是 Joni」是 **prompt 內的角色聲明**（給 Agent 判斷視角），不是登入帳號。**實際登入仍是 admin@moneyyu.com**。

**預期成果**：
- **Joni 視角**：建議減持台泥（1101.TW Scope1+2 排放 2,820 萬 tCO2e）、亞泥（1102.TW 2,240 萬）的具體量
- **Johanna 視角**：判斷是否觸發金管會審查、環團攻擊風險、ISSB IFRS S2 揭露要求
- **Irvin 視角**：水泥業氣候轉型風險評估（CR-003 轉型政策）、影響 ICS 多少
- **Lidia 視角**：對外揭露怎麼措辭最有利、與玉山金 89 分對比

---

### Step 5：對比與結語（1 min）

**講師結語**：
> 「同一個 ESG 揭露專案，過去四個部門要開 5 場會議才能對齊。
>
> 建立『ESG 揭露專案 Agent』後：
> - 投信、法遵、風險、CDO **四方共用同一份知識庫**
> - 每方都能用**自己的視角**得到客製化答覆
> - **金管會 4/22 AI 治理新規**對「人類覆核」的要求 → Agent 標示不確定處 + 出處追蹤
>
> 這就是 MS-4019 Module 4 的核心：**Agent 不只是工具，是團隊協作的介面**。」

---

## 學員 Q&A 提示

| 學員可能問 | 講師可回答 |
|---|---|
| 不同角色看到同一份資料的不同視角，會不會誤解？ | 視角是「強調重點」，原始資料相同，沒有誤解問題 |
| 四個部門權限要不要分開？ | SharePoint 權限可細到資料夾層級，Agent 會繼承 |
| Agent 被董事會問起怎麼建議的，要負責嗎？ | 是，使用者責任；Agent 是輔助，不取代決策 |
| 6/30 對外公布前 Agent 內容要鎖定嗎？ | Custom Instructions 可加「2026/6/30 之前內部討論用，不可對外公布」鎖定 |

---

## Researcher / Analyst / SharePoint Agent 對應預埋資料

| Agent | 預埋資料 |
|---|---|
| **Researcher** | `S5_2025TCFD揭露報告草稿.docx`、`S5_2050淨零路徑研究.docx` |
| **Analyst** | `S5_組合碳足跡原始資料.xlsx`、`S5_ESG淨零Dashboard.xlsx` |
| **SharePoint Agent**（建立用） | 全部 5 份 S5 系列 + 過往 TCFD 報告 |
| **Copilot** | 4 封跨部門 email + Teams S5 channel 4 個討論 |

---

## 場景五彩蛋（時間允許可加碼）

讓學員觀摩 **「Goldman Marcus 失敗教訓的應用」** —

ESG 揭露和數位轉型一樣，也有對應的「不要做的事」：
- ❌ Greenwashing：誇大環境效益但無實質改善
- ❌ 揭露不足：被環團攻擊
- ❌ 過度承諾：2050 淨零拍胸脯但路徑不可行

可以在 ESG Agent 的 Custom Instructions 中加入這三條警告，讓每次回覆都自動提醒。
