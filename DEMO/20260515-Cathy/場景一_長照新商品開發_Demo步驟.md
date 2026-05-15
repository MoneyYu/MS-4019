# 場景一：國泰人壽 — 長照新商品開發 Demo 步驟

> **MS-4019 對應**：Module 2（Explore prebuilt Researcher / Analyst Agents）
> **時長**：30 分鐘
> **主角（故事設定）**：Christie Cline（商品企劃協理 / 國泰人壽）
> **協作（故事設定）**：Lidia Holloway（CDO）、Irvin Sayers（風險）
> **操作帳號**：⚠️ **admin@moneyyu.com**（全程唯一登入帳號，不切換；Christie/Lidia/Irvin 僅為 **故事中的角色背景**，不是登入帳號）

---

## 場景背景（30 秒講師開場）

> 「下週四就是商審會，Christie 要決定『安心久久』長照新商品的三檔費率方案中要主推哪一檔。她剛收到富邦 4/30 公布新版居家照護給付加碼到 5,000 元的消息，市場壓力立刻變大。
>
> 同時，Irvin 給的精算報告 25 頁、Joni 的 ESG 研究 18 頁、競品分析報告 12 頁、加上 5 月初 Email 來來回回的討論⋯⋯Christie 沒時間全部看完。
>
> 這時候 Researcher Agent 與 Analyst Agent 就是救命稻草。」

---

## Demo 5 步驟（建議用 admin@moneyyu.com 帳號登入 M365 Copilot）

### Step 1：開場 — 用 Copilot Chat 摘要本週 inbox（3 min）

打開 M365 Copilot Chat，問：

```
這一週我（Christie 視角）關於「安心久久」長照新商品有哪些往來郵件？請列出每一封的發信人、重點、與我需要的回覆。
```

**預期成果**：列出 5 月初的 5 封 email thread，包括 Irvin 的 Monte Carlo 結果、Johanna 的外匯規範回覆、Isaiah 的系統時程選項、Lidia 的決策、富邦競品加碼等。

---

### Step 2：Researcher Agent — 競品與市場深度研究（7 min）

切換到 **Researcher Agent**，輸入：

```
我（admin）正在協助 Christie Cline 準備下週「安心久久」長照新商品的商審會，要決定三檔費率中要主推哪一檔。

請整合以下資訊：
1. OneDrive 中「S1_長照保單競品分析報告.docx」的競品條款比較
2. 公開網路最新資料：富邦人壽 2026 年 4 月公布的新版「守護一生長照」居家照護給付調整內容
3. 日本介護保險 2024 年改革對民間長照商品的影響
4. ESG / 影響力投資型保單在歐洲市場的滻透率

最後請給我一段「為什麼進階型應該是主推方案」的 200 字論述，引用具體數字，讓 Christie 可以直接用在商審會。
```

**預期成果**：Researcher Agent 整合 OneDrive 文件 + 公開網路資料，產出一段引用具體數字的論述，含富邦最新動態。

---

### Step 3：Analyst Agent — 三檔費率敏感度分析（7 min）

切換到 **Analyst Agent**，附上 OneDrive 中的 `S1_長照精算原始資料.xlsx`，輸入：

```
請基於這份檔案的「費率方案保費」與「失能發生率經驗表」兩個分頁：

1. 計算三檔方案（基本/進階/尊榮）在「失能發生率 +10%」與「失能發生率 -10%」兩種情境下的損失率變化
2. 找出哪一個年齡段（30-60 歲）對基本型最敏感
3. 用一個圖表呈現「進階型 vs 尊榮型」在不同投保年齡的累積給付倍率
4. 給我一段 100 字的精算結論，作為商審會 PPT 的引用文字
```

**預期成果**：Analyst Agent 跑出三情境敏感度、找出 50-55 歲對基本型最敏感、繪出累積給付倍率圖、給出可直接用的結論文字。

---

### Step 4：用 Copilot 升級半成品 PPT（8 min）

打開 OneDrive 中的 `S1_安心久久商品提案_半成品.pptx`，在 PowerPoint 中啟動 Copilot：

```
這是一份半成品的商審會 PPT，每頁都有 [此處待補：請用 Copilot 補上 X] 的提示。

請依序：
1. 第 1 頁市場機會：補上 5 個關鍵市場數據（從 OneDrive 的 S1_長照保單競品分析報告.docx 整合）
2. 第 2 頁競品比較：根據 Researcher Agent 剛整合的內容更新表格
3. 第 3 頁三檔方案：詳細參數與目標客群描述
4. 第 4 頁敏感度：用 Analyst Agent 剛才的計算結果
5. 第 5 頁時程與 KPI：整合精算備忘錄 + 商品企劃書的時程

升級後直接覆蓋原檔案。
```

**預期成果**：半成品 PPT 在 8 分鐘內升級到接近 `_完整版.pptx` 的內容深度。

---

### Step 5：對比與結語（5 min）

打開 `S1_安心久久商品提案_完整版.pptx` 與剛升級後的 PPT 並排比較。

**講師結語**：
> 「同樣的內容，過去 Christie 要花 2-3 天整合 5 篇文件 + 5 封 email + 公開網路資料 + 三檔精算敏感度分析。
>
> 用 Researcher + Analyst Agent，**25 分鐘完成**，並且**有資料來源可追蹤**。
>
> 這就是 MS-4019 想傳達的核心：Agent 不是取代你的判斷，是讓你的判斷可以更快、更扎實。」

---

## 學員 Q&A 提示

| 學員可能問 | 講師可回答 |
|---|---|
| Researcher 的「公開網路資料」會不會引用到不可信來源？ | Researcher 會標註出處，使用者責任要 review |
| Analyst Agent 跑的數字可信嗎？ | Analyst 是基於你給的 Excel 計算，邏輯透明可驗 |
| 我們有金管會 4/22 AI 治理新規，這樣用 Agent 合規嗎？ | 是的，因為「決策權」仍在 Christie，Agent 只是輔助 |
| 商審會委員會問「為何選進階型？」，PPT 是 Copilot 寫的能用嗎？ | 完全可以，但 Christie 必須能解釋每個論點，這是責任 |

---

## Researcher / Analyst Agent 對應預埋資料

| Agent | 預埋資料來源 | 對應 Word/Excel |
|---|---|---|
| **Researcher** | 競品條款、超高齡市場、ESG 趨勢 | `S1_長照保單競品分析報告.docx`、`S1_新版長照商品精算備忘錄.docx` |
| **Analyst** | 失能/失智發生率、三檔保費、CP 值 | `S1_長照精算原始資料.xlsx`、`S1_長照競品Dashboard.xlsx` |
| **Copilot** | 商品企劃完整脈絡 | `S1_安心久久商品企劃書.docx`、5 封 email thread |
