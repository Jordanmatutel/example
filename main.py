import pandas as pd
import requests
from bs4 import BeautifulSoup

restaurants = []
address = []
number = []

url = "https://sandiego.eater.com/maps/best-happy-hours-san-diego"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
search_area = soup.find_all("section", class_="c-mapstack__card")
for i in search_area:
    name = i.find("div", class_="c-mapstack__card-hed")
    if name is not None:
        result = name.find("h1")
        restaurants.append(result.text)
    location = i.find("div", class_="c-mapstack__address")
    if location is not None:
        address.append(location.text)
    phone_number = i.find("div", class_="c-mapstack__phone desktop-only")
    if phone_number is not None:
        number.append(phone_number.text)

address = address[0:14]
number = number[0:14]

c = pd.DataFrame({"Restaurant/Bar": restaurants, "Address": address, "Number": number})

c.to_csv("Recollected Information.csv")
