from selenium import webdriver 


class ChromeOptions:
    """Class for masking Selenium as a regular browser"""
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.options = webdriver.ChromeOptions()

    def disable_browser_volume(self):
        """Disable browser volume"""
        print("Switch off browser volume")
        self.options.add_argument("--mute-audio")

    def disable_browser_notifications(self):
        """Disable browser notification"""
        print("Disable browser notifications")
        self.options.add_argument("--disable-notifications")

    def disable_automation_control(self):
        """Disable the AutomationControlled flag"""
        print("Switch off the AutomationControlled flag")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
    
    def disable_enable_automation_switches(self):
        """Exclude enable-automation switches"""
        print("Switch off enable-automation switches")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

    def disable_user_automation_extension(self):
        """Disable userAutomationExtension"""
        print("Switch off userAutomationExtension")
        self.options.add_experimental_option("useAutomationExtension", False)

    def get_browser(self):
        self.disable_browser_volume()
        self.disable_automation_control()
        # self.disable_browser_notifications()
        self.disable_user_automation_extension()
        self.disable_enable_automation_switches()
        driver = self.webdriver.Chrome(options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
