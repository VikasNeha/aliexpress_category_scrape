from bs4 import BeautifulSoup
import urllib2
import csv


def make_soup(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html, "html5lib")

print "200"

ifile = open("csv/divided/6_200_sub_cats.csv", "rb")
csv_reader = csv.reader(ifile)

ofile = open("csv/divided_out/7_200_sub_cats.csv", "wb")
csv_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

i = 1

for row in csv_reader:
    soup = make_soup(row[2])
    dl = soup.find("dl", class_="son-category")
    lis = dl.find_all("li")

    if len(lis) > 0:
        for li in lis:
            csv_writer.writerow([li.a.text, row[0], li.a["href"]])

    print i
    i += 1

ifile.close()
ofile.close()