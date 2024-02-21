from selenium import webdriver
import datetime
import time

browser = webdriver.Firefox()
browser.get('https://duckduckgo.com')
time_now = datetime.datetime.now()
browser.save_screenshot('screenshots/' + str(time_now) + '.png')
browser.close()
