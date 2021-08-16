from bs4 import BeautifulSoup, element
import mechanicalsoup
import mechanicalsoup.stateful_browser
import time
import requests
import re

#STILL NEED SOCIAL MEDIA AND ROLLING OVER NEWS PAGE
url = "https://castalum.com/"

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent = 'MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

#See if browser successfully found
#print(browser.url)

main_page = browser.page

loop_count = 0

for main_info in main_page:
    main_info = main_page.find_all("p")
    main_title = main_page.find_all("h2")
    for title in main_title:
        print(title.text)
    for info in main_info:
        print(info.text)
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("what-we-do")

#See if follow success
#print(browser.url)

what_we_do = browser.page

#See if what_we_do page success
#print(what_we_do)


for what_info in what_we_do:
    what_info_title = what_we_do.find_all("h3")
    what_info_text = what_we_do.find_all("p")
    for title in what_info_title:
        print(title.text)
    for text in what_info_text:
        print(text.text)
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("our-components")

#print(browser.page)

our_components = browser.page

for components in our_components:
    our_components_title = our_components.find_all("h3")
    our_components_text = our_components.find_all("p")
    for title in our_components_title:
        print(title.text)
    for text in our_components_text:
        print(text.text)
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("our-policies")

#print(browser.page)

our_policies = browser.page

for policies in our_policies:
    our_policies_title = our_policies.find_all("h3")
    our_policies_text = our_policies.find_all("p")
    for title in our_policies_title:
        print(title.text)
    for text in our_policies_text:
        print(text.text)
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("who-we-are")

#print(browser.page)

us = browser.page

for who_we_are in us:
    who_we_are_title = us.find_all("h3")
    who_we_are_text = us.find_all("p")
    for title in who_we_are_title:
        print(title.text)
    for text in who_we_are_text:
        print(text.text)
    loop_count +=1
    print(loop_count)
    if loop_count >= 1:
        break

browser.follow_link("our-awards")

#print(browser.page)

awards = browser.page

for our_awards in awards:
    our_awards_title = awards.find_all("h3")
    our_awards_text = awards.find_all("p")
    for title in our_awards_title:
        print(title.text)
    for text in our_awards_text:
        print(text.text)
    loop_count +=1    
    print(loop_count)
    if loop_count >= 1:
        break
