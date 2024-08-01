import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Define Graphing Function
#In this section, we define the function make_graph. 
# You don't have to know how the function works, you should only care about the inputs. 
# It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), 
# and the name of the stock.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
#Question 1: Use yfinance to Extract Stock Data
tesla = yf.Ticker("tsla")
tesla_data = tesla.history(period = 'max')
#Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function. 
# Take a screenshot of the results and code from the beginning of Question 1 to the results below.
tesla_data.reset_index(inplace=True)
tesla_data.head()

# Use Webscraping to Extract Tesla Revenue Data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text
soup_1 = BeautifulSoup(html_data, 'html.parser')

#Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into a dataframe named tesla_revenue. 
# The dataframe should have columns Date and Revenue.

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
tables = soup_1.find_all('table')
table_index = 0

for index, table in enumerate(tables):
    if "Tesla Quarterly Revenue" in str(table):
        table_index = index

for row in tables[table_index].find('tbody').find_all('tr'): 
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date":[date], "Revenue":[revenue]})], ignore_index=True)
#Execute the following line to remove the comma and dollar sign from the Revenue column.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace('$',"")
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',',"")

#Execute the following lines to remove an null or empty strings in the Revenue column.

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.tail(5)

#Use yfinance to Extract Stock Data
GameStop = yf.Ticker('GME')
gme_data = GameStop.history(period = 'max')
gme_data
gme_data.reset_index(inplace=True)
gme_data.head(5)

#Use Webscraping to Extract GME Revenue Data

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url).text
soup_2 = BeautifulSoup(html_data_2, "html.parser")
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
data_2 = soup_2.find_all('table')
data_2_index = 0

for index, table in enumerate(data_2):
    if "GameStop Quarterly Revenue" in str(table): 
        data_2_index = index

for row in data_2[data_2_index].find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date":[date], "Revenue":[revenue]})], ignore_index=True)
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace('$',"")
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

gme_revenue.tail(5)

#Plot Tesla Stock Graph

make_graph(tesla_data, tesla_revenue, "Tesla Stock Data")

#Plot GameStop Stock Graph

make_graph(gme_data,gme_revenue, "")