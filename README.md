# Binance Futures Trading Bot (Testnet)

This project is a simple Python CLI trading bot that places orders on Binance Futures Testnet.

## Features
- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Command Line Interface using argparse
- Logging of API responses and errors
- Basic input validation

## Setup

1. Clone the repository

2. Install dependencies
pip install -r requirements.txt

3. Add your Binance Testnet API keys in bot/client.py

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 72000

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── trading_bot.log

## Notes
- This project uses Binance Futures Testnet for safe testing.
- Minimum order value must be greater than 100 USDT.