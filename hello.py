# import necessary library

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
# make page request and beautifulsoup object

page=urlopen("http://www.jnu.ac.in")
html=BeautifulSoup(page.read(),"lxml")
link_set=set()
# find only those link that start from http!

for link in html.find_all("a",attrs={"href":re.compile("^http://")}):
    web_links=link.get("href")
    print(web_links)
    link_set.add(web_links)
#save data(link) in csv file

csvfile=open("url.csv","w+",newline="")
writer=csv.writer(csvfile)
writer.writerow(["links"])
for link in link_set:
    writer.writerow([link])
csvfile.close()
# crawl csv get output in list using function

def crawl_csvfile():
    f=open("url.csv")
    csv_f=csv.reader(f)
    for link in csv_f:
        print(link)
# function call

crawl_csvfile()
# you can also print row
def pr():
    p=open("url.csv")
    csv_p=csv.reader(p)
    for row in csv_p:
        print(row[0])      # print  only single row
pr()



