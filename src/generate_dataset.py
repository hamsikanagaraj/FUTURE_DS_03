"""
Dataset Generator for Marketing Funnel & Conversion Performance Analysis
Task 3 - Future Interns (2026)
Generates realistic multi-channel marketing funnel session and lead conversion data.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_funnel_dataset(num_records=65000, seed=42):
    np.random.seed(seed)
    
    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 9, 30)
    total_days = (end_date - start_date).days
    
    # Marketing Channels and realistic distribution weights
    channels = [
        'Organic Search', 
        'Paid Search (Google Ads)', 
        'LinkedIn Ads (B2B)', 
        'Email Marketing', 
        'Referral / Partner', 
        'Social Media (Meta/X)', 
        'Direct Traffic'
    ]
    channel_weights = [0.26, 0.22, 0.14, 0.11, 0.08, 0.10, 0.09]
    
    # Campaigns associated with channels
    campaign_map = {
        'Organic Search': ['SEO_Inbound_Blog', 'SEO_Product_Keywords', 'Organic_Brand'],
        'Paid Search (Google Ads)': ['SEM_HighIntent_Competitor', 'SEM_Category_Search', 'SEM_Brand_Defense'],
        'LinkedIn Ads (B2B)': ['LI_Enterprise_Whitepaper', 'LI_CTO_DecisionMaker_Video', 'LI_Retargeting_CaseStudy'],
        'Email Marketing': ['Nurture_Workflow_Weekly', 'Product_Newsletter_ProductUpdates', 'Winback_Cold_Sequence'],
        'Referral / Partner': ['Partner_Integration_CoMarketing', 'Affiliate_Network_2026', 'Customer_Advocacy_Referral'],
        'Social Media (Meta/X)': ['Social_Thought_Leadership', 'Viral_Infographic_Campaign', 'Community_Event_Promo'],
        'Direct Traffic': ['Direct_Brand_Nav', 'Offline_Conference_Handouts', 'Word_of_Mouth']
    }
    
    devices = ['Desktop', 'Mobile', 'Tablet']
    device_weights = [0.58, 0.36, 0.06]
    
    regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America']
    region_weights = [0.48, 0.28, 0.16, 0.08]
    
    industries = ['Software & SaaS', 'Financial Services', 'Healthcare & Life Sciences', 'Retail & E-commerce', 'Manufacturing']
    industry_weights = [0.35, 0.22, 0.18, 0.15, 0.10]

    # Channel conversion rate characteristics (realistic B2B SaaS benchmarks)
    # [Visitor->Lead, Lead->MQL, MQL->SQL, SQL->Opp, Opp->Customer]
    channel_benchmarks = {
        'Organic Search':            [0.055, 0.46, 0.52, 0.62, 0.28],
        'Paid Search (Google Ads)':  [0.048, 0.42, 0.48, 0.58, 0.26],
        'LinkedIn Ads (B2B)':        [0.038, 0.65, 0.68, 0.72, 0.35], # High quality, higher CAC
        'Email Marketing':           [0.082, 0.58, 0.62, 0.68, 0.32], # Warm audience, high conversion
        'Referral / Partner':        [0.095, 0.68, 0.74, 0.78, 0.42], # Highest conversion & trust
        'Social Media (Meta/X)':     [0.024, 0.28, 0.32, 0.44, 0.18], # Low intent, high drop-off
        'Direct Traffic':            [0.062, 0.50, 0.55, 0.64, 0.30]
    }
    
    # Channel Cost Per Click / Visit (for CAC calculation)
    channel_cpc = {
        'Organic Search': 0.45,           # Content / SEO amortization
        'Paid Search (Google Ads)': 4.80, # Ad spend
        'LinkedIn Ads (B2B)': 9.50,       # Targeted executive B2B clicks
        'Email Marketing': 0.15,          # ESP infrastructure cost
        'Referral / Partner': 1.20,       # Affiliate fee / partner revenue share baseline
        'Social Media (Meta/X)': 1.90,    # Social display ad spend
        'Direct Traffic': 0.05            # Direct baseline infrastructure
    }

    records = []
    
    for i in range(1, num_records + 1):
        session_id = f"SES-{2026000000 + i}"
        user_id = f"USR-{100000 + (i % 42000)}"
        
        # Date generation with slight growth trend over time
        day_offset = int(np.random.beta(1.3, 1.0) * total_days)
        session_time = start_date + timedelta(days=day_offset, 
                                              hours=np.random.randint(0, 24), 
                                              minutes=np.random.randint(0, 60))
        
        channel = np.random.choice(channels, p=channel_weights)
        campaign = np.random.choice(campaign_map[channel])
        device = np.random.choice(devices, p=device_weights)
        region = np.random.choice(regions, p=region_weights)
        industry = np.random.choice(industries, p=industry_weights)
        
        # Device adjustment multipliers (Desktop converts higher in B2B than mobile)
        dev_mult = 1.15 if device == 'Desktop' else (0.75 if device == 'Mobile' else 0.85)
        
        # Region multiplier
        reg_mult = 1.10 if region == 'North America' else (1.02 if region == 'Europe' else 0.88)
        
        probs = channel_benchmarks[channel]
        
        # Engagement metrics
        if device == 'Mobile':
            time_on_page = int(np.random.exponential(scale=65) + 10)
            pages_viewed = int(np.random.geometric(p=0.45))
        else:
            time_on_page = int(np.random.exponential(scale=140) + 25)
            pages_viewed = int(np.random.geometric(p=0.32))
            
        bounce = 1 if (time_on_page < 15 and pages_viewed == 1) else 0
        
        # Stage 1: Visitor (Always 1)
        is_visitor = 1
        
        # Stage 2: Lead (e.g. Content download, newsletter, demo request)
        p_lead = min(0.40, probs[0] * dev_mult * reg_mult * (0.2 if bounce == 1 else 1.25))
        is_lead = 1 if np.random.rand() < p_lead else 0
        
        is_mql = 0
        is_sql = 0
        is_opp = 0
        is_customer = 0
        drop_off_stage = 'Visitor'
        deal_value = 0.0
        days_to_close = 0
        
        if is_lead:
            # Stage 3: Marketing Qualified Lead (MQL)
            p_mql = min(0.90, probs[1] * (1.1 if industry in ['Software & SaaS', 'Financial Services'] else 0.95))
            if np.random.rand() < p_mql:
                is_mql = 1
                # Stage 4: Sales Qualified Lead (SQL)
                p_sql = min(0.90, probs[2] * dev_mult)
                if np.random.rand() < p_sql:
                    is_sql = 1
                    # Stage 5: Opportunity (Demo / Proposal)
                    p_opp = min(0.90, probs[3])
                    if np.random.rand() < p_opp:
                        is_opp = 1
                        # Stage 6: Customer (Closed-Won)
                        p_cust = min(0.85, probs[4] * (1.15 if channel in ['LinkedIn Ads (B2B)', 'Referral / Partner'] else 1.0))
                        if np.random.rand() < p_cust:
                            is_customer = 1
                            drop_off_stage = 'Converted (Customer)'
                            # High-value SaaS deal ACV ($8,000 to $48,000)
                            base_deal = np.random.lognormal(mean=9.6, sigma=0.55) # ~$15k average
                            if channel == 'LinkedIn Ads (B2B)':
                                base_deal *= 1.35 # Higher tier enterprise
                            elif channel == 'Referral / Partner':
                                base_deal *= 1.20
                            deal_value = round(base_deal, 2)
                            days_to_close = int(np.random.gamma(shape=5, scale=6) + 7) # ~37 days average
                        else:
                            drop_off_stage = 'Opportunity'
                    else:
                        drop_off_stage = 'SQL'
                else:
                    drop_off_stage = 'MQL'
            else:
                drop_off_stage = 'Lead'
                
        # Acquisition cost for this visitor session
        acq_cost = channel_cpc[channel]
        
        records.append({
            'session_id': session_id,
            'user_id': user_id,
            'timestamp': session_time.strftime('%Y-%m-%d %H:%M:%S'),
            'date': session_time.strftime('%Y-%m-%d'),
            'month': session_time.strftime('%Y-%m'),
            'channel': channel,
            'campaign': campaign,
            'device': device,
            'region': region,
            'industry': industry,
            'time_on_page_sec': time_on_page,
            'pages_viewed': pages_viewed,
            'is_bounce': bounce,
            'is_visitor': is_visitor,
            'is_lead': is_lead,
            'is_mql': is_mql,
            'is_sql': is_sql,
            'is_opportunity': is_opp,
            'is_customer': is_customer,
            'drop_off_stage': drop_off_stage,
            'deal_value': deal_value,
            'cost_usd': acq_cost,
            'days_to_close': days_to_close
        })
        
    df = pd.DataFrame(records)
    return df

if __name__ == '__main__':
    print("Generating comprehensive marketing funnel dataset...")
    df = generate_funnel_dataset(num_records=65000, seed=2026)
    
    import os
    os.makedirs('data', exist_ok=True)
    raw_path = 'data/raw_marketing_funnel_data.csv'
    df.to_csv(raw_path, index=False)
    print(f"Dataset successfully saved to {raw_path} with {len(df):,} records.")
    
    # Quick sanity check
    print("\n--- Funnel Stage Counts ---")
    print(f"Total Visitors:      {df['is_visitor'].sum():,}")
    print(f"Total Leads:         {df['is_lead'].sum():,} ({df['is_lead'].sum()/df['is_visitor'].sum():.2%})")
    print(f"Total MQLs:          {df['is_mql'].sum():,} ({df['is_mql'].sum()/df['is_lead'].sum():.2%} of Leads)")
    print(f"Total SQLs:          {df['is_sql'].sum():,} ({df['is_sql'].sum()/df['is_mql'].sum():.2%} of MQLs)")
    print(f"Total Opportunities: {df['is_opportunity'].sum():,} ({df['is_opportunity'].sum()/df['is_sql'].sum():.2%} of SQLs)")
    print(f"Total Customers:     {df['is_customer'].sum():,} ({df['is_customer'].sum()/df['is_opportunity'].sum():.2%} of Opps)")
    print(f"Overall Visitor->Customer Conversion: {df['is_customer'].sum()/df['is_visitor'].sum():.3%}")
    print(f"Total Closed Pipeline Revenue: ${df['deal_value'].sum():,.2f}")
    print(f"Total Marketing Spend:         ${df['cost_usd'].sum():,.2f}")
    print(f"Overall ROAS:                  {df['deal_value'].sum()/df['cost_usd'].sum():.2f}x")
