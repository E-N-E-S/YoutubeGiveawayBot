from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random


ytLiveChatUrl = "https://www.youtube.com/live_chat?v=5qap5aO4i9A" # Your YouTube Live Chat link here
keyword = "a" # Your keyword here
eligibleUsers = set()

# start web browser
browser=webdriver.Firefox()


def getHTML(url):

    # get source code
    browser.get(ytLiveChatUrl)
    time.sleep(1)

    page_source = browser.page_source



    return page_source

def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')


def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")

def updateEligibleUsers(messages):

    for message in messages:
        content = message.find("div", {"id": "content"})
        author = content.find("span", {"id": "author-name"}).text
        message_content = content.find("span", {"id": "message"}).text

        # if message includes your keyword
        if keyword in message_content.lower():
            #print("Added")
            eligibleUsers.add(author)

        #else:
            #print("Not added")

        # if you want to print author and messages: 
        # print(author, ": ", message_content)


def startDrawing(eligibleUsersList):
    print("Giveaway starts now! {totalUserCount} : total user count".format(
        totalUserCount = len(eligibleUsersList)))

    for i in range(1, 5):
        dots = i * "."
        time.sleep(1.5)
        print("Drawing{dots}".format(
            dots = dots
        ))

    print("Are you ready?")
    time.sleep(1.5)

    print("Checking permissions :)")
    time.sleep(1.5)

    print("From {totalUserCount} users. WINNER: ".format(
        totalUserCount = len(eligibleUsersList)), random.choice(eligibleUsersList))


def main():
    
    for i in range(0, 5):
        html_source = getHTML(ytLiveChatUrl)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateEligibleUsers(messages)
        print("{count} users joined to giveaway".format
            (count = len(eligibleUsers)))
        time.sleep(10)

    eligibleUsersList = list(eligibleUsers)
    startDrawing(eligibleUsersList)

    # close web browser
    browser.close()


main()