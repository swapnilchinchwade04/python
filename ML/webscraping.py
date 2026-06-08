# Script for web scrapping.
import requests
from bs4 import BeautifulSoup

url ="www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for paragraph in soup.find_all("p"):
    print(paragraph.txt)

