import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go

# Function to extract stock data using yfinance
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="max")
    data.reset_index(inplace=True)
    return data

# Function to scrape revenue data from Macrotrends
def get_revenue_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    revenue_table = soup.find('table', {'class': 'historical_data_table table'})
    revenue_data = []
    for row in revenue_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) == 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace(',', '').replace('$', '')
            revenue_data.append({'Date': date, 'Revenue': float(revenue)})
    revenue_df = pd.DataFrame(revenue_data)
    return revenue_df

# Function to create an interactive graph
def make_graph(data, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Year'], y=data.groupby('Year')['Close'].mean(), name='Average Closing Price', mode='lines'))
    fig.add_trace(go.Bar(x=data['Year'], y=data['Revenue'], name='Revenue', yaxis='y2'))
    fig.update_layout(
        title=title,
        xaxis_title='Year',
        yaxis=dict(title='Average Closing Price'),
        yaxis2=dict(title='Revenue', overlaying='y', side='right'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    fig.show()

# Extract Tesla stock data
tesla_data = get_stock_data("TSLA")
print("Tesla Stock Data:")
print(tesla_data.head())

# Extract Tesla revenue data
tesla_revenue_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_revenue_data = get_revenue_data(tesla_revenue_url)
print("\nTesla Revenue Data:")
print(tesla_revenue_data.tail())

# Combine Tesla stock and revenue data
tesla_data['Year'] = tesla_data['Date'].dt.year
tesla_revenue_data['Year'] = pd.to_datetime(tesla_revenue_data['Date']).dt.year
valid_years = tesla_revenue_data['Year'].unique()
filtered_tesla_data = tesla_data[tesla_data['Year'].isin(valid_years)]
combined_tesla_data = pd.merge(filtered_tesla_data, tesla_revenue_data, on='Year', how='inner')
print("\nCombined Tesla Data:")
print(combined_tesla_data.head())

# Extract GameStop stock data
gme_data = get_stock_data("GME")
print("\nGameStop Stock Data:")
print(gme_data.head())

# Extract GameStop revenue data
gme_revenue_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_revenue_data = get_revenue_data(gme_revenue_url)
print("\nGameStop Revenue Data:")
print(gme_revenue_data.tail())

# Combine GameStop stock and revenue data
gme_data['Year'] = gme_data['Date'].dt.year
gme_revenue_data['Year'] = pd.to_datetime(gme_revenue_data['Date']).dt.year
valid_years = gme_revenue_data['Year'].unique()
filtered_gme_data = gme_data[gme_data['Year'].isin(valid_years)]
combined_gme_data = pd.merge(filtered_gme_data, gme_revenue_data, on='Year', how='inner')
print("\nCombined GameStop Data:")
print(combined_gme_data.head())

# Plot Tesla stock graph
#make_graph(combined_tesla_data, title="Tesla Stock Price vs Revenue")

# Plot GameStop stock graph
make_graph(combined_gme_data, title="GameStop Stock Price vs Revenue")