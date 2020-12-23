import requests
import csv
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A" #EXR.D.USD.EUR.SP00.A
HISTORIC_RATES_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml"
LAST_90_DAYS_RATES_URL = ("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#data = soup.findall("generic:ObsDimension", {"value" : "2020-11-27"})
#print(data)
#for d in data:
#    print(d)
#tree = ET.parse('https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A')
#root = tree.getroot()
#root.tag
import requests
import xml.etree.ElementTree as ET
 
r = requests.get(url) 
test = (r.text)
#print(test)
for i in ET.fromstring(test).findall(): 
    print (i.text)
                

