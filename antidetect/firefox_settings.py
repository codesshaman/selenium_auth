from selenium import webdriver


class FirefoxOptions:
    """Class for masking Selenium as a regular browser for Firefox"""
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.options = webdriver.FirefoxOptions()

    def disable_automation_control(self):
        """Disable the AutomationControlled flag"""
        print("Switch off the AutomationControlled flag")
        self.options.set_preference("dom.webdriver.enabled", False)

    def disable_enable_automation_switches(self):
        """Exclude enable-automation switches"""
        print("Switch off enable-automation switches")
        self.options.set_preference("devtools.jsonview.enabled", False)

    def disable_user_automation_extension(self):
        """Disable userAutomationExtension"""
        print("Switch off userAutomationExtension")
        self.options.set_preference("extensions.legacy.enabled", False)

    def disable_webnotifications_switches(self):
        """Disable web notification"""
        print("Switch off web notification")
        self.options.set_preference("devtools.dom.webnotifications.enabled", False)

    def disable_browser_volume(self):
        """Disable browser volume"""
        print("Switch off browser volume")
        self.options.set_preference("media.volume_scale", "0.0")

    def get_browser(self):
        self.disable_browser_volume()
        self.disable_automation_control()
        self.disable_enable_automation_switches()
        self.disable_user_automation_extension()
        self.disable_webnotifications_switches()
        driver = self.webdriver.Firefox(options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
