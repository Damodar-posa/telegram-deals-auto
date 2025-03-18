import feedparser
import requests
import os

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID")
RSS_FEED_URL = "https://www.desidime.com/deals.rss"

def post_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def fetch_and_post_deals():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries[:3]:  # Top 3 deals
        title = entry.title
        link = entry.link
        summary = entry.summary
        message = f"<b>{title}</b>\n{summary}\n👉 <a href='{link}'>Buy Now</a>"
        post_to_telegram(message)

fetch_and_post_deals()
