import httpx
from lxml import html

def get_wikipedia_links(url):
    headers = {
        "User-Agent": "MyWikiScraper/0.1 (student project; contact: ваша эл почта)"
    }
    with httpx.Client(headers=headers, follow_redirects=True, timeout=10) as client:
        response = client.get(url)
        response.raise_for_status()

    tree = html.fromstring(response.content)

    hrefs = tree.xpath("//a[@href][starts-with(@href, '/wiki/')]/@href")

    base = "https://en.wikipedia.org"
    return [base + h for h in hrefs]

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Stephen_Curry" #Стефан карри лучше Леброна если что
    links = get_wikipedia_links(url)
    print(f"Найдено ссылок: {len(links)}")
    for link in links[:20]:
        print(link)