#-------------------------------------------------------------------------
# AUTHOR: Keldon Davis Aceituno
# FILENAME: scraper.py
# SPECIFICATION: Crawls the Circular Links section of TestingURL.dev with a
#                frontier/seen crawler, printing each page's <h1> text and,
#                at the end, every URL in seen.
# FOR: CS 4250 - Assignment #2
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]
seen = [seed]

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    if h1:
        print(h1.get_text(strip=True))

    # Extracting and processing hyperlinks
    for a in soup.find_all("a", href=True):

        # Converting relative URLs to absolute URLs
        link = urljoin(url, a["href"])

        # Following only links that begin with the seed URL
        if link.startswith(seed) and link not in seen:
            seen.append(link)
            frontier.append(link)

# Printing all URLs in seen
for link in seen:
    print(link)