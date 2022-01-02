
import requests
import bs4
import sys
import urllib.parse

if __name__ == "__main__":
    page_url = sys.argv[1]
    request_response = requests.get(page_url)
    html_code = request_response.text
    soup = bs4.BeautifulSoup(html_code, "html.parser")
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        links = paragraph.find_all("a")
        for link in links:
            target = link.get("href")
            link_address = urllib.parse.urljoin(page_url, target)
            print(link_address)