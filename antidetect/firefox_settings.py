from fake_useragent import UserAgent
from selenium_stealth import stealth
from selenium import webdriver
from core.debug import dd
import functools


@dd
def options_decorator(key, value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            self.options.set_preference(key, value)
            return func(self)
        return wrapper
    return decorator

@dd
def ua_generator():
    """Generate random fake user-agent"""
    ua = UserAgent(browsers=["firefox"])
    return ua.random

class FirefoxOptions:
    """Class for masking Selenium as a regular browser for Firefox"""
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.options = webdriver.FirefoxOptions()

    @dd
    @options_decorator("media.volume_scale", "0.0")
    @options_decorator("dom.webdriver.enabled", False)
    @options_decorator("devtools.jsonview.enabled", False)
    @options_decorator("extensions.legacy.enabled", False)
    @options_decorator("general.useragent.override", ua_generator())
    @options_decorator("devtools.dom.webnotifications.enabled", False)
    def get_browser(self):
        driver = self.webdriver.Firefox(options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.maximize_window()
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        return driver
