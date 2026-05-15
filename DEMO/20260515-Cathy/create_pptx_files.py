# -*- coding: utf-8 -*-
"""
MS-4019 國泰集團 Demo — 建立所有 PPT 範例檔案 (10 份)

10 份 = 5 場景 × 2 類型：
  類型 A 完整版（_完整版.pptx）— 結構完整、看起來像最終提報
  類型 B 半成品（_半成品.pptx）— 留 [此處待補] 標記，課程現場用 Copilot 升級

採用國泰金控品牌色：深綠 #006633 + 金 #CC9933。
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEMO-FILE")

CATHAY_GREEN = RGBColor(0x00, 0x66, 0x33)
CATHAY_GOLD  = RGBColor(0xCC, 0x99, 0x33)
LIGHT_GREEN  = RGBColor(0xC8, 0xE6, 0xD2)
DARK_GREY    = RGBColor(0x40, 0x40, 0x40)
TEXT_GREY    = RGBColor(0x59, 0x59, 0x59)
PLACEHOLDER_RED = RGBColor(0xC0, 0x00, 0x00)
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
SLIDE_W      = Inches(13.333)
SLIDE_H      = Inches(7.5)


def _font(run, size=18, bold=False, color=DARK_GREY, name="Microsoft JhengHei"):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def new_pres():
    pres = Presentation()
    pres.slide_width  = SLIDE_W
    pres.slide_height = SLIDE_H
    return pres


def add_title_slide(pres, title, subtitle, footer="國泰金控 — Confidential"):
    slide = pres.slides.add_slide(pres.slide_layouts[6])  # blank
    # Background bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(2.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = CATHAY_GREEN
    bar.line.fill.background()

    # Gold accent bar
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(2.2), SLIDE_W, Inches(0.12))
    accent.fill.solid()
    accent.fill.fore_color.rgb = CATHAY_GOLD
    accent.line.fill.background()

    # Title
    tx = slide.shapes.add_textbox(Inches(0.6), Inches(2.6), Inches(12), Inches(2.0))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = title
    _font(r, 40, bold=True, color=CATHAY_GREEN)

    # Subtitle
    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.LEFT
    r2 = p2.add_run()
    r2.text = subtitle
    _font(r2, 20, color=TEXT_GREY)

    # Footer
    ft = slide.shapes.add_textbox(Inches(0.6), Inches(7.0), Inches(12), Inches(0.4))
    p3 = ft.text_frame.paragraphs[0]
    r3 = p3.add_run()
    r3.text = footer
    _font(r3, 10, color=TEXT_GREY)

    return slide


def add_section_slide(pres, section_no, section_title):
    slide = pres.slides.add_slide(pres.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = CATHAY_GREEN

    # Section number
    tx = slide.shapes.add_textbox(Inches(0.6), Inches(2.5), Inches(12), Inches(1.0))
    p = tx.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = f"PART {section_no}"
    _font(r, 18, color=CATHAY_GOLD, bold=True)

    # Section title
    tx2 = slide.shapes.add_textbox(Inches(0.6), Inches(3.4), Inches(12), Inches(1.5))
    p2 = tx2.text_frame.paragraphs[0]
    r2 = p2.add_run()
    r2.text = section_title
    _font(r2, 44, color=WHITE, bold=True)


def add_content_slide(pres, title, bullets, page_no=None, footer="國泰金控 — Confidential"):
    slide = pres.slides.add_slide(pres.slide_layouts[6])
    # Title bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(0.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = CATHAY_GREEN
    bar.line.fill.background()

    tx = slide.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7))
    p = tx.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = title
    _font(r, 22, color=WHITE, bold=True)

    # Bullets
    body = slide.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(12), Inches(5.6))
    tf = body.text_frame
    tf.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if isinstance(b, dict):
            # heading + sub-bullets
            r = p.add_run()
            r.text = "▸ " + b["heading"]
            _font(r, 18, bold=True, color=CATHAY_GREEN)
            for s in b.get("subs", []):
                sp = tf.add_paragraph()
                sp.level = 1
                sr = sp.add_run()
                sr.text = "  • " + s
                _font(sr, 14, color=DARK_GREY)
        elif b.startswith("[此處待補"):
            r = p.add_run()
            r.text = "💡 " + b
            _font(r, 16, bold=True, color=PLACEHOLDER_RED)
            r.font.italic = True
        else:
            r = p.add_run()
            r.text = "▸ " + b
            _font(r, 16, color=DARK_GREY)

    # Footer
    ft = slide.shapes.add_textbox(Inches(0.4), Inches(7.0), Inches(12), Inches(0.4))
    p3 = ft.text_frame.paragraphs[0]
    r3 = p3.add_run()
    r3.text = footer + (f"   |   {page_no}" if page_no else "")
    _font(r3, 10, color=TEXT_GREY)

    return slide


def add_table_slide(pres, title, headers, rows, footer="國泰金控 — Confidential"):
    slide = pres.slides.add_slide(pres.slide_layouts[6])
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(0.8))
    bar.fill.solid(); bar.fill.fore_color.rgb = CATHAY_GREEN; bar.line.fill.background()

    tx = slide.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7))
    r = tx.text_frame.paragraphs[0].add_run(); r.text = title
    _font(r, 22, color=WHITE, bold=True)

    n_rows = len(rows) + 1
    n_cols = len(headers)
    table_h = Inches(min(5.5, 0.5 + n_rows * 0.42))
    table = slide.shapes.add_table(n_rows, n_cols, Inches(0.6), Inches(1.1), Inches(12), table_h).table

    # header
    for ci, h in enumerate(headers):
        c = table.cell(0, ci)
        c.fill.solid(); c.fill.fore_color.rgb = CATHAY_GREEN
        c.text_frame.text = ""
        p = c.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = str(h); _font(r, 12, bold=True, color=WHITE)

    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = table.cell(ri + 1, ci)
            c.text_frame.text = ""
            p = c.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run(); r.text = str(val); _font(r, 11, color=DARK_GREY)

    ft = slide.shapes.add_textbox(Inches(0.4), Inches(7.0), Inches(12), Inches(0.4))
    p3 = ft.text_frame.paragraphs[0]
    r3 = p3.add_run(); r3.text = footer
    _font(r3, 10, color=TEXT_GREY)


def add_placeholder_slide(pres, title, hint):
    """半成品專用：標題 + 一個大的 [此處待補] 提示框"""
    slide = pres.slides.add_slide(pres.slide_layouts[6])
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(0.8))
    bar.fill.solid(); bar.fill.fore_color.rgb = CATHAY_GREEN; bar.line.fill.background()
    tx = slide.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7))
    r = tx.text_frame.paragraphs[0].add_run(); r.text = title
    _font(r, 22, color=WHITE, bold=True)

    # Big placeholder box
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2), Inches(10.3), Inches(4))
    box.fill.solid(); box.fill.fore_color.rgb = LIGHT_GREEN
    box.line.color.rgb = CATHAY_GREEN
    box.line.width = Pt(2)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = "💡 此處待補"
    _font(r, 32, bold=True, color=PLACEHOLDER_RED)
    p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run(); r2.text = " "
    _font(r2, 12)
    p3 = tf.add_paragraph(); p3.alignment = PP_ALIGN.CENTER
    r3 = p3.add_run(); r3.text = hint
    _font(r3, 18, color=DARK_GREY)


# ═══════════════════════════════════════════════════════════
# 場景一：國泰人壽 — 長照新商品
# ═══════════════════════════════════════════════════════════

def s1_full():
    pres = new_pres()
    add_title_slide(pres, "「安心久久」長照新商品提案", "商審會提報 — 商品企劃部 / Christie Cline")
    add_section_slide(pres, "01", "市場機會")
    add_content_slide(pres, "1. 為什麼是現在？", [
        "2026 年台灣正式進入超高齡社會（65+ 達 20%）",
        "失能/失智人口推估 91.5 萬人，但長照險滲透率僅 4.2%",
        "舊版商品『永康長照』新契約年成長率自 12% 滑落至 4.1%",
        "金管會長照 3.0 上路 + 投資型保單規範鬆綁，創造新商品空間",
        "ESG 退休金與長照需求結合，是國泰投信協作的關鍵切點",
    ], page_no=3)
    add_table_slide(pres, "2. 五大競品條款比較",
        ["項目", "本公司", "富邦", "南山", "新光", "三商美邦"],
        [
            ["每月給付", "36,000", "40,000", "36,000", "30,000", "32,000"],
            ["保證給付", "180月", "180月", "120月", "240月", "180月"],
            ["免責期", "90天", "90天", "180天", "90天", "60天"],
            ["失智保障", "需附約", "CDR≥1", "另售", "CDR≥0.5", "輕度不保"],
            ["居家照護", "無", "5,000", "無", "8,000", "無"],
            ["保費（40M）", "87,500", "92,000", "79,800", "105,000", "76,500"],
        ])
    add_section_slide(pres, "02", "商品設計")
    add_content_slide(pres, "3. 三檔費率方案", [
        {"heading": "基本型 NT$ 30,000/月 — 年繳 68,400", "subs": [
            "保證給付 180 個月 / CDR ≥1 失智保障",
            "目標客群：35-45 歲入門族",
        ]},
        {"heading": "進階型 NT$ 40,000/月 — 年繳 95,200", "subs": [
            "CDR ≥0.5 + 居家照護日額 6,000",
            "目標客群：45-55 歲中產",
        ]},
        {"heading": "尊榮型 NT$ 60,000/月 — 年繳 158,000", "subs": [
            "保證給付 240 個月 + 失智專屬服務",
            "目標客群：55+ 高資產 + 國泰投信 ESG 附約",
        ]},
    ], page_no=5)
    add_table_slide(pres, "4. 精算敏感度（Monte Carlo 10 萬次）",
        ["敏感度因子", "+10% 衝擊", "-10% 衝擊", "風險"],
        [
            ["失能發生率", "損失率 +7.5pp", "-6.9pp", "🔴 高"],
            ["失智發生率", "+3.2pp", "-2.7pp", "🟡 中"],
            ["長期折現率", "-2.4pp", "+2.7pp", "🟡 中"],
            ["醫療通膨",   "+4.9pp", "-4.4pp", "🟡 中"],
            ["解約率",     "+1.3pp", "-1.2pp", "🟢 低"],
        ])
    add_section_slide(pres, "03", "上市計畫")
    add_content_slide(pres, "5. 上市時程", [
        "T - 6 週：精算費率定稿（Irvin）",
        "T - 5 週：金管會送審（Johanna）",
        "T - 4 ~ -1 週：核保系統開發（Isaiah）",
        "T - 2 週：業務員教育訓練（Christie）",
        "T = 2026 Q3：正式上市（Lidia 監督）",
    ], page_no=7)
    add_content_slide(pres, "6. 預期 KPI", [
        "首月銷售件數：1,800 件",
        "首季銷售件數：6,200 件",
        "首年銷售件數：21,500 件",
        "首年保費收入：21.4 億",
        "預估損失率：57.8%（在 55-60% 目標區間）",
        "綜合 CP 值：91（業界第 1）",
    ], page_no=8)
    pres.save(os.path.join(OUTPUT_DIR, "S1_安心久久商品提案_完整版.pptx"))
    print("  ✓ S1_安心久久商品提案_完整版.pptx")


def s1_draft():
    pres = new_pres()
    add_title_slide(pres, "「安心久久」長照新商品提案", "商審會提報（草稿）— 待 Copilot 完善")
    add_content_slide(pres, "1. 市場機會", [
        "2026 年台灣進入超高齡社會",
        "[此處待補：請用 Copilot 補上 5 個關鍵市場數據（含資料來源）]",
    ])
    add_placeholder_slide(pres, "2. 競品條款比較",
        "請用 Copilot：\n基於 OneDrive 中的「長照保單競品分析報告」整合 5 家競品比較表")
    add_content_slide(pres, "3. 三檔費率方案", [
        "基本型 / 進階型 / 尊榮型",
        "[此處待補：請用 Copilot 補上每方案的詳細參數與目標客群描述]",
    ])
    add_placeholder_slide(pres, "4. 精算敏感度",
        "請用 Analyst Agent：\n基於「長照精算原始資料.xlsx」產出五大敏感度因子的衝擊摘要")
    add_content_slide(pres, "5. 上市時程與 KPI", [
        "[此處待補：請用 Copilot 整合精算備忘錄 + 商品企劃書，產出 8 週時程甘特圖與首年 KPI 預估]",
    ])
    pres.save(os.path.join(OUTPUT_DIR, "S1_安心久久商品提案_半成品.pptx"))
    print("  ✓ S1_安心久久商品提案_半成品.pptx")


# ═══════════════════════════════════════════════════════════
# 場景二：財富管理
# ═══════════════════════════════════════════════════════════

def s2_full():
    pres = new_pres()
    add_title_slide(pres, "2026 Q3 全球市場展望", "國泰投信 / 國泰世華 — 投資觀點月報")
    add_section_slide(pres, "01", "宏觀環境")
    add_content_slide(pres, "1. 三大主軸", [
        "Fed：4.25-4.50% 維持，市場預期 9 月降 25bps",
        "ECB：6 月可能進一步降息至 2.50%",
        "BOJ：三段式升息至 0.75%，日圓有望從 158 區間回升",
        "中國：Q1 GDP 4.7%，房市尚未回穩",
        "AI 半導體供應鏈題材延續，台股相對抗跌",
    ], page_no=3)
    add_table_slide(pres, "2. 各區域配置建議",
        ["區域 / 資產", "本月", "上月", "變動", "邏輯"],
        [
            ["美股",       "+2", "0",   "↑", "AI capex 強"],
            ["日股",       "+3", "+2",  "↑", "公司治理 + 日圓回升"],
            ["新興市場",   "0",  "-1",  "↑", "美元見頂"],
            ["台股",       "+3", "+3",  "—", "AI 供應鏈"],
            ["美債（長）", "+2", "0",   "↑", "降息前布局"],
            ["黃金",       "0",  "+2",  "↓", "風險溢價已反映"],
        ])
    add_section_slide(pres, "02", "高資產組合績效")
    add_table_slide(pres, "3. 績效歸因（VIP-2024-08321 組合）",
        ["資產類別", "權重", "報酬", "貢獻 (pp)", "vs 基準"],
        [
            ["已開發股票", "40%", "9.8%", "3.92", "+0.85"],
            ["新興市場股", "10%", "5.2%", "0.52", "-0.32"],
            ["投資級債",   "20%", "1.8%", "0.36", "-0.15"],
            ["高收益債",   "8%",  "3.4%", "0.27", "+0.08"],
            ["REITs",      "6%",  "4.8%", "0.29", "+0.12"],
            ["商品/黃金",  "5%",  "-1.2%","-0.06","-0.18"],
            ["合計",       "100%","9.2%", "9.20", "+0.40"],
        ])
    add_content_slide(pres, "4. 風險指標", [
        "年化波動率 11.8%（目標 ≤13%）✅",
        "Sharpe Ratio 0.72（目標 ≥0.6）✅",
        "Max Drawdown -7.4%（目標 ≥-10%）✅",
        "Information Ratio 0.32（目標 ≥0.25）✅",
        "VaR(95%, 月) -5.2%（目標 ≥-7%）✅",
    ], page_no=6)
    add_section_slide(pres, "03", "下季建議")
    add_content_slide(pres, "5. 三大行動", [
        "減碼歐股（中性偏空）→ 加碼美債（中性 → 加碼）",
        "新興市場由中性偏空調至中性，準備分批進場",
        "若 Fed 6 月會議鴿派，啟動再平衡：股債 60/40 → 65/35",
        "ESG / 永續主題基金加碼 5%，搭配長照新商品銷售",
    ], page_no=7)
    pres.save(os.path.join(OUTPUT_DIR, "S2_2026Q3市場展望_完整版.pptx"))
    print("  ✓ S2_2026Q3市場展望_完整版.pptx")


def s2_draft():
    pres = new_pres()
    add_title_slide(pres, "2026 Q3 全球市場展望", "客戶月報草稿 — 待 Copilot 完善")
    add_content_slide(pres, "1. 宏觀環境", [
        "Fed / ECB / BOJ / 中國 / AI 主題",
        "[此處待補：請用 Copilot 補上各區域最新政策利率與市場共識]",
    ])
    add_placeholder_slide(pres, "2. 區域配置矩陣",
        "請用 Copilot：\n基於「全球市場原始資料.xlsx」產出 8 大資產類別配置表（含上月對比）")
    add_placeholder_slide(pres, "3. 客戶組合績效歸因",
        "請用 Analyst Agent：\n基於「組合績效Dashboard.xlsx」產出 Brinson 歸因摘要")
    add_content_slide(pres, "4. 下季三大行動", [
        "[此處待補：請用 Copilot 整合本月觀點 + 客戶風險屬性，提出 3 個具體再平衡建議]",
    ])
    pres.save(os.path.join(OUTPUT_DIR, "S2_2026Q3市場展望_半成品.pptx"))
    print("  ✓ S2_2026Q3市場展望_半成品.pptx")


# ═══════════════════════════════════════════════════════════
# 場景三：法遵風險
# ═══════════════════════════════════════════════════════════

def s3_full():
    pres = new_pres()
    add_title_slide(pres, "2026 Q1 風險與法遵董事會月報", "風險委員會 / 稽核委員會聯席會議")
    add_section_slide(pres, "01", "資本與風險")
    add_content_slide(pres, "1. ICS 資本適足率", [
        "本月：165%（業界 195%，落後 30pp）",
        "Q1 變動：172% → 165%（-7pp，主因利率波動）",
        "監理門檻 100% / 內部目標 150% — 仍充足",
        "建議：利率對沖比率提升至 75%，降低敏感度",
    ], page_no=3)
    add_table_slide(pres, "2. KRI 熱圖",
        ["KRI", "本月", "上月", "閾值", "狀態"],
        [
            ["違約率(%)",     "0.42", "0.38", "≤0.50", "🟢"],
            ["VaR 利用率(%)", "62",   "58",   "≤85",   "🟢"],
            ["利率 BPV",      "23",   "18",   "≤25",   "🟡"],
            ["LCR(%)",        "132",  "138",  "≥100",  "🟢"],
            ["ICS(%)",        "165",  "172",  "≥150",  "🟡"],
            ["WACI",          "187",  "192",  "≤220",  "🟢"],
        ])
    add_section_slide(pres, "02", "壓力測試")
    add_table_slide(pres, "3. 三大壓力情境衝擊",
        ["指標", "基準", "輕度衰退", "重度衰退", "尾端風險"],
        [
            ["GDP 衝擊",       "0%",   "-1.2%", "-3.5%", "-6.8%"],
            ["違約率",         "0.42%","0.78%", "1.45%", "3.20%"],
            ["ICS",            "165%", "152%",  "131%",  "108%"],
            ["LCR",            "132%", "121%",  "108%",  "95%"],
            ["稅前淨利衝擊",   "0%",   "-12%",  "-38%",  "-72%"],
            ["相對監理門檻",   "充足", "充足",  "邊際",  "🔴 不足"],
        ])
    add_section_slide(pres, "03", "AML 與法遵")
    add_content_slide(pres, "4. AML / STR 重點", [
        "本季 STR 申報：509 件（誤報率 96.6%）",
        "新興風險：合成身分開戶 +183%、VASP 對接、新南向穩定幣",
        "GraphML 偵測模型 F1 從 0.205 → 0.301（+47%）",
        "建議：擴大 GraphML 至全集團，預估誤報率可降至 95.2%",
    ], page_no=6)
    add_content_slide(pres, "5. 重大法規追蹤", [
        "🔴 保險業電子商務應注意事項修正（影響長照新商品）",
        "🟡 金融機構 AI 應用治理指引（影響 GraphML、Copilot）",
        "🟡 永續金融揭露準則 2.0（影響 TCFD 報告）",
        "🟡 個資法施行細則（影響 KYC、客戶資料應用）",
        "🟢 外匯管理及投資型保單（影響 ESG 附約）",
    ], page_no=7)
    pres.save(os.path.join(OUTPUT_DIR, "S3_風險法遵董事會月報_完整版.pptx"))
    print("  ✓ S3_風險法遵董事會月報_完整版.pptx")


def s3_draft():
    pres = new_pres()
    add_title_slide(pres, "2026 Q1 風險與法遵董事會月報", "草稿版 — 待 Copilot 完善")
    add_placeholder_slide(pres, "1. ICS 資本適足率",
        "請用 Analyst Agent：\n基於「風險原始資料KRI_STR.xlsx」與「風險指標Dashboard.xlsx」整合 24 個月趨勢")
    add_placeholder_slide(pres, "2. KRI 熱圖",
        "請用 Copilot：\n基於 KRI 月度資料產出 8 個關鍵指標的本月 vs 上月對比")
    add_placeholder_slide(pres, "3. 壓力測試",
        "請用 Analyst Agent：\n基於「風險指標Dashboard.xlsx」的「壓力測試情境」分頁產出董事會友善摘要")
    add_content_slide(pres, "4. AML / 法遵重點", [
        "[此處待補：請用 Researcher Agent + Copilot 整合 AML 風險評估報告 + 法遵摘要 + IFRS17 備忘錄，提出 5 個重點]",
    ])
    pres.save(os.path.join(OUTPUT_DIR, "S3_風險法遵董事會月報_半成品.pptx"))
    print("  ✓ S3_風險法遵董事會月報_半成品.pptx")


# ═══════════════════════════════════════════════════════════
# 場景四：數位轉型
# ═══════════════════════════════════════════════════════════

def s4_full():
    pres = new_pres()
    add_title_slide(pres, "國泰集團 2026-2028 數位轉型藍圖", "Steering Committee — Q2 提報")
    add_section_slide(pres, "01", "策略與支柱")
    add_content_slide(pres, "1. 三年策略目標", [
        "2026：核心系統雲原生改造（保單核心、銀行 OB、投信 OMS）",
        "2027：四大子公司客戶旅程整合 + 集團 SSO + 統一行動 App",
        "2028：以 GenAI 為核心的智能助理覆蓋所有客戶觸點",
        "投資總額：53.7 億 / 三年 = 13.5 + 17.9 + 22.3",
    ], page_no=3)
    add_table_slide(pres, "2. 五大支柱關鍵指標",
        ["支柱", "2025 實績", "2026 目標", "2028 願景"],
        [
            ["雲端化(%)",          "32",  "55",  "90"],
            ["數位 MAU(萬)",       "495", "620", "920"],
            ["集團 NPS",           "57",  "60",  "68"],
            ["數位收入佔比(%)",    "31",  "42",  "65"],
            ["AI 案件覆蓋率(%)",   "21",  "45",  "80"],
            ["Open API 數",        "84",  "130", "280"],
        ])
    add_section_slide(pres, "02", "客戶旅程")
    add_table_slide(pres, "3. 客戶旅程 NPS：本集團 vs. 業界",
        ["階段", "本集團", "業界平均", "Gap"],
        [
            ["1 認知",  "32", "28", "+4"],
            ["3 簽約",  "61", "52", "+9"],
            ["4 上手",  "55", "48", "+7"],
            ["6 服務",  "44", "42", "+2"],
            ["7 變更",  "38", "41", "🔴 -3"],
            ["8 終止",  "62", "55", "+7"],
        ])
    add_section_slide(pres, "03", "Fintech 同業 benchmark")
    add_table_slide(pres, "4. 五大能力評分（5 分制）",
        ["公司", "雲端", "資料/AI", "客戶體驗", "Open API", "資安"],
        [
            ["DBS",            "5", "5", "5", "4", "5"],
            ["JPMorgan",       "5", "5", "4", "5", "5"],
            ["UBS",            "4", "5", "4", "3", "5"],
            ["國泰（現況）",   "3", "3", "4", "3", "4"],
            ["國泰（2028 目標）", "5", "5", "5", "5", "5"],
        ])
    add_content_slide(pres, "5. 預期 ROI", [
        "2026 年化效益：8.5 億 / 投資 13.5 億 = ROI 63%",
        "2027 年化效益：18.4 億 / 投資 17.9 億 = ROI 102%",
        "2028 年化效益：32.6 億 / 投資 22.3 億 = ROI 146%",
        "三年累積投資 53.7 億，三年累積效益 59.5 億",
    ], page_no=6)
    pres.save(os.path.join(OUTPUT_DIR, "S4_數位轉型藍圖_完整版.pptx"))
    print("  ✓ S4_數位轉型藍圖_完整版.pptx")


def s4_draft():
    pres = new_pres()
    add_title_slide(pres, "國泰集團 2026-2028 數位轉型藍圖", "草稿版 — 待 Copilot 完善")
    add_content_slide(pres, "1. 三年策略目標", [
        "2026 / 2027 / 2028 三階段",
        "[此處待補：請用 Copilot 補上三年具體里程碑與投資金額]",
    ])
    add_placeholder_slide(pres, "2. 五大支柱 KPI",
        "請用 Copilot：\n基於「數位轉型KPI_Dashboard.xlsx」產出三年路徑表")
    add_placeholder_slide(pres, "3. 客戶旅程 NPS",
        "請用 Analyst Agent：\n基於「通路NPS月度原始.xlsx」產出八階段 vs 業界對比")
    add_placeholder_slide(pres, "4. Fintech 同業 benchmark",
        "請用 Researcher Agent：\n基於「全球Fintech同業比較研究.docx」+ 公開資料更新最新案例")
    add_content_slide(pres, "5. ROI 預估", [
        "[此處待補：請用 Analyst Agent 計算三年累積投資、效益、淨現值（NPV）]",
    ])
    pres.save(os.path.join(OUTPUT_DIR, "S4_數位轉型藍圖_半成品.pptx"))
    print("  ✓ S4_數位轉型藍圖_半成品.pptx")


# ═══════════════════════════════════════════════════════════
# 場景五：永續金融 ESG
# ═══════════════════════════════════════════════════════════

def s5_full():
    pres = new_pres()
    add_title_slide(pres, "2025 TCFD 氣候相關財務揭露報告", "永續金融委員會 — 季度提報")
    add_section_slide(pres, "01", "TCFD 四大支柱")
    add_content_slide(pres, "1. 治理 (Governance)", [
        "永續金融委員會（副董主持，每季召開）",
        "下設氣候風險、永續商品、ESG 投資三個工作小組",
        "各子公司 C-suite 擔任工作小組召集人",
        "ESG 績效已納入高階經理人 KPI（占 15%）",
    ], page_no=3)
    add_content_slide(pres, "2. 策略 (Strategy)", [
        "SBTi 1.5°C 目標已驗證：2030 自身 -50%、2050 淨零",
        "投融資組合 2030 -38%（覆蓋電力、石化、水泥、鋼鐵）",
        "永續商品系列：ESG 基金 + 綠色融資 + 投資型保單 ESG 附約",
        "2025 綠色金融餘額 3,820 億，2030 目標 6,500 億",
    ], page_no=4)
    add_table_slide(pres, "3. 風險管理 — 氣候風險矩陣",
        ["風險類別", "情境", "時程", "影響", "因應"],
        [
            ["實體 - 颱風",   "RCP 8.5", "短期",   "中", "理賠 + 再保"],
            ["實體 - 海平面", "RCP 8.5", "長期",   "中", "區位調整"],
            ["轉型 - 政策",   "1.5°C",   "中期",   "高", "高碳 -5%/年"],
            ["轉型 - 技術",   "綠色躍進","中期",   "中", "再生 + 儲能"],
            ["轉型 - 訴訟",   "氣候訴訟","中長期", "低", "強化揭露"],
        ])
    add_section_slide(pres, "02", "指標與目標")
    add_table_slide(pres, "4. 關鍵 ESG 指標",
        ["指標", "2020 基準", "2025 實績", "2030 目標"],
        [
            ["自身營運碳排（tCO2e）",      "82,400",  "61,200", "41,200"],
            ["投融資組合碳排（百萬 tCO2e）","18.4",   "15.2",   "11.4"],
            ["綠色金融餘額（億）",         "1,250",   "3,820",  "6,500"],
            ["高碳資產佔比",               "12.8%",   "8.5%",   "≤5%"],
            ["WACI",                       "245",     "187",    "≤140"],
        ])
    add_section_slide(pres, "03", "同業 benchmark")
    add_table_slide(pres, "5. TCFD 揭露品質：本公司 vs 同業",
        ["公司", "治理", "策略", "風險", "目標", "合計"],
        [
            ["國泰金", "22", "24", "22", "20", "88"],
            ["中信金", "20", "22", "22", "21", "85"],
            ["富邦金", "22", "24", "21", "20", "87"],
            ["玉山金", "23", "24", "22", "20", "89"],
            ["業界平均", "18", "20", "19", "17", "74"],
        ])
    pres.save(os.path.join(OUTPUT_DIR, "S5_2025TCFD揭露報告_完整版.pptx"))
    print("  ✓ S5_2025TCFD揭露報告_完整版.pptx")


def s5_draft():
    pres = new_pres()
    add_title_slide(pres, "2025 TCFD 氣候相關財務揭露報告", "草稿版 — 待 Copilot 完善")
    add_content_slide(pres, "1. 治理", [
        "[此處待補：請用 Copilot 整合「TCFD揭露報告草稿.docx」第一節，產出三條重點]",
    ])
    add_content_slide(pres, "2. 策略", [
        "SBTi 1.5°C / 2030 / 2050 目標",
        "[此處待補：請用 Copilot 補上四大子公司各自策略行動]",
    ])
    add_placeholder_slide(pres, "3. 風險管理矩陣",
        "請用 Copilot：\n基於「2050淨零路徑研究.docx」整合五大氣候風險矩陣")
    add_placeholder_slide(pres, "4. 關鍵指標表",
        "請用 Analyst Agent：\n基於「組合碳足跡原始資料.xlsx」+「ESG淨零Dashboard.xlsx」產出 5 大指標進度表")
    add_placeholder_slide(pres, "5. 同業 benchmark",
        "請用 Researcher Agent：\n更新中信、富邦、玉山金 2025 TCFD 報告最新分數")
    pres.save(os.path.join(OUTPUT_DIR, "S5_2025TCFD揭露報告_半成品.pptx"))
    print("  ✓ S5_2025TCFD揭露報告_半成品.pptx")


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n📽️ Generating PPT files into: {OUTPUT_DIR}\n")

    s1_full()
    s1_draft()
    s2_full()
    s2_draft()
    s3_full()
    s3_draft()
    s4_full()
    s4_draft()
    s5_full()
    s5_draft()

    print(f"\n✅ Total PPT files generated.\n")
