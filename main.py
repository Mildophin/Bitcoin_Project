from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#Test

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '257c3523-f7a8-4866-8fcf-cee9da4bfe8d',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  price = data['data'][0]['quote']['USD']['price']
  price = int(price)
  print("Prix du bitcoin: " + str(price) + " $")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)