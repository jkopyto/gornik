import requests
from bs4 import BeautifulSoup


def get_url(num):
    return "http://www.gornik.tbg.net.pl/news.htm?page={0}".format(num)


def fetch_data(num):

    r = requests.get(url=get_url(int(num)), params={})
    soup = BeautifulSoup(r.text, "html.parser")
    headers_list = soup.find_all("span", class_="cont_header")

    for i in headers_list:
        print(i.get_text())

    msg = input("\nType y to show next page titles: ")
    if msg == "y":
        fetch_data(int(num) + 1)
    else:
        return


fetch_data(1)
