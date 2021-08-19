from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re


url = "http://www.psminternational.com/en/index/"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

browser.follow_link("about")

#print(browser.url)

# Webscraping about/profile data:
profile_about_page = browser.page
prof_list = []
for info in profile_about_page:
    info = profile_about_page.find("div", class_="ContainerRight")
    output_proftext = info.text
    prof_list.append(output_proftext)

#print(prof_list)



browser.follow_link("capability")
#print(browser.url)

# Scraping about/capability data:
capa_page = browser.page
capa_list = []
for info in capa_page:
    info = capa_page.find("div", class_="ContainerRight")
    output_capatext = info.text
    capa_list.append(output_capatext)

#print(capa_list)

browser.follow_link("application")
#print(browser.url)

pattern = re.compile("...*/application/.*?")
loop_count2 = 0
path = browser.page
container = path.find("div", class_="ContainerRight")
applications_links_list = []

app_links = container.find_all("a", href=pattern)
        
for links in app_links:
    if (loop_count2 % 2) == 0:         
        #print("Even", links)
        applications_links_list.append(links)

    
    else:
        #print("Odd", links)
        pass
    loop_count2 += 1

#print(applications_links_list)

# Cleaning up link list because of issues with '..':

#Extracting applications data:

applications_list = []
for pages in applications_links_list:
    browser.follow_link(pages)
    services_page = browser.page
    services_info = services_page.find_all("div", class_="div100")
    for text in services_info:
        services_info_text = str(text.text)
        services_title = text.find_next("div", class_="ZiTitle")
        #services_title.text
            
        #print(services_info_text)
        #services_info_text.strip()
            
        #print(services_title, services_info_text)
        all_services = (services_title.text) + (services_info_text)
        applications_list.append(all_services)
        # print(all_services)
        #pages_loop += 1
#print(pages.url)
#print(services_info_text)
print(applications_list)