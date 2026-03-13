from binance.client import Client

API_KEY = "3CclHHvBYuIT30OBZ0p0wkDBIsHfWKnAwTyo5PYbxepO9uEH85ZdOPe7BPSnTMMM"
API_SECRET = "rKdKeGtZg37gNZbr9ZJnfNHo4kwfm5y38baV5zdyhHDnV31yAKhNj6MtvRe1Sc6L"

def get_client():
    client = Client(API_KEY, API_SECRET)

    # Connect to Binance Futures Testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client