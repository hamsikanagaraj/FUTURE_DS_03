# 📊 Marketing Funnel & Conversion Performance Analysis
### **Future Interns – Data Science & Analytics Track (Task 3 – 2026)**
**Domain:** Growth Analytics, Marketing Attribution & Revenue Operations  
**Deliverables:** End-to-End Pipeline, Jupyter Notebook EDA, Interactive Web Dashboard, Executive PDF & Markdown Reports  

---

## 🌟 Executive Overview

In SaaS, digital marketing agencies, and high-growth sales teams, optimizing how users progress from **Visitors → Leads → MQLs → SQLs → Opportunities → Customers** directly dictates revenue growth and capital efficiency.

This project delivers a complete data science and marketing analytics solution analyzing **65,000 multi-channel visitor sessions**, **4,466 qualified leads**, and **363 closed-won enterprise customers**, generating **$6,978,674 in closed pipeline ARR** against **$182,367.05 in marketing spend** (**38.27x blended ROAS**).

---

## 🎯 Key Questions Answered

| Business Question | Data-Backed Finding | Recommended Action |
| :--- | :--- | :--- |
| **1. Where are users dropping off?** | **93.13% drop-off at Visitor → Lead** (Top-of-funnel leak); **63.81% drop-off at Opportunity → Customer** (Late-stage ARR loss of $12.3M). | Overhaul mobile landing page forms (reduce 7 fields to 1-tap auth) and implement deal desks with 48-hr security packets. |
| **2. Which channels bring high-quality leads?** | **Referral / Partner** is the top channel: **20.48% Lead-to-Customer conversion**, **$49.59 CAC**, and **416.2x ROAS** ($2.62M ARR). **LinkedIn Ads** delivers the highest enterprise deal size ($21,355 ACV). | Triple co-marketing spend with integration partners; shift 50% of display budget into LinkedIn Account-Based Marketing (ABM). |
| **3. Which channels are inefficient?** | **Social Media (Meta/X)** converts at only **1.10%** with a **$6,101.85 CAC** (ROAS 2.46x). **Paid Search (Google Ads)** has a steep **$2,058.76 CAC**. | Prune unviable social display ad spend; restructure Google Ads exclusively around exact-match competitor displacement keywords. |
| **4. What is the impact of conversion lifts?** | A synchronized +10% lift across landing page CRO, lead qualification, and deal closing unlocks **+$2,306,944 in incremental ARR** with **zero additional ad spend**. | Execute the 90-day phased growth playbook outlined in the strategic report. |

---

## 📁 Repository Structure

```
task3/
├── data/
│   ├── raw_marketing_funnel_data.csv       # 65,000 session multi-channel records
│   └── cleaned_funnel_data.csv             # Cleaned, validated monotonic dataset
├── src/
│   ├── generate_dataset.py                 # Statistically grounded data generator
│   ├── data_cleaning_and_funnel_analysis.py# Data cleaning, metric calculation & plot generation
│   └── build_notebook.py                   # Automated Jupyter Notebook constructor
├── notebooks/
│   └── marketing_funnel_analysis.ipynb     # Complete Jupyter Notebook with full EDA, stats & charts
├── dashboard/
│   ├── index.html                          # Executive Glassmorphic Dashboard UI
│   ├── style.css                           # Modern CSS design system (Dark/Light themes)
│   ├── app.js                              # Dynamic charts, filter handlers & What-If simulator
│   └── data/
│       └── funnel_metrics.json             # Aggregated metrics for dashboard consumption
├── visualizations/
│   ├── 01_funnel_waterfall.png             # Stage-by-stage volume & drop-off waterfall
│   ├── 02_channel_lead_quality_matrix.png  # Lead volume vs Lead-to-Customer conversion rate
│   ├── 03_stage_dropoff_rates.png          # Friction percentage across transitions
│   ├── 04_channel_cac_vs_roas.png          # Unit economics (CAC vs ROAS) comparison
│   └── 05_device_performance.png          # Desktop vs Mobile conversion disparity
├── reports/
│   ├── Marketing_Funnel_Performance_Report.md # Formal executive strategy report
│   ├── generate_pdf_report.py              # ReportLab PDF compiler
│   └── Executive_Marketing_Funnel_Report.pdf  # Multi-page publication-ready PDF deliverable
└── README.md                               # Project documentation
```

---

## 📊 Macro Funnel Stage Conversion Benchmark

```
[ Visitor ] ──(6.87%)──> [ Lead ] ──(55.08%)──> [ MQL ] ──(59.19%)──> [ SQL ] ──(68.89%)──> [ Opportunity ] ──(36.19%)──> [ Customer ]
  65,000                   4,466                  2,460                 1,456                   1,003                     363
```

* **Overall Funnel Conversion Rate (Visitor → Customer):** **0.558%**
* **Total Pipeline ARR Generated:** **$6,978,674.18**
* **Total Marketing Spend:** **$182,367.05**
* **Blended Customer Acquisition Cost (CAC):** **$502.39**
* **Overall Return on Ad Spend (ROAS):** **38.27x**

---

## 🚀 How to Run the Project

### 1. Requirements
Ensure Python 3.10+ is installed. Essential libraries:
```bash
pip install pandas numpy matplotlib seaborn plotly reportlab
```

### 2. Run Data Ingestion & Analytics Pipeline
To regenerate the dataset, validate monotonicity, compute all metrics, and export high-res charts:
```bash
python src/generate_dataset.py
python src/data_cleaning_and_funnel_analysis.py
```

### 3. Generate Executive PDF Deliverable
```bash
python reports/generate_pdf_report.py
```
Outputs a publication-quality PDF at `reports/Executive_Marketing_Funnel_Report.pdf`.

### 4. Launch the Interactive Web Dashboard
You can open `dashboard/index.html` directly in any web browser, or serve it via Python:
```bash
cd dashboard
python -m http.server 5500
```
Then navigate to: **`http://localhost:5500`**

#### Dashboard Features:
* **Interactive Macro Funnel Visualizer:** Proportional animated stage bars with volume, drop-off rates, and conversion percentages.
* **Global Filter Panel:** Filter by Acquisition Channel, Device Platform, and Quarter in real-time.
* **Interactive "What-If" Revenue Simulator:** Real-time sliders allowing executives to model conversion lifts (+X% Visitor→Lead, +Y% Lead→MQL, +Z% Opp→Cust) and instantly compute added pipeline revenue and ROI.
* **Channel Scorecard Table:** Real-time search filter and sortable column headers.
* **Theme Switching:** Dark mode default with light mode toggle.
* **One-Click Export:** Download cleaned CSV and print formatted executive briefs.

---

## 📈 Executive Growth Roadmap

1. **Phase 1 (Days 1–30): Channel Reallocation & Mobile CRO**
   * Reallocate 60% of underperforming Social Ads budget ($12k/quarter) into Referral co-marketing and LinkedIn ABM.
   * Replace 7-field mobile forms with 1-tap Google/LinkedIn authentication to eliminate the 55% mobile conversion penalty.
2. **Phase 2 (Days 31–60): Automated Lead Qualification**
   * Deploy behavioral lead scoring and route high-intent leads to SDRs within 5 minutes.
3. **Phase 3 (Days 61–90): Opportunity Acceleration & Deal Desk**
   * Implement in-demo ROI calculators and 48-hour security packet turnarounds to compress sales cycle length from 37 days down to 22 days.
