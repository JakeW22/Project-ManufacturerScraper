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
    loop_count1 = 0
    place_list = []
    for place in find_all_a:
        if (loop_count1 % 2) == 0:
            #print("Even", place)
            place_list.append(place["href"])

    
        else:
            #print("Odd", place)
            pass
        loop_count1 +=1
    #print(info["href"])

#print(place_list)
#print(about_page_info.text)


# Moving on to next webpage within tritech to webscrape:
browser.follow_link("/products_and_services.html")

#print(browser.url)
pands_page = browser.page
#print(pandr_page)
link_list_left = []
link_list_right = []
loop_count2 = 0

services_list_left = []
services_list_right = []

# Obtaining all data from the products & services tab:
for pands_page_info in pands_page:
    pands_page_info = pands_page.find("div", id="halftextleft")
    page_left = pands_page_info.find_all("a")
    
for links in page_left:
    if (loop_count2 % 2) == 0:         
        #print("Even", links)
        link_list_left.append(links["href"])

    
    else:
        #print("Odd", links)
        pass
    loop_count2 += 1

#print(loop_count2)


pages_loop = 0    
for pages in link_list_left:
    
    browser.follow_link(pages)
    services_page = browser.page
    services_info = services_page.find_all("div", id="righttextfull1")
    for text in services_info:
        services_info_text = str(text.text)
        services_title = text.find_next("h3")
        #services_title.text
            
        #print(services_info_text)
        services_info_text.strip()
            
        #print(services_title, services_info_text)
        all_services = str(services_title.text) + str(services_info_text)
        services_list_left.append(all_services)
        # print(all_services)
        pages_loop += 1
    
#print(all_services)
#print(services_list_left)
#print(pages_loop)
#print(link_list)


for pands_right_info in pands_page:
    pands_right_info = pands_page.find("div", id="halftextright")
    page_right = pands_right_info.find_all("a")

for links in page_right:
    if (loop_count2 % 2) == 0:         
        #print("Even", links)
        link_list_right.append(links["href"])

    
    else:
        #print("Odd", links)
        pass
    loop_count2 += 1

# Checking to see if links have append to list properly
#print(link_list_right)


# Extracting info from the right links:
for pages in link_list_right:
    browser.follow_link(pages)
    services_page = browser.page
    services_info = services_page.find_all("div", id="righttextfull1")
    for text in services_info:
        services_info_text = str(text.text)
        services_title = text.find_next("h3")
        #services_title.text
            
        #print(services_info_text)
        services_info_text.strip()
            
        #print(services_title, services_info_text)
        all_services = str(services_title.text) + str(services_info_text)
        services_list_right.append(all_services)
        # print(all_services)
        
#print(services_list_right)

# Now extracting the "Technical Services data"
browser.follow_link("/technical_services.html")
#print(browser.url)
tech_serv_list = []
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
    
    full_tech_serv_info = info_text + tech_text
    tech_serv_list.append(full_tech_serv_info) 
    #print(tech_text)

print(tech_serv_list)
#print(links)
#print(tech_text)
#print(info_text)