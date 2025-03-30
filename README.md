# python-project
# Stock Price and Revenue Analysis of Tesla and GameStop

## Overview
This project analyzes the historical stock prices and annual revenue data of Tesla (TSLA) and GameStop (GME). The goal is to compare the trends in stock prices with the companies' annual revenues over time. The analysis includes:
- Extracting stock price data using `yfinance`.
- Scraping revenue data from Macrotrends using `BeautifulSoup`.
- Combining the data and visualizing it with interactive graphs using `Plotly`.

## Files Included
1. **`stock_data_extraction.py`**: The main Python script containing all the code for data extraction, processing, and visualization.
2. **`tesla_dashboard.html`**: Interactive HTML file for Tesla's stock price vs revenue graph.
3. **`gme_dashboard.html`**: Interactive HTML file for GameStop's stock price vs revenue graph.

## Requirements
To run this project, you need the following Python libraries installed:
- `yfinance`
- `pandas`
- `requests`
- `beautifulsoup4`
- `plotly`

Install them using:
```bash
pip install yfinance pandas requests beautifulsoup4 plotly
