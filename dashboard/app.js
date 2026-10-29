/**
 * Marketing Funnel & Conversion Analytics Dashboard Logic
 * Future Interns - Task 3 (2026)
 */

// Embedded Baseline Data (guarantees instantaneous rendering even if opened via file://)
const DEFAULT_DATA = {
  "metadata": {
    "total_sessions": 65000,
    "total_customers": 363,
    "total_pipeline_revenue": 6978674.18,
    "total_marketing_spend": 182367.05,
    "overall_conversion_rate": 0.558,
    "overall_roas": 38.27,
    "avg_cac": 502.39,
    "avg_deal_size": 19225.0
  },
  "macro_funnel": [
    { "Stage": "Visitor", "Count": 65000, "Stage_Conversion_Rate_%": 100.0, "Cumulative_Conversion_Rate_%": 100.0, "Drop_Off_Count": 0, "Drop_Off_Rate_%": 0.0, "gradient": "var(--grad-visitor)", "icon": "fa-globe" },
    { "Stage": "Lead", "Count": 4466, "Stage_Conversion_Rate_%": 6.87, "Cumulative_Conversion_Rate_%": 6.87, "Drop_Off_Count": 60534, "Drop_Off_Rate_%": 93.13, "gradient": "var(--grad-lead)", "icon": "fa-user-plus" },
    { "Stage": "MQL", "Count": 2460, "Stage_Conversion_Rate_%": 55.08, "Cumulative_Conversion_Rate_%": 3.79, "Drop_Off_Count": 2006, "Drop_Off_Rate_%": 44.92, "gradient": "var(--grad-mql)", "icon": "fa-id-card-clip" },
    { "Stage": "SQL", "Count": 1456, "Stage_Conversion_Rate_%": 59.19, "Cumulative_Conversion_Rate_%": 2.24, "Drop_Off_Count": 1004, "Drop_Off_Rate_%": 40.81, "gradient": "var(--grad-sql)", "icon": "fa-comments-dollar" },
    { "Stage": "Opportunity", "Count": 1003, "Stage_Conversion_Rate_%": 68.89, "Cumulative_Conversion_Rate_%": 1.54, "Drop_Off_Count": 453, "Drop_Off_Rate_%": 31.11, "gradient": "var(--grad-opp)", "icon": "fa-briefcase" },
    { "Stage": "Customer", "Count": 363, "Stage_Conversion_Rate_%": 36.19, "Cumulative_Conversion_Rate_%": 0.558, "Drop_Off_Count": 640, "Drop_Off_Rate_%": 63.81, "gradient": "var(--grad-cust)", "icon": "fa-award" }
  ],
  "channels": [
    { "channel": "Referral / Partner", "Visitors": 5248, "Leads": 620, "Customers": 127, "Traffic_to_Lead_%": 11.81, "Lead_to_Customer_%": 20.48, "CAC_USD": 49.59, "ROAS": 416.19, "Revenue_USD": 2621027.20, "Spend_USD": 6297.60, "rating": "Tier 1: High Quality" },
    { "channel": "LinkedIn Ads (B2B)", "Visitors": 9150, "Leads": 476, "Customers": 70, "Traffic_to_Lead_%": 5.20, "Lead_to_Customer_%": 14.71, "CAC_USD": 1241.79, "ROAS": 17.20, "Revenue_USD": 1494918.26, "Spend_USD": 86925.00, "rating": "Tier 1: High ACV" },
    { "channel": "Email Marketing", "Visitors": 7263, "Leads": 716, "Customers": 62, "Traffic_to_Lead_%": 9.86, "Lead_to_Customer_%": 8.66, "CAC_USD": 17.57, "ROAS": 906.50, "Revenue_USD": 987585.02, "Spend_USD": 1089.45, "rating": "Tier 2: High ROI" },
    { "channel": "Organic Search", "Visitors": 16935, "Leads": 1157, "Customers": 48, "Traffic_to_Lead_%": 6.83, "Lead_to_Customer_%": 4.15, "CAC_USD": 158.77, "ROAS": 110.38, "Revenue_USD": 841199.28, "Spend_USD": 7620.75, "rating": "Tier 2: Sustainable" },
    { "channel": "Paid Search (Google Ads)", "Visitors": 14154, "Leads": 890, "Customers": 33, "Traffic_to_Lead_%": 6.29, "Lead_to_Customer_%": 3.71, "CAC_USD": 2058.76, "ROAS": 9.20, "Revenue_USD": 624931.42, "Spend_USD": 67939.20, "rating": "Tier 3: Moderate" },
    { "channel": "Direct Traffic", "Visitors": 5827, "Leads": 426, "Customers": 21, "Traffic_to_Lead_%": 7.31, "Lead_to_Customer_%": 4.93, "CAC_USD": 13.87, "ROAS": 1300.85, "Revenue_USD": 379002.26, "Spend_USD": 291.35, "rating": "Tier 2: Baseline" },
    { "channel": "Social Media (Meta/X)", "Visitors": 6423, "Leads": 181, "Customers": 2, "Traffic_to_Lead_%": 2.82, "Lead_to_Customer_%": 1.10, "CAC_USD": 6101.85, "ROAS": 2.46, "Revenue_USD": 30010.74, "Spend_USD": 12203.70, "rating": "Tier 4: Underperforming" }
  ],
  "devices": [
    { "device": "Desktop", "Visitors": 37458, "Leads": 3072, "Customers": 278, "Traffic_to_Lead_%": 8.20, "Lead_to_Customer_%": 9.05, "Overall_Conv_%": 0.742, "Bounce_Rate_%": 0.0, "Revenue": 5352840.10 },
    { "device": "Mobile", "Visitors": 23579, "Leads": 1198, "Customers": 78, "Traffic_to_Lead_%": 5.08, "Lead_to_Customer_%": 6.52, "Overall_Conv_%": 0.331, "Bounce_Rate_%": 3.34, "Revenue": 1492340.50 },
    { "device": "Tablet", "Visitors": 3963, "Leads": 196, "Customers": 7, "Traffic_to_Lead_%": 4.95, "Lead_to_Customer_%": 3.57, "Overall_Conv_%": 0.177, "Bounce_Rate_%": 0.0, "Revenue": 133493.58 }
  ],
  "monthly_trends": [
    { "month": "Jan 2026", "Visitors": 3766, "Leads": 254, "Customers": 18, "Revenue": 317869.61, "Spend": 10321.05, "Conv_Rate_%": 0.478 },
    { "month": "Feb 2026", "Visitors": 5162, "Leads": 359, "Customers": 22, "Revenue": 398328.08, "Spend": 14528.20, "Conv_Rate_%": 0.426 },
    { "month": "Mar 2026", "Visitors": 6537, "Leads": 458, "Customers": 37, "Revenue": 697294.45, "Spend": 18245.55, "Conv_Rate_%": 0.566 },
    { "month": "Apr 2026", "Visitors": 7012, "Leads": 445, "Customers": 43, "Revenue": 795239.37, "Spend": 19747.90, "Conv_Rate_%": 0.613 },
    { "month": "May 2026", "Visitors": 7843, "Leads": 547, "Customers": 43, "Revenue": 764905.09, "Spend": 21897.95, "Conv_Rate_%": 0.548 },
    { "month": "Jun 2026", "Visitors": 8224, "Leads": 573, "Customers": 55, "Revenue": 1152211.91, "Spend": 23227.90, "Conv_Rate_%": 0.669 },
    { "month": "Jul 2026", "Visitors": 8685, "Leads": 569, "Customers": 43, "Revenue": 735202.09, "Spend": 24322.75, "Conv_Rate_%": 0.495 },
    { "month": "Aug 2026", "Visitors": 9067, "Leads": 623, "Customers": 55, "Revenue": 1265723.42, "Spend": 25154.35, "Conv_Rate_%": 0.607 },
    { "month": "Sep 2026", "Visitors": 8704, "Leads": 638, "Customers": 47, "Revenue": 851900.16, "Spend": 24921.40, "Conv_Rate_%": 0.540 }
  ]
};

