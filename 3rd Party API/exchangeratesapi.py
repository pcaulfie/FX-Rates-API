import requests
import csv
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = "https://api.exchangeratesapi.io/latest" 
page = requests.get(url)
#print(page.contents)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

                

