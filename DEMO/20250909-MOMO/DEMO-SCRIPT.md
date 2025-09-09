# 完整 DEMO 腳本

涵蓋 **M365 Copilot in Excel / Word / Teams / Loop** 與 **Copilot Chat Agent**（含 Chat Agents 與 Copilot Studio 兩條路徑）。  
依提供的兩個 Excel 範例檔設計所有操作與提示語，並明確標注每一段的**時間、步驟、貼上即用的 Prompt、預期產出**與**風險備案**。  

> **資料來源**：[商店報表分析_範例.xls](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B517450B5-D078-4B91-891B-31C14FC5A641%7D&file=%E5%95%86%E5%BA%97%E5%A0%B1%E8%A1%A8%E5%88%86%E6%9E%90_%E7%AF%84%E4%BE%8B.xls&action=default&mobileredirect=true&EntityRepresentationId=f7d786f2-37c7-47ec-a9c6-43359efa94aa)、[法人大量訂購資料_範例.xlsx](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B6ED13A08-4550-4A3D-AB0A-DBE0C1AE399F%7D&file=%E6%B3%95%E4%BA%BA%E5%A4%A7%E9%87%8F%E8%A8%82%E8%B3%BC%E8%B3%87%E6%96%99_%E7%AF%84%E4%BE%8B.xlsx&action=default&mobileredirect=true&EntityRepresentationId=6ad03b5e-066f-4df6-a49d-5bd7c69d07b3)（多工作表）— 作為 Demo 與 Lab 的主資料集。[1](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B517450B5-D078-4B91-891B-31C14FC5A641%7D&file=%E5%95%86%E5%BA%97%E5%A0%B1%E8%A1%A8%E5%88%86%E6%9E%90_%E7%AF%84%E4%BE%8B.xls&action=default&mobileredirect=true)[2](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B6ED13A08-4550-4A3D-AB0A-DBE0C1AE399F%7D&file=%E6%B3%95%E4%BA%BA%E5%A4%A7%E9%87%8F%E8%A8%82%E8%B3%BC%E8%B3%87%E6%96%99_%E7%AF%84%E4%BE%8B.xlsx&action=default&mobileredirect=true)  
> **能力對齊**：M365 Copilot in PowerPoint（起稿、插入與連結 Excel 視覺、講者備忘、手冊）、Copilot Chat 具備 **Agents 與 IT 管控** 能力供知識型 Q&A。

---

## ⏱ 全時序（總長 180 分｜兩次 15 分休息）

- **00:00–00:10**　開場與情境（10 分）  
- **00:10–01:00**　**Demo 串接（50 分）**＝Excel（商店）→ Word → Loop → **PowerPoint 模組（新）** → Excel（法人「點題」）  
- **01:00–01:15**　**休息 #1（15 分）**  
- **01:15–02:05**　**Hands‑on（50 分）**＝分組實作（營運快報／法人風險）＋（可選）組內小型 Deck 產出  
- **02:05–02:20**　**休息 #2（15 分）**  
- **02:20–02:55**　**Copilot Chat Agent（35 分）**（含 Teams 匯報示範 5 分）  
- **02:55–03:00**　收尾（5 分）

---

# 00:00–00:10｜開場與情境（10 分）

**目標**：界定今日產出（管理摘要＋Agent 雛型）與資料範圍。  
**動作**  
1) 簡介兩份資料檔的用途與粒度（門店／法人）。[1](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B517450B5-D078-4B91-891B-31C14FC5A641%7D&file=%E5%95%86%E5%BA%97%E5%A0%B1%E8%A1%A8%E5%88%86%E6%9E%90_%E7%AF%84%E4%BE%8B.xls&action=default&mobileredirect=true)[2](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B6ED13A08-4550-4A3D-AB0A-DBE0C1AE399F%7D&file=%E6%B3%95%E4%BA%BA%E5%A4%A7%E9%87%8F%E8%A8%82%E8%B3%BC%E8%B3%87%E6%96%99_%E7%AF%84%E4%BE%8B.xlsx&action=default&mobileredirect=true)  
2) 在 Excel 開 Copilot（任一檔），先盤點工作表與欄位：

```text
請列出此活頁簿所有工作表與其主要欄位、資料列數，並指出是否包含空值或全 0 列。
```

---

# 00:10–01:00｜Demo 串接（50 分）

> **分配**：  
> • **Excel（商店）18 分** → **Word 8 分** → **Loop 7 分** → **PowerPoint 12 分（新）** → **Excel（法人）5 分（點題）**  
> 目的是形成「看數據 → 產摘要 → 任務化 → 變簡報」的完整閉環。

