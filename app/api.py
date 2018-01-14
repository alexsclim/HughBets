from app import app
import ita

@app.route('/')
@app.route('/index')
def index():
    client = ita.Account("dragonboatfelist@gmail.com", "felist123")
    client.trade("GOOG", ita.Action.buy, 10)
    open_trades = client.get_open_trades()
    for open_trade in open_trades:
      print(open_trade.date_time)
      print(open_trade.description)
      print(open_trade.symbol)
      print(open_trade.quantity)
    return "Hello, World!"
