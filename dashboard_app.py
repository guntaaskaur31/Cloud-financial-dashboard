import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from io import BytesIO

# Optional: For forecasting
try:
    from prophet import Prophet
except ImportError:
    Prophet = None

# --- Sidebar Navigation ---
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Dashboard', 'Predictions'])

# --- Load or Upload Data ---
def load_data():
    st.sidebar.header('Upload Data')
    uploaded_file = st.sidebar.file_uploader('Upload CSV', type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    else:
        # Generate sample data if no file is uploaded
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', end=datetime.today(), freq='D')
        data = {
            'Date': dates,
            'Region': np.random.choice(['North', 'South', 'East', 'West'], size=len(dates)),
            'Category': np.random.choice(['A', 'B', 'C', 'D'], size=len(dates)),
            'Sales': np.random.randint(20, 200, size=len(dates)),
            'Revenue': np.random.uniform(1000, 5000, size=len(dates)),
            'Profit': np.random.uniform(200, 1000, size=len(dates)),
        }
        df = pd.DataFrame(data)
    return df

df = load_data()

# --- Dashboard Page ---
if page == 'Dashboard':
    st.title('📊 Business Dashboard')
    st.markdown('---')

    # --- Metrics ---
    total_sales = int(df['Sales'].sum())
    total_revenue = float(df['Revenue'].sum())
    total_profit = float(df['Profit'].sum())
    col1, col2, col3 = st.columns(3)
    col1.metric('Total Sales', f"{total_sales:,}")
    col2.metric('Total Revenue', f"${total_revenue:,.2f}")
    col3.metric('Total Profit', f"${total_profit:,.2f}")

    st.markdown('---')

    # --- Region Filter ---
    regions = ['All'] + sorted(df['Region'].unique().tolist())
    selected_region = st.selectbox('Select Region', regions)
    if selected_region != 'All':
        region_df = df[df['Region'] == selected_region]
    else:
        region_df = df

    # --- Monthly Sales Trend (Line Chart) ---
    monthly_sales = region_df.resample('M', on='Date')['Sales'].sum()
    st.subheader('Monthly Sales Trend')
    st.line_chart(monthly_sales)

    # --- Revenue by Category (Bar Chart) ---
    category_revenue = region_df.groupby('Category')['Revenue'].sum()
    st.subheader('Revenue by Product Category')
    st.bar_chart(category_revenue)

    # --- Cumulative Revenue (Area Chart) ---
    region_df_sorted = region_df.sort_values('Date')
    region_df_sorted['Cumulative Revenue'] = region_df_sorted['Revenue'].cumsum()
    st.subheader('Cumulative Revenue Over Time')
    st.area_chart(region_df_sorted.set_index('Date')['Cumulative Revenue'])

# --- Predictions Page ---
if page == 'Predictions':
    st.title('🔮 Sales & Revenue Forecast')
    st.markdown('---')
    st.markdown('Enter the number of months ahead to predict sales and revenue. Uses Prophet if available, else a simple linear regression.')

    months_ahead = st.number_input('Months Ahead', min_value=1, max_value=24, value=3)
    future_periods = months_ahead * 30  # Approximate days

    # Prepare data for forecasting
    sales_df = df.resample('D', on='Date').sum().reset_index()
    sales_df = sales_df[['Date', 'Sales', 'Revenue']]

    # Prophet Forecasting
    if Prophet:
        # Sales Forecast
        sales_prophet = Prophet()
        sales_prophet.fit(sales_df.rename(columns={'Date': 'ds', 'Sales': 'y'}))
        future_sales = sales_prophet.make_future_dataframe(periods=future_periods)
        sales_forecast = sales_prophet.predict(future_sales)
        # Revenue Forecast
        revenue_prophet = Prophet()
        revenue_prophet.fit(sales_df.rename(columns={'Date': 'ds', 'Revenue': 'y'}))
        future_revenue = revenue_prophet.make_future_dataframe(periods=future_periods)
        revenue_forecast = revenue_prophet.predict(future_revenue)
        # Results
        pred_df = pd.DataFrame({
            'Date': sales_forecast['ds'],
            'Predicted Sales': sales_forecast['yhat'],
            'Predicted Revenue': revenue_forecast['yhat']
        })
        pred_df = pred_df.tail(future_periods)
    else:
        # Fallback: Simple Linear Regression
        from sklearn.linear_model import LinearRegression
        # Sales
        X = np.arange(len(sales_df)).reshape(-1, 1)
        y_sales = sales_df['Sales'].values
        model_sales = LinearRegression().fit(X, y_sales)
        X_future = np.arange(len(sales_df), len(sales_df) + future_periods).reshape(-1, 1)
        sales_pred = model_sales.predict(X_future)
        # Revenue
        y_revenue = sales_df['Revenue'].values
        model_revenue = LinearRegression().fit(X, y_revenue)
        revenue_pred = model_revenue.predict(X_future)
        # Results
        future_dates = [sales_df['Date'].max() + timedelta(days=i+1) for i in range(future_periods)]
        pred_df = pd.DataFrame({
            'Date': future_dates,
            'Predicted Sales': sales_pred,
            'Predicted Revenue': revenue_pred
        })

    st.subheader('Prediction Results')
    st.dataframe(pred_df)

    # Download Button
    csv = pred_df.to_csv(index=False).encode('utf-8')
    st.download_button('Download Predictions as CSV', data=csv, file_name='predictions.csv', mime='text/csv')

# --- Footer ---
st.markdown('---')
st.markdown('Made with ❤️ using Streamlit | Modern Business Dashboard') 
