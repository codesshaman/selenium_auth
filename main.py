from antidetect.firefox_settings import FirefoxOptions
from antidetect.chrome_settings import ChromeOptions
from antidetect.proxy_settings import SetProxy
from selenium import webdriver
import datetime
import time


proxy = SetProxy()


# options = FirefoxOptions(webdriver)
options = ChromeOptions(webdriver)
browser = options.get_browser()

# proxy = proxy.get_proxy()
# if len(proxy) == 4:
#     PROXY_HOST = proxy[0]
#     PROXY_PORT = proxy[1]
#     PROXY_USER = proxy[2]
#     PROXY_PASS = proxy[3]
# else:
#     PROXY_HOST = proxy[0]
#     PROXY_PORT = proxy[1]

# browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
browser.get('https://2ip.ru')

time_now = datetime.datetime.now()
# browser.save_screenshot('screenshots/' + str(time_now) + '.png')
time.sleep(7)
browser.close()
