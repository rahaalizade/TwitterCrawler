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
    li_rawtweets = []
    rawtweets = []
    for _ in range(10):
        tweet_with_data =  browser.find_elements_by_xpath('//div[@data-testid="tweet"]')
        raw_tweets_data  = browser.find_elements_by_xpath('//div[@lang="en"]')
        
        for t in tweet_with_data:
            x = t.find_elements_by_xpath('.//span')
            likes = x[-1].text
            retweets = x[-3].text
            replies = x[-5].text
            tweet = x[-7].text
                
            tweets.append(tuple([tweet,likes,retweets,replies]))     
        
        for tweet in raw_tweets_data:
            rawtweets.append(tweet.text)
        
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        
    tweets = set(tweets)   
    rawtweets = set(rawtweets)      
     
    """
    Printing tweets in json format (tweets with replies, likes and retweets)
    """
    # return [jsonify_tweet(tweet) for tweet in tweets]
    
    """
    Printing rawtweets (just tweets)
    """
    return [{"tweet": tweet} for tweet in rawtweets]

def jsonify_tweet(tweet):
    json_data_format = {
                        "tweet": tweet[0],"likes":tweet[1],
                        "retweets":tweet[2], "replies":tweet[3]
                       }   
    return (json_data_format)
    
if __name__ == '__main__':
    
    print("Enter the username: ")
    user = input()
    with open("rawtweets.txt", "w") as file:
        file.write(str(crawl_user_tweet(user)).replace("\'","\""))