import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
URL = 'https://newsapi.org/v2/top-headlines'
PARAMS = {
    'country': 'us',
    'pageSize': 10,
    'apiKey': API_KEY
}

def get_top_headlines():
    try:
        response = requests.get(URL, params=PARAMS)
        response.raise_for_status()
        news_data = response.json()

        if news_data.get("status") != "ok":
            print("Error fetching news:", news_data.get("message"))
            return

        print("\n📰 Top Headlines:\n")
        for idx, article in enumerate(news_data['articles'], 1):
            print(f"{idx}. {article['title']}")
            if article.get('description'):
                print(f"   {article['description']}")
            print(f"   Link: {article['url']}\n")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == '__main__':
    get_top_headlines()
