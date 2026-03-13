import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

validate_side(args.side)
validate_order_type(args.type)

client = get_client()

print("Order Request Summary")
print("Symbol:", args.symbol)
print("Side:", args.side)
print("Type:", args.type)
print("Quantity:", args.quantity)

order = place_order(
    client,
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

if order:
    print("Order placed successfully")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
else:
    print("Order failed")