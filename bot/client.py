from binance.client import Client

API_KEY = "here we can paste our API_Key"
API_SECRET = "here paste the API_Secret"

def get_client():
    client = Client(API_KEY, API_SECRET)

    # Connect to Binance Futures Testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client