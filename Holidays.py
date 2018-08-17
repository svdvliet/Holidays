#!/usr/bin/env python

from requests import get
from bs4 import BeautifulSoup


url = 'https://www.secretflying.com/search2/?cityFrom=Amsterdam&cityTo=&month='
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
Secretflying = html_soup.find_all('div', class_ = "site-content snews-boxed")
Secretflying = Secretflying[0]
Secretflying_results = Secretflying.find_all("a")
for i in range(0,70,14):
 title_pos_start = str(Secretflying_results[i]).find("title=")
 title_pos_end = str(Secretflying_results[i]).find('"><a href=')
 print(str(Secretflying_results[i])[title_pos_start+7:title_pos_end])
print("\n")

url = 'https://www.secretflying.com/search2/?cityFrom=Brussels&cityTo=&month='
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
Secretflying = html_soup.find_all('div', class_ = "site-content snews-boxed")
Secretflying = Secretflying[0]
Secretflying_results = Secretflying.find_all("a")
for i in range(0,70,14):
 title_pos_start = str(Secretflying_results[i]).find("title=")
 title_pos_end = str(Secretflying_results[i]).find('"><a href=')
 print(str(Secretflying_results[i])[title_pos_start+7:title_pos_end])
print("\n")

url = 'https://www.secretflying.com/search2/?cityFrom=Dusseldorf&cityTo=&month='
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
Secretflying = html_soup.find_all('div', class_ = "site-content snews-boxed")
Secretflying = Secretflying[0]
Secretflying_results = Secretflying.find_all("a")
for i in range(0,70,14):
 title_pos_start = str(Secretflying_results[i]).find("title=")
 title_pos_end = str(Secretflying_results[i]).find('"><a href=')
 print(str(Secretflying_results[i])[title_pos_start+7:title_pos_end])
print("\n")# Holidays
# Holidays
