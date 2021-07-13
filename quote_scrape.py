from selenium import webdriver
from time import sleep
import os
import csv

clear = lambda: os.system('cls')

quotes_list=[]
authors_list=[]
clear()
driver = webdriver.Firefox(executable_path=r"C:\Users\Bona\Documents\Python Projects\geckodriver-v0.29.0-win64\geckodriver.exe")
driver.maximize_window()

driver.get("https://quotes.toscrape.com/")
sleep(3)
quotes = driver.find_elements_by_xpath("//span[@class='text']")
authors = driver.find_elements_by_xpath("//small[@class='author']")

for quote in quotes:
    quotes_list.append(quote.text)
    quote_text = quote.text

for author in authors:
    authors_list.append(author.text)
    author_text = author.text

results = dict((a, b) for a, b in zip(quotes_list, authors_list))
results_size = len(results)
qtlist = list(results)
qtlist_len = len(qtlist)
at = results.values()
atlist = list(at)
atlist_len = len(atlist)

with open('quotes.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Quote', 'Author'])
    for t in range(atlist_len):
        thewriter.writerow([qtlist[t], atlist[t]])
        print("Quote: {}\nAuthor: {}".format(qtlist[t],atlist[t]))