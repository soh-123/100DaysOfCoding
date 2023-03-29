import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
AUTH_CODE = os.environ.get("AUTH_CODE")
account_sid = "AC31231ec2bafa0063a47a69117eaaef60"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#--------------------------------------- STOCK API -----------------------------------------#

stock_parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey":STOCK_API_KEY
    }

stocks = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stocks.raise_for_status()
stock_data = stocks.json()["Time Series (Daily)"]
#creating a list to loop through the days everyday
data_list = [value for (key, value) in stock_data.items()]
yesterdays_close = float(data_list[0]["4. close"])
daybeforeyesterdays_close = float(data_list[1]["4. close"])

#--------------------------------------- NEWS API -----------------------------------------#

def difference_calculator(d1, d2):
    difference = d1 - d2
    average = (d1+d2)/2
    percentage = round((abs(difference)/average)*100,2)
    return percentage

if yesterdays_close > daybeforeyesterdays_close:
    arrow = "🔺"
else:
    arrow = "🔻"
diff_percentage = difference_calculator(yesterdays_close, daybeforeyesterdays_close)
if diff_percentage > 1:

    news_parameters = {
    "q":COMPANY_NAME,
    "searchIn":"title",
    "apiKey":NEWS_API_KEY,
    "language":"en"
    }
    news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news.raise_for_status()
    articles = news.json()["articles"]

    three_articles = articles[:3]
    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, AUTH_CODE)
    for article in formatted_article:
        message = client.messages.create(
            body=f"{STOCK}: {arrow}{diff_percentage}%\n{article}",
            from_="+14346029262",
            to="+971526738751"
            )
    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



# print(f"With difference {difference_calculator(yesterdays_close, daybeforeyesterdays_close)}%")