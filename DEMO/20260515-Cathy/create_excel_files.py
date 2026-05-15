# -*- coding: utf-8 -*-
"""
MS-4019 國泰集團 Demo — 建立所有 Excel 範例檔案 (10 份)

10 份 = 5 場景 × 2 類型：
  類型 A 純資料表（給 Analyst Agent 自行分析用，扁平化、無 chart）
  類型 B 預製分析（含 pivot、chart、KPI 摘要，模擬日常工作檔）
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, PieChart, Reference, BarChart3D
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.table import Table, TableStyleInfo
import os, random
from datetime import datetime, timedelta

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEMO-FILE")

random.seed(20260515)

# ── Styles ──
HEADER_FONT = Font(name="Microsoft JhengHei", bold=True, size=11, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="006633", end_color="006633", fill_type="solid")
TITLE_FONT  = Font(name="Microsoft JhengHei", bold=True, size=14, color="006633")
DATA_FONT   = Font(name="Microsoft JhengHei", size=10)
THIN = Border(left=Side(style="thin"), right=Side(style="thin"),
              top=Side(style="thin"), bottom=Side(style="thin"))
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT   = Alignment(horizontal="left",   vertical="center", wrap_text=True)


def style_header(ws, row, n_cols, fill=None):
    fill = fill or HEADER_FILL
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HEADER_FONT
        cell.fill = fill
        cell.alignment = CENTER
        cell.border = THIN


def style_data(ws, r0, r1, n_cols, align=CENTER):
    for r in range(r0, r1 + 1):
        for c in range(1, n_cols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = DATA_FONT
            cell.alignment = align
            cell.border = THIN


def auto_width(ws, min_w=10, max_w=32):
    for col in ws.columns:
        L = get_column_letter(col[0].column)
        m = 0
        for c in col:
            if c.value is not None:
                m = max(m, len(str(c.value)))
        ws.column_dimensions[L].width = min(max(m + 4, min_w), max_w)


def add_excel_table(ws, ref, name):
    tab = Table(displayName=name, ref=ref)
    tab.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium9", showFirstColumn=False,
        showLastColumn=False, showRowStripes=True, showColumnStripes=False,
    )
    ws.add_table(tab)


def add_title_row(ws, title, n_cols, row=1):
    ws.cell(row=row, column=1, value=title).font = TITLE_FONT
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=n_cols)
    ws.cell(row=row, column=1).alignment = LEFT


# ═══════════════════════════════════════════════════════════
# 場景一：國泰人壽 — 長照新商品
# ═══════════════════════════════════════════════════════════

def s1_actuarial_data():
    """S1-Excel-1 (純資料表)：長照精算原始資料"""
    wb = openpyxl.Workbook()

    # Sheet 1: 失能發生率經驗表
    ws = wb.active
    ws.title = "失能發生率經驗表"
    ws.sheet_properties.tabColor = "006633"
    headers = ["年齡", "性別", "失能發生率(%)", "失能持續年(中位數)", "資料來源年度", "樣本數"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header(ws, 1, len(headers))

    rows = []
    ages = list(range(40, 91, 5))
    base_rates_male = {40:0.08,45:0.12,50:0.18,55:0.27,60:0.42,65:0.71,70:1.18,75:2.05,80:3.62,85:5.84,90:8.42}
    for age in ages:
        m = base_rates_male[age]
        f = round(m * 1.31, 3)  # female slightly higher
        rows.append([age, "男", m,         round(2.8 + age*0.04, 1), 2024, random.randint(5000, 22000)])
        rows.append([age, "女", f,         round(3.5 + age*0.05, 1), 2024, random.randint(5000, 22000)])
    for r in rows:
        ws.append(r)
    style_data(ws, 2, len(rows) + 1, len(headers))
    add_excel_table(ws, f"A1:F{len(rows) + 1}", "tbl_disability")
    auto_width(ws)

    # Sheet 2: 失智發生率經驗表
    ws2 = wb.create_sheet("失智發生率經驗表")
    ws2.sheet_properties.tabColor = "FFC000"
    headers2 = ["年齡組", "CDR 分級", "發生率(%)", "資料來源", "樣本數"]
    for c, h in enumerate(headers2, 1):
        ws2.cell(row=1, column=c, value=h)
    style_header(ws2, 1, len(headers2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))

    dementia = [
        ["55-64", "CDR 0.5", 1.2, "台灣失智症協會 2024", 8420],
        ["55-64", "CDR ≥1",   0.8, "台灣失智症協會 2024", 8420],
        ["65-74", "CDR 0.5", 4.8, "台灣失智症協會 2024", 11250],
        ["65-74", "CDR ≥1",   3.0, "台灣失智症協會 2024", 11250],
        ["75-84", "CDR 0.5", 11.2,"台灣失智症協會 2024", 9870],
        ["75-84", "CDR ≥1",   7.2, "台灣失智症協會 2024", 9870],
        ["85+",   "CDR 0.5", 22.4,"台灣失智症協會 2024", 4520],
        ["85+",   "CDR ≥1",   13.8,"台灣失智症協會 2024", 4520],
    ]
    for r in dementia:
        ws2.append(r)
    style_data(ws2, 2, len(dementia) + 1, len(headers2))
    add_excel_table(ws2, f"A1:E{len(dementia) + 1}", "tbl_dementia")
    auto_width(ws2)

    # Sheet 3: 三檔費率方案保費
    ws3 = wb.create_sheet("費率方案保費")
    ws3.sheet_properties.tabColor = "5B9BD5"
    h3 = ["方案", "投保年齡", "性別", "年繳保費(NTD)", "20年總繳", "預期給付期望值(NTD)", "損失率"]
    for c, h in enumerate(h3, 1):
        ws3.cell(row=1, column=c, value=h)
    style_header(ws3, 1, len(h3), fill=PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid"))

    plans = [("基本", 30_000), ("進階", 40_000), ("尊榮", 60_000)]
    age_factor = {30: 0.82, 35: 0.91, 40: 1.00, 45: 1.18, 50: 1.42, 55: 1.78, 60: 2.31}
    base_premium = {"基本": 68_400, "進階": 95_200, "尊榮": 158_000}
    rate_3 = []
    for plan_name, monthly_benefit in plans:
        for age in age_factor:
            for gender in ["男", "女"]:
                gf = 1.13 if gender == "女" else 1.0
                premium = round(base_premium[plan_name] * age_factor[age] * gf / 100) * 100
                expected_payout = monthly_benefit * (45 if plan_name == "基本" else 60 if plan_name == "進階" else 90) * (0.32 if gender == "男" else 0.41)
                loss_ratio = round(expected_payout / (premium * 20) * 100, 1)
                rate_3.append([plan_name, age, gender, premium, premium * 20, round(expected_payout), f"{loss_ratio}%"])
    for r in rate_3:
        ws3.append(r)
    style_data(ws3, 2, len(rate_3) + 1, len(h3))
    add_excel_table(ws3, f"A1:G{len(rate_3) + 1}", "tbl_premium")
    auto_width(ws3)

    output = os.path.join(OUTPUT_DIR, "S1_長照精算原始資料.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s1_competitor_dashboard():
    """S1-Excel-2 (預製分析)：競品比較 Dashboard 含 chart"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "競品 KPI 對比"
    ws.sheet_properties.tabColor = "006633"
    add_title_row(ws, "📊 國泰人壽 vs. 競品 — 長照保單關鍵指標對比", 6)

    headers = ["公司", "每月給付(NTD)", "保證給付月數", "免責期(天)", "年繳保費(40M)", "綜合 CP 值"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=3, column=c, value=h)
    style_header(ws, 3, len(headers))

    data = [
        ["國泰（現行）", 36_000, 180, 90,  87_500,  82],
        ["國泰（新版）", 40_000, 180, 90,  95_200,  91],
        ["富邦",        40_000, 180, 90,  92_000,  87],
        ["南山",        36_000, 120, 180, 79_800,  74],
        ["新光",        30_000, 240, 90,  105_000, 79],
        ["三商美邦",    32_000, 180, 60,  76_500,  81],
    ]
    for r in data:
        ws.append(r)
    style_data(ws, 4, 3 + len(data), len(headers))
    auto_width(ws)

    # CP 值橫條圖
    chart = BarChart()
    chart.type = "bar"
    chart.style = 11
    chart.title = "綜合 CP 值對比（值越高越好）"
    chart.y_axis.title = "公司"
    chart.x_axis.title = "CP 值（越高越好）"
    data_ref = Reference(ws, min_col=6, min_row=3, max_row=3 + len(data), max_col=6)
    cats_ref = Reference(ws, min_col=1, min_row=4, max_row=3 + len(data))
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.height = 9
    chart.width  = 18
    ws.add_chart(chart, "H3")

    # 第二 sheet: 保費 vs. 給付對比
    ws2 = wb.create_sheet("保費 vs 給付")
    ws2.sheet_properties.tabColor = "FFC000"
    add_title_row(ws2, "💰 保費 vs. 累計可能給付（20 年期）", 4)
    h2 = ["公司", "20 年總繳保費(萬)", "可能給付(萬)", "倍率"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=3, column=c, value=h)
    style_header(ws2, 3, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))
    data2 = [
        ["國泰（新版）", 190.4, 720,  3.78],
        ["富邦",        184.0, 720,  3.91],
        ["南山",        159.6, 432,  2.71],
        ["新光",        210.0, 720,  3.43],
        ["三商美邦",    153.0, 576,  3.76],
    ]
    for r in data2:
        ws2.append(r)
    style_data(ws2, 4, 3 + len(data2), len(h2))
    auto_width(ws2)

    chart2 = BarChart()
    chart2.type = "col"
    chart2.style = 13
    chart2.grouping = "clustered"
    chart2.title = "保費 vs. 可能給付（萬）"
    data_ref = Reference(ws2, min_col=2, min_row=3, max_col=3, max_row=3 + len(data2))
    cats_ref = Reference(ws2, min_col=1, min_row=4, max_row=3 + len(data2))
    chart2.add_data(data_ref, titles_from_data=True)
    chart2.set_categories(cats_ref)
    chart2.height = 10
    chart2.width  = 18
    ws2.add_chart(chart2, "F3")

    # KPI 摘要
    ws3 = wb.create_sheet("KPI 摘要")
    ws3.sheet_properties.tabColor = "70AD47"
    ws3["A1"] = "🎯 國泰人壽『安心久久』新版商品 KPI 摘要"
    ws3["A1"].font = TITLE_FONT
    ws3.merge_cells("A1:D1")
    kpis = [
        ("關鍵指標",          "目標",     "預估",    "對齊度"),
        ("綜合 CP 值",        "≥85",      "91",     "✅"),
        ("市場排名（保費）",  "第 2",     "第 2",   "✅"),
        ("差異化分數",        "≥80",      "88",     "✅"),
        ("預估首年銷售件數",  "≥18,000",  "21,500", "✅"),
        ("預估首年保費收入(億)", "≥18", "21.4",   "✅"),
        ("預估損失率",        "55-60%",   "57.8%",  "✅"),
    ]
    for r, row in enumerate(kpis, 3):
        for c, v in enumerate(row, 1):
            ws3.cell(row=r, column=c, value=v)
    style_header(ws3, 3, 4, fill=PatternFill(start_color="375623", end_color="375623", fill_type="solid"))
    style_data(ws3, 4, 3 + len(kpis) - 1, 4)
    auto_width(ws3)

    output = os.path.join(OUTPUT_DIR, "S1_長照競品Dashboard.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景二：財富管理
# ═══════════════════════════════════════════════════════════

def s2_market_data():
    """S2-Excel-1 (純資料表)：全球市場原始資料"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "區域指數月報酬"
    ws.sheet_properties.tabColor = "006633"
    headers = ["月份", "S&P500", "NASDAQ", "Nikkei225", "Stoxx600", "MSCI EM", "TWSE", "US10Y(%)", "USD Index"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header(ws, 1, len(headers))

    months = [
        "2025-05", "2025-06", "2025-07", "2025-08", "2025-09",
        "2025-10", "2025-11", "2025-12", "2026-01", "2026-02",
        "2026-03", "2026-04",
    ]
    base = {"sp": 5200, "nq": 16800, "nk": 38500, "stx": 510, "em": 1080, "tw": 21800}
    rs = []
    for m in months:
        sp_r  = round(random.uniform(-3.2, 4.5), 2)
        nq_r  = round(sp_r + random.uniform(-1.2, 1.5), 2)
        nk_r  = round(random.uniform(-2.5, 5.8), 2)
        stx_r = round(random.uniform(-2.8, 3.2), 2)
        em_r  = round(random.uniform(-3.5, 4.2), 2)
        tw_r  = round(random.uniform(-2.5, 5.2), 2)
        us10y = round(random.uniform(3.85, 4.75), 3)
        usdx  = round(random.uniform(99.2, 106.8), 2)
        rs.append([m, sp_r, nq_r, nk_r, stx_r, em_r, tw_r, us10y, usdx])
    for r in rs:
        ws.append(r)
    style_data(ws, 2, 1 + len(rs), len(headers))
    add_excel_table(ws, f"A1:I{1+len(rs)}", "tbl_market")
    auto_width(ws)

    # Sheet 2: 客戶投資組合明細（5 位範例客戶）
    ws2 = wb.create_sheet("客戶組合明細")
    ws2.sheet_properties.tabColor = "FFC000"
    h2 = ["客戶代號", "風險屬性", "AUM(萬)", "資產類別", "市值(萬)", "佔比(%)", "目標佔比(%)", "偏離(pp)"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=1, column=c, value=h)
    style_header(ws2, 1, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))

    clients = [
        ("VIP-2024-08321", "RR4", 2850),
        ("VIP-2024-04918", "RR3", 1620),
        ("VIP-2025-01234", "RR5", 5240),
        ("VIP-2024-09955", "RR2", 980),
        ("VIP-2025-06677", "RR4", 3475),
    ]
    classes = [
        ("已開發股", 38), ("新興股", 12), ("投資級債", 22),
        ("高收益債", 8), ("REITs", 5), ("商品/黃金", 5), ("現金", 10),
    ]
    rs2 = []
    for code, rr, aum in clients:
        for cls, target in classes:
            actual = max(0, target + random.uniform(-3, 3))
            value = round(aum * actual / 100, 1)
            rs2.append([code, rr, aum, cls, value, round(actual, 1), target, round(actual - target, 1)])
    for r in rs2:
        ws2.append(r)
    style_data(ws2, 2, 1 + len(rs2), len(h2))
    add_excel_table(ws2, f"A1:H{1+len(rs2)}", "tbl_clients")
    auto_width(ws2)

    output = os.path.join(OUTPUT_DIR, "S2_全球市場原始資料.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s2_portfolio_dashboard():
    """S2-Excel-2 (預製分析)：投資組合績效歸因 Dashboard"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "績效歸因"
    ws.sheet_properties.tabColor = "006633"
    add_title_row(ws, "📈 高資產組合 2026 Q1 績效歸因（VIP-2024-08321）", 5)

    headers = ["資產類別", "權重(%)", "報酬(%)", "貢獻(pp)", "vs 基準(pp)"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=3, column=c, value=h)
    style_header(ws, 3, len(headers))

    data = [
        ["已開發股票", 40.0, 9.8,  3.92, +0.85],
        ["新興市場股", 10.0, 5.2,  0.52, -0.32],
        ["投資級債",   20.0, 1.8,  0.36, -0.15],
        ["高收益債",   8.0,  3.4,  0.27, +0.08],
        ["REITs",      6.0,  4.8,  0.29, +0.12],
        ["商品/黃金",  5.0,  -1.2, -0.06, -0.18],
        ["現金 / 短票", 11.0, 0.45, 0.05, 0.00],
        ["合計",       100,  9.2,  9.2,  +0.40],
    ]
    for r in data:
        ws.append(r)
    style_data(ws, 4, 3 + len(data), len(headers))
    auto_width(ws)

    # 貢獻長條圖
    chart = BarChart()
    chart.type = "bar"
    chart.style = 12
    chart.title = "各資產類別對總報酬貢獻（pp）"
    data_ref = Reference(ws, min_col=4, min_row=3, max_row=3 + len(data) - 1, max_col=4)
    cats_ref = Reference(ws, min_col=1, min_row=4, max_row=3 + len(data) - 1)
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.height = 10
    chart.width  = 18
    ws.add_chart(chart, "G3")

    # Sheet 2: 風險指標
    ws2 = wb.create_sheet("風險指標")
    ws2.sheet_properties.tabColor = "FFC000"
    add_title_row(ws2, "⚠️ 組合風險指標雷達", 4)
    h2 = ["指標", "本季", "上季", "目標"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=3, column=c, value=h)
    style_header(ws2, 3, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))
    risk = [
        ["年化波動率", "11.8%", "12.5%", "≤13%"],
        ["Sharpe Ratio", "0.72", "0.55", "≥0.6"],
        ["Max Drawdown", "-7.4%", "-9.1%", "≥-10%"],
        ["Tracking Error", "2.1%", "2.4%", "≤3%"],
        ["Beta", "0.92", "0.95", "0.85-1.05"],
        ["Information Ratio", "0.32", "0.18", "≥0.25"],
        ["VaR (95%, 月)", "-5.2%", "-5.8%", "≥-7%"],
    ]
    for r in risk:
        ws2.append(r)
    style_data(ws2, 4, 3 + len(risk), len(h2))
    auto_width(ws2)

    # Sheet 3: 月度趨勢
    ws3 = wb.create_sheet("月度報酬")
    ws3.sheet_properties.tabColor = "5B9BD5"
    add_title_row(ws3, "📊 過去 12 個月組合報酬", 3)
    h3 = ["月份", "組合報酬(%)", "基準(60/40)(%)"]
    for c, h in enumerate(h3, 1):
        ws3.cell(row=3, column=c, value=h)
    style_header(ws3, 3, len(h3), fill=PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid"))
    months = ["2025-05","2025-06","2025-07","2025-08","2025-09","2025-10","2025-11","2025-12","2026-01","2026-02","2026-03","2026-04"]
    p_returns = [1.2, 0.8, -0.5, 1.8, 2.2, -1.1, 1.5, 2.8, 0.9, 1.3, 2.1, 0.4]
    b_returns = [1.0, 0.6, -0.4, 1.5, 1.9, -1.0, 1.3, 2.4, 0.7, 1.1, 1.8, 0.3]
    for m, p, b in zip(months, p_returns, b_returns):
        ws3.append([m, p, b])
    style_data(ws3, 4, 3 + len(months), len(h3))
    auto_width(ws3)

    line = LineChart()
    line.title = "組合 vs. 基準月度報酬"
    line.style = 12
    line.y_axis.title = "月報酬 (%)"
    line.x_axis.title = "月份"
    data_ref = Reference(ws3, min_col=2, min_row=3, max_col=3, max_row=3 + len(months))
    cats_ref = Reference(ws3, min_col=1, min_row=4, max_row=3 + len(months))
    line.add_data(data_ref, titles_from_data=True)
    line.set_categories(cats_ref)
    line.height = 10
    line.width  = 18
    ws3.add_chart(line, "E3")

    output = os.path.join(OUTPUT_DIR, "S2_組合績效Dashboard.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景三：法遵風險
# ═══════════════════════════════════════════════════════════

def s3_risk_data():
    """S3-Excel-1 (純資料表)：KRI 風險指標明細"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "KRI 月度資料"
    ws.sheet_properties.tabColor = "006633"
    headers = ["月份", "KRI 編號", "風險類別", "指標名稱", "本月值", "閾值", "狀態"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header(ws, 1, len(headers))

    months = ["2025-11","2025-12","2026-01","2026-02","2026-03","2026-04"]
    kris = [
        ("KRI-001", "信用風險", "違約率(%)",         0.42, 0.50),
        ("KRI-002", "信用風險", "高風險集中度(%)",   8.2,  10.0),
        ("KRI-003", "市場風險", "VaR 利用率(%)",     62,   85),
        ("KRI-004", "市場風險", "利率敏感度 BPV",    18,   25),
        ("KRI-005", "操作風險", "重大事件數",         2,    5),
        ("KRI-006", "操作風險", "稽核發現重大件數",   2,    5),
        ("KRI-007", "流動性",   "LCR(%)",             132,  100),
        ("KRI-008", "流動性",   "NSFR(%)",            115,  100),
        ("KRI-009", "保險",     "ICS 資本適足率(%)", 165,  150),
        ("KRI-010", "AML",      "STR 申報數",         85,   "—"),
        ("KRI-011", "AML",      "誤報率(%)",          96.6, "—"),
        ("KRI-012", "氣候",     "WACI",               187,  220),
    ]
    for m in months:
        for code, cat, name, base, threshold in kris:
            jitter = random.uniform(-0.12, 0.12)
            value = round(base * (1 + jitter), 2) if isinstance(base, (int, float)) else base
            status = "🟢 正常"
            if isinstance(threshold, (int, float)):
                if isinstance(value, (int, float)):
                    if name in ("LCR(%)", "NSFR(%)", "ICS 資本適足率(%)"):  # higher is better
                        if value < threshold:
                            status = "🔴 警示"
                        elif value < threshold * 1.05:
                            status = "🟡 注意"
                    else:  # lower is better
                        if value > threshold:
                            status = "🔴 警示"
                        elif value > threshold * 0.9:
                            status = "🟡 注意"
            ws.append([m, code, cat, name, value, threshold, status])

    style_data(ws, 2, 1 + len(months) * len(kris), len(headers))
    add_excel_table(ws, f"A1:G{1 + len(months) * len(kris)}", "tbl_kri")
    auto_width(ws)

    # Sheet 2: STR 申報明細
    ws2 = wb.create_sheet("STR 申報明細")
    ws2.sheet_properties.tabColor = "C00000"
    h2 = ["STR 編號", "申報日", "子公司", "案件類型", "可疑樣態", "金額(NTD 萬)", "覆核結果"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=1, column=c, value=h)
    style_header(ws2, 1, len(h2), fill=PatternFill(start_color="C00000", end_color="C00000", fill_type="solid"))
    typologies = [
        ("AML-T01", "短時間多筆等額拆解"),
        ("AML-T02", "高風險 jurisdictions 跨境"),
        ("AML-T03", "與帳戶背景不符的大額"),
        ("AML-T04", "VASP 數位錢包對接"),
        ("AML-T05", "合成身分開戶疑慮"),
        ("AML-T06", "公司型保單異常解約"),
        ("AML-T07", "新南向穩定幣管道"),
    ]
    subs = ["國泰世華", "國泰人壽", "國泰投信", "國泰證券"]
    for i in range(1, 31):
        date = (datetime(2026, 4, 1) - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        sub = random.choice(subs)
        ttype, tname = random.choice(typologies)
        amount = round(random.uniform(50, 2200), 1)
        result = random.choice(["申報 FIU", "持續監控", "申報 FIU", "結案"])
        ws2.append([f"STR-2026-{i:04d}", date, sub, ttype, tname, amount, result])
    style_data(ws2, 2, 31, len(h2))
    add_excel_table(ws2, f"A1:G31", "tbl_str")
    auto_width(ws2)

    output = os.path.join(OUTPUT_DIR, "S3_風險原始資料KRI_STR.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s3_risk_dashboard():
    """S3-Excel-2 (預製分析)：風險指標 Dashboard + 壓力測試"""
    wb = openpyxl.Workbook()

    # Sheet 1: KRI 熱圖摘要
    ws = wb.active
    ws.title = "KRI 熱圖"
    ws.sheet_properties.tabColor = "006633"
    add_title_row(ws, "🔥 國泰金控 KRI 熱圖（2026 Q1）", 6)

    headers = ["KRI", "風險類別", "本月值", "上月值", "閾值", "狀態"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=3, column=c, value=h)
    style_header(ws, 3, len(headers))
    data = [
        ["違約率(%)",       "信用",   0.42, 0.38, "≤0.50", "🟢 正常"],
        ["VaR 利用率(%)",   "市場",   62,   58,   "≤85",   "🟢 正常"],
        ["利率 BPV",        "市場",   23,   18,   "≤25",   "🟡 注意"],
        ["重大事件數",       "操作",   2,    1,    "≤5",    "🟢 正常"],
        ["LCR(%)",          "流動性", 132,  138,  "≥100",  "🟢 正常"],
        ["ICS 資本適足率",  "保險",   165,  172,  "≥150",  "🟡 注意"],
        ["STR 申報誤報率",  "AML",    96.6, 96.4, "—",     "🟢 持續優化"],
        ["WACI",            "氣候",   187,  192,  "≤220",  "🟢 正常"],
    ]
    for r in data:
        ws.append(r)
    style_data(ws, 4, 3 + len(data), len(headers))
    auto_width(ws)

    # Sheet 2: 壓力測試情境結果
    ws2 = wb.create_sheet("壓力測試情境")
    ws2.sheet_properties.tabColor = "C00000"
    add_title_row(ws2, "💥 三大壓力情境下的關鍵指標衝擊", 5)
    h2 = ["指標", "基準", "輕度衰退", "重度衰退", "尾端風險"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=3, column=c, value=h)
    style_header(ws2, 3, len(h2), fill=PatternFill(start_color="C00000", end_color="C00000", fill_type="solid"))
    stress = [
        ["GDP 衝擊",       "0%",   "-1.2%", "-3.5%", "-6.8%"],
        ["失業率",         "3.6%", "4.5%",  "6.2%",  "9.5%"],
        ["違約率(%)",      "0.42", "0.78",  "1.45",  "3.20"],
        ["ICS 資本適足率", "165%", "152%",  "131%",  "108%"],
        ["LCR",            "132%", "121%",  "108%",  "95%"],
        ["稅前淨利衝擊",   "0%",   "-12%",  "-38%",  "-72%"],
        ["相對監理門檻",   "充足", "充足",  "邊際",  "🔴 不足"],
    ]
    for r in stress:
        ws2.append(r)
    style_data(ws2, 4, 3 + len(stress), len(h2))
    auto_width(ws2)

    # Sheet 3: 趨勢圖
    ws3 = wb.create_sheet("ICS 趨勢")
    ws3.sheet_properties.tabColor = "5B9BD5"
    add_title_row(ws3, "📉 ICS 資本適足率 24 個月趨勢", 3)
    h3 = ["月份", "ICS(%)", "業界平均(%)"]
    for c, h in enumerate(h3, 1):
        ws3.cell(row=3, column=c, value=h)
    style_header(ws3, 3, len(h3), fill=PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid"))

    months = []
    base = datetime(2024, 5, 1)
    for i in range(24):
        d = base + timedelta(days=30 * i)
        months.append(d.strftime("%Y-%m"))
    ics = [205, 198, 192, 185, 178, 175, 178, 180, 178, 174, 172, 170,
           172, 170, 168, 165, 165, 167, 170, 172, 172, 168, 165, 165]
    avg = [220, 215, 210, 205, 200, 198, 195, 195, 195, 193, 192, 190,
           192, 192, 190, 195, 195, 196, 198, 197, 196, 196, 195, 195]
    for m, a, b in zip(months, ics, avg):
        ws3.append([m, a, b])
    style_data(ws3, 4, 3 + len(months), len(h3))
    auto_width(ws3)

    line = LineChart()
    line.title = "ICS 資本適足率：本公司 vs 業界平均"
    line.style = 12
    line.y_axis.title = "資本適足率 (%)"
    line.x_axis.title = "月份"
    data_ref = Reference(ws3, min_col=2, min_row=3, max_col=3, max_row=3 + len(months))
    cats_ref = Reference(ws3, min_col=1, min_row=4, max_row=3 + len(months))
    line.add_data(data_ref, titles_from_data=True)
    line.set_categories(cats_ref)
    line.height = 11
    line.width  = 22
    ws3.add_chart(line, "E3")

    output = os.path.join(OUTPUT_DIR, "S3_風險指標Dashboard.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景四：數位轉型
# ═══════════════════════════════════════════════════════════

def s4_channel_data():
    """S4-Excel-1 (純資料表)：通路使用 + NPS 月度原始"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "通路月度使用"
    ws.sheet_properties.tabColor = "006633"
    headers = ["月份", "子公司", "通路", "MAU(萬)", "交易筆數", "客訴件數", "NPS"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header(ws, 1, len(headers))

    months = []
    base = datetime(2025, 5, 1)
    for i in range(12):
        d = base + timedelta(days=30 * i)
        months.append(d.strftime("%Y-%m"))

    subs_channels = [
        ("國泰人壽", "行動 App",   45, 65),
        ("國泰人壽", "Web",        18, 60),
        ("國泰人壽", "業務員",     65, 70),
        ("國泰世華", "行動 App",  185, 62),
        ("國泰世華", "Web",        82, 60),
        ("國泰世華", "ATM",       125, 58),
        ("國泰投信", "行動 App",   28, 52),
        ("國泰投信", "Web",        16, 50),
        ("國泰證券", "行動 App",   38, 46),
        ("國泰證券", "Web",        22, 44),
    ]
    rs = []
    for m_idx, m in enumerate(months):
        for sub, ch, base_mau, base_nps in subs_channels:
            mau = round(base_mau * (1 + m_idx * 0.012 + random.uniform(-0.03, 0.03)), 1)
            tx  = int(mau * random.uniform(8, 18) * 10000)
            cmp_ = int(tx / random.uniform(800, 1500))
            nps_v = round(base_nps + m_idx * 0.18 + random.uniform(-1.2, 1.5), 1)
            rs.append([m, sub, ch, mau, tx, cmp_, nps_v])
    for r in rs:
        ws.append(r)
    style_data(ws, 2, 1 + len(rs), len(headers))
    add_excel_table(ws, f"A1:G{1+len(rs)}", "tbl_channel")
    auto_width(ws)

    output = os.path.join(OUTPUT_DIR, "S4_通路NPS月度原始.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s4_transformation_dashboard():
    """S4-Excel-2 (預製分析)：數位轉型 KPI Dashboard"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "三年路徑"
    ws.sheet_properties.tabColor = "006633"
    add_title_row(ws, "🚀 國泰集團 2026-2028 數位轉型關鍵指標", 5)
    headers = ["指標", "2024 基準", "2025 實績", "2026 目標", "2028 願景"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=3, column=c, value=h)
    style_header(ws, 3, len(headers))
    data = [
        ["雲端化比率(%)",       18, 32, 55, 90],
        ["數位通路 MAU(萬)",   382, 495, 620, 920],
        ["集團 NPS",            53, 57, 60, 68],
        ["數位通路收入佔比(%)",  22, 31, 42, 65],
        ["AI 案件覆蓋率(%)",      8, 21, 45, 80],
        ["IT 雲遷移完成(%)",     12, 28, 50, 95],
        ["Open API 數",         52, 84, 130, 280],
    ]
    for r in data:
        ws.append(r)
    style_data(ws, 4, 3 + len(data), len(headers))
    auto_width(ws)

    chart = BarChart()
    chart.type = "col"
    chart.style = 11
    chart.grouping = "clustered"
    chart.title = "三年路徑關鍵指標進度"
    data_ref = Reference(ws, min_col=2, min_row=3, max_col=5, max_row=3 + len(data))
    cats_ref = Reference(ws, min_col=1, min_row=4, max_row=3 + len(data))
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.height = 11
    chart.width  = 22
    ws.add_chart(chart, "G3")

    # Sheet 2: NPS 旅程
    ws2 = wb.create_sheet("NPS 旅程")
    ws2.sheet_properties.tabColor = "FFC000"
    add_title_row(ws2, "🗺️ 客戶旅程八階段 NPS 對比", 4)
    h2 = ["階段", "本集團", "業界平均", "Gap"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=3, column=c, value=h)
    style_header(ws2, 3, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))
    nps_journey = [
        ["1 認知", 32, 28, +4],
        ["2 比較", 48, 45, +3],
        ["3 簽約", 61, 52, +9],
        ["4 上手", 55, 48, +7],
        ["5 使用", 58, 52, +6],
        ["6 服務", 44, 42, +2],
        ["7 變更", 38, 41, -3],
        ["8 終止", 62, 55, +7],
    ]
    for r in nps_journey:
        ws2.append(r)
    style_data(ws2, 4, 3 + len(nps_journey), len(h2))
    auto_width(ws2)

    line = LineChart()
    line.title = "客戶旅程 NPS"
    line.style = 12
    data_ref = Reference(ws2, min_col=2, min_row=3, max_col=3, max_row=3 + len(nps_journey))
    cats_ref = Reference(ws2, min_col=1, min_row=4, max_row=3 + len(nps_journey))
    line.add_data(data_ref, titles_from_data=True)
    line.set_categories(cats_ref)
    line.height = 10
    line.width  = 18
    ws2.add_chart(line, "F3")

    # Sheet 3: 投資與效益
    ws3 = wb.create_sheet("投資 ROI")
    ws3.sheet_properties.tabColor = "5B9BD5"
    add_title_row(ws3, "💰 三年投資 vs. 預期效益（億 NTD）", 4)
    h3 = ["項目", "2026", "2027", "2028"]
    for c, h in enumerate(h3, 1):
        ws3.cell(row=3, column=c, value=h)
    style_header(ws3, 3, len(h3), fill=PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid"))
    invest = [
        ["雲端基礎建設投資", 6.8, 8.2, 9.5],
        ["AI / GenAI 投資",  4.2, 6.5, 8.8],
        ["資安治理投資",      2.5, 3.2, 4.0],
        ["合計投資",         13.5, 17.9, 22.3],
        ["預期年化效益",      8.5, 18.4, 32.6],
        ["累積 ROI(%)",      63,  102, 146],
    ]
    for r in invest:
        ws3.append(r)
    style_data(ws3, 4, 3 + len(invest), len(h3))
    auto_width(ws3)

    output = os.path.join(OUTPUT_DIR, "S4_數位轉型KPI_Dashboard.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# 場景五：永續金融 ESG
# ═══════════════════════════════════════════════════════════

def s5_carbon_data():
    """S5-Excel-1 (純資料表)：投資組合碳足跡明細"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "持股碳足跡明細"
    ws.sheet_properties.tabColor = "006633"
    headers = ["持股代號", "公司名稱", "產業", "持股市值(NTD 億)", "Scope1+2 排放(萬 tCO2e)", "排放強度", "ESG 評分", "TCFD 揭露分數"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header(ws, 1, len(headers))

    holdings = [
        ["2330.TW", "台積電",         "半導體",       1245, 1280, 105, "AAA", 85],
        ["2308.TW", "台達電",         "電子零件",      385, 158, 72, "AA", 78],
        ["1301.TW", "台塑",           "石化",          280, 5840, 612, "A", 62],
        ["1303.TW", "南亞",           "石化",          245, 4250, 588, "A", 65],
        ["1101.TW", "台泥",           "水泥",          120, 2820, 845, "BBB", 58],
        ["1102.TW", "亞泥",           "水泥",           95, 2240, 812, "BBB", 55],
        ["2002.TW", "中鋼",           "鋼鐵",          165, 8450, 920, "BB", 48],
        ["2884.TW", "玉山金",         "金融",          112, 28, 12, "AA", 81],
        ["3034.TW", "聯詠",           "半導體",         85, 14, 22, "AA", 76],
        ["8454.TW", "富邦媒",         "通路",           52, 22, 18, "A", 70],
        ["MSFT.US", "Microsoft",     "軟體",          325, 285, 18, "AAA", 92],
        ["NVDA.US", "NVIDIA",        "半導體",        425, 218, 32, "AA", 84],
        ["AAPL.US", "Apple",         "硬體",          385, 458, 42, "AAA", 88],
        ["TSLA.US", "Tesla",         "汽車",          165, 145, 38, "BBB", 52],
        ["XOM.US",  "ExxonMobil",    "石油",           65, 12450, 2840, "BB", 45],
        ["AAPL.NV", "AppleHedge",    "ESG ETF",       180, 35, 8, "AAA", 95],
        ["ESGV.US", "Vanguard ESG",  "ESG ETF",       240, 42, 6, "AAA", 96],
        ["ICLN.US", "iShares 清能",  "再生能源",      120, 18, 3, "AAA", 98],
    ]
    for h in holdings:
        ws.append(h)
    style_data(ws, 2, 1 + len(holdings), len(headers))
    add_excel_table(ws, f"A1:H{1+len(holdings)}", "tbl_holdings")
    auto_width(ws)

    # Sheet 2: 同業 ESG 揭露對比
    ws2 = wb.create_sheet("同業 ESG 揭露")
    ws2.sheet_properties.tabColor = "FFC000"
    h2 = ["同業", "TCFD 分數", "永續報告書品質", "綠色融資餘額(億)", "WACI", "SBTi 已驗證"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=1, column=c, value=h)
    style_header(ws2, 1, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))
    peers = [
        ["國泰金（本公司）", 88, "A+", 3820, 187, "✅"],
        ["中信金",           85, "A",  3450, 195, "✅"],
        ["富邦金",           87, "A+", 3680, 192, "✅"],
        ["玉山金",           89, "A+", 2850, 178, "✅"],
        ["元大金",           82, "A",  2120, 215, "❌（規劃中）"],
        ["第一金",           78, "B+", 1850, 232, "❌"],
    ]
    for r in peers:
        ws2.append(r)
    style_data(ws2, 2, 1 + len(peers), len(h2))
    add_excel_table(ws2, f"A1:F{1+len(peers)}", "tbl_peers")
    auto_width(ws2)

    output = os.path.join(OUTPUT_DIR, "S5_組合碳足跡原始資料.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


def s5_esg_dashboard():
    """S5-Excel-2 (預製分析)：ESG / 淨零路徑 Dashboard"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "淨零路徑"
    ws.sheet_properties.tabColor = "006633"
    add_title_row(ws, "🌱 投融資組合 2050 淨零路徑（百萬 tCO2e）", 4)

    headers = ["年度", "電力", "石化", "水泥", "鋼鐵", "其他", "合計"]
    for c, h in enumerate(headers, 1):
        ws.cell(row=3, column=c, value=h)
    style_header(ws, 3, len(headers))
    data = [
        [2020, 8.2, 4.8, 2.5, 4.2, 0.8, 20.5],
        [2025, 6.8, 3.6, 1.9, 3.5, 0.4, 16.2],
        [2030, 4.5, 3.2, 1.5, 2.4, 0.4, 12.0],
        [2035, 2.8, 2.4, 1.2, 1.5, 0.3, 8.2],
        [2040, 1.6, 1.5, 0.8, 0.9, 0.2, 5.0],
        [2045, 0.8, 0.6, 0.4, 0.4, 0.1, 2.3],
        [2050, 0.0, 0.1, 0.1, 0.1, 0.0, 0.3],
    ]
    for r in data:
        ws.append(r)
    style_data(ws, 4, 3 + len(data), len(headers))
    auto_width(ws)

    chart = LineChart()
    chart.title = "投融資組合淨零路徑"
    chart.style = 12
    chart.y_axis.title = "百萬 tCO2e"
    chart.x_axis.title = "年度"
    data_ref = Reference(ws, min_col=2, min_row=3, max_col=7, max_row=3 + len(data))
    cats_ref = Reference(ws, min_col=1, min_row=4, max_row=3 + len(data))
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.height = 11
    chart.width  = 22
    ws.add_chart(chart, "I3")

    # Sheet 2: TCFD 揭露對比
    ws2 = wb.create_sheet("TCFD 對比")
    ws2.sheet_properties.tabColor = "FFC000"
    add_title_row(ws2, "📊 TCFD 揭露品質：本公司 vs 同業", 5)
    h2 = ["公司", "治理", "策略", "風險管理", "指標目標"]
    for c, h in enumerate(h2, 1):
        ws2.cell(row=3, column=c, value=h)
    style_header(ws2, 3, len(h2), fill=PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid"))
    tcfd = [
        ["國泰金（本公司）", 22, 24, 22, 20],
        ["中信金",           20, 22, 22, 21],
        ["富邦金",           22, 24, 21, 20],
        ["玉山金",           23, 24, 22, 20],
        ["業界平均",         18, 20, 19, 17],
    ]
    for r in tcfd:
        ws2.append(r)
    style_data(ws2, 4, 3 + len(tcfd), len(h2))
    auto_width(ws2)

    radar_data = Reference(ws2, min_col=2, min_row=3, max_col=5, max_row=3 + len(tcfd))
    radar_cats = Reference(ws2, min_col=1, min_row=4, max_row=3 + len(tcfd))
    chart2 = BarChart()
    chart2.type = "bar"
    chart2.style = 11
    chart2.grouping = "clustered"
    chart2.title = "TCFD 四大支柱分數"
    chart2.add_data(radar_data, titles_from_data=True)
    chart2.set_categories(radar_cats)
    chart2.height = 11
    chart2.width  = 22
    ws2.add_chart(chart2, "G3")

    # Sheet 3: 高碳產業曝險
    ws3 = wb.create_sheet("高碳曝險")
    ws3.sheet_properties.tabColor = "C00000"
    add_title_row(ws3, "🔥 高碳產業曝險與減碳目標", 5)
    h3 = ["產業", "投資金額(億)", "WACI", "vs 基準(%)", "2030 減碳目標"]
    for c, h in enumerate(h3, 1):
        ws3.cell(row=3, column=c, value=h)
    style_header(ws3, 3, len(h3), fill=PatternFill(start_color="C00000", end_color="C00000", fill_type="solid"))
    high = [
        ["電力（火力）", 85.2, 385, "+18%", "-45%"],
        ["石化",         62.1, 212, "+5%",  "-32%"],
        ["水泥",         18.4, 528, "+24%", "-38%"],
        ["鋼鐵",         31.6, 415, "+12%", "-42%"],
        ["合計",         197.3, "—", "—",   "—"],
    ]
    for r in high:
        ws3.append(r)
    style_data(ws3, 4, 3 + len(high), len(h3))
    auto_width(ws3)

    output = os.path.join(OUTPUT_DIR, "S5_ESG淨零Dashboard.xlsx")
    wb.save(output)
    print(f"  ✓ {os.path.basename(output)}")


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n📊 Generating Excel files into: {OUTPUT_DIR}\n")

    # 5 純資料表
    s1_actuarial_data()
    s2_market_data()
    s3_risk_data()
    s4_channel_data()
    s5_carbon_data()

    # 5 預製分析
    s1_competitor_dashboard()
    s2_portfolio_dashboard()
    s3_risk_dashboard()
    s4_transformation_dashboard()
    s5_esg_dashboard()

    print(f"\n✅ Total Excel files generated.\n")
