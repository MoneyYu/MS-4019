# 場景三：國泰金控 — 法遵與風險管理 Demo 步驟

> **MS-4019 對應**：**Module 3b（Build and manage an agent — SharePoint Agent）**
> **時長**：30 分鐘（含 SharePoint Agent 建立）
> **主角（故事設定）**：Johanna Lorenz（法遵稽核經理）+ Irvin Sayers（風險管理副理）
> **協作（故事設定）**：Lidia Holloway（CDO）、Isaiah Langer（架構師）
> **操作帳號**：⚠️ **admin@moneyyu.com**（全程唯一登入帳號，不切換；Johanna/Irvin/Lidia/Isaiah 僅為 **故事中的角色背景**，不是登入帳號）
> **SharePoint Site**：`國泰金控 — 法令遵循處`（由 Phase 7 預建）

---

## 場景背景（30 秒講師開場）

> 「金管會在 4/22 一次公布三項新規，影響範圍橫跨整個國泰集團。Johanna 負責整合影響評估，5/15 要對董事會報告。
>
> 但問題是：
> - 她要看：3 個新規 × 4 個子公司 × 多個既有專案 = 數十份相關資料
> - 她要算：避險加碼成本對 ICS 的影響、AI 應用治理盤點、永續揭露差距
> - 她要決定：哪個子公司優先因應、哪些專案要調整時程
>
> 這個場景我們要展示：**從 Researcher / Analyst 用法，進階到建立『法遵新規追蹤』SharePoint Agent，讓未來新規一公布就自動分派**。」

---

## Demo 5 步驟

### Step 1：Researcher Agent — 三大新規影響盤點（6 min）

打開 M365 Copilot，切換到 **Researcher Agent**：

```
我（admin）正在協助 Johanna Lorenz（國泰金控法遵稽核經理）準備 5/15 董事會報告。金管會 4/22 同步公布三項新規。
請整合以下資訊，產出「新規影響盤點」摘要：

1. OneDrive 中的：
   - S3_IFRS17_ICS2_影響評估備忘錄.docx
   - S3_AML風險評估Q1報告.docx
   - S3_2026Q1法遵執行摘要.docx
   - S3 Email thread（特別是 Johanna 4/23 寄出的「金管會 4/22 三大新規」整合信）

2. 公開網路最新資料：
   - 金管會官網上述三項新規的完整條文（2026/4/22 公布）
   - 巴塞爾 III 終局版對台灣銀行業的最新影響評估
   - 同業（中信、富邦、玉山）對這三項新規的公開回應

最後請給董事會一段 200 字的摘要，包含：
- 三項新規的合規時程
- 對本集團 ICS 資本適足率的具體衝擊
- Johanna 的應變決策（採用三招併行方案）
```

**預期成果**：Researcher 整合 3 份 Word + 5 封 email + 公開金管會資料，產出董事會友善摘要。

---

### Step 2：Analyst Agent — 壓力測試與 KRI 熱圖（7 min）

切換到 **Analyst Agent**，附上 `S3_風險原始資料KRI_STR.xlsx` + `S3_風險指標Dashboard.xlsx`：

```
請基於這兩個檔案：

1. 從「KRI 月度資料」分頁找出近 6 個月 12 個 KRI 的趨勢
2. 計算「壓力測試情境」分頁中三大情境（輕度/重度/尾端）對 ICS 的衝擊
3. 找出最值得董事會關注的 3 個 KRI（依趨勢、距閾值距離綜合判斷）
4. 重新計算：如果按 Irvin 的應變方案（避險加碼到 70% + 美債切信用債 + 長照再保強化），ICS 從 165% 預估會落到多少？

最後產出：
- 一個「KRI 紅黃綠燈摘要表」
- 一段 100 字的「向董事會建議的應變優先級」
```

**預期成果**：Analyst 跑完 KRI 熱圖、壓力測試摘要、重算應變後 ICS（呼應 Irvin email 中的 168% 結果）。

---

### Step 3：用 Copilot 升級半成品 PPT（5 min）

打開 `S3_風險法遵董事會月報_半成品.pptx`：

```
這是 5/17 風險委員會董事會月報，請依序：

1. 第 1 頁 ICS 資本適足率：用 Analyst Agent 的 24 個月趨勢
2. 第 2 頁 KRI 熱圖：用 Analyst 剛才的「紅黃綠燈摘要表」
3. 第 3 頁壓力測試：三情境衝擊摘要
4. 第 4 頁 AML / 法遵重點：用 Researcher Agent 整合的內容（包含三大新規影響）

注意：第 4 頁要特別強調「集團 AI 應用登記簿」這個 Isaiah 提的解方。
```

---

### Step 4：建立『法遵新規追蹤』SharePoint Agent（10 min — Module 3 主軸）

> **這是本場景的精華 — 從「使用 Agent」進階到「建立 Agent」**
>
> 📌 **UI 註記**：以下操作以 2026 年 5 月 SharePoint 介面為準。若 UI 微調，操作意圖 = **在 SharePoint 文件庫範圍內建立 Custom Agent**，含 Name / Description / Instructions / Knowledge。

#### 4.1 打開預建的 SharePoint Site（Phase 7 已建好）

