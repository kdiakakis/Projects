# Skroutz Price Tracker

Monitors the price of a product on [Skroutz](https://www.skroutz.gr) and sends a Telegram notification when it drops below your target price.

## Requirements

- Python 3.8+
- Google Chrome installed (ChromeDriver is downloaded automatically)
- A Telegram bot token (create one with [@BotFather](https://t.me/BotFather)) and your chat ID

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the same folder as `main.py`:

```
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Then edit these values at the top of `main.py`:

| Variable         | Description                                         |
|------------------|-----------------------------------------------------|
| `URL`            | The Skroutz product page to track                   |
| `TARGET_PRICE`   | Price (in €) under which you want to be notified    |
| `CHECK_INTERVAL` | How often to check, in seconds (default: `3600`)    |

## Usage

```bash
python main.py
```

The script checks the price every hour. You get a Telegram message when the price is at or below `TARGET_PRICE` and has changed since the last check.

## Notes

- Never commit your `.env` file. It is excluded via `.gitignore`.
- If Skroutz changes its page layout, the CSS class names in `get_price()` (`integer-part`, `decimal-part`) may need updating.
- Skroutz may block headless browsers. If the script stops finding the price, try running it without `--headless=new`.
