from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata
import attr

#it works!

with open('hw_2_Sasha.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("title", "published date", "issues", "number of signatures"))
  w.writeheader()    
  for i in range(0,4):
    new_web_page = urllib.request.urlopen('https://petitions.whitehouse.gov/?page=%s' %i)
    new_all_html = BeautifulSoup(new_web_page.read())
    all_bills = new_all_html.find_all('div')
    for i in all_bills:
        bills = {} 
        try:
            extension = i.article.find('h3').find('a').attrs['href']
        except AttributeError: 
            continue
        bill_page = urllib.request.urlopen('https://petitions.whitehouse.gov' +extension)
        all_about_bill = BeautifulSoup(bill_page.read())
        bill_title = all_about_bill.find("h1")
        bills["title"] = bill_title.get_text()
        bill_date = all_about_bill.find('h4', {'class': 'petition-attribution'})
        bills["published date"]  = bill_date.get_text()
        bill_issue = all_about_bill.find('div', {'class' : "field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"})
        bills["issues"] = bill_issue.get_text()
        bill_signature = all_about_bill.find('span', {'class':"signatures-number"})
        bills["number of signatures"] = bill_signature.get_text()
        w.writerow(bills)