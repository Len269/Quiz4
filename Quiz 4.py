import requests
import bs4
import csv
from time import sleep
from random import randint

file = open("content.csv", 'w', encoding='UTF-8', newline='\n')
page = 1
file_obj = csv.writer(file)
file_obj.writerow(["name", "price"])

while page < 6:
    url = f'https://alta.ge/smartphones-page-{page}.html'
    response = requests.get(url)
    content = response.text
    soup = bs4.BeautifulSoup(content, "html.parser")
    full_item = soup.find('div', {"class": "grid-list"})
    single_item = full_item.find_all('div', {"class": "ty-column3"})
    for each in single_item:
        name = each.find('a', {"class": "product-title"})
        final_name = name.text
        price = each.find('span', {"class": "ty-price-num"})
        final_price = price.text
        file_obj.writerow([final_name, final_price])

    page += 1
    sleep(randint(15, 20))
