from get_news import get_news
from send_news import send_news


def main():
    """gets the news and sends it to myself"""
    get_news()
    send_news()


if __name__ == "__main__":
    main()
