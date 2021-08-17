from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re

#STILL NEED NEWS PAGE

url = "https://amnitec.co.uk/"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

loop_count = 0

#print(browser.page)

browser.follow_link("about")

#print(browser.page)

about = browser.page

#print(about)

for about_page in about:
    about_info = about.find("div", class_="text-content")
    for content in about_info:
        content = about_info.find_all("p")
    
#print(content)

browser.follow_link("products")

#print(browser.page)

product_page = browser.page

for product in product_page:
    complete_range_title_h2 = product_page.find("h2")
    complete_range_title_h3 = product_page.find_all("h3")
    complete_range_title_h4 = product_page.find_all("h4")
    complete_range_title = complete_range_title_h2, complete_range_title_h3, complete_range_title_h4
    complete_range_text = product_page.find_all("p")
    
    for title in complete_range_title:
        print(title)

    for text in complete_range_text:
        print(text.text)
    
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("industries")

#print(browser.page)

industries_page = browser.page

for industry in industries_page:
    industry_title = industries_page.find_all("h2")
    industry_text = industries_page.find_all("p")
    industry_span = industries_page.find_all("span")
    industry_span_content = industries_page.find_all("div", class_="text-content mb-2")
    
    for title in industry_title:
        print(title.text)

    for text in industry_text:
        print(text.text)
    
    for span_1 in industry_span:
        print(span_1.text)

    for span_2 in industry_span_content:
        print(span_2.text)
    
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("resources")

resources_page = browser.page

for resource in resources_page:
    text_content = resources_page.find("div", class_="text-content")
    links_all = text_content.find_all("a")

    for links in links_all:
        print(links)

    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("certification")

quality_page = browser.page

#print(quality_page)

for certification in quality_page:
    quality_title = quality_page.find_all("h2")
    quality_text_container = quality_page.find("div", class_="text-content")
    quality_text = quality_text_container.find_all("p")
    link_container = quality_page.find_all("div", class_="text-content")
    
    for href in link_container:
        links = href.find_all("a")

    for title in quality_title:
        print(title.text)

    for text in quality_text:
        print(text.text)
    
    for url in links:
        print(url)

    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("innovation")

innovation = browser.page

for creative in innovation:
    creative_title = innovation.find_all("h2")
    
    creative_text = innovation.find_all("p")

    for title in creative_title:
        print(title.text)

    for text in creative_text:
        print(text.text)

    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break