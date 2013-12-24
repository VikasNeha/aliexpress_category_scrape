from bs4 import BeautifulSoup
import urllib2
import csv


def make_soup(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html, "html5lib")


BASE_URL = "http://www.aliexpress.com/all-wholesale-products.html"

soup = make_soup(BASE_URL)
main_cats = soup.find_all("a", class_="main-category")

ofile = open("csv/1_main_cats.csv", "wb")
csv_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for category in main_cats:
    csv_writer.writerow([category.text, "", category["href"]])

ofile.close()