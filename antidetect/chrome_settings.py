from fake_useragent import UserAgent
from selenium_stealth import stealth
from selenium import webdriver
from core.debug import dd


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

    @dd
    def user_agent_generator(self):
        """Generate fake user-agent"""
        self.options.add_argument("user-agent=" + ua_generator())

    @dd
    def disable_browser_volume(self):
        """Disable browser volume"""
        self.options.add_argument("--mute-audio")

    @dd
    def browser_start_maximized(self):
        """Open browser to full screen"""
        self.options.add_argument("start-maximized")

    @dd
    def disable_browser_notifications(self):
        """Disable browser notification"""
        self.options.add_argument("--disable-notifications")

    @dd
    def disable_automation_control(self):
        """Disable the AutomationControlled flag"""
        self.options.add_argument("--disable-blink-features=AutomationControlled")

    @dd
    def disable_enable_automation_switches(self):
        """Exclude enable-automation switches"""
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

    @dd
    def disable_user_automation_extension(self):
        """Disable userAutomationExtension"""
        self.options.add_experimental_option("useAutomationExtension", False)

    @debug
    def get_browser(self):
        self.user_agent_generator()
        self.disable_browser_volume()
        self.browser_start_maximized()
        self.disable_automation_control()
        # self.disable_browser_notifications()
        self.disable_user_automation_extension()
        self.disable_enable_automation_switches()
        driver = self.webdriver.Chrome(options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        return driver
