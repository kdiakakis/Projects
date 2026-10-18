import os
import time
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

URL = "https://www.skroutz.gr/s/65089742/samsung-odyssey-g5-g50sf-oled-hdr-gaming-monitor-27-qhd-2560x1440-180hz-me-chrono-apokrisis-0-03ms-gtg.html"
TARGET_PRICE = 150
CHECK_INTERVAL = 3600  # seconds


def send_message(text):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text},
        timeout=10,
    )


def get_price(driver):
    driver.get(URL)
    time.sleep(5)
    integer_part = driver.find_element(By.CLASS_NAME, "integer-part").text
    decimal_part = driver.find_element(By.CLASS_NAME, "decimal-part").text
    return float(integer_part.replace(".", "") + "." + decimal_part.replace(",", ""))


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())

    previous_price = None

    while True:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Checking price on Skroutz...")
            price = get_price(driver)
            print(f"Price found: {price}€")

            if price <= TARGET_PRICE and price != previous_price:
                send_message(f"Price dropped: {price}€\n{URL}")
                print("Notification sent to Telegram!\n")

            previous_price = price

        except Exception as e:
            print(f"Error while checking price: {e}")
        finally:
            driver.quit()

        print("Waiting 1 hour until the next check...\n")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
