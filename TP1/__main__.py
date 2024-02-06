import time
import urllib.robotparser
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

import sqlite3
import time
import urllib.robotparser
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def create_database():
    conn = sqlite3.connect('crawled_pages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pages
                 (url TEXT PRIMARY KEY, title TEXT, crawled_at TIMESTAMP)''')
    conn.commit()
    conn.close()

def insert_page(url, title):
    conn = sqlite3.connect('crawled_pages.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO pages (url, title, crawled_at) VALUES (?, ?, CURRENT_TIMESTAMP)", (url, title))
    conn.commit()
    conn.close()

def get_links(url):
    try:
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        insert_page(url, title)
        return [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
    except Exception:
        return []

def can_fetch(url, user_agent='*'):
    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(urljoin(url, '/robots.txt'))
    parser.read()
    return parser.can_fetch(user_agent, url)

def get_links(url):
    try:
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
    except Exception:
        return []

def crawl(url, crawled_urls, to_crawl, depth=0, max_depth=1):
    if url in crawled_urls or not can_fetch(url):
        return
    if depth > max_depth:
        return

    print(f"Crawling: {url}")
    crawled_urls.add(url)
    time.sleep(3)

    links = get_links(url)
    for link in links[:5]:  # Limiter à 5 liens par page
        if link not in crawled_urls:
            to_crawl.add(link)

    while to_crawl:
        next_url = to_crawl.pop()
        crawl(next_url, crawled_urls, to_crawl, depth+1, max_depth)

def main(start_url):
    crawled_urls = set()
    to_crawl = set([start_url])

    crawl(start_url, crawled_urls, to_crawl, max_depth=20)  # Profondeur de 20 niveaux

    with open('crawled_webpages.txt', 'w') as file:
        for url in crawled_urls:
            file.write(url + '\n')

    print("Crawling terminé.")

if __name__ == "__main__":
    create_database()
    main("https://ensai.fr/")
