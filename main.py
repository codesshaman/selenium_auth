from antidetect.firefox_settings import FirefoxOptions
from antidetect.chrome_settings import ChromeOptions
from selenium import webdriver
import datetime
import time


# options = FirefoxOptions(webdriver)
options = ChromeOptions(webdriver)
browser = options.get_browser()

browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
time_now = datetime.datetime.now()
browser.save_screenshot('screenshots/' + str(time_now) + '.png')
time.sleep(200)
# browser.close()
