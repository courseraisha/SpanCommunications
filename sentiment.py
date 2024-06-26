import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import matplotlib.pyplot as plt

# Load data from Excel file
try:
    df = pd.read_excel("NPS Trust_Ticket_Report_20240625104249.xlsx")
    df.dropna(subset=["Date"], inplace=True)
    df = df[["Date", "Source Type", "Author", "Followers", "Title", "Sentiment"]]
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date2"] = df['Date'].dt.date  
except FileNotFoundError:
    st.error("File 'NPS Trust_Ticket_Report_20240625104249.xlsx' not found.")
    st.stop()

st.markdown('<h1 class="full-width-heading">Sentiment Analysis and Forecasting </h1>', unsafe_allow_html=True)
st.markdown('')
st.title("**_Volume -_**")

# Define layout columns
col1, col2 = st.columns([1, 2])

# Column 2: Main sentiment analysis and visualization
with col1:
    # Styling for large font (you already have this, it's good!)
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 25px !important;
        }

        table {
            width: 100%; 
            border-collapse: collapse; 
            margin-bottom: 20px;
            font-family: "Arial", sans-serif; /* Modern font choice */
        }

        th, td {
            border: 1px solid #ddd;
            padding: 15px; /* Increased padding for more space */
            text-align: left;
            font-size: 18px; 
        }

        th {
            background-color: #007bff; /* Bootstrap blue for header */
            color: white;
            font-weight: bold;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2; 
        }

        .total-row td {
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display volume analysis
    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Counts']

    # Add a "Total" Row for Overall Count
    total_counts = sentiment_counts['Counts'].sum()
    total_row = pd.DataFrame({'Sentiment': ['Total'], 'Counts': [total_counts]})
    sentiment_counts = pd.concat([sentiment_counts, total_row], ignore_index=True)
    # Highlight the "Total" row
    sentiment_counts_styled = sentiment_counts.style.apply(lambda x: ['background: lightblue' if x.name == len(sentiment_counts)-1 else '' for i in x], axis=1)

    # Display using st.dataframe for easier customization
    st.dataframe(sentiment_counts_styled) 



# Column 1 and 3: Additional sections
with col2:
    # Enhanced visualization: Bar chart with date filter
    start_date = st.date_input("Start Date", value=df["Date2"].min())
    end_date = st.date_input("End Date", value=df["Date2"].max())
    masked_df = df[(df["Date2"] >= start_date) & (df["Date2"] <= end_date)]
    sentiment_counts_filtered = masked_df["Sentiment"].value_counts().reset_index()
    sentiment_counts_filtered.columns = ['Sentiment', 'Counts']

    fig_volume = px.bar(sentiment_counts_filtered, x='Sentiment', y='Counts',
                        labels={"x": "Sentiment", "y": "Count"},
                        title="Sentiment Volume Distribution (Filtered)")
    st.plotly_chart(fig_volume)

st.title("**_Predictive Analysis -_**")
st.subheader("Example:")
# Adjusted Dummy Time Series Data
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
np.random.seed(42)  # For reproducibility
df = pd.DataFrame({
    'Date': date_range,
    'Increasing': range(50, len(date_range) + 50),      # Increasing from 50
    'Constant': [50] * len(date_range),               # Constant value at 50
    'Decreasing': range(50, -len(date_range) + 50, -1)  # Decreasing from 50
})

# Plotly Express Line Chart
fig = px.line(
    df, x='Date', y=['Increasing', 'Constant', 'Decreasing'],
    title='Time Series with Three Trends',
    labels={'value': 'Negative Sentiment Trend', 'Date': 'Date'},
    color_discrete_map={'Increasing': 'red', 'Constant': 'yellow', 'Decreasing': 'blue'}
)

# Customize layout to have white background and black text
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Increasing'], color='red', label='Increasing')
ax.plot(df['Date'], df['Constant'], color='yellow', label='Constant')
ax.plot(df['Date'], df['Decreasing'], color='blue', label='Decreasing')

# Customize layout to have white background and black text
ax.set_facecolor('white')  # Set plot background to white
fig.patch.set_facecolor('white')  # Set figure background to white
ax.set_xlabel('Date', color='black')  # X-axis label
ax.set_ylabel('Values', color='black')  # Y-axis label
ax.tick_params(axis='x', colors='black')  # X-axis tick labels
ax.tick_params(axis='y', colors='black')  # Y-axis tick labels
ax.legend()  # Add legend

# Set the title of the plot
ax.set_title('Time Series with Three Trends', color='black')

# Display the Plotly chart
st.pyplot(fig)
st.write('''The graph above illustrates three potential trends in negative sentiments over time. The red line indicates an increase in negative sentiment, 
         the yellow line shows a constant level of negative sentiment, and the blue line represents a decrease in negative sentiment over time.        
         ''')
st.write('')
st.write('')

# Display the chart
st.subheader("Analysis:")
st.image("download.png", use_column_width=True)
st.write('''The graph illustrates the forecasted trend of negative sentiment over the upcoming 150 days with a 95% confidence interval. 
         The observed data shows a significant decrease in negative sentiment up to around April 2024. 
         Beyond this period, the trend stabilizes and remains relatively constant. The shaded blue area represents the 95% confidence interval, 
         showing a range of possible outcomes. 
          Overall, the forecast suggests that while negative sentiments are expected to decrease.''')
# Display the plot in Streamlit