### Demo‑1｜Excel（商店）— 營運總覽與異常（18 分）  
**檔案**：[商店報表分析_範例.xls](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B517450B5-D078-4B91-891B-31C14FC5A641%7D&file=%E5%95%86%E5%BA%97%E5%A0%B1%E8%A1%A8%E5%88%86%E6%9E%90_%E7%AF%84%E4%BE%8B.xls&action=default&mobileredirect=true&EntityRepresentationId=f7d786f2-37c7-47ec-a9c6-43359efa94aa)（商店編號、mo 幣折抵、mo 抵用券、貨款、A–J 手續費…）。[1](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B517450B5-D078-4B91-891B-31C14FC5A641%7D&file=%E5%95%86%E5%BA%97%E5%A0%B1%E8%A1%A8%E5%88%86%E6%9E%90_%E7%AF%84%E4%BE%8B.xls&action=default&mobileredirect=true)

**步驟 & Prompt**
```text
以「商店編號」為粒度建立彙總表，新增：
- 折扣占比 = (mo幣折抵 + mo抵用券) / 貨款
- 手續費占比 = (A手續費+…+J手續費) / 貨款
- 淨收 = 貨款 - (mo幣折抵 + mo抵用券) - (所有手續費)
輸出前10與後10商店清單，並建立條形圖與「折扣占比 vs 手續費占比」雷達圖（Top5/Bottom5）。
在表中加入「異常」欄：若折扣占比或手續費占比 > 0.3 則標記「是」，並以紅底標示。
```

---

### Demo‑2｜Word — 150 字管理摘要（8 分）

**步驟 & Prompt**
```text
根據貼上的彙總表與圖表，撰寫 150 字內的週報管理摘要：
- 亮點 2 點、風險 2 點
- 下週行動建議 3 項（條列）
語氣：專業、中文（繁體）。
```

---

### Demo‑3｜Loop — 把異常轉任務（7 分）

**步驟 & Prompt**
```text
請將「異常商店一覽」轉成任務清單：
欄位＝商店編號｜問題說明｜負責人｜到期日（下週五）｜備註。
並根據彙總數據自動填入「問題說明」草案。
```

---

### 🆕 Demo‑4｜**PowerPoint（M365 Copilot in PPT）— 生成 Deck v1（12 分）**

> **能力對齊**：一鍵起稿、插入並連結 Excel 圖表、講者備忘、手冊頁（MS‑4018 的呈現能力場景）。  
> **輸入**：上一段產出的 **Word 摘要** 與 **Excel 圖表/表格**（保存在同一 SharePoint 位置）。

**步驟 1｜建立初稿（3–4 分）**
```text
建立 10 張投影片的〈Momoshop 營運與客戶獲利週報〉。
來源：
1) 這份 Word 摘要（插入連結）
2) 這兩個 Excel 視覺（Top/Bottom 門店條圖、雷達圖）
結構：標題、議程、門店洞察×2、綜合觀察、行動建議、下一步、Q&A。
語氣：專業、中文（繁體）；套用公司預設主題；每張附 1 句講者備忘。
```

**步驟 2｜插入/連結 Excel 視覺（3–4 分）**
```text
把「Top/Bottom 門店條形圖」與「雷達圖」插到對應章節，
與資料來源維持連結，並於圖下生成 2 句圖表解讀。
```

**步驟 3｜敘事與版面優化（2–3 分）**
```text
將本頁條列改為「問題→洞察→建議」結構，每點 ≤ 14 字；
統一品牌色系與圖例位置，標題套用同一樣式並左右對齊。
```

**步驟 4｜講者備忘＋手冊（1–2 分）**
```text
為每張投影片補齊 2–3 句講者備忘（轉場語＋風險提示），
並產出 1 頁「會後摘要（Handout）」供列印成 PDF。
```

> **備案**：若主題樣式未套用，追加指令「改用 *公司主題名稱* 重新排版」。

---

### Demo‑5｜Excel（法人）— 負毛利點題（5 分）

