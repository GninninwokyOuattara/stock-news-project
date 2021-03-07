STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os
import requests
import datetime as dt

ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_KEY")
NEWSAPI_KEY=os.environ.get("NEWSAPI_KEY")

response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHAVANTAGE_KEY}")
response = response.json()

date = dt.datetime.now()
present_date = f"{date.year}-{date.month:02d}-{(date.day-2):02d}"
previous_date = f"{date.year}-{date.month:02d}-{(date.day-3):02d}"

diff = float(response["Time Series (Daily)"][previous_date]["4. close"])-float(response["Time Series (Daily)"][present_date]["4. close"])
diff_percent = (diff * 100) / float(response["Time Series (Daily)"][present_date]["4. close"])






