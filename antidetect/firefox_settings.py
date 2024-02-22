from fake_useragent import UserAgent
from selenium_stealth import stealth
from selenium import webdriver
from core.debug import debug


@debug
def ua_generator():
    """Generate random fake user-agent"""
    ua = UserAgent(browsers=["firefox"])
    return ua.random

class FirefoxOptions:
    """Class for masking Selenium as a regular browser for Firefox"""
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.options = webdriver.FirefoxOptions()

    @debug
    def user_agent_generator(self):
        """Generate fake user-agent"""
        self.options.set_preference("general.useragent.override", ua_generator())

    @debug
    def disable_webdriver_flag(self):
        """Disable the webdriver flag"""
        self.options.set_preference("dom.webdriver.enabled", False)

    @debug
    def disable_enable_automation_switches(self):
        """Exclude enable-automation switches"""
        self.options.set_preference("devtools.jsonview.enabled", False)

    @debug
    def disable_user_automation_extension(self):
        """Disable userAutomationExtension"""
        self.options.set_preference("extensions.legacy.enabled", False)

    @debug
    def disable_webnotifications_switches(self):
        """Disable web notification"""
        self.options.set_preference("devtools.dom.webnotifications.enabled", False)

    @debug
    def disable_browser_volume(self):
        """Disable browser volume"""
        self.options.set_preference("media.volume_scale", "0.0")

    @debug
    def get_browser(self):
        self.user_agent_generator()
        self.disable_webdriver_flag()
        self.disable_browser_volume()
        self.disable_enable_automation_switches()
        self.disable_user_automation_extension()
        self.disable_webnotifications_switches()
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
