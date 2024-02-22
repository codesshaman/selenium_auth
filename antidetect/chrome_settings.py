from antidetect.proxy_settings import SetProxy
from fake_useragent import UserAgent
from selenium_stealth import stealth
from core.settings import proxy
from selenium import webdriver
from core.debug import dd
import functools


@dd
def options_decorator(key, value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            self.options.add_argument(f"{key}={value}")
            return func(self)
        return wrapper
    return decorator

@dd
def experimental_decorator(key, value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            self.options.add_experimental_option(key, value)
            return func(self)
        return wrapper
    return decorator

@dd
def ua_generator():
    """Generate random fake user-agent"""
    ua = UserAgent(browsers=["chrome"])
    return ua.random

class ChromeOptions:
    """Class for masking Selenium as a regular browser"""
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.options = webdriver.ChromeOptions()

    def set_proxy(self):
        if proxy:
            set_proxy_instance = SetProxy()
            proxy_array = set_proxy_instance.get_proxy()
            if len(proxy_array) == 4:
                user = proxy_array[2]
                pswd = proxy_array[3]
                host = proxy_array[0]
                port = proxy_array[1]
                proxy_addr = f"{user}:{pswd}@{host}:{port}"
                print(proxy_addr)
                self.options.add_argument(f'--proxy-server=http://{proxy_addr}')
            else:
                host = proxy_array[0]
                port = proxy_array[1]
                proxy_addr = f"{host}:{port}"
                self.options.add_argument(f'--proxy-server=http://{proxy_addr}')
        else:
            print("WARNING! Proxy is not set!")

    @dd
    # @options_decorator("--mute-audio", "")
    @options_decorator("start-maximized", "")
    @options_decorator("user-agent", ua_generator())
    # @options_decorator("--disable-notifications", "")
    @options_decorator("--disable-blink-features", "AutomationControlled")
    @experimental_decorator("excludeSwitches", ["enable-automation"])
    @experimental_decorator("useAutomationExtension", False)
    def get_browser(self):
        driver = self.webdriver.Chrome(options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.set_proxy()
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        return driver
