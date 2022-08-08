import requests, bs4, datetime, time
from twilio.rest import Client

account_SID = 
auth_token = 
twilio_cli = Client(account_SID, auth_token)
my_twilio_number = 
my_call_phone = 

wakeup_time = datetime.datetime(2022,  6, 28, 15, 8)
while datetime.datetime.now() < wakeup_time:
    time.sleep(1)

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78873500000003&lon=-122.3945#.YrumGNLP2-V')
res.raise_for_status

soup = bs4.BeautifulSoup(res.text, 'lxml')
elem = soup.select('.tombstone-container p')

for i in range(0, len(elem)):
    if i == 6 and elem[i].getText() == 'Sunny'
    twilio_cli.messages.create(
        body='今日は雨が降るよ。傘を持ってね。'
        from=my_twilio_number,
        to=my_call_phone
    )