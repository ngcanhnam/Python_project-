import yfinance as yf
import pandas as pd
import matplotlib_inline
apple = yf.Ticker("AAPL")

wget =  "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
#Sử dụng mô-đun Ticker, chúng ta có thể tạo một đối tượng cho phép chúng ta truy cập các chức năng để trích xuất dữ liệu. 
# Để làm điều này, chúng ta cần cung cấp mã cổ phiếu cho cổ phiếu,
# ở đây công ty là Apple và mã cổ phiếu là AAPL.
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info
#A share is the single smallest part of a company stock that you can buy, the prices of these shares fluctuate over time. Using the history() method we can get the share price of the stock over a certain period of time. 
#Using the period parameter we can set how far back from the present to get data. 
#The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period = "max")
apple_share_price_data.head()

#We can reset the index of the DataFrame with the reset_index function. 
#We also set the inplace paramter to True so the change takes place to the DataFrame itself.

apple_share_price_data.reset_index(inplace = True)

apple_share_price_data.plot(x="Date", y="Open")

#Dividends are the distribution of a companys profits to shareholders. 
#In this case they are defined as an amount of money returned per share an investor owns.
#Using the variable dividends we can get a dataframe of the data. 
#The period of the data is given by the period defined in the 'history` function.

apple.dividends.plot()
    