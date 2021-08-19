from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re



url = "http://www.team-precision.co.uk/"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

# Scraping Our Services pages:
ourservices_link_list = ["/project-management/", "/design-engineering/", "/tube-metal-forming/", "/product-assembly/",
"/pack-dispatch/"]

ourservices_info_list = []
for links in ourservices_link_list:
    browser.follow_link(links)
    ourservices_page = browser.page
    ourservices_content = ourservices_page.find("div", class_="content ua")
    title = ourservices_content.find("h3", class_= "article-title")
    title_text = title.text
    body_info = ourservices_content.text
    complete_body = title_text + body_info 
    ourservices_info_list.append(complete_body)

#print(ourservices_info_list)


# Scraping About pages:
about_link_list = ["/our-team/", "/visions-values/", "/quality-control/", "/health-safety/"]

about_info_list = []
for links in about_link_list:
    browser.follow_link(links)
    about_page = browser.page
    about_content = about_page.find("div", class_="content ua")
    title = about_content.find("h3", class_= "article-title")
    title_text = title.text
    body_info = about_content.text
    complete_body = title_text + body_info 
    about_info_list.append(complete_body)

#print(about_info_list)


# Moving to scrape data for Latest News:
browser.follow_link("latest-news")
#print(browser.url)

news_links_list = []

late_news = browser.page
#print(late_news)
loop_count2 = 0
for news_links in late_news:
    news_page = late_news.find("div", id="linkedin-content")
    news_links = news_page.find_all("a")
    #news_links_list.append(news_links["href"])

for links2 in news_links:
    if (loop_count2 % 2) == 0:         
    #print("Even", links)
        news_links_list.append(links2["href"])

    
#    else:
        #print("Odd", links)
#        pass
#    loop_count2 += 1

#print(browser.url)
#print(news_links_list)
#print(news_links)

for news_posts in news_links_list:
    browser.open(news_posts)
    print(news_posts)
    news_info = browser.page
    events_news = news_info.find("section", class_="fixed-fill")
    #profile_title = news_info.find("")
    news_info_text = events_news.find_all("div", class_="feed-shared-text relative feed-shared-update-v2__commentary")
    #output_news_info = news_info_text.text
    print(news_info_text)
    time.sleep(3)

#print(events_news)
#print(output_news_info)

# Currently running into an issue with extracting data from Latest News page:
# 1. browser.follow_link() producing a linkNotFoundError - meaning that my list of news_links_list = wrong OR
# 2. news_posts is messing with the list in an unexpected way. Need to investigate further