STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DROP="DOWN"
RAISE="UP"

import os
import requests
import datetime as dt
import smtplib

ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_KEY")
NEWSAPI_KEY=os.environ.get("NEWSAPI_KEY")
EMAIL=os.environ.get("EMAIL")
PASSWORD= os.environ.get("PASSWORD")
MAIL_TO = os.environ.get("MAIL_TO")

response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHAVANTAGE_KEY}")
response = response.json()

date = dt.datetime.now()
present_date = f"{date.year}-{date.month:02d}-{(date.day-2):02d}"
previous_date = f"{date.year}-{date.month:02d}-{(date.day-3):02d}"

diff = float(response["Time Series (Daily)"][previous_date]["4. close"])-float(response["Time Series (Daily)"][present_date]["4. close"])
diff_percent = round((diff * 100) / float(response["Time Series (Daily)"][present_date]["4. close"]),2)

if abs(diff_percent) > 5:
    response = requests.get(url=f"https://newsapi.org/v2/everything?q=Tesla&from={present_date}&sortBy=popularity&apiKey={NEWSAPI_KEY}")
    response = response.json()

    #Sign assignement
    sign :str
    if diff_percent<0:
        sign = DROP
    else:
        sign = RAISE

    #Needed data from the response
    headline = response["articles"][0]["title"]
    brief = response["articles"][0]["description"]
    source = response["articles"][0]["source"]["name"]
    url = response["articles"][0]["url"]

    #Notify thru mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,to_addrs=MAIL_TO, msg=f"Subject:Stock Alert\n\nTSLA : {sign} {diff_percent}%\nHeadline : {headline}\nLink : {url}")
            connection.close()
    
    




