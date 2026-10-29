"""
Executive PDF Report Generator for Task 3: Marketing Funnel Analysis
Utilizes ReportLab to generate a multi-page, publication-quality PDF executive deliverable.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = "reports/Executive_Marketing_Funnel_Report.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor("#0f172a")
    c_blue = colors.HexColor("#2563eb")
    c_emerald = colors.HexColor("#059669")
    c_slate = colors.HexColor("#475569")
    c_card_bg = colors.HexColor("#f8fafc")
    c_border = colors.HexColor("#cbd5e1")
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=c_slate,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_blue,
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=c_primary,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_primary,
        leftIndent=12,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'THStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TCStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=c_primary,
        alignment=1
    )

    story = []

    # Document Header
    story.append(Paragraph("<b>MARKETING FUNNEL & CONVERSION ANALYTICS REPORT</b>", title_style))
    story.append(Paragraph("<b>Future Interns (Task 3 - 2026)</b> | Multi-Channel Attribution, Drop-Off Diagnostics & Growth Strategy", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_blue, spaceBefore=0, spaceAfter=10))

    # KPI Summary Metric Banner
    kpi_data = [
        [
            Paragraph("<b>TOTAL TRAFFIC</b><br/><font size=12 color='#2563eb'><b>65,000</b></font><br/><font size=6.5 color='#64748b'>Sessions (Q1-Q3)</font>", table_cell_style),
            Paragraph("<b>QUALIFIED LEADS</b><br/><font size=12 color='#7c3aed'><b>4,466</b></font><br/><font size=6.5 color='#64748b'>6.87% Conv Rate</font>", table_cell_style),
            Paragraph("<b>CUSTOMERS WON</b><br/><font size=12 color='#059669'><b>363</b></font><br/><font size=6.5 color='#64748b'>0.558% Overall Conv</font>", table_cell_style),
            Paragraph("<b>CLOSED PIPELINE ARR</b><br/><font size=12 color='#059669'><b>$6,978,674</b></font><br/><font size=6.5 color='#64748b'>Avg ACV: $19,225</font>", table_cell_style),
            Paragraph("<b>BLENDED CAC & ROAS</b><br/><font size=12 color='#e11d48'><b>$502.39</b></font><br/><font size=6.5 color='#059669'><b>38.27x ROAS</b></font>", table_cell_style),
        ]
    ]
    t_kpi = Table(kpi_data, colWidths=[108, 108, 108, 108, 108])
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_card_bg),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_kpi)
    story.append(Spacer(1, 10))

    # Section 1: Executive Summary
    story.append(Paragraph("<b>1. Executive Summary & Core Insights</b>", h1_style))
    summary_text = (
        "This evaluation analyzes full-funnel lead progression from raw website traffic to signed enterprise contracts. "
        "The analysis demonstrates an overall <b>0.558% Visitor-to-Customer conversion yield</b>. "
        "The primary top-of-funnel leak occurs at the <b>Visitor → Lead transition (93.13% drop-off)</b>, driven heavily by mobile form friction. "
        "The most critical downstream bottleneck exists at <b>Opportunity → Customer (63.81% drop-off)</b>, causing over <b>$12.3M in unrealized ARR leakage</b>. "
        "<b>Referral / Partner</b> emerged as the highest-performing channel (<b>20.48% Lead-to-Customer conversion</b>, <b>$49.59 CAC</b>, and <b>416x ROAS</b>), "
        "whereas <b>Paid Search ($2,058 CAC)</b> and <b>Social Ads ($6,101 CAC)</b> exhibited severe capital inefficiency."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 8))

    # Section 2: Macro Funnel Progression Table
    story.append(Paragraph("<b>2. Macro Funnel Progression & Stage Conversion Rates</b>", h1_style))
    funnel_table_data = [
        [
            Paragraph("<b>Funnel Stage</b>", table_header_style),
            Paragraph("<b>Volume</b>", table_header_style),
            Paragraph("<b>Stage Conv %</b>", table_header_style),
            Paragraph("<b>Cumulative %</b>", table_header_style),
            Paragraph("<b>Drop-Off Count</b>", table_header_style),
            Paragraph("<b>Drop-Off Rate %</b>", table_header_style),
        ],
        [Paragraph("1. Visitor", table_cell_style), Paragraph("65,000", table_cell_style), Paragraph("100.00%", table_cell_style), Paragraph("100.000%", table_cell_style), Paragraph("0", table_cell_style), Paragraph("0.00%", table_cell_style)],
        [Paragraph("2. Lead", table_cell_style), Paragraph("4,466", table_cell_style), Paragraph("6.87%", table_cell_style), Paragraph("6.871%", table_cell_style), Paragraph("60,534", table_cell_style), Paragraph("93.13%", table_cell_style)],
        [Paragraph("3. MQL", table_cell_style), Paragraph("2,460", table_cell_style), Paragraph("55.08%", table_cell_style), Paragraph("3.785%", table_cell_style), Paragraph("2,006", table_cell_style), Paragraph("44.92%", table_cell_style)],
        [Paragraph("4. SQL", table_cell_style), Paragraph("1,456", table_cell_style), Paragraph("59.19%", table_cell_style), Paragraph("2.240%", table_cell_style), Paragraph("1,004", table_cell_style), Paragraph("40.81%", table_cell_style)],
        [Paragraph("5. Opportunity", table_cell_style), Paragraph("1,003", table_cell_style), Paragraph("68.89%", table_cell_style), Paragraph("1.543%", table_cell_style), Paragraph("453", table_cell_style), Paragraph("31.11%", table_cell_style)],
        [Paragraph("6. Customer", table_cell_style), Paragraph("363", table_cell_style), Paragraph("36.19%", table_cell_style), Paragraph("0.558%", table_cell_style), Paragraph("640", table_cell_style), Paragraph("63.81%", table_cell_style)],
    ]
    t_funnel = Table(funnel_table_data, colWidths=[100, 80, 85, 90, 95, 90])
    t_funnel.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_card_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_funnel)
    story.append(Spacer(1, 10))

    # Embedded Funnel & Drop-off Visualizations
    if os.path.exists("visualizations/01_funnel_waterfall.png") and os.path.exists("visualizations/03_stage_dropoff_rates.png"):
        img_table = Table([
            [
                Image("visualizations/01_funnel_waterfall.png", width=3.6*inch, height=2.1*inch),
                Image("visualizations/03_stage_dropoff_rates.png", width=3.6*inch, height=2.1*inch)
            ]
        ], colWidths=[270, 270])
        img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(img_table)
        story.append(Spacer(1, 10))

    # Section 3: Channel Performance & Unit Economics
    story.append(Paragraph("<b>3. Acquisition Channel Scorecard & Attribution Economics</b>", h1_style))
    channel_table_data = [
        [
            Paragraph("<b>Channel</b>", table_header_style),
            Paragraph("<b>Visitors</b>", table_header_style),
            Paragraph("<b>Leads</b>", table_header_style),
            Paragraph("<b>Cust</b>", table_header_style),
            Paragraph("<b>V→L %</b>", table_header_style),
            Paragraph("<b>L→C %</b>", table_header_style),
            Paragraph("<b>CAC ($)</b>", table_header_style),
            Paragraph("<b>ROAS</b>", table_header_style),
            Paragraph("<b>Revenue ($ ARR)</b>", table_header_style),
        ],
        [Paragraph("Referral / Partner", table_cell_style), Paragraph("5,248", table_cell_style), Paragraph("620", table_cell_style), Paragraph("127", table_cell_style), Paragraph("11.81%", table_cell_style), Paragraph("20.48%", table_cell_style), Paragraph("$49.59", table_cell_style), Paragraph("416.2x", table_cell_style), Paragraph("$2,621,027", table_cell_style)],
        [Paragraph("LinkedIn Ads (B2B)", table_cell_style), Paragraph("9,150", table_cell_style), Paragraph("476", table_cell_style), Paragraph("70", table_cell_style), Paragraph("5.20%", table_cell_style), Paragraph("14.71%", table_cell_style), Paragraph("$1,241.79", table_cell_style), Paragraph("17.2x", table_cell_style), Paragraph("$1,494,918", table_cell_style)],
        [Paragraph("Email Marketing", table_cell_style), Paragraph("7,263", table_cell_style), Paragraph("716", table_cell_style), Paragraph("62", table_cell_style), Paragraph("9.86%", table_cell_style), Paragraph("8.66%", table_cell_style), Paragraph("$17.57", table_cell_style), Paragraph("906.5x", table_cell_style), Paragraph("$987,585", table_cell_style)],
        [Paragraph("Organic Search", table_cell_style), Paragraph("16,935", table_cell_style), Paragraph("1,157", table_cell_style), Paragraph("48", table_cell_style), Paragraph("6.83%", table_cell_style), Paragraph("4.15%", table_cell_style), Paragraph("$158.77", table_cell_style), Paragraph("110.4x", table_cell_style), Paragraph("$841,199", table_cell_style)],
        [Paragraph("Paid Search (Google)", table_cell_style), Paragraph("14,154", table_cell_style), Paragraph("890", table_cell_style), Paragraph("33", table_cell_style), Paragraph("6.29%", table_cell_style), Paragraph("3.71%", table_cell_style), Paragraph("$2,058.76", table_cell_style), Paragraph("9.2x", table_cell_style), Paragraph("$624,931", table_cell_style)],
        [Paragraph("Direct Traffic", table_cell_style), Paragraph("5,827", table_cell_style), Paragraph("426", table_cell_style), Paragraph("21", table_cell_style), Paragraph("7.31%", table_cell_style), Paragraph("4.93%", table_cell_style), Paragraph("$13.87", table_cell_style), Paragraph("1300.9x", table_cell_style), Paragraph("$379,002", table_cell_style)],
        [Paragraph("Social Media (Meta/X)", table_cell_style), Paragraph("6,423", table_cell_style), Paragraph("181", table_cell_style), Paragraph("2", table_cell_style), Paragraph("2.82%", table_cell_style), Paragraph("1.10%", table_cell_style), Paragraph("$6,101.85", table_cell_style), Paragraph("2.5x", table_cell_style), Paragraph("$30,011", table_cell_style)],
    ]
    t_ch = Table(channel_table_data, colWidths=[100, 52, 48, 42, 50, 52, 60, 50, 86])
    t_ch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_blue),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_card_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_ch)
    story.append(Spacer(1, 10))

    # Embedded Lead Quality Matrix & CAC Chart
    if os.path.exists("visualizations/02_channel_lead_quality_matrix.png") and os.path.exists("visualizations/04_channel_cac_vs_roas.png"):
        img_table2 = Table([
            [
                Image("visualizations/02_channel_lead_quality_matrix.png", width=3.6*inch, height=2.0*inch),
                Image("visualizations/04_channel_cac_vs_roas.png", width=3.6*inch, height=2.0*inch)
            ]
        ], colWidths=[270, 270])
        img_table2.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(img_table2)
        story.append(Spacer(1, 8))

    # Section 4: Actionable Recommendations
    story.append(Paragraph("<b>4. Actionable Recommendations & Growth Roadmap</b>", h1_style))
    story.append(Paragraph("<b>1. Triple Down on Referral & Partner Channels (High Impact):</b> Referral delivers 20.48% conversion, $49.59 CAC, and 416x ROAS. Expand integration partnerships and co-marketing webinars to scale share of traffic from 8% to 18% (+ $1.2M ARR).", bullet_style))
    story.append(Paragraph("<b>2. Mobile Landing Page UX Redesign:</b> Mobile conversion lags desktop by 55% (0.331% vs 0.742%). Implement 1-click Google/LinkedIn authentication and reduce form fields to recover ~450 lost leads.", bullet_style))
    story.append(Paragraph("<b>3. Prune Social & Restructure Google Search Ads:</b> Reallocate 60% of underperforming Meta/X ad budget ($6,101 CAC) into LinkedIn ABM campaigns targeting C-level buyers, while focusing Google Ads strictly on exact-match competitor displacement terms.", bullet_style))
    story.append(Paragraph("<b>4. Deal Acceleration & Security Enablement:</b> 63.8% of opportunities drop off at proposal. Implement standardized 48-hour security packs (SOC2/GDPR) and dynamic ROI calculators during demos to compress deal cycles from 37 days down to 22 days.", bullet_style))
    
    doc.build(story)
    print(f"Executive PDF report generated successfully at {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
