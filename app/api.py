from app import app
from InvestopediaApi import ita
import requests
import random

@app.route('/')
def index():
  return "nwHacks 2018 - Alex T, Alex L, Clarence L, Felix T :)"

@app.route('/alext', methods=['GET', 'POST'])
def alext():
  client = ita.Account("dragonboatfelist@gmail.com", "felist123")

  shares = requests.get("http://yolo-on-fannie-mae.herokuapp.com/shares")

  if not shares:
    client.trade("SNAP", ita.Action.buy, random.randint(1, 100))
  else:
    tickers = []
    for share in shares.json():
      tickers.append(share['ticker'])
    buy_share = random.choice(tickers)
    client.trade(str(buy_share), ita.Action.buy, random.randint(1, 100))
  return "what is the website for amazon.ca"

@app.route('/alexl', methods=['GET', 'POST'])
def alexl():
  client = ita.Account("dragonboatfelist@gmail.com", "felist123")

  shares = requests.get("http://yolo-on-fannie-mae.herokuapp.com/shares")

  if not shares:
    client.trade("HMMJ", ita.Action.buy, random.randint(1, 100))
  else:
    tickers = []
    for share in shares.json():
      tickers.append(share['ticker'])
    buy_share = random.choice(tickers)
    client.trade(str(buy_share), ita.Action.buy, random.randint(1, 100))
  return "arigatou 4 the house"

@app.route('/clarence', methods=['GET', 'POST'])
def clarence():
  client = ita.Account("dragonboatfelist@gmail.com", "felist123")

  shares = requests.get("http://yolo-on-fannie-mae.herokuapp.com/shares")

  if not shares:
    client.trade("MPX", ita.Action.buy, random.randint(1, 100))
  else:
    tickers = []
    for share in shares.json():
      tickers.append(share['ticker'])
    buy_share = random.choice(tickers)
    client.trade(str(buy_share), ita.Action.buy, random.randint(1, 100))
  return "fresha fresha ya"

@app.route('/felix', methods=['GET', 'POST'])
def felix():
  client = ita.Account("dragonboatfelist@gmail.com", "felist123")

  shares = requests.get("http://yolo-on-fannie-mae.herokuapp.com/shares")

  if not shares:
    client.trade("AMZN", ita.Action.buy, random.randint(1, 100))
  else:
    tickers = []
    for share in shares.json():
      tickers.append(share['ticker'])
    buy_share = random.choice(tickers)
    client.trade(str(buy_share), ita.Action.buy, random.randint(1, 100))
  return "show me da whey"
