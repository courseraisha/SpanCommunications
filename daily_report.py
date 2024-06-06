import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime

st.set_page_config(layout="wide")

st.title(":orange[_SPAN COMMUNICATIONS_]")
selected_option = st.sidebar.selectbox("Select an option", ["December Daily Report", "January Performance Leads"])

if selected_option == "December Daily Report":
    data = pd.read_excel("C:/Users/Admin/Desktop/SPAN COMMUNICATIONS/EXCEL FILES/DEC_DAILY_REPORT.xlsx")
    
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Scaling Numeric Columns
    scaler = MinMaxScaler()
    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    # Add back the 'Date' column for plotting later
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Multi-line graph for Impressions and Clicks
    df_impressions_clicks = data[['Date', 'Impressions', 'Clicks']]
    df_impressions_clicks_melted = df_impressions_clicks.melt(id_vars='Date', value_vars=['Impressions', 'Clicks'], var_name='Metric', value_name='Scaled Value')
    
    fig1 = px.line(df_impressions_clicks_melted, x='Date', y='Scaled Value', color='Metric', title='Impressions and Clicks Over Time', markers=True)
    fig1.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""
        **Analysis:**
             In December, both Impressions and Clicks showed an overall upward trend, with a notable increase on December 9, 
             fluctuations from December 12 to 21, a significant spike around December 24 to 27 likely due to holiday activities, 
             and a sharp decline after December 27 possibly due to reduced online activity during the holiday break
        """)
    
    # Multi-line graph for Leads and CPL
    df_leads_cpl = data[['Date', 'Leads', 'CPL']]
    df_leads_cpl_melted = df_leads_cpl.melt(id_vars='Date', value_vars=['Leads', 'CPL'], var_name='Metric', value_name='Scaled Value')
    fig2 = px.line(df_leads_cpl_melted, x='Date', y='Scaled Value', color='Metric', title='Leads and CPL Over Time', markers=True)
    fig2.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig2, use_container_width=True)
    st.write("""
        **Analysis:**
             In December, Leads and Cost Per Lead (CPL) showed varying trends. There was a spike around December 9, 
             likely due to a new campaign. Stability with fluctuations between December 12 and 23 suggests ongoing campaigns. 
             An increase in Leads around December 24 to 27 likely relates to holiday activities, followed by a decline, possibly due to campaign winding down or reduced online activity.
        """)
    
    # Scatter Plot of Leads (or Calls) vs Impressions
    fig5 = px.scatter(data, x='Impressions', y='Leads', title='Leads vs. Impressions Scatter Plot', labels={'Impressions': 'Total Impressions', 'Leads': 'Number of Leads'}, color_discrete_map={"Festival": "blue", "Offer": "orange"})
    st.plotly_chart(fig5, use_container_width=True)  
    st.write("""
        **Analysis:**

        - **Positive Relationship**: There is a general weak relationship between the number of impressions and the number of leads.
        - **Density of Data Points**: Most data points are clustered in the middle range of impressions and leads, indicating moderate engagement.
        """)
    # Correlation Matrix Calculation and Display
    corr_matrix = data[numeric_cols].corr(method='pearson')
    
    # Display correlation matrix
    st.write("**Correlation Matrix:**")
    st.table(corr_matrix.style.background_gradient(cmap='coolwarm').format("{:.3f}"))
    st.write("""
**Analysis:**

- **Positive Correlations:**
   - Impressions and Clicks (0.907): More impressions lead to more clicks, showcasing ad effectiveness.
   - Impressions and Amount Spent (0.983): Increased spending yields wider reach.
   - Clicks and Amount Spent (0.948): Higher spending is linked to increased clicks.
   - Clicks and Leads (0.798): More clicks result in more leads, demonstrating campaign effectiveness.

- **Negative Correlations:**
   - CTR% and CPL (-0.741): Engaging ads with higher CTR are more cost-effective.
   - Leads and CPL (-0.667): More leads generally lead to a lower cost per lead, likely due to economies of scale.

- **Weak Correlations:**
   - CPL and Amount Spent (-0.040): Increasing budget doesn't guarantee lower cost per lead. 
