from bs4 import BeautifulSoup
import requests
import csv

file = open("countries_temp.csv","w",encoding="UTF-8")
cwriter = csv.writer(file,dialect="excel")
cwriter.writerow(['country','temp','continent'])


website = "https://berkeleyearth.lbl.gov/country-list/"

site = requests.get(website).text

soup = BeautifulSoup(site, "html.parser")

rows = soup.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    country,temp,continent = 0,0,0
    for index,column in enumerate(columns):
        if index==0:
            country = column.text
        elif index==1:
            temp = column.text[:4]
        elif index==2:
            continent = column.text
    cwriter.writerow([country,temp,continent])