import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_ACCOUNT_SID = "AC557bfd164123779b6b52a5de0c8171a7"
TWILIO_AUTH_TOKEN = "fa0fa907fc0c84486e187ef21c5456c0"
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "1B7C8X9YDOMDUTBC"
NEWS_API_KEY = 'a121a2ee67894e14a586edfa0026a1f9'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

res = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = res.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing = data_list[0]['4. close']

# TODO 2. - Get the day before yesterday's closing stock price
daybefore_data = data_list[1]
daybefore_closing = data_list[1]['4. close']
print(yesterdays_closing)
print(daybefore_closing)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(float(yesterdays_closing) - float(daybefore_closing))
print((diff))
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
news_params={
    "apiKey":NEWS_API_KEY,
    "searchIn":"title",
    "q":COMPANY_NAME
}
if diff > 6:
    res2=requests.get(url=NEWS_ENDPOINT,params=news_params)
    data2=res2.json()['articles'][:3]
    formatted=[f"Heading : {article['title']}\nBrief: {article['description']}" for article in data2 ][0]
    print(formatted)
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=formatted,
        from_='++18317447708',
        to='+916303975024'
    )

    print(message.sid)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# stocks-api-key:1B7C8X9YDOMDUTBC
# news-api-key:a121a2ee67894e14a586edfa0026a1f9
# twilio account sid:AC557bfd164123779b6b52a5de0c8171a7
# twilio auth key:fa0fa907fc0c84486e187ef21c5456c0
