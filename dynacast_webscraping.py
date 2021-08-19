from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re


url = "https://www.dynacast.com/en-gb"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

# Main Page data scraping: (Not a lot to scrape here so no need for a loop)
main_page = browser.page
main_page_list = []
#main_info = main_page.find("h1")
#main_info.strip
#main_page_list.append(main_info.text)
main_page_list.append("Die Casting Company")
description = main_page.find("span")
description_refined = description.text.replace(u'\xa0', u'')
main_page_list.append(description_refined)


#print(main_page_list)

# Now moving to extracting data from about section:
about_link = browser.find_link("a", class_="a0 first has-submenu")
#print(about_link)
browser.follow_link(about_link)

#print(browser.url)


# Extracting data from investor relations in the about section:
browser.follow_link("/investor-relations")
#print(browser.url)

invrel_page = browser.page
pdf_loop = 0
for policies in invrel_page:
    polices = invrel_page.find("div", style="background-color: none;")
    pdfs = polices.find_all("a")
    pdf_loop += 1
    #print("Pdf", pdf_loop, pdfs)
    
for href in pdfs:
    output_invrel_pdfs = url + href["href"]
    #print(output_invrel_pdfs)

# Moving on to scraping data in specialty die casting section:
browser.follow_link("/speciality-die-casting")

print(browser.url)

