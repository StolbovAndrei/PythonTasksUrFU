from collections import deque
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='WikiPathFinder/1.0', language='ru')
page_start = wiki_wiki.page('Стефен Карри')
page_end = wiki_wiki.page('Футбол')

def search_count(page_start, page_end):
    queue = deque([[page_start]])
    visited = set()
    visited.add(page_start.title)
    while queue:
        path = queue.popleft()
        node = path[-1]
        node_links = node.links
        for link in node_links:
            if link == page_end.title:
                return path + [wiki_wiki.page(link)]
            if link not in visited:
                visited.add(link)
                queue.append(path + [wiki_wiki.page(link)])
    return None


refs = search_count(page_start, page_end)
for ref in refs:
    print(ref.title)
print(len(refs))