// Global State
let funnelData = JSON.parse(JSON.stringify(DEFAULT_DATA));
let currentTableSort = { column: 'Revenue_USD', ascending: false };
let charts = {};

// Helper Formatters
const fmt = {
  currency: (v) => '$' + Number(v).toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 }),
  decimalCurrency: (v) => '$' + Number(v).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }),
  number: (v) => Number(v).toLocaleString('en-US'),
  percent: (v) => Number(v).toFixed(2) + '%',
  precisePercent: (v) => Number(v).toFixed(3) + '%'
};

// Initialization on DOM Loaded
document.addEventListener('DOMContentLoaded', async () => {
  console.log("Initializing Marketing Funnel Analytics Dashboard...");
  
  // Try fetching dynamic JSON if available (HTTP server mode)
  try {
    const res = await fetch('data/funnel_metrics.json');
    if (res.ok) {
      const liveJson = await res.json();
      if (liveJson && liveJson.metadata) {
        funnelData.metadata = liveJson.metadata;
        funnelData.macro_funnel = liveJson.macro_funnel;
        funnelData.channels = liveJson.channels;
        funnelData.devices = liveJson.devices;
        console.log("Loaded live funnel_metrics.json successfully.");
      }
    }
  } catch (e) {
    console.log("Using embedded baseline data (offline/file mode).");
  }

  // Render Components
  renderKPIs(funnelData.metadata);
  renderFunnelWaterfall(funnelData.macro_funnel);
  initCharts();
  renderChannelTable(funnelData.channels);
  initSimulator();
  initEventListeners();
});

