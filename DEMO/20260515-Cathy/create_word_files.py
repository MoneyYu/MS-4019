# -*- coding: utf-8 -*-
"""
MS-4019 國泰集團 Demo — 建立所有 Word 範例檔案 (14 份)

5 個場景：
  S1 國泰人壽 — 長照新商品開發
  S2 國泰世華 + 投信 — 財富管理投資建議
  S3 國泰金控 — 法遵與風險管理
  S4 跨子公司 — 數位轉型
  S5 國泰金控 + 投信 — 永續金融 ESG

每場景 2-3 份 Word（含 Researcher Agent / Analyst Agent 預埋素材與 Copilot 預留區塊）。
"""
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEMO-FILE")

CATHAY_GREEN = RGBColor(0, 102, 51)        # 國泰金控品牌綠
CATHAY_GOLD  = RGBColor(204, 153, 51)       # 點綴金
TEXT_GREY    = RGBColor(89, 89, 89)
HIGHLIGHT_RED = RGBColor(192, 0, 0)


def set_cell_shading(cell, color_hex):
    sh = cell._element.get_or_add_tcPr()
    el = sh.makeelement(qn('w:shd'), {
        qn('w:val'): 'clear', qn('w:color'): 'auto', qn('w:fill'): color_hex
    })
    sh.append(el)


def styled_table(doc, headers, rows, header_hex="006633"):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.size = Pt(10)
                r.font.name = "Microsoft JhengHei"
        set_cell_shading(cell, header_hex)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10)
                    r.font.name = "Microsoft JhengHei"
    return table


def add_title(doc, text):
    h = doc.add_heading(text, level=1)
    for run in h.runs:
        run.font.color.rgb = CATHAY_GREEN
    return h


def add_meta(doc, items):
    """items: list of (label, value)"""
    for label, value in items:
        p = doc.add_paragraph()
        run_l = p.add_run(f"{label}：")
        run_l.bold = True
        run_l.font.color.rgb = CATHAY_GREEN
        p.add_run(value)


def add_copilot_placeholder(doc, hint):
    """加上 Copilot 預留區塊（上課現場用 Copilot 補上）"""
    p = doc.add_paragraph()
    run = p.add_run(f"💡【此處待補：請用 Copilot 補上 {hint}】")
    run.font.color.rgb = HIGHLIGHT_RED
    run.bold = True
    run.font.italic = True


def setup_doc():
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Microsoft JhengHei"
    style.font.size = Pt(11)
    return doc


# ═══════════════════════════════════════════════════════════
# 場景一：國泰人壽 — 長照新商品開發
# ═══════════════════════════════════════════════════════════

