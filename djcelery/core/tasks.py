import random
from celery import shared_task
from bs4 import BeautifulSoup
import requests
from csv import writer

@shared_task
def add(x, y):
# Celery recognizes this as the `movies.tasks.add` task
# the name is purposefully omitted here.
    return x + y

@shared_task(bind=True)
def Task_Scrapper(self):

    print('scarpper is working')
    

    url = "https://www.pararius.com/apartments/amsterdam"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    lists = soup.find_all("section", class_="listing-search-item")

    with open("housing.csv", "w", encoding="utf8", newline="") as f :
        theWriter = writer(f)
        header = ["title", "location", "price", "area"]

        theWriter.writerow(header)

        for list in lists:
            title = list.find("a", class_="listing-search-item__link--title").text.replace("\n", "")
            location = list.find("div", class_="listing-search-item__sub-title").text.replace("\n", "")
            price = list.find("div", class_="listing-search-item__price").text.replace("\n", "")
            area = list.find("li", class_="illustrated-features__item illustrated-features__item--surface-area").text.replace("\n", "")
            info = [title, location, price, area]

            theWriter.writerow(info)

    return 'done'
    