// Render Top KPI Cards
function renderKPIs(meta) {
  document.getElementById('kpiVisitors').textContent = fmt.number(meta.total_sessions);
  document.getElementById('kpiLeads').textContent = fmt.number(meta.total_sessions * 0.0687);
  document.getElementById('kpiCustomers').textContent = fmt.number(meta.total_customers);
  document.getElementById('kpiRevenue').textContent = fmt.currency(meta.total_pipeline_revenue);
  document.getElementById('kpiCAC').textContent = fmt.decimalCurrency(meta.avg_cac);
  document.getElementById('kpiROAS').textContent = Number(meta.overall_roas).toFixed(2) + 'x';
  
  document.getElementById('kpiAvgDeal').textContent = 'Avg ACV: ' + fmt.currency(meta.avg_deal_size);
  document.getElementById('kpiSpend').textContent = 'Total Spend: ' + fmt.currency(meta.total_marketing_spend);
}

// Render Interactive Funnel Waterfall Rows
function renderFunnelWaterfall(stages) {
  const container = document.getElementById('funnelContainer');
  container.innerHTML = '';
  
  const stageMeta = [
    { desc: "Inbound sessions on site", icon: "fa-globe", grad: "var(--grad-visitor)" },
    { desc: "Form fill / Whitepaper / Trial", icon: "fa-user-plus", grad: "var(--grad-lead)" },
    { desc: "Firmographic criteria passed", icon: "fa-id-card-clip", grad: "var(--grad-mql)" },
    { desc: "Discovery call & BANT verified", icon: "fa-comments-dollar", grad: "var(--grad-sql)" },
    { desc: "Product demo & custom proposal", icon: "fa-briefcase", grad: "var(--grad-opp)" },
    { desc: "Contract signed & won", icon: "fa-award", grad: "var(--grad-cust)" }
  ];

  const maxVolume = stages[0].Count;

  stages.forEach((st, idx) => {
    const meta = stageMeta[idx] || { desc: "", icon: "fa-circle", grad: "var(--grad-lead)" };
    
    // Width logic: proportional with visual log smoothing so bottom stages are prominent
    const rawPct = (st.Count / maxVolume) * 100;
    const visualWidthPct = Math.max(12, Math.min(100, Math.pow(st.Count / maxVolume, 0.45) * 100));

    const row = document.createElement('div');
    row.className = 'funnel-stage-row';
    row.innerHTML = `
      <div class="stage-info">
        <span class="stage-title"><i class="fa-solid ${meta.icon}"></i> ${st.Stage}</span>
        <span class="stage-desc">${meta.desc}</span>
      </div>
      
      <div class="stage-bar-wrapper">
        <div class="stage-bar-fill" style="width: ${visualWidthPct}%; background: ${meta.grad};">
          <span class="stage-bar-val">${fmt.number(st.Count)} (${st['Cumulative_Conversion_Rate_%']}%)</span>
        </div>
      </div>

      <div class="stage-stats">
        <div class="stat-block">
          <span class="stat-label">Stage Conv</span>
          <span class="stat-value conv">${st['Stage_Conversion_Rate_%']}%</span>
        </div>
        <div class="stat-block">
          <span class="stat-label">Drop-Off</span>
          <span class="stat-value dropoff">${idx === 0 ? '-' : st['Drop_Off_Rate_%'] + '%'}</span>
        </div>
        <div class="stat-block">
          <span class="stat-label">Lost Leads</span>
          <span class="stat-value">${idx === 0 ? '-' : fmt.number(st.Drop_Off_Count)}</span>
        </div>
      </div>
    `;
    container.appendChild(row);
  });
}

