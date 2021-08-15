from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re


url = "https://www.tritechgroup.co.uk/"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

# Checking to see if sucessfully open browser:
#print(browser.url)

browser.follow_link("about.html")
pattern = re.compile('<".*?">')
# Checking to see if follow link worked
#print(browser.url)

about_page = browser.page
#print(about_page)
for about_page_info in about_page:
    about_page_info = about_page.find("div", id="righttextfull1")
    links = about_page.find("div", id="lefttextabout")
    find_all_a = links.find_all("a")
    loop_count = 0
    place_list = []
    for place in find_all_a:
        if (loop_count % 2) == 0:
            #print("Even", place)
            place_list.append(place["href"])

    
        else:
            #print("Odd", place)
            pass
        loop_count +=1
    #print(info["href"])

#print(place_list)
#print(about_page_info.text)

print(browser.url)