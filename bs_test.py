import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_url(user):
    url = "https://twitter.com/"+ user
    return url