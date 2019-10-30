import re
import sys
from urllib.parse import urlparse
from urllib.request import urlopen

LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")


class LinkCollector:

    def __init__(self, url):
        # print(url)
        # print(urlparse(url))
        # print(urlparse(url).netloc)
        self.url = "http://" + urlparse(url).netloc

    def collect_links(self, path="/"):
        full_url = self.url + path
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        print(links)


if __name__ == "__main__":
    LinkCollector(sys.argv[1]).collect_links()