// Initialize Charts with Chart.js
function initCharts() {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const textColor = isDark ? '#94a3b8' : '#475569';
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)';

  // Chart 1: Channel Quality Bubble / Dual Bar Chart
  const ctx1 = document.getElementById('channelQualityChart').getContext('2d');
  const chData = funnelData.channels;

  charts.channelQuality = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: chData.map(c => c.channel.replace(' (Google Ads)', '').replace(' (Meta/X)', '').replace(' (B2B)', '')),
      datasets: [
        {
          label: 'Lead-to-Customer %',
          data: chData.map(c => c['Lead_to_Customer_%']),
          backgroundColor: '#3b82f6',
          borderRadius: 6,
          yAxisID: 'y1'
        },
        {
          label: 'Total Leads Generated',
          data: chData.map(c => c.Leads),
          backgroundColor: 'rgba(139, 92, 246, 0.35)',
          borderColor: '#8b5cf6',
          borderWidth: 1.5,
          borderRadius: 6,
          yAxisID: 'y'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { labels: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 11 } } },
        tooltip: {
          callbacks: {
            footer: (items) => {
              const idx = items[0].dataIndex;
              return `Closed ARR: ${fmt.currency(chData[idx].Revenue_USD)} | CAC: $${chData[idx].CAC_USD}`;
            }
          }
        }
      },
      scales: {
        x: { ticks: { color: textColor, font: { size: 10 } }, grid: { display: false } },
        y: {
          type: 'linear',
          position: 'left',
          title: { display: true, text: 'Total Leads', color: textColor, font: { size: 10 } },
          ticks: { color: textColor },
          grid: { color: gridColor }
        },
        y1: {
          type: 'linear',
          position: 'right',
          title: { display: true, text: 'Conversion %', color: textColor, font: { size: 10 } },
          ticks: { color: '#3b82f6', callback: (v) => v + '%' },
          grid: { display: false }
        }
      }
    }
  });

  // Chart 2: Drop-off Rate by Funnel Stage Transition
  const ctx2 = document.getElementById('stageDropoffChart').getContext('2d');
  charts.stageDropoff = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: [
        'Visitor → Lead',
        'Lead → MQL',
        'MQL → SQL',
        'SQL → Opp',
        'Opp → Customer'
      ],
      datasets: [{
        label: 'Drop-Off Rate (%)',
        data: [93.13, 44.92, 40.81, 31.11, 63.81],
        backgroundColor: [
          '#ef4444', // Red (largest leak)
          '#f97316',
          '#f59e0b',
          '#3b82f6',
          '#ec4899'  // High opportunity leakage
        ],
        borderRadius: 8
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => `Drop-Off: ${ctx.raw}% of prospects lost at this milestone`
          }
        }
      },
      scales: {
        x: {
          max: 100,
          ticks: { color: textColor, callback: (v) => v + '%' },
          grid: { color: gridColor }
        },
        y: { ticks: { color: textColor, font: { weight: 600 } }, grid: { display: false } }
      }
    }
  });

  // Chart 3: Monthly Performance Trends
  const ctx3 = document.getElementById('monthlyTrendChart').getContext('2d');
  const moData = funnelData.monthly_trends;
  charts.monthlyTrend = new Chart(ctx3, {
    type: 'line',
    data: {
      labels: moData.map(m => m.month),
      datasets: [
        {
          label: 'Closed ARR ($)',
          data: moData.map(m => m.Revenue),
          borderColor: '#10b981',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          fill: true,
          tension: 0.35,
          yAxisID: 'y'
        },
        {
          label: 'Marketing Spend ($)',
          data: moData.map(m => m.Spend),
          borderColor: '#f59e0b',
          backgroundColor: 'transparent',
          borderDash: [5, 5],
          tension: 0.35,
          yAxisID: 'y'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { labels: { color: textColor } },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: ${fmt.currency(ctx.raw)}`
          }
        }
      },
      scales: {
        x: { ticks: { color: textColor }, grid: { display: false } },
        y: {
          ticks: { color: textColor, callback: (v) => '$' + (v / 1000) + 'k' },
          grid: { color: gridColor }
        }
      }
    }
  });

  // Chart 4: Device & Platform Performance
  const ctx4 = document.getElementById('deviceChart').getContext('2d');
  const devData = funnelData.devices;
  charts.device = new Chart(ctx4, {
    type: 'bar',
    data: {
      labels: devData.map(d => d.device),
      datasets: [
        {
          label: 'Traffic-to-Lead Conv %',
          data: devData.map(d => d['Traffic_to_Lead_%']),
          backgroundColor: '#3b82f6',
          borderRadius: 6
        },
        {
          label: 'Overall Visitor-to-Customer %',
          data: devData.map(d => d['Overall_Conv_%'] * 10), // scaled 10x for visual clarity
          backgroundColor: '#10b981',
          borderRadius: 6
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: textColor } },
        tooltip: {
          callbacks: {
            label: (ctx) => {
              if (ctx.datasetIndex === 1) {
                return `Overall Conv: ${(ctx.raw / 10).toFixed(3)}%`;
              }
              return `Traffic-to-Lead: ${ctx.raw}%`;
            }
          }
        }
      },
      scales: {
        x: { ticks: { color: textColor }, grid: { display: false } },
        y: {
          ticks: { color: textColor, callback: (v) => v + '%' },
          grid: { color: gridColor }
        }
      }
    }
  });
}

// Render Channel Scorecard Table with Sorting
function renderChannelTable(channels) {
  const tbody = document.getElementById('channelTableBody');
  tbody.innerHTML = '';

  const getTierClass = (rating) => {
    if (rating.includes('Tier 1')) return 'rating-tier1';
    if (rating.includes('Tier 2')) return 'rating-tier2';
    if (rating.includes('Tier 3')) return 'rating-tier3';
    return 'rating-tier4';
  };

  channels.forEach(ch => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${ch.channel}</strong></td>
      <td>${fmt.number(ch.Visitors)}</td>
      <td>${fmt.number(ch.Leads)}</td>
      <td><strong>${fmt.number(ch.Customers)}</strong></td>
      <td>${ch['Traffic_to_Lead_%']}%</td>
      <td><strong>${ch['Lead_to_Customer_%']}%</strong></td>
      <td>$${Number(ch.CAC_USD).toFixed(2)}</td>
      <td><span style="color: #10b981; font-weight:700;">${Number(ch.ROAS).toFixed(1)}x</span></td>
      <td><strong>${fmt.currency(ch.Revenue_USD)}</strong></td>
      <td><span class="rating-badge ${getTierClass(ch.rating || '')}">${ch.rating || 'Standard'}</span></td>
    `;
    tbody.appendChild(tr);
  });
}

// "What-If" Revenue Optimization Simulator Engine
function initSimulator() {
  const sliderVtoL = document.getElementById('sliderVtoL');
  const sliderLtoMQL = document.getElementById('sliderLtoMQL');
  const sliderOppToCust = document.getElementById('sliderOppToCust');

  const baseVisitors = funnelData.metadata.total_sessions;
  const baseAvgDeal = funnelData.metadata.avg_deal_size; // $19,225
  const baseSpend = funnelData.metadata.total_marketing_spend;

  const baseRates = {
    v_to_l: 0.06871,
    l_to_mql: 0.5508,
    mql_to_sql: 0.5919,
    sql_to_opp: 0.6889,
    opp_to_cust: 0.3619
  };

  function updateSimulation() {
    const liftVtoL = Number(sliderVtoL.value) / 100;
    const liftLtoMQL = Number(sliderLtoMQL.value) / 100;
    const liftOppToCust = Number(sliderOppToCust.value) / 100;

    // Display labels
    document.getElementById('dispVtoL').textContent = `+${sliderVtoL.value}%`;
    document.getElementById('dispLtoMQL').textContent = `+${sliderLtoMQL.value}%`;
    document.getElementById('dispOppToCust').textContent = `+${sliderOppToCust.value}%`;

    const simRateVtoL = baseRates.v_to_l * (1 + liftVtoL);
    const simRateLtoMQL = baseRates.l_to_mql * (1 + liftLtoMQL);
    const simRateOppToCust = baseRates.opp_to_cust * (1 + liftOppToCust);

    document.getElementById('projVtoL').textContent = `Simulated: ${(simRateVtoL * 100).toFixed(2)}%`;
    document.getElementById('projLtoMQL').textContent = `Simulated: ${(simRateLtoMQL * 100).toFixed(2)}%`;
    document.getElementById('projOppToCust').textContent = `Simulated: ${(simRateOppToCust * 100).toFixed(2)}%`;

    // Cascade stages
    const simLeads = baseVisitors * simRateVtoL;
    const simMQLs = simLeads * simRateLtoMQL;
    const simSQLs = simMQLs * baseRates.mql_to_sql;
    const simOpps = simSQLs * baseRates.sql_to_opp;
    const simCusts = simOpps * simRateOppToCust;

    const baseCusts = 363;
    const addedCusts = Math.max(0, Math.round(simCusts - baseCusts));
    const addedRevenue = addedCusts * baseAvgDeal;
    const newTotalRevenue = funnelData.metadata.total_pipeline_revenue + addedRevenue;
    const newROAS = newTotalRevenue / baseSpend;

    // Update Simulator Output
    document.getElementById('simAddedRevenue').textContent = `+${fmt.currency(addedRevenue)}`;
    document.getElementById('simTotalRevenue').textContent = fmt.currency(newTotalRevenue);
    document.getElementById('simTotalCust').textContent = `${Math.round(simCusts)} Deals`;
    document.getElementById('simAddedCust').textContent = `+${addedCusts} Deals Won`;
    document.getElementById('simNewROAS').textContent = `${newROAS.toFixed(2)}x`;

    const summaryText = addedRevenue > 0
      ? `By increasing Visitor→Lead by ${sliderVtoL.value}%, MQL qualification by ${sliderLtoMQL.value}%, and Deal Close Rate by ${sliderOppToCust.value}%, the company unlocks ${fmt.currency(addedRevenue)} in incremental ARR with 0 additional ad spend!`
      : `Move the sliders above to model compound conversion lift across funnel stages.`;
    document.getElementById('simSummaryText').textContent = summaryText;
  }

  sliderVtoL.addEventListener('input', updateSimulation);
  sliderLtoMQL.addEventListener('input', updateSimulation);
  sliderOppToCust.addEventListener('input', updateSimulation);

  document.getElementById('resetSimBtn').addEventListener('click', () => {
    sliderVtoL.value = 0;
    sliderLtoMQL.value = 0;
    sliderOppToCust.value = 0;
    updateSimulation();
  });
}

// Global Event Listeners & Filter Handlers
function initEventListeners() {
  // Theme Toggle
  const themeToggle = document.getElementById('themeToggleBtn');
  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    themeToggle.innerHTML = newTheme === 'dark' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
    // Re-render charts with updated theme colors
    Object.values(charts).forEach(c => c.destroy());
    initCharts();
  });

  // Print Executive Report
  document.getElementById('printReportBtn').addEventListener('click', () => {
    window.print();
  });

  // Export CSV
  document.getElementById('exportCsvBtn').addEventListener('click', () => {
    const csvContent = "data:text/csv;charset=utf-8," 
      + "Channel,Visitors,Leads,Customers,Visitor_to_Lead_%,Lead_to_Customer_%,CAC_USD,ROAS,Revenue_USD\n"
      + funnelData.channels.map(c => 
          `"${c.channel}",${c.Visitors},${c.Leads},${c.Customers},${c['Traffic_to_Lead_%']},${c['Lead_to_Customer_%']},${c.CAC_USD},${c.ROAS},${c.Revenue_USD}`
        ).join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "marketing_funnel_channel_performance.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });

  // Channel Table Search
  document.getElementById('channelSearchInput').addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const filtered = funnelData.channels.filter(c => c.channel.toLowerCase().includes(query));
    renderChannelTable(filtered);
  });

  // Table Column Sort Click Handlers
  document.querySelectorAll('#channelTable th[data-sort]').forEach(th => {
    th.addEventListener('click', () => {
      const col = th.getAttribute('data-sort');
      if (currentTableSort.column === col) {
        currentTableSort.ascending = !currentTableSort.ascending;
      } else {
        currentTableSort.column = col;
        currentTableSort.ascending = false;
      }

      funnelData.channels.sort((a, b) => {
        let vA = a[col];
        let vB = b[col];
        if (typeof vA === 'string') {
          return currentTableSort.ascending ? vA.localeCompare(vB) : vB.localeCompare(vA);
        }
        return currentTableSort.ascending ? vA - vB : vB - vA;
      });

      renderChannelTable(funnelData.channels);
    });
  });

  // Filter Select Handlers
  const channelFilter = document.getElementById('channelFilter');
  const deviceFilter = document.getElementById('deviceFilter');
  const quarterFilter = document.getElementById('quarterFilter');

  function applyGlobalFilters() {
    const selChannel = channelFilter.value;
    const selDevice = deviceFilter.value;
    const selQuarter = quarterFilter.value;

    let mult = 1.0;
    if (selQuarter === 'Q1') mult = 0.25;
    else if (selQuarter === 'Q2') mult = 0.38;
    else if (selQuarter === 'Q3') mult = 0.37;

    let targetChannel = funnelData.channels.find(c => c.channel === selChannel);

    if (selChannel !== 'ALL' && targetChannel) {
      renderKPIs({
        total_sessions: Math.round(targetChannel.Visitors * mult),
        total_customers: Math.round(targetChannel.Customers * mult),
        total_pipeline_revenue: targetChannel.Revenue_USD * mult,
        total_marketing_spend: targetChannel.Spend_USD * mult,
        overall_conversion_rate: ((targetChannel.Customers / targetChannel.Visitors) * 100),
        overall_roas: targetChannel.ROAS,
        avg_cac: targetChannel.CAC_USD,
        avg_deal_size: targetChannel.Revenue_USD / targetChannel.Customers
      });

      // Filtered funnel
      const filteredFunnel = [
        { Stage: "Visitor", Count: Math.round(targetChannel.Visitors * mult), "Stage_Conversion_Rate_%": 100, "Cumulative_Conversion_Rate_%": 100, "Drop_Off_Count": 0, "Drop_Off_Rate_%": 0 },
        { Stage: "Lead", Count: Math.round(targetChannel.Leads * mult), "Stage_Conversion_Rate_%": targetChannel['Traffic_to_Lead_%'], "Cumulative_Conversion_Rate_%": targetChannel['Traffic_to_Lead_%'], "Drop_Off_Count": Math.round((targetChannel.Visitors - targetChannel.Leads) * mult), "Drop_Off_Rate_%": (100 - targetChannel['Traffic_to_Lead_%']).toFixed(1) },
        { Stage: "Customer", Count: Math.round(targetChannel.Customers * mult), "Stage_Conversion_Rate_%": targetChannel['Lead_to_Customer_%'], "Cumulative_Conversion_Rate_%": ((targetChannel.Customers / targetChannel.Visitors) * 100).toFixed(2), "Drop_Off_Count": Math.round((targetChannel.Leads - targetChannel.Customers) * mult), "Drop_Off_Rate_%": (100 - targetChannel['Lead_to_Customer_%']).toFixed(1) }
      ];
      renderFunnelWaterfall(filteredFunnel);
    } else {
      // Revert to full blended metrics
      renderKPIs({
        total_sessions: Math.round(DEFAULT_DATA.metadata.total_sessions * mult),
        total_customers: Math.round(DEFAULT_DATA.metadata.total_customers * mult),
        total_pipeline_revenue: DEFAULT_DATA.metadata.total_pipeline_revenue * mult,
        total_marketing_spend: DEFAULT_DATA.metadata.total_marketing_spend * mult,
        overall_conversion_rate: DEFAULT_DATA.metadata.overall_conversion_rate,
        overall_roas: DEFAULT_DATA.metadata.overall_roas,
        avg_cac: DEFAULT_DATA.metadata.avg_cac,
        avg_deal_size: DEFAULT_DATA.metadata.avg_deal_size
      });
      renderFunnelWaterfall(DEFAULT_DATA.macro_funnel);
    }
  }

  channelFilter.addEventListener('change', applyGlobalFilters);
  deviceFilter.addEventListener('change', applyGlobalFilters);
  quarterFilter.addEventListener('change', applyGlobalFilters);

  document.getElementById('resetFiltersBtn').addEventListener('click', () => {
    channelFilter.value = 'ALL';
    deviceFilter.value = 'ALL';
    quarterFilter.value = 'ALL';
    applyGlobalFilters();
  });
}
