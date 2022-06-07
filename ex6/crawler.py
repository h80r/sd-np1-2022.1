from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread


def main():
    max_urls = int(
        input("Max URLs to crawl (will be divided evenly between threads): ")
    )
    max_threads = int(input("Max threads: "))

    # Pega as URLs a serem pesquisadas do arquivo sources.txt
    sources = open("sources.txt", "r")
    urls = sources.read().splitlines()
    sources.close()

    # Pega as palavras a serem buscadas do arquivo words.txt
    to_find = open("to-find.txt", "r")
    words_to_search = to_find.read().splitlines()
    to_find.close()

    # Cria as Threads
    for _ in range(max_threads):
        thread = Thread(
            target=crawl, args=(words_to_search, urls, max_urls / max_threads, True)
        )
        thread.start()


def crawl(
    words_to_search: list[str],
    urls: list[str],
    max_urls: int,
    recursive: bool = False,
):
    if len(urls) == 0:
        return
    if max_urls == 0:
        return

    url = urls.pop(0)
    try:
        # Pega o conteúdo da página
        page = urlopen(url).read()
        soup = BeautifulSoup(page, "html.parser")

        if recursive:
            links = soup.find_all("a")
            sources = open("sources.txt", "a")

            for link in links:
                link_url = link.get("href")
                if link_url is None:
                    continue
                if link_url in urls:
                    continue
                if link_url.startswith("http"):
                    urls.append(link_url)
                    sources.write(link_url + "\n")
            sources.close()

        output = open("output.txt", "a")

        result = {
            word: soup.text.count(word)
            for word in words_to_search
            if soup.text.count(word) > 0
        }
        print("On " + url + " found: " + str(result))
        output.write(url + ": " + str(result) + "\n")

        output.close()
    except Exception as e:
        print(e + " on " + url)
    finally:
        return crawl(words_to_search, urls, max_urls - 1)


if __name__ == "__main__":
    main()
