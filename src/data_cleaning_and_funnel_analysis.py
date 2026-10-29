"""
Comprehensive Marketing Funnel Cleaning and Analytics Engine
Task 3 - Future Interns (2026)
Author: Data Science & Analytics Team
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for professional publication-quality figures
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 11

def run_funnel_analytics():
    print("=" * 70)
    print("MARKETING FUNNEL & CONVERSION PERFORMANCE ANALYSIS PIPELINE")
    print("=" * 70)
    
    # 1. Load Data
    raw_path = 'data/raw_marketing_funnel_data.csv'
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data file not found at {raw_path}")
        
    df = pd.read_csv(raw_path)
    print(f"Loaded raw dataset: {len(df):,} records, {len(df.columns)} columns.")
    
    # 2. Data Cleaning & Validation
    print("\n--- Data Cleaning & Integrity Audit ---")
    initial_count = len(df)
    
    # Missing values check
    missing = df.isnull().sum()
    print(f"Missing values count across columns:\n{missing[missing > 0] if missing.sum() > 0 else 'None'}")
    
    # Datetime conversions
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = pd.to_datetime(df['date'])
    
    # Ensure categorical standardizations
    df['channel'] = df['channel'].astype(str).str.strip()
    df['campaign'] = df['campaign'].astype(str).str.strip()
    df['device'] = df['device'].astype(str).str.strip()
    df['region'] = df['region'].astype(str).str.strip()
    
    # Validate Funnel Monotonicity (A customer MUST be an opportunity, SQL, MQL, Lead, Visitor)
    monotonic_valid = (
        (df['is_customer'] <= df['is_opportunity']) &
        (df['is_opportunity'] <= df['is_sql']) &
        (df['is_sql'] <= df['is_mql']) &
        (df['is_mql'] <= df['is_lead']) &
        (df['is_lead'] <= df['is_visitor'])
    ).all()
    print(f"Funnel Monotonicity Constraint Check: {'PASSED (100% Strict Integrity)' if monotonic_valid else 'VIOLATED'}")
    
    # Check for duplicate session IDs
    dupes = df.duplicated(subset=['session_id']).sum()
    print(f"Duplicate Session IDs: {dupes}")
    if dupes > 0:
        df = df.drop_duplicates(subset=['session_id']).reset_index(drop=True)
        
    # Save cleaned dataset
    os.makedirs('data', exist_ok=True)
    cleaned_path = 'data/cleaned_funnel_data.csv'
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned dataset saved to {cleaned_path} ({len(df):,} records).")
    
    # 3. Macro Funnel Stage Metrics
    print("\n--- Macro Funnel Stage Performance ---")
    stages = ['Visitor', 'Lead', 'MQL', 'SQL', 'Opportunity', 'Customer']
    stage_cols = ['is_visitor', 'is_lead', 'is_mql', 'is_sql', 'is_opportunity', 'is_customer']
    
    counts = [df[col].sum() for col in stage_cols]
    
    funnel_summary = []
    prev_count = None
    top_count = counts[0]
    
    for i, (stage, count) in enumerate(zip(stages, counts)):
        stage_conv = (count / prev_count * 100) if prev_count else 100.0
        cum_conv = (count / top_count * 100)
        drop_off_count = (prev_count - count) if prev_count else 0
        drop_off_rate = (drop_off_count / prev_count * 100) if prev_count else 0.0
        
        funnel_summary.append({
            'Stage': stage,
            'Count': count,
            'Stage_Conversion_Rate_%': round(stage_conv, 2),
            'Cumulative_Conversion_Rate_%': round(cum_conv, 3),
            'Drop_Off_Count': drop_off_count,
            'Drop_Off_Rate_%': round(drop_off_rate, 2)
        })
        prev_count = count
        
    df_funnel = pd.DataFrame(funnel_summary)
    print(df_funnel.to_string(index=False))
    
    # 4. Channel Performance & Lead Quality Analysis
    print("\n--- Channel Performance & Attribution Analysis ---")
    channel_agg = df.groupby('channel').agg(
        Visitors=('is_visitor', 'sum'),
        Leads=('is_lead', 'sum'),
        MQLs=('is_mql', 'sum'),
        SQLs=('is_sql', 'sum'),
        Opportunities=('is_opportunity', 'sum'),
        Customers=('is_customer', 'sum'),
        Spend_USD=('cost_usd', 'sum'),
        Revenue_USD=('deal_value', 'sum'),
        Avg_Days_to_Close=('days_to_close', lambda x: x[x > 0].mean() if len(x[x > 0]) > 0 else 0)
    ).reset_index()
    
    # Derived Conversion Rates & Unit Economics
    channel_agg['Traffic_to_Lead_%'] = round(channel_agg['Leads'] / channel_agg['Visitors'] * 100, 2)
    channel_agg['Lead_to_Customer_%'] = round(channel_agg['Customers'] / channel_agg['Leads'] * 100, 2)
    channel_agg['Overall_Conversion_%'] = round(channel_agg['Customers'] / channel_agg['Visitors'] * 100, 3)
    channel_agg['CPL_USD'] = round(channel_agg['Spend_USD'] / channel_agg['Leads'], 2)
    channel_agg['CAC_USD'] = round(channel_agg['Spend_USD'] / channel_agg['Customers'], 2)
    channel_agg['Avg_Deal_Size_USD'] = round(channel_agg['Revenue_USD'] / channel_agg['Customers'], 2)
    channel_agg['ROAS'] = round(channel_agg['Revenue_USD'] / channel_agg['Spend_USD'], 2)
    channel_agg['Net_Profit_USD'] = round(channel_agg['Revenue_USD'] - channel_agg['Spend_USD'], 2)
    
    # Quality score: weighted combination of MQL/Lead and Lead-to-Customer
    channel_agg['Lead_Quality_Score'] = round(
        (channel_agg['MQLs'] / channel_agg['Leads'] * 0.4 + 
         channel_agg['Customers'] / channel_agg['Leads'] * 0.6) * 100, 1
    )
    
    channel_agg = channel_agg.sort_values(by='Revenue_USD', ascending=False)
    print(channel_agg[['channel', 'Visitors', 'Leads', 'Customers', 'Lead_to_Customer_%', 'CAC_USD', 'ROAS', 'Revenue_USD']].to_string(index=False))
    
    # 5. Device Disparities
    print("\n--- Device Conversion Performance ---")
    device_agg = df.groupby('device').agg(
        Visitors=('is_visitor', 'sum'),
        Leads=('is_lead', 'sum'),
        Customers=('is_customer', 'sum'),
        Revenue=('deal_value', 'sum'),
        Spend=('cost_usd', 'sum'),
        Avg_Time_Sec=('time_on_page_sec', 'mean'),
        Bounce_Rate=('is_bounce', 'mean')
    ).reset_index()
    device_agg['Traffic_to_Lead_%'] = round(device_agg['Leads'] / device_agg['Visitors'] * 100, 2)
    device_agg['Lead_to_Customer_%'] = round(device_agg['Customers'] / device_agg['Leads'] * 100, 2)
    device_agg['Overall_Conv_%'] = round(device_agg['Customers'] / device_agg['Visitors'] * 100, 3)
    device_agg['Bounce_Rate_%'] = round(device_agg['Bounce_Rate'] * 100, 2)
    print(device_agg[['device', 'Visitors', 'Traffic_to_Lead_%', 'Lead_to_Customer_%', 'Overall_Conv_%', 'Bounce_Rate_%']].to_string(index=False))

    # 6. Monthly Trend Analysis
    print("\n--- Monthly Conversion & Revenue Trend ---")
    monthly_agg = df.groupby('month').agg(
        Visitors=('is_visitor', 'sum'),
        Leads=('is_lead', 'sum'),
        Customers=('is_customer', 'sum'),
        Revenue=('deal_value', 'sum'),
        Spend=('cost_usd', 'sum')
    ).reset_index()
    monthly_agg['Conv_Rate_%'] = round(monthly_agg['Customers'] / monthly_agg['Visitors'] * 100, 3)
    monthly_agg['ROAS'] = round(monthly_agg['Revenue'] / monthly_agg['Spend'], 2)
    print(monthly_agg.to_string(index=False))
    
    # 7. Campaign Level Analysis (Top 5 and Bottom 5)
    print("\n--- Campaign Level Performance ---")
    campaign_agg = df.groupby(['channel', 'campaign']).agg(
        Visitors=('is_visitor', 'sum'),
        Leads=('is_lead', 'sum'),
        Customers=('is_customer', 'sum'),
        Spend=('cost_usd', 'sum'),
        Revenue=('deal_value', 'sum')
    ).reset_index()
    campaign_agg['Lead_to_Cust_%'] = round(campaign_agg['Customers'] / campaign_agg['Leads'] * 100, 2)
    campaign_agg['ROAS'] = round(campaign_agg['Revenue'] / campaign_agg['Spend'], 2)
    campaign_agg['CAC'] = round(campaign_agg['Spend'] / campaign_agg['Customers'].replace(0, np.nan), 2)
    top_campaigns = campaign_agg.sort_values(by='Revenue', ascending=False).head(5)
    print("Top 5 Campaigns by Revenue:")
    print(top_campaigns[['campaign', 'channel', 'Leads', 'Customers', 'Lead_to_Cust_%', 'Revenue', 'ROAS']].to_string(index=False))

    # 8. Generate Charts
    os.makedirs('visualizations', exist_ok=True)
    print("\n--- Generating High-Resolution Analytical Visualizations ---")
    
    # Chart 1: Funnel Waterfall
    plt.figure(figsize=(10, 6))
    colors = ['#1e293b', '#3b82f6', '#0ea5e9', '#6366f1', '#8b5cf6', '#10b981']
    bars = plt.bar(df_funnel['Stage'], df_funnel['Count'], color=colors, width=0.6, edgecolor='#0f172a', linewidth=1.5)
    plt.title('B2B Marketing & Sales Funnel: Stage-by-Stage Volume & Drop-off', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Funnel Stage', fontweight='semibold')
    plt.ylabel('User Volume', fontweight='semibold')
    plt.yscale('log') # Log scale to clearly display all stages from 65,000 down to 363
    
    for bar, (_, row) in zip(bars, df_funnel.iterrows()):
        yval = bar.get_height()
        label_text = f"{int(row['Count']):,}\n({row['Stage_Conversion_Rate_%']}%)"
        plt.text(bar.get_x() + bar.get_width()/2, yval * 1.15, label_text, ha='center', va='bottom', fontsize=9, fontweight='bold')
        
    plt.tight_layout()
    plt.savefig('visualizations/01_funnel_waterfall.png', dpi=300)
    plt.close()
    print("Saved visualizations/01_funnel_waterfall.png")

    # Chart 2: Channel Lead Quality vs Conversion Rate
    plt.figure(figsize=(11, 6))
    scatter = sns.scatterplot(
        data=channel_agg,
        x='Leads',
        y='Lead_to_Customer_%',
        size='Revenue_USD',
        sizes=(150, 1000),
        hue='channel',
        palette='turbo',
        legend=False,
        edgecolor='black',
        linewidth=1.2,
        alpha=0.9
    )
    for _, row in channel_agg.iterrows():
        plt.text(
            row['Leads'] + 20, 
            row['Lead_to_Customer_%'] + 0.15, 
            f"{row['channel']}\n(${row['Revenue_USD']/1000:,.0f}k ARR)", 
            fontsize=8.5, 
            fontweight='semibold'
        )
    plt.title('Lead Volume vs. Lead-to-Customer Conversion Rate by Channel\n(Bubble Size = Total Closed Revenue)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Total Leads Generated', fontweight='semibold')
    plt.ylabel('Lead-to-Customer Conversion Rate (%)', fontweight='semibold')
    plt.axhline(channel_agg['Customers'].sum() / channel_agg['Leads'].sum() * 100, color='red', linestyle='--', alpha=0.7, label='Average Conv Rate')
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('visualizations/02_channel_lead_quality_matrix.png', dpi=300)
    plt.close()
    print("Saved visualizations/02_channel_lead_quality_matrix.png")

    # Chart 3: Stage Drop-off Rates
    plt.figure(figsize=(9, 5))
    drop_stages = df_funnel.iloc[1:].copy()
    stage_transitions = [
        'Visitor → Lead\n(Landing Page Friction)',
        'Lead → MQL\n(Qualification Criteria)',
        'MQL → SQL\n(Sales Discovery Call)',
        'SQL → Opportunity\n(Demo & Proposal)',
        'Opportunity → Customer\n(Closing & Contracting)'
    ]
    drop_stages['Transition'] = stage_transitions
    bars = plt.barh(drop_stages['Transition'], drop_stages['Drop_Off_Rate_%'], color=['#ef4444', '#f97316', '#f59e0b', '#3b82f6', '#10b981'], edgecolor='#1f2937', height=0.55)
    plt.title('Percentage of Drop-off at Each Funnel Transition', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Drop-off Rate (%)', fontweight='semibold')
    plt.xlim(0, 100)
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1.2, bar.get_y() + bar.get_height()/2, f"{width:.1f}%", va='center', fontweight='bold', fontsize=9.5)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('visualizations/03_stage_dropoff_rates.png', dpi=300)
    plt.close()
    print("Saved visualizations/03_stage_dropoff_rates.png")

    # Chart 4: CAC vs ROAS by Channel
    fig, ax1 = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(channel_agg))
    width = 0.35
    
    rects1 = ax1.bar(x - width/2, channel_agg['CAC_USD'], width, label='CAC ($ USD)', color='#e11d48', edgecolor='#881337')
    ax1.set_ylabel('Customer Acquisition Cost (USD $)', color='#e11d48', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(channel_agg['channel'], rotation=25, ha='right', fontsize=9)
    
    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, channel_agg['ROAS'], width, label='ROAS (x)', color='#059669', edgecolor='#064e3b')
    ax2.set_ylabel('Return on Ad Spend (ROAS)', color='#059669', fontweight='bold')
    ax2.grid(False)
    
    plt.title('Unit Economics by Channel: Acquisition Cost (CAC) vs. ROAS', fontsize=13, fontweight='bold', pad=15)
    fig.tight_layout()
    plt.savefig('visualizations/04_channel_cac_vs_roas.png', dpi=300)
    plt.close()
    print("Saved visualizations/04_channel_cac_vs_roas.png")

    # Chart 5: Device Performance
    plt.figure(figsize=(9, 4.5))
    palette = ['#2563eb', '#f59e0b', '#10b981']
    sns.barplot(data=device_agg, x='device', y='Traffic_to_Lead_%', palette=palette, edgecolor='#1e293b')
    plt.title('Landing Page Traffic-to-Lead Conversion Rate by Device', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Device Type', fontweight='semibold')
    plt.ylabel('Visitor-to-Lead Conversion (%)', fontweight='semibold')
    for i, row in device_agg.iterrows():
        plt.text(i, row['Traffic_to_Lead_%'] + 0.2, f"{row['Traffic_to_Lead_%']}% (Bounce: {row['Bounce_Rate_%']}%)", ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig('visualizations/05_device_performance.png', dpi=300)
    plt.close()
    print("Saved visualizations/05_device_performance.png")

    # 9. Export Comprehensive JSON for the Interactive Web Dashboard
    dashboard_data = {
        'metadata': {
            'analysis_title': 'Marketing Funnel & Conversion Performance Analysis',
            'period': 'Jan 2026 - Sep 2026 (Q1-Q3)',
            'total_sessions': int(len(df)),
            'total_customers': int(df['is_customer'].sum()),
            'total_pipeline_revenue': float(round(df['deal_value'].sum(), 2)),
            'total_marketing_spend': float(round(df['cost_usd'].sum(), 2)),
            'overall_conversion_rate': float(round(df['is_customer'].sum() / len(df) * 100, 3)),
            'overall_roas': float(round(df['deal_value'].sum() / df['cost_usd'].sum(), 2)),
            'avg_cac': float(round(df['cost_usd'].sum() / df['is_customer'].sum(), 2)),
            'avg_deal_size': float(round(df['deal_value'].sum() / df['is_customer'].sum(), 2))
        },
        'macro_funnel': df_funnel.to_dict(orient='records'),
        'channels': channel_agg.to_dict(orient='records'),
        'devices': device_agg.to_dict(orient='records'),
        'monthly_trends': monthly_agg.to_dict(orient='records'),
        'campaigns': campaign_agg.to_dict(orient='records')
    }
    
    os.makedirs('dashboard/data', exist_ok=True)
    with open('dashboard/data/funnel_metrics.json', 'w') as f:
        json.dump(dashboard_data, f, indent=2)
    print("Saved dashboard/data/funnel_metrics.json successfully.")

    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    run_funnel_analytics()
