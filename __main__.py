import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import http.client

class SimpleCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.failed_urls = set()
        self.robot_parser = RobotFileParser()
        self.blocked_domains = ["twitter.com", "linkedin.com"]

    def can_fetch(self, url):
        self.robot_parser.set_url(urljoin(url, '/robots.txt'))
        self.robot_parser.read()
        return self.robot_parser.can_fetch("*", url) and not any(domain in url for domain in self.blocked_domains)

    def is_html(self, response):
        content_type = response.info().get_content_type()
        return content_type == 'text/html'

    def fetch_links(self, current_url, soup):
        found_links = []
        for link in soup.find_all('a'):
            if len(found_links) >= 5:
                break
            absolute_link = urljoin(current_url, link.get('href'))
            if absolute_link not in self.visited_urls and absolute_link not in self.failed_urls and self.can_fetch(absolute_link):
                found_links.append(absolute_link)
        return found_links

    def crawl(self):
        urls_to_crawl = [self.base_url]
        while urls_to_crawl and len(self.visited_urls) < 50:
            current_url = urls_to_crawl.pop(0)
            if current_url in self.visited_urls or current_url in self.failed_urls:
                continue
            try:
                if not self.can_fetch(current_url):
                    print(f"Skipping {current_url} as per robots.txt")
                    continue
                
                response = urllib.request.urlopen(current_url)
                if response.getcode() == 200 and self.is_html(response):
                    soup = BeautifulSoup(response, 'html.parser')
                    new_links = self.fetch_links(current_url, soup)
                    urls_to_crawl.extend(new_links)
                    self.visited_urls.add(current_url)  # Add to visited only if successful
                    print(f"Visited: {current_url}")
                    with open('crawled_webpages.txt', 'a') as file:
                        file.write(current_url + '\n')
                        print(f"Added to crawled_webpages.txt: {current_url}")
            except urllib.error.URLError as e:
                print(f"Failed to access {current_url}: {e}")
                self.failed_urls.add(current_url)
            except http.client.RemoteDisconnected as e:
                print(f"RemoteDisconnected error for {current_url}: {e}")
                self.failed_urls.add(current_url)
            elapsed_time = time.time() - start_time
            if elapsed_time < 3:
                time.sleep(3 - elapsed_time)

if __name__ == "__main__":
    start_time = time.time()
    crawler = SimpleCrawler("https://ensai.fr/")
    time.sleep(1)  # Attendez une seconde avant de commencer le crawl
    crawler.crawl()