""")
if selected_option == "January Performance Leads":
    data = pd.read_excel("C:/Users/Admin/Desktop/SPAN COMMUNICATIONS/EXCEL FILES/JAN_PERFORMANCE_LEADS.xlsx")
    
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Scaling Numeric Columns
    scaler = MinMaxScaler()
    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    # Add back the 'Date' column for plotting later
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Multi-line graph for Impressions and Clicks
    df_impressions_clicks = data[['Date', 'Impressions', 'Clicks']]
    df_impressions_clicks_melted = df_impressions_clicks.melt(id_vars='Date', value_vars=['Impressions', 'Clicks'], var_name='Metric', value_name='Scaled Value')
    
    fig1 = px.line(df_impressions_clicks_melted, x='Date', y='Scaled Value', color='Metric', title='Impressions and Clicks Over Time', markers=True)
    fig1.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""
        **Analysis:**
             In January, Impressions and Clicks showed fluctuating trends. There was an initial rise, 
             followed by a brief setback. A significant increase occurred from January 17, peaking on January 20, 
             but there was a notable decline thereafter, despite an increase in Impressions, suggesting a discrepancy in Clicks.
        """)
    
    # Multi-line graph for Leads and CPL
    df_leads_cpl = data[['Date', 'Leads', 'CPL']]
    df_leads_cpl_melted = df_leads_cpl.melt(id_vars='Date', value_vars=['Leads', 'CPL'], var_name='Metric', value_name='Scaled Value')
    fig2 = px.line(df_leads_cpl_melted, x='Date', y='Scaled Value', color='Metric', title='Leads and CPL Over Time', markers=True)
    fig2.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig2, use_container_width=True)
    st.write("""
        **Analysis:**
             In January, Leads and Cost Per Lead (CPL) showed varying trends, indicating changes in user engagement and campaign performance. 
             There was a significant spike in both metrics around January 9, likely due to a new campaign, followed by relative stability in CPL 
             with fluctuations in Leads. A sharp decline in Leads towards the end of January, after December 21, accompanied by high CPL, suggests 
             a decline in campaign effectiveness.
        """)
    
    # Scatter Plot of Leads (or Calls) vs Impressions
    fig5 = px.scatter(data, x='Impressions', y='Leads', title='Leads vs. Impressions Scatter Plot', labels={'Impressions': 'Total Impressions', 'Leads': 'Number of Leads'}, color_discrete_map={"Festival": "blue", "Offer": "orange"})
    st.plotly_chart(fig5, use_container_width=True)  
    st.write("""
        **Analysis:**

        - **Positive Relationship**: There is a moderate relationship between the number of impressions and the number of leads.
        - **Density of Data Points**: The relationship is not perfectly linear, as the data points are scattered and do not form a straight line.
        """)
    # Correlation Matrix Calculation and Display
    corr_matrix = data[numeric_cols].corr(method='pearson')
    
    # Display correlation matrix
    st.write("**Correlation Matrix:**")
    st.table(corr_matrix.style.background_gradient(cmap='coolwarm').format("{:.3f}"))
    st.write("""
**Analysis:**

**Positive Correlations:**

* **Impressions and Clicks (0.843):** Strong positive relationship, indicating as impressions increase, clicks tend to increase, suggesting effective ads.
* **Impressions and Amount Spent (0.990):** Very strong positive correlation, higher spending leads to more impressions, expanding reach.
* **Clicks and Amount Spent (0.878):** Strong positive correlation, increased spending leads to more clicks.
* **Clicks and Leads (0.922):** Very strong positive correlation, ads with more clicks are likely to generate more leads, effective in driving interest.

**Negative Correlations:**

* **CTR% and CPL (-0.640):** Engaging ads with higher CTR are more cost-effective.
* **Leads and CPL (-0.588):** More leads generally lead to a lower cost per lead, likely due to economies of scale.

**Weak Correlations:**

* **Impressions and CPL (-0.006), CPL and Amount Spent (-0.009):** Increasing budget doesn't guarantee lower or higher cost per lead. 
* **CTR% and Amount Spent (-0.346):** More spending doesn't always result in higher click-through rate, indicating other factors at play.
""")


