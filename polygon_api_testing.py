## NEED TO UPGRADE PLAN, WILL REVISIT##

#import
from polygon import RESTClient

#api key
api_key = 'lgOPpBnVxygYIOh7SiKQapwkf6xCYHNY'

#initiating client
client = RESTClient(api_key=api_key)

#getting aggs of "APPL"

aggs = client.get_aggs(
    "AAPL",
    1,
    "day",
    "2022-04-04",
    "2022-04-04",
)
print(aggs)

appl_last_trade = client.get_last_trade(ticker= "AAPL")

print(appl_last_trade)