def s1_long_term_care_competitor_analysis():
    """S1-Word-1：長照保單競品分析（Researcher Agent 主要素材）"""
    doc = setup_doc()
    add_title(doc, "長照保單競品分析報告")
    add_meta(doc, [
        ("文件編號", "CL-S1-CA-2026-001"),
        ("撰寫人",   "Christie Cline（商品企劃協理）"),
        ("協作者",   "Irvin Sayers（風險管理）、Joni Sherman（投信量化）"),
        ("撰寫日期", "2026 年 5 月（執行日 -3）"),
        ("文件目的", "為 2026 Q3 新長照商品定位提供市場與競品基礎研究"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、市場概況", level=2)
    doc.add_paragraph(
        "依國發會 2024 年人口推估，台灣 65 歲以上人口將於 2025 年達 19.8%（超高齡社會門檻 20% 將於 2026 年突破），"
        "失能/失智人口推估 91.5 萬人，但長照保險滲透率僅 4.2%，相較日本（27%）、美國（9%）仍有明顯成長空間。"
    )
    doc.add_paragraph(
        "本公司現有「國泰永康長照終身險」自 2018 年銷售以來累計有效契約 18.7 萬件，但近兩年新契約年成長率自 12% 降至 4.1%，"
        "顯示既有商品已進入成熟期，亟需新世代商品接棒。"
    )

    doc.add_heading("二、五大競品條款比較", level=2)
    styled_table(doc,
        ["項目", "本公司現行版", "富邦人壽", "南山人壽", "新光人壽", "三商美邦"],
        [
            ["商品名稱", "永康長照終身險", "守護一生長照", "美滿長照", "新光長照守護", "美邦長照樂活"],
            ["給付定義", "巴氏量表 ≤35 分", "巴氏量表 ≤30 分", "ADL 三項以上", "巴氏 + CDR 雙條件", "ADL 兩項以上"],
            ["免責期", "90 天", "90 天", "180 天", "90 天", "60 天"],
            ["每月給付（基本）", "NT$ 36,000", "NT$ 40,000", "NT$ 36,000", "NT$ 30,000", "NT$ 32,000"],
            ["保證給付期間", "180 個月", "180 個月", "120 個月", "240 個月", "180 個月"],
            ["保費（40 歲男）", "年繳 87,500", "年繳 92,000", "年繳 79,800", "年繳 105,000", "年繳 76,500"],
            ["失智保障", "輕度需追加附約", "包含 CDR ≥1", "另售失智專屬險", "包含 CDR ≥0.5", "輕度不保障"],
            ["居家照護給付", "無", "有，每月 5,000", "無", "有，每月 8,000", "無"],
        ]
    )

    doc.add_heading("三、本公司競爭定位 SWOT", level=2)
    styled_table(doc,
        ["面向", "內容", "策略意涵"],
        [
            ["S 優勢", "國泰金控通路最廣（5,200 業務員 + 168 分行）、品牌信任度第一（NPS 65）", "以通路 × 品牌力強化長期續保"],
            ["W 弱勢", "失智保障需附約、保費中段、居家照護未涵蓋", "新版主打「失智 × 居家」一張保單到位"],
            ["O 機會", "超高齡社會 2026 年正式達標、政府長照 3.0 上路、ESG 退休金需求", "與國泰投信合作推「長照 + ESG 投資型」"],
            ["T 威脅", "新光以保證給付 240 個月切入高資產客群、富邦居家照護給付加碼", "需在 2026 Q4 前推出回應方案"],
        ]
    )

    doc.add_heading("四、Researcher Agent 待整合題目", level=2)
    doc.add_paragraph("（此份報告將於 5/15 課程現場由 Researcher Agent 進一步整合下列外部資訊）：")
    bullets = [
        "日本介護保險制度近三年改革重點（特別是 2024 年改革對民間商品的影響）",
        "美國 LTCi (Long-Term Care Insurance) 市場萎縮原因與替代商品趨勢（hybrid 終身壽險 + LTC rider）",
        "金管會保險局針對長照險「失智輕度納入給付」的最新意見（2026 函釋）",
        "高齡化日韓對「居家失智照護科技」的補助政策",
        "ESG / 影響力投資型保單在歐洲市場的滲透率與定價結構",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("五、Analyst Agent 待計算題目", level=2)
    doc.add_paragraph("（此份報告中的數據將於課程現場由 Analyst Agent 與精算 Excel 結合進行下列分析）：")
    bullets = [
        "三檔費率方案（基本 / 進階 / 尊榮）在不同失能率假設下的損失率分佈",
        "保費敏感度：免責期 60 / 90 / 180 天對保費影響的試算",
        "競品保費 vs. 給付金額的「CP 值」量化比較矩陣",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_paragraph("─" * 50)
    add_copilot_placeholder(doc, "本報告 Executive Summary（200 字內，含 3 個關鍵數字 + 1 個策略建議）")

    output = os.path.join(OUTPUT_DIR, "S1_長照保單競品分析報告.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s1_long_term_care_actuarial_memo():
    """S1-Word-2：精算備忘錄（Analyst Agent 素材）"""
    doc = setup_doc()
    add_title(doc, "新版長照商品精算備忘錄")
    add_meta(doc, [
        ("文件編號", "CL-S1-AM-2026-002"),
        ("撰寫人",   "Irvin Sayers（風險管理副理）"),
        ("審核",     "外部簽證精算師 — 安永精算諮詢"),
        ("撰寫日期", "2026 年 5 月（執行日 -2）"),
        ("文件目的", "新版長照商品三檔費率方案精算依據與敏感度分析"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、精算假設總覽", level=2)
    styled_table(doc,
        ["假設項目", "數值", "資料來源"],
        [
            ["失能發生率（65 歲以上）", "男 1.85% / 女 2.42%（年）", "TMSC 2024 經驗表 + 衛福部長照數據"],
            ["失能持續期（中位數）", "男 4.2 年 / 女 5.7 年", "本公司舊版商品 2015-2024 經驗"],
            ["失智發生率", "65+ 7.8% / 75+ 18.4% / 85+ 36.2%", "台灣失智症協會 2024 報告"],
            ["利率（折現）", "1.50%（30 年期 IFRS17 折現曲線）", "金管會公布長期利率"],
            ["費用率", "首年 35% / 續年 8%", "公司預算"],
            ["解約率", "首年 8% / 5 年後 1.5%（穩態）", "舊版商品經驗"],
            ["醫療通膨", "年 3.8%（影響每月給付調整）", "中央銀行物價統計"],
        ]
    )

    doc.add_heading("二、三檔費率方案", level=2)
    styled_table(doc,
        ["方案", "每月給付", "保證給付期", "失智保障", "居家照護", "年繳保費（40M）"],
        [
            ["基本型", "NT$ 30,000", "180 月", "CDR ≥1", "—", "NT$ 68,400"],
            ["進階型", "NT$ 40,000", "180 月", "CDR ≥0.5", "每月 6,000", "NT$ 95,200"],
            ["尊榮型", "NT$ 60,000", "240 月", "CDR ≥0.5 + 失智專屬服務", "每月 12,000", "NT$ 158,000"],
        ]
    )

    doc.add_heading("三、敏感度分析結果（Monte Carlo 10 萬次）", level=2)
    styled_table(doc,
        ["敏感度因子", "基準值", "+10% 衝擊", "-10% 衝擊", "風險評等"],
        [
            ["失能發生率", "損失率 58.2%", "65.7%（+7.5pp）", "51.3%（-6.9pp）", "🔴 高"],
            ["失智發生率", "損失率 58.2%", "61.4%（+3.2pp）", "55.5%（-2.7pp）", "🟡 中"],
            ["長期折現率", "損失率 58.2%", "55.8%（-2.4pp）", "60.9%（+2.7pp）", "🟡 中"],
            ["醫療通膨", "損失率 58.2%", "63.1%（+4.9pp）", "53.8%（-4.4pp）", "🟡 中"],
            ["解約率", "損失率 58.2%", "59.5%（+1.3pp）", "57.0%（-1.2pp）", "🟢 低"],
        ]
    )

    doc.add_heading("四、與競品對比的精算觀察", level=2)
    doc.add_paragraph(
        "新光人壽尊榮版保證給付 240 個月，但其失能定義要求「巴氏量表 + CDR 雙條件」明顯較嚴格，"
        "我方建議在尊榮型採用「擇一條件即賠」設計，雖會推升損失率約 3.5pp，但可創造明顯產品差異。"
    )
    doc.add_paragraph(
        "富邦居家照護每月 5,000 元相對保守，新光則達 8,000 元；本案進階型 6,000 / 尊榮型 12,000 屬中高位定價，"
        "對高資產客群有吸引力，建議搭配國泰投信 ESG 投資型附約共售。"
    )

    doc.add_heading("五、風險警示", level=2)
    bullets = [
        "若 IFRS17 折現曲線下調超過 30bps（情境分析），尊榮型損失率將突破 65%，建議列入定期追蹤指標",
        "失能發生率為最敏感因子，建議每季比對舊版商品經驗值校準",
        "醫療通膨若連 3 年 >5%，需啟動費率調整條款（金管會核准前提）",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "本備忘錄結論段（含 3 個關鍵風險指標 + 給商審會的決策建議）")

    output = os.path.join(OUTPUT_DIR, "S1_新版長照商品精算備忘錄.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s1_product_proposal():
    """S1-Word-3：商品企劃書（內含 Researcher + Analyst 整合預留）"""
    doc = setup_doc()
    add_title(doc, "國泰人壽『安心久久』長照新商品企劃書")
    add_meta(doc, [
        ("文件編號", "CL-S1-PP-2026-003"),
        ("提案人",   "Christie Cline（商品企劃協理）"),
        ("贊助者",   "Lidia Holloway（數位金融長 / Sponsor）"),
        ("商審會議", "預定執行日 +3"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、商品定位與目標客群", level=2)
    doc.add_paragraph(
        "「安心久久」鎖定 35-55 歲都會中產與高資產雙客群，主打「失智 × 居家 × ESG」三合一保障，"
        "是國內首檔將投資型保單收益連動 ESG 主題基金的長照終身險。"
    )

    doc.add_heading("二、商品架構", level=2)
    styled_table(doc,
        ["元件", "說明"],
        [
            ["主約", "長照終身險（失能 + 失智擇一即賠）"],
            ["附約 A", "居家照護日額附約（每日 NT$ 200 起）"],
            ["附約 B", "ESG 投資連結附約（連動國泰投信 ESG 基金）"],
            ["豁免條款", "全殘 / 失能達 35 分以上免繳保費"],
        ]
    )

    doc.add_heading("三、上市時程", level=2)
    styled_table(doc,
        ["階段", "時程", "Owner"],
        [
            ["精算費率定稿", "T - 6 週", "Irvin"],
            ["金管會送審", "T - 5 週", "Johanna"],
            ["核保系統開發", "T - 4 週 ~ T - 1 週", "Isaiah"],
            ["業務員教育訓練", "T - 2 週", "Christie"],
            ["正式上市", "T", "Christie + Lidia"],
        ]
    )

    add_copilot_placeholder(doc, "本商品的『差異化價值主張』段落（請結合競品分析報告與精算備忘錄資訊）")
    add_copilot_placeholder(doc, "上市後 12 個月的關鍵 KPI 預估（首月、Q1、首年銷售件數與保費收入）")

    output = os.path.join(OUTPUT_DIR, "S1_安心久久商品企劃書.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景二：國泰世華 + 投信 — 財富管理投資建議
# ═══════════════════════════════════════════════════════════

def s2_global_market_outlook():
    """S2-Word-1：全球市場展望（Researcher 素材）"""
    doc = setup_doc()
    add_title(doc, "2026 Q3 全球市場展望與配置建議")
    add_meta(doc, [
        ("文件編號", "CL-S2-MO-2026-001"),
        ("撰寫人",   "Joni Sherman（國泰投信量化分析師）"),
        ("審閱",     "Lidia Holloway（CDO）、Isaiah Langer（世華數位金融部）"),
        ("撰寫日期", "執行日 -5"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、宏觀觀點", level=2)
    doc.add_paragraph(
        "美國 Fed 於 2026 年 4 月維持利率區間 4.25-4.50%，市場預期 9 月有 25bps 降息空間。"
        "歐洲央行 6 月可能進一步降息至 2.50%。日本央行已啟動三段式升息至 0.75%，日圓有望從 158 區間回升。"
    )
    doc.add_paragraph(
        "中國 2026 Q1 GDP 4.7%，仍處於『以舊換新』政策刺激後段，房市指標尚未明顯回穩。"
        "新興市場與台股因 AI 半導體供應鏈題材延續，預期相對抗跌。"
    )

    doc.add_heading("二、各區域配置建議", level=2)
    styled_table(doc,
        ["區域 / 資產", "本月建議", "上月", "變動", "主要邏輯"],
        [
            ["美股", "中性偏多 (+2)", "中性 (0)", "↑", "AI 資本支出仍強，估值接近 5 年中位數"],
            ["歐股", "中性偏空 (-1)", "中性偏空 (-1)", "—", "ECB 降息不確定性，工業景氣偏弱"],
            ["日股", "加碼 (+3)", "中性偏多 (+2)", "↑", "企業治理改革 + 日圓回升雙利"],
            ["新興市場", "中性 (0)", "中性偏空 (-1)", "↑", "美元指數見頂，資金有望回流"],
            ["台股", "加碼 (+3)", "加碼 (+3)", "—", "AI 供應鏈本益比 16.8 仍合理"],
            ["美債（長天期）", "加碼 (+2)", "中性 (0)", "↑", "降息循環啟動前布局"],
            ["黃金 / 大宗", "中性 (0)", "加碼 (+2)", "↓", "地緣政治風險溢價已反映"],
            ["REITs", "中性偏多 (+1)", "中性 (0)", "↑", "降息利多 + 通膨對沖價值"],
        ]
    )

    doc.add_heading("三、關鍵變數監控", level=2)
    bullets = [
        "美國通膨：核心 PCE 維持 2.4%，須觀察是否能順利回到 2%",
        "Fed 政策：6 月會議決議與點陣圖可能影響全年降息幅度",
        "中國刺激：4 月底政治局會議是否擴大消費補貼",
        "AI 資本支出：超大型雲服務商 Q2 財報是否維持高 capex 指引",
        "地緣政治：紅海航運、台海情勢、俄烏停火進度",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("四、Researcher Agent 整合題目", level=2)
    doc.add_paragraph("（請於課程現場用 Researcher Agent 補上）：")
    bullets = [
        "Fed 主席 Jerome Powell 5 月最新公開談話對降息路徑的暗示",
        "競品（中信、富邦、永豐）4 月私行月報的差異觀點",
        "最新 BofA Fund Manager Survey 對全球資金流向的反映",
        "Bridgewater、橋水基金 5 月最新市場觀點（公開資料）",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "本展望的 1 頁 Executive Summary（含 3 個資產類別建議 + 2 個風險提醒）")

    output = os.path.join(OUTPUT_DIR, "S2_2026Q3全球市場展望.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s2_client_portfolio_review():
    """S2-Word-2：客戶投資組合複核範本（Analyst 素材）"""
    doc = setup_doc()
    add_title(doc, "高資產客戶投資組合季度複核範本")
    add_meta(doc, [
        ("文件編號", "CL-S2-PR-2026-002"),
        ("撰寫人",   "Isaiah Langer（國泰世華數位金融部）"),
        ("協作",     "Joni Sherman（投信量化）"),
        ("適用客群", "金卡 / 鑽卡 / 私行客戶"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、客戶資料（範例）", level=2)
    styled_table(doc,
        ["項目", "內容"],
        [
            ["客戶代號", "VIP-2024-08321（去識別）"],
            ["風險屬性", "RR4（積極穩健）"],
            ["投資目標", "退休準備 + 子女教育，10 年期"],
            ["AUM", "NT$ 2,850 萬"],
            ["主要約束", "不投資加密貨幣、軍工、菸草"],
        ]
    )

    doc.add_heading("二、目前資產配置（截至執行日 -7）", level=2)
    styled_table(doc,
        ["資產類別", "市值（NT$ 萬）", "佔比", "目標", "偏離"],
        [
            ["全球股票（已開發）", "1,140", "40.0%", "38%", "+2.0pp"],
            ["全球股票（新興）", "285",   "10.0%", "12%", "-2.0pp"],
            ["全球債券（投資級）", "570",  "20.0%", "22%", "-2.0pp"],
            ["全球債券（高收益）", "228",  "8.0%",  "8%",  "—"],
            ["REITs",          "171",   "6.0%",  "5%",  "+1.0pp"],
            ["大宗商品 / 黃金", "143",   "5.0%",  "5%",  "—"],
            ["現金 / 短票",     "313",   "11.0%", "10%", "+1.0pp"],
        ]
    )

    doc.add_heading("三、關鍵績效指標", level=2)
    styled_table(doc,
        ["指標", "本季", "上季", "同期目標", "達成"],
        [
            ["年化報酬率", "+9.2%", "+7.5%", "+8.0%", "✅"],
            ["年化波動度", "11.8%", "12.5%", "≤13%", "✅"],
            ["Sharpe Ratio", "0.72", "0.55", "≥0.6", "✅"],
            ["Max Drawdown", "-7.4%", "-9.1%", "≥-10%", "✅"],
            ["費用率", "0.58%", "0.62%", "≤0.7%", "✅"],
        ]
    )

    doc.add_heading("四、Analyst Agent 待計算項目", level=2)
    bullets = [
        "計算各資產類別對總組合報酬的貢獻歸因（Brinson 法）",
        "與基準（60/40 全球配置）的超額報酬與資訊比率",
        "若再平衡至目標權重，預估需賣出 / 買入金額",
        "下一季在三種市場情境（基準 / 升息延後 / 衰退）下的預期報酬區間",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "客戶月報摘要段（含本季績效亮點 + 下季 1 個再平衡建議）")

    output = os.path.join(OUTPUT_DIR, "S2_高資產客戶組合複核範本.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景三：國泰金控 — 法遵與風險管理
# ═══════════════════════════════════════════════════════════

def s3_ifrs17_memo():
    """S3-Word-1：IFRS17 影響評估備忘錄"""
    doc = setup_doc()
    add_title(doc, "IFRS17 / ICS 2.0 第二年度影響評估備忘錄")
    add_meta(doc, [
        ("文件編號", "CL-S3-IF-2026-001"),
        ("撰寫人",   "Irvin Sayers（風險管理副理）"),
        ("協辦",     "Johanna Lorenz（法令遵循處）"),
        ("呈送對象", "風險委員會、董事會"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、IFRS17 / ICS 2.0 兩年來的關鍵影響", level=2)
    doc.add_paragraph(
        "本公司於 2025/1/1 同步導入 IFRS17 與 ICS 2.0。第一年度自有資本佔風險資本比率（資本適足率）"
        "從台版 RBC 的 320% 平移至 ICS 的 178%，第二年度 Q1 進一步因利率波動降至 165%，"
        "雖仍高於 100% 監理門檻，但與業界平均 195% 已有差距。"
    )

    doc.add_heading("二、關鍵指標趨勢", level=2)
    styled_table(doc,
        ["指標", "2025/Q1", "2025/Q4", "2026/Q1", "監理門檻", "業界平均"],
        [
            ["ICS 資本適足率", "178%", "172%", "165%", "100%", "195%"],
            ["CSM（合約服務邊際）", "382 億", "405 億", "418 億", "—", "—"],
            ["未來保險服務利潤", "412 億", "428 億", "439 億", "—", "—"],
            ["利率風險暴險", "中", "中高", "高", "—", "—"],
            ["對沖比率（利率）", "62%", "68%", "72%", "≥60%", "75%"],
        ]
    )

    doc.add_heading("三、與舊版 RBC 比較", level=2)
    doc.add_paragraph(
        "舊版 RBC 主要差異：(1) 折現率採市場利率而非鎖定利率；(2) 風險邊際以信賴區間 75% 計算（舊版為 60%）；"
        "(3) 新增營運風險、長壽風險的明確壓力測試要求。此三項合計推升所需資本約 NT$ 720 億。"
    )

    doc.add_heading("四、待 Researcher Agent 整合的外部資料", level=2)
    bullets = [
        "金管會保險局 2026 年 4 月最新監理函釋 / 公開談話",
        "亞洲三大同業（友邦、保誠、安達）IFRS17 第二年度揭露重點",
        "巴塞爾 III 終局版（Basel III Endgame）對銀行子公司資本要求的最新影響",
        "FSB 2026 年最新 G-SII（系統重要性保險）名單異動",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "本備忘錄總結（含未來 12 個月 3 大法遵風險 + 1 項提案）")

    output = os.path.join(OUTPUT_DIR, "S3_IFRS17_ICS2_影響評估備忘錄.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s3_aml_assessment():
    """S3-Word-2：AML 風險評估報告"""
    doc = setup_doc()
    add_title(doc, "AML / 防制洗錢 2026 Q1 風險評估報告")
    add_meta(doc, [
        ("文件編號", "CL-S3-AM-2026-002"),
        ("撰寫人",   "Johanna Lorenz（法遵稽核經理）"),
        ("協辦",     "Irvin Sayers（風險管理）"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、本季可疑交易申報（STR）統計", level=2)
    styled_table(doc,
        ["子公司", "監測警示", "覆核後申報 STR", "誤報率"],
        [
            ["國泰世華銀行", "12,485", "428", "96.6%"],
            ["國泰人壽", "1,243", "41", "96.7%"],
            ["國泰投信", "385", "12", "96.9%"],
            ["國泰證券", "642", "28", "95.6%"],
            ["合計", "14,755", "509", "96.6%"],
        ]
    )

    doc.add_heading("二、新興 AML 風險主題", level=2)
    bullets = [
        "虛擬資產服務商（VASP）灰色地帶交易：數位錢包對接傳統金融帳戶（持續上升）",
        "AI 生成合成身分（synthetic ID）開戶：本季偵測 17 起，較上季 +183%",
        "跨境快速轉帳濫用（特別是新南向 / 東南亞穩定幣管道）",
        "公司型保險商品（如躉繳投資型）異常解約洗錢",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("三、AI / 機器學習偵測效能", level=2)
    styled_table(doc,
        ["模型", "Precision", "Recall", "F1", "上線時間"],
        [
            ["規則引擎（既有）", "3.4%", "62%", "0.064", "2018"],
            ["XGBoost v2", "11.8%", "78%", "0.205", "2024 Q3"],
            ["GraphML（新）", "18.5%", "82%", "0.301", "2025 Q4 試行"],
        ]
    )

    add_copilot_placeholder(doc, "本季 STR 重點案例摘要（去識別化，3 個典型樣態）")
    add_copilot_placeholder(doc, "下季 AML 強化重點（含新規衝擊與內部資源建議）")

    output = os.path.join(OUTPUT_DIR, "S3_AML風險評估Q1報告.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s3_compliance_summary():
    """S3-Word-3：Q1 法遵摘要（給董事會）"""
    doc = setup_doc()
    add_title(doc, "國泰金控 2026 Q1 法令遵循執行摘要")
    add_meta(doc, [
        ("文件編號", "CL-S3-CS-2026-003"),
        ("撰寫人",   "Johanna Lorenz（法遵稽核經理）"),
        ("呈送對象", "稽核委員會、獨立董事"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、本季重大法規異動追蹤", level=2)
    styled_table(doc,
        ["編號", "法規名稱", "公布日期", "影響等級", "負責子公司"],
        [
            ["R-2026-001", "保險業辦理電子商務應注意事項修正", "2026/2/15", "🔴 高", "人壽 / 產險"],
            ["R-2026-002", "金融機構 AI 應用治理指引", "2026/3/1", "🟡 中", "全集團"],
            ["R-2026-003", "永續金融揭露準則 2.0", "2026/3/28", "🟡 中", "金控 / 投信"],
            ["R-2026-004", "個人資料保護法施行細則", "2026/4/12", "🟡 中", "全集團"],
            ["R-2026-005", "外匯管理及投資型保單規範", "2026/4/22", "🟢 低", "人壽"],
        ]
    )

    doc.add_heading("二、本季稽核發現重點", level=2)
    styled_table(doc,
        ["發現等級", "本季件數", "上季", "變動"],
        [
            ["🔴 重大", "2",  "4", "↓"],
            ["🟡 一般", "18", "23", "↓"],
            ["🟢 改進建議", "47", "52", "↓"],
        ]
    )

    doc.add_heading("三、待 Researcher / Analyst 補強", level=2)
    bullets = [
        "Researcher：金管會 2026 年金檢計畫重點（公開資料）整合",
        "Researcher：巴塞爾 III 終局版對台灣銀行業的最新影響評估",
        "Analyst：本季 STR、KYC、CDD 三大指標在子公司間的對比熱圖",
        "Analyst：與業界平均（金融研訓院公開資料）的 benchmark gap 量化",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "下季 3 大法遵優先工作（含資源需求與時程）")

    output = os.path.join(OUTPUT_DIR, "S3_2026Q1法遵執行摘要.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景四：跨子公司 — 數位轉型
# ═══════════════════════════════════════════════════════════

def s4_digital_blueprint():
    """S4-Word-1：數位轉型藍圖"""
    doc = setup_doc()
    add_title(doc, "國泰集團 2026-2028 數位轉型藍圖")
    add_meta(doc, [
        ("文件編號", "CL-S4-DB-2026-001"),
        ("撰寫人",   "Christie Cline（PMO 負責人）"),
        ("贊助者",   "Lidia Holloway（CDO）"),
        ("協作",     "Isaiah Langer（世華架構師）"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、三年策略目標", level=2)
    bullets = [
        "2026：完成關鍵核心系統雲原生改造（保單核心、銀行 OB、投信 OMS）",
        "2027：四大子公司客戶旅程數位整合，集團單一登入（SSO）+ 統一行動 App",
        "2028：以 GenAI 為核心的智能助理上線，覆蓋所有客戶觸點",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("二、五大支柱", level=2)
    styled_table(doc,
        ["支柱", "2026 重點", "2027 重點", "2028 重點"],
        [
            ["1. 雲端基礎建設", "Azure / AWS 雙雲落地", "DR + 多區複製", "邊緣運算"],
            ["2. 資料平台", "集團資料湖完成", "Customer 360 上線", "Real-time analytics"],
            ["3. AI / GenAI", "M365 Copilot 全員導入", "客戶服務 AI Agent", "投資 / 核保智能助理"],
            ["4. 數位通路", "行動 App 改版", "全通路一致體驗", "Conversational Banking"],
            ["5. 資安治理", "Zero Trust 啟動", "Zero Trust 全面落地", "AI 治理框架"],
        ]
    )

    doc.add_heading("三、Researcher Agent 整合題目", level=2)
    bullets = [
        "新加坡 DBS、星展銀行 GenAI 應用案例（公開報導 2025-2026）",
        "美國 JPMorgan COIN / IndexGPT 最新進展",
        "Open Banking 在英國、台灣、新加坡的滲透率對比",
        "金管會數位金融沙盒 2026 最新核准案例",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("四、Analyst Agent 整合題目", level=2)
    bullets = [
        "本集團數位通路使用率與客戶 NPS 趨勢（年度）",
        "投資金額對應業務指標（IT spend ratio 與營收成長率）",
        "與同業對比：Fintech 採用速度量化指標",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "三年投資總額分項 + 預期效益（含 KPI 達成預測）")

    output = os.path.join(OUTPUT_DIR, "S4_2026-2028數位轉型藍圖.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s4_fintech_benchmark():
    """S4-Word-2：Fintech 同業比較"""
    doc = setup_doc()
    add_title(doc, "全球 Fintech 同業數位能力比較研究")
    add_meta(doc, [
        ("文件編號", "CL-S4-FB-2026-002"),
        ("撰寫人",   "Isaiah Langer（世華 / 數位金融部）"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、九家比較對象", level=2)
    styled_table(doc,
        ["公司", "國家", "特徵", "本案借鏡重點"],
        [
            ["DBS",          "新加坡", "亞洲數位銀行領導者",         "Customer Journey Lab"],
            ["JPMorgan",     "美國",   "全球最大 IT 預算 ($17B/yr)", "GenAI 治理框架"],
            ["UBS",          "瑞士",   "私行 AI 投資建議",           "Hybrid advisor model"],
            ["Goldman Marcus","美國",  "純數位消金",                 "Onboarding flow"],
            ["Revolut",      "英國",   "Super App",                  "通路整合"],
            ["Nubank",       "巴西",   "新興市場數位銀行",           "客戶獲取成本"],
            ["Ping An Tech", "中國",   "保險科技規模化",             "理賠 AI"],
            ["MUFG",         "日本",   "傳統銀行轉型",               "雲遷移路徑"],
            ["KakaoBank",    "韓國",   "通訊軟體切入金融",           "行動體驗"],
        ]
    )

    doc.add_heading("二、五大能力維度評分（5 分制）", level=2)
    styled_table(doc,
        ["公司", "雲端", "資料/AI", "客戶體驗", "Open API", "資安"],
        [
            ["DBS",         "5", "5", "5", "4", "5"],
            ["JPMorgan",    "5", "5", "4", "5", "5"],
            ["UBS",         "4", "5", "4", "3", "5"],
            ["國泰集團（現況）", "3", "3", "4", "3", "4"],
            ["國泰集團（2028 目標）", "5", "5", "5", "5", "5"],
        ]
    )

    add_copilot_placeholder(doc, "Top 3 我們可立即學習的具體做法（含投入估計）")

    output = os.path.join(OUTPUT_DIR, "S4_全球Fintech同業比較研究.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景五：永續金融 ESG
# ═══════════════════════════════════════════════════════════

def s5_tcfd_draft():
    """S5-Word-1：TCFD 揭露草稿"""
    doc = setup_doc()
    add_title(doc, "國泰金控 2025 TCFD 氣候相關財務揭露報告（草稿）")
    add_meta(doc, [
        ("文件編號", "CL-S5-TC-2026-001"),
        ("撰寫人",   "Joni Sherman（投信量化）"),
        ("法遵審閱", "Johanna Lorenz"),
        ("撰寫日期", "執行日 -6"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、治理 (Governance)", level=2)
    doc.add_paragraph(
        "國泰金控於 2024 年成立『永續金融委員會』，由副董事長親自主持，每季召開一次。"
        "委員會下設氣候風險、永續商品、ESG 投資三個工作小組，由各子公司 C-suite 擔任召集人。"
    )

    doc.add_heading("二、策略 (Strategy)", level=2)
    doc.add_paragraph(
        "已承諾 SBTi 1.5°C 目標，2030 年自身營運碳排（Scope 1+2）較 2020 年減 50%、2050 年達淨零。"
        "投融資組合（Scope 3 第 15 類）2030 年減 38%，覆蓋電力、石化、水泥、鋼鐵四大高碳產業。"
    )

    doc.add_heading("三、風險管理 (Risk Management)", level=2)
    styled_table(doc,
        ["氣候風險類別", "情境", "影響時程", "影響程度", "因應措施"],
        [
            ["實體風險 - 颱風", "RCP 8.5", "短期 (1-3yr)", "中",   "理賠模型加碼、再保強化"],
            ["實體風險 - 海平面", "RCP 8.5", "長期 (10yr+)", "中",   "不動產組合區位調整"],
            ["轉型風險 - 政策", "1.5°C 路徑", "中期 (3-7yr)", "高",   "高碳產業曝險年降 5%"],
            ["轉型風險 - 技術", "綠色科技躍進", "中期",       "中",   "再生能源、儲能加碼"],
            ["轉型風險 - 訴訟", "氣候訴訟",   "中長期",       "低",   "強化 ESG 揭露品質"],
        ]
    )

    doc.add_heading("四、指標與目標 (Metrics & Targets)", level=2)
    styled_table(doc,
        ["指標", "2020 基準", "2025 實績", "2030 目標"],
        [
            ["自身營運碳排（tCO2e）", "82,400", "61,200", "41,200"],
            ["投融資組合碳排（百萬 tCO2e）", "18.4", "15.2", "11.4"],
            ["綠色金融餘額（億）", "1,250", "3,820", "6,500"],
            ["高碳資產佔投資比", "12.8%", "8.5%", "≤5%"],
            ["WACI（加權平均碳強度）", "245", "187", "≤140"],
        ]
    )

    doc.add_heading("五、Researcher 整合題目", level=2)
    bullets = [
        "TCFD 2024 年最新框架更新（公開）",
        "金管會 2026 年永續金融揭露 2.0 細則",
        "ISSB IFRS S2 與 TCFD 對應關係",
        "亞洲三大同業（中國信託、富邦金、玉山金）2025 TCFD 報告差異",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "TCFD 第六項『情境分析』段落（含 1.5°C / 2°C / 3°C 三情境的量化結果摘要）")

    output = os.path.join(OUTPUT_DIR, "S5_2025TCFD揭露報告草稿.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s5_net_zero_pathway():
    """S5-Word-2：淨零路徑研究"""
    doc = setup_doc()
    add_title(doc, "投融資組合 2050 淨零路徑研究")
    add_meta(doc, [
        ("文件編號", "CL-S5-NZ-2026-002"),
        ("撰寫人",   "Joni Sherman（投信）"),
        ("協作",     "Irvin Sayers（風險管理）"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、SBTi 高碳產業金融機構準則 (FI 1.0)", level=2)
    doc.add_paragraph(
        "本公司於 2024/8 提交 SBTi 承諾，於 2025/12 完成驗證。涵蓋四大產業（電力、石化、水泥、鋼鐵），"
        "其餘產業採用 PCAF 整體強度法。本研究檢視 2026-2030 五年路徑可行性。"
    )

    doc.add_heading("二、四大高碳產業曝險現況", level=2)
    styled_table(doc,
        ["產業", "投資金額 (億)", "WACI", "與基準比", "減碳路徑"],
        [
            ["電力（火力）", "85.2",  "385", "高 +18%", "2030 -45%"],
            ["石化", "62.1",  "212", "中 +5%",   "2030 -32%"],
            ["水泥", "18.4",  "528", "高 +24%", "2030 -38%"],
            ["鋼鐵", "31.6",  "415", "高 +12%", "2030 -42%"],
            ["合計", "197.3", "—",   "—",        "—"],
        ]
    )

    doc.add_heading("三、Analyst Agent 整合題目", level=2)
    bullets = [
        "情境分析：1.5°C / 2°C / 延誤轉型三情境下的 5 年累積投資損失",
        "個別發行人轉型評分（CA100+, TPI, ISS）整合計算",
        "綠色金融餘額成長 vs. 高碳曝險下降的『雙軸』達標監控",
    ]
    for b in bullets:
        doc.add_paragraph(b, style="List Bullet")

    add_copilot_placeholder(doc, "本研究結論段（含 3 個關鍵風險 + 1 個年度行動計畫）")

    output = os.path.join(OUTPUT_DIR, "S5_2050淨零路徑研究.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 額外：跨場景共用文件（湊滿 14 份）
# ═══════════════════════════════════════════════════════════

def cross_meeting_minutes():
    """跨場景：CDO 月會逐字稿（橫跨 5 個場景）"""
    doc = setup_doc()
    add_title(doc, "CDO 月會逐字稿 — 五大專案統合報告")
    add_meta(doc, [
        ("會議日期", "執行日 -6"),
        ("主持人",   "Lidia Holloway（CDO）"),
        ("出席",     "Christie / Irvin / Isaiah / Johanna / Joni / admin（觀察）"),
    ])
    doc.add_paragraph("─" * 50)

    speakers = [
        ("Lidia", "各位，這個月我們同時推動五個關鍵專案：長照新商品、財富管理升級、法遵風險強化、集團數位轉型、永續金融揭露。今天請每個 owner 用 5 分鐘報告現況。"),
        ("Christie", "長照商品『安心久久』競品研究已完成，發現富邦居家照護給付有提高跡象，我們的差異化要更明確。商審會我預計排在執行日 +3。"),
        ("Joni", "投信這邊財富管理的全球展望已經初稿，但 5 月 Fed 表態還沒明朗。另外我也在準備永續金融的 TCFD 草稿，預計下週末交件。"),
        ("Irvin", "IFRS17 第二年度的資本適足率掉到 165%，比業界 195% 落後，這是要立刻處理的。我這個月會提利率對沖加碼建議。"),
        ("Isaiah", "世華這邊的雲端基礎建設今年要把核心銀行帳務系統搬到 Azure。預算 6.8 億已批，但跨子公司資料治理規範還沒統一，這是瓶頸。"),
        ("Johanna", "本季法規異動有 5 件高 / 中影響等級，特別是 4/22 公布的外匯管理及投資型保單規範會直接影響長照新商品的 ESG 附約設計，請 Christie 注意。"),
        ("Lidia", "好。我聽到三個跨專案議題：一是長照商品的 ESG 附約涉及外匯規範；二是投資型保單需要法遵與商品同步；三是 Fintech 同業 GenAI 應用我們落後。請 Isaiah 整合這三件做行動方案，下次月會匯報。"),
        ("Christie", "我建議我們開始用 M365 Copilot 與 Researcher / Analyst Agent 來處理跨專案的整合。比如競品研究、法規追蹤、組合分析這些都很適合。"),
        ("Lidia", "好建議。把今天會議結論交給 Researcher Agent 整理，也讓 Analyst Agent 把五大專案的 KPI 跑一個 Dashboard 出來，我下週要看。散會。"),
    ]
    for sp, text in speakers:
        p = doc.add_paragraph()
        run_sp = p.add_run(f"{sp}：")
        run_sp.bold = True
        run_sp.font.color.rgb = CATHAY_GREEN
        p.add_run(text)

    add_copilot_placeholder(doc, "本次會議的『三大跨專案行動項目』摘要（含 Owner、時程、KPI）")

    output = os.path.join(OUTPUT_DIR, "CDO月會逐字稿_五大專案統合報告.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s4_nps_journey():
    """S4-Word-3：NPS 客戶旅程研究（補足 S4，並湊到 14 份）"""
    doc = setup_doc()
    add_title(doc, "集團客戶 NPS 旅程地圖 2026 Q1")
    add_meta(doc, [
        ("文件編號", "CL-S4-NJ-2026-003"),
        ("撰寫人",   "Christie Cline（PMO）"),
    ])
    doc.add_paragraph("─" * 50)

    doc.add_heading("一、各子公司 NPS 表現", level=2)
    styled_table(doc,
        ["子公司", "2025/Q1", "2025/Q4", "2026/Q1", "業界平均", "Gap"],
        [
            ["國泰人壽", "52", "55", "58", "48", "+10"],
            ["國泰世華", "61", "63", "62", "55", "+7"],
            ["國泰投信", "47", "50", "52", "45", "+7"],
            ["國泰證券", "42", "44", "46", "42", "+4"],
            ["集團平均", "55", "57", "58", "49", "+9"],
        ]
    )

    doc.add_heading("二、客戶旅程八階段 NPS", level=2)
    styled_table(doc,
        ["階段", "Touchpoint", "NPS", "痛點"],
        [
            ["1 認知", "廣告 / 社群", "32", "訊息一致性差"],
            ["2 比較", "官網 / 試算工具", "48", "資訊孤島"],
            ["3 簽約", "業務員 / 行動 App", "61", "—"],
            ["4 上手", "Onboarding", "55", "簡訊提醒過多"],
            ["5 使用", "App / Web", "58", "—"],
            ["6 服務", "客服 / 線上", "44", "等待時間長"],
            ["7 變更", "保全 / 異動", "38", "🔴 流程繁瑣"],
            ["8 終止", "解約 / 滿期", "62", "—"],
        ]
    )

    add_copilot_placeholder(doc, "三個 NPS 最低階段的 1 頁改善建議（含投資 ROI 預估）")

    output = os.path.join(OUTPUT_DIR, "S4_集團NPS客戶旅程2026Q1.docx")
    doc.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n📝 Generating Word files into: {OUTPUT_DIR}\n")

    # S1 — 國泰人壽 長照
    s1_long_term_care_competitor_analysis()
    s1_long_term_care_actuarial_memo()
    s1_product_proposal()

    # S2 — 國泰世華+投信 財富管理
    s2_global_market_outlook()
    s2_client_portfolio_review()

    # S3 — 國泰金控 法遵風險
    s3_ifrs17_memo()
    s3_aml_assessment()
    s3_compliance_summary()

    # S4 — 跨子公司 數位轉型
    s4_digital_blueprint()
    s4_fintech_benchmark()
    s4_nps_journey()

    # S5 — 永續金融 ESG
    s5_tcfd_draft()
    s5_net_zero_pathway()

    # 跨場景
    cross_meeting_minutes()

    print(f"\n✅ Total Word files generated.\n")
