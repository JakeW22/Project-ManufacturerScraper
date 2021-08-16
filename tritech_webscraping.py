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


# Moving on to next webpage within tritech to webscrape:
browser.follow_link("/products_and_services.html")

#print(browser.url)
pandr_page = browser.page
#print(pandr_page)

# Obtaining all data from the products & services tab:
for pandr_page_info in pandr_page:
    pandr_page_info = pandr_page.find("div", id="halftextleft")
    page_left = pandr_page_info.find_all("a")
    link_list = []
    loop_count = 0
    for links in page_left:
        if (loop_count % 2) == 0:         
            #print("Even", place)
            link_list.append(links["href"])

    
        else:
            #print("Odd", place)
            pass
        loop_count += 1
    services_list = []
    for pages in link_list:
        browser.follow_link(pages)
        services_page = browser.page
        services_info = services_page.find_all("div", id="righttextfull1")
        for text in services_info:
            services_info_text = str(text.text)
            services_title = text.find_next("h3")
            services_title.text
            
        #print(services_info_text)
            services_info_text.strip()
            
            #print(services_title, services_info_text)
            all_services = str(services_title) + str(services_info_text)
            #print(all_services)
    
#print(all_services)
#print(services_list)
#print(link_list)

# Now extracting the "Technical Services data"
browser.follow_link("/technical_services.html")
#print(browser.url)

tech_serv_page = browser.page
for links3 in tech_serv_page:
    info = tech_serv_page.find("div", id="righttextabout")
    info_text = info.text
    box = tech_serv_page.find("div", id="lefttext1")
    links3 = box.find_all("a")

    for information in links3:
        browser.follow_link(information)
        tech_page = browser.page
        tech = tech_page.find("div", id="righttextfull1")
        tech_text = tech.text
    
        print(tech_text)

#print(links)
#print(tech_text)
#print(info_text)