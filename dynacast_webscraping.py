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

# Now moving into the locations of about dynacast and extracting all the locations of their workplaces:
browser.follow_link("/locations")
#print(browser.url)

locations_page = browser.page
#print(locations_page)

locations_list = []
locations_description = locations_page.find("h2")
output_loc_descrip = locations_description.text
locations_list.append(output_loc_descrip)

locations_list = locations_page.find_all("div", id="location-list")

for locations_grid in locations_list:
    grid = locations_grid.find_all_next("div", class_="grid-4")

#print(grid)