操作帳號：**admin@moneyyu.com**

打開 SharePoint，在「Following sites」或「Your sites」中找到 **「國泰金控 — 法令遵循處」**（alias: `cathay-compliance`）。

> 💡 這個 site **不需要從零建立** — Phase 7 (`Invoke-SeedSharePoint.ps1`) 已預建好，內含：
> - **文件庫**：7 份 S3 系列文件（與 OneDrive 雙存）
> - **3 個 List**：法規異動追蹤（10 條）、稽核發現追蹤（10 條）、AML STR 摘要（10 條）
>
> 學員看到這個 site，就能直接操作「在現成知識庫上建 Agent」 — 這比「從零建文件庫」更接近真實工作場景。

#### 4.2 建立 SharePoint Agent（學員觀摩 + 動手）

在 site 文件庫頂端右上角，點選 **`+ Add an agent`** → 選擇 **Custom agent**：

| 欄位 | 內容 |
|---|---|
| **Agent Name** | `國泰法遵新規追蹤 Agent` |
| **Description** | 本 Agent 負責：(1) 監控金管會新規異動；(2) 自動分派影響子公司；(3) 追蹤合規時程；(4) 產出董事會友善摘要 |
| **Knowledge Sources** | 自動 = 整個 `國泰金控 — 法令遵循處` site（含 7 docs + 3 lists）|
| **Capabilities** | ✅ 啟用 Web Search（讓 Agent 可整合金管會、保險局公開資訊）|

**Custom Instructions**（複製貼上）：

```
你是國泰金控法令遵循處的智能助理。當使用者詢問新規或合規時，請依序：

1. 先查閱 SharePoint 文件庫中相關歷史函釋與既有評估報告
2. 查閱「法規異動追蹤」List 找出已記錄的法規影響等級與時程
3. 查閱「稽核發現追蹤」List 找出相關稽核發現
4. 用 Web Search 確認最新公布（特別是金管會、保險局、銀行局官網）
5. 影響盤點：人壽 / 世華 / 投信 / 證券四個子公司，哪些受影響
6. 應變建議：必引用過往類似案例的應變方式

格式：用表格回覆 + 結尾給董事會友善的 100 字摘要。
語氣：精準、保守、明確標示「不確定」之處（如「待金管會函釋確認」）。
```

按 **Save**（先個人測試，**不 Publish 不 Share**避免送出至他人信箱）。

#### 4.3 試問 Agent

```
2026 年金管會 4 月有哪些新規？對國泰人壽的長照新商品開發有什麼具體影響？我們應該怎麼應變？請給我可以直接用在董事會的摘要。
```

**預期成果**：Agent 整合：
- 「法規異動追蹤」List 中 R-2026-001~004 的 4/22 新規記錄
- 「稽核發現追蹤」List 中 AUD-2026-Q1-001、002 的相關發現
- SharePoint 文件中的 IFRS17 與 AML 評估報告
- Web Search 補上的金管會最新函釋
- 給董事會可用的摘要（呼應 email 中已決議的「V1 用境內 ESG 基金」決定）

---

### Step 5：對比與結語（2 min）

**講師結語**：
> 「過去 Johanna 每次新規發布要花 5-7 天追蹤、影響盤點、跨子公司 sync。
>
> 建立 SharePoint Agent 後，**新規一發布即可自動產出影響評估初稿**，Johanna 只需審核而非從零開始。
>
> 更重要的是：這個 Agent 由法遵團隊『擁有』，可以隨時調整 instructions，符合金管會 4/22 AI 治理新規對『人類保有控制權』的要求。
>
> 這是 MS-4019 **Module 3b** 的核心：**No-code 建立的 Agent 直接被業務團隊擁有**。
>
> 而場景六（Module 3a）的 Copilot Chat Agent 是另一條路 — 跨來源、流程化。**兩條路並列，學員自選**。」

---

## 學員 Q&A 提示

| 學員可能問 | 講師可回答 |
|---|---|
| SharePoint Agent 跟 Copilot Studio Agent 有何差異？ | SharePoint Agent 完全 no-code，知識限於 SharePoint；Copilot Studio 可串外部 API 但需更多技術 |
| Agent 引用的金管會資料如何確保正確？ | Agent 標示出處，但合規責任仍在使用者；不能完全信任 |
| 怎麼確保 Agent 不會給出錯誤合規建議？ | Custom Instructions 中明確要求「不確定處要標示」；最終仍由 Johanna 審核 |
| 多個子公司能共用嗎？ | SharePoint Agent 可分享給特定群組或全公司，本案分享給 LidiaH + IrvinS |

---

## Researcher / Analyst / SharePoint Agent 對應預埋資料

| Agent | 預埋資料 |
|---|---|
| **Researcher** | `S3_IFRS17_ICS2_影響評估備忘錄.docx`、`S3_AML風險評估Q1報告.docx`、`S3_2026Q1法遵執行摘要.docx` |
| **Analyst** | `S3_風險原始資料KRI_STR.xlsx`、`S3_風險指標Dashboard.xlsx` |
| **SharePoint Agent**（建立用） | 上述三份 Word + 既有合規清單 |
| **Copilot** | 5 封跨部門 email + Teams S3 channel 4 個歷史討論 |
