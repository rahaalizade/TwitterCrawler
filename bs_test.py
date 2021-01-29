import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint

def get_url(user):
    url = "https://twitter.com/"+ user
    return url

def crawl_user_tweet(user):
    browser = webdriver.Chrome()
    browser.get(get_url(user))
    time.sleep(1)
    body = browser.find_element_by_tag_name('body')
    
    tweets = []
    for _ in range(10):
        part_of_tweets = browser.find_elements_by_xpath('//article[@role="article"]')
        for tweet in part_of_tweets:
            tweets.append(tweet.text)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
    
    return set(tweets)