**檔案**：[法人大量訂購資料_範例.xlsx](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B6ED13A08-4550-4A3D-AB0A-DBE0C1AE399F%7D&file=%E6%B3%95%E4%BA%BA%E5%A4%A7%E9%87%8F%E8%A8%82%E8%B3%BC%E8%B3%87%E6%96%99_%E7%AF%84%E4%BE%8B.xlsx&action=default&mobileredirect=true&EntityRepresentationId=6ad03b5e-066f-4df6-a49d-5bd7c69d07b3)（*原始資料*）。[2](https://microsoftapc-my.sharepoint.com/personal/tzyu_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B6ED13A08-4550-4A3D-AB0A-DBE0C1AE399F%7D&file=%E6%B3%95%E4%BA%BA%E5%A4%A7%E9%87%8F%E8%A8%82%E8%B3%BC%E8%B3%87%E6%96%99_%E7%AF%84%E4%BE%8B.xlsx&action=default&mobileredirect=true)

**步驟 & Prompt**
```text
在〈原始資料〉新增「銷售額＝數量*單價」「毛利＝數量*(單價-成本價)」「毛利率＝(單價-成本價)/單價」。
按「發票抬頭」分群，列出毛利率<0 的商品 Top 清單與 Top10 風險客戶頁。
```

---

# 01:00–01:15｜休息 #1（15 分）

---

# 01:15–02:05｜Hands‑on（50 分）

> **分組**：A 組做「營運快報」，B 組做「法人風險」。  
> （各組可在段末 **可選 5 分** 用 Copilot in PPT 產出 4–6 張 Deck 小樣。）

### Lab‑A｜營運快報（25 分｜商店檔）
**Excel Prompt**
```text
建立每家商店 KPI 卡（淨收、折扣占比、手續費占比、異常旗標）。
輸出 Top5/Bottom5，並建立「費用率±10%」情境分析表與折線圖。
```
**Word Prompt**
```text
生成 120 字內的快報開場白＋ 2 條可執行建議（中文繁體、條列）。
```
**（可選）PPT Prompt（5 分）**
```text
把剛才的 Word 摘要與兩張圖表整理成 4–6 張投影片的小型簡報，
每張附 1 句講者備忘。
```

### Lab‑B｜法人風險（25 分｜法人檔）
**Excel Prompt**
```text
按「發票抬頭」彙總：銷售額、毛利、平均毛利率。
輸出每位客戶的「毛利率<0 的商品」及佔比，列出 Top10 風險客戶。
再按「廠商名稱」彙總，輸出平均毛利率<10% 的前三個問題商品。
```
**Word Prompt**
```text
生成給供應商的溝通草稿：主旨＋現況3點＋數據依據＋建議（調價/換品/包裝），200 字內。
```

---

# 02:05–02:20｜休息 #2（15 分）

---

# 02:20–02:55｜Copilot **Chat Agent**（35 分，含 Teams 匯報 5 分）

> **路徑 A（建議）**：**Copilot Chat Agents**（若租戶已啟用）  
> **路徑 B**：**Copilot Studio**（備援/進階）  
> Copilot Chat 具備 **Agents 與 IT 控制**；可將今天產出的 Word／Excel／PPT（或其所在的 SharePoint 資料夾）作為知識來源。

### 路徑 A｜Copilot Chat Agents（20–25 分）

**建立與設定**
- `New → Create agent` → 名稱：**Momoshop 營運助理**  
- **Knowledge**：連結含兩份 Excel 與今日 PPT／Word 的 SharePoint 資料夾  
- **Style & Safety**：中文（繁體）＋引用來源強制

**Instructions（貼上即可）**
```text
你是「Momoshop 營運助理」。任務：
1) 僅依據提供的 Excel/Word/PPT 內容作答；若資料不足，請明確說明未知並要求補件。
2) 固定輸出：〔結論 3–5 點〕＋〔引用來源：檔名/工作表/頁碼/欄位〕＋〔下一步建議〕。
3) 回覆語氣專業、中文（繁體）；避免臆測。
```

**測試題庫**
- 商店檔：
```text
列出折扣占比最高的 5 家商店與可能原因，附來源檔名/工作表/欄位。
```
- 法人檔：
```text
針對「生活有限公司」，列出毛利率 < 0 的商品與 3 點改善建議，附來源欄位。
```
- 摘要輸出：
```text
用 120 字為明天的週會寫一段開場白，涵蓋門店費用結構與法人毛利風險，並附兩個下一步。
```

### 路徑 B｜Copilot Studio（10–15 分）
- 建立同名 Agent → 貼上相同 Instructions  
- **Knowledge**：連結同一個 SharePoint 資料夾或直接上傳檔案  
- **Actions（可選）**：Power Automate 寄送「Top10 風險客戶」給採購群組  
- **Publish**：發佈到 Teams 供群組使用

### Teams 匯報（穿插 5 分）
**Teams Prompt**
```text
請用 5 句內總結今日門店與法人兩面向的洞察，@採購 與 @營運 召集明早 15 分 stand‑up，
並附上 Loop 任務與今日簡報 Deck 連結。
```

---

# 02:55–03:00｜收尾（5 分）
- 成果確認：**管理摘要＋PPT Deck v1＋Agent 雛型＋Loop 任務板**  
- 課後延伸：**MS‑4018（寫作/分析/簡報）→ MS‑4017（管理與擴充）→ PL‑7008（Studio 建置）**。

---

## 風險與臨場備案（講師小抄）
- **欄位/表名對不上**：先請 Copilot「列欄位並建議對映」，再套公式／樞紐。  
- **PPT 主題跑版**：下指令「改用 *公司主題名稱* 重新排版並對齊標題高度」。  
- **Agent 未附來源**：追加規則「所有回覆一律附檔名/工作表/頁碼/欄位」，再生。  
- **無 Chat Agents 權限**：改走 **Copilot Studio**（本腳本已備援）。