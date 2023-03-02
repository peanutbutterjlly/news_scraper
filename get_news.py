def getLinks(num_links: int) -> set[str]:
    """get num_links numbers of news article links from y-combinator"""
    import requests

    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    topLinks: list = requests.get(url).json()[:num_links]
    base_url = "https://hacker-news.firebaseio.com/v0/item/"
    url_suffix = ".json"
    links_set: set = set()
    for link in topLinks:
        url = f"{base_url}{link}{url_suffix}"
        response = requests.get(url)
        url = response.json()["url"] if "url" in response.json() else None
        links_set.add(url)
    return links_set


def getArticleText(url: str) -> tuple[list, str | None]:
    """returns the keywords and summary text from the url provided"""
    from newspaper import Article

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.keywords, article.summary


def main():
    from textwrap import fill
    from time import perf_counter

    print("starting summarization")
    tic = perf_counter()
    links = getLinks(20)
    with open("summary.txt", "w") as f:
        for url in links:
            print(f"summarizing {url}")
            try:
                key_words, text = getArticleText(url)
                f.write(
                    f'{url} \nkeywords: [{fill(", ".join(key_words), 100)}] \n\n{fill(text, width=100)}\n\n{"-" * 100}\n\n'
                ) if text is not None else None
            except Exception as e:
                print(e)
                pass
    toc = perf_counter()
    print(f"summarizations done in {toc - tic} seconds")


if __name__ == "__main__":
    main()
