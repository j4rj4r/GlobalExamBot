from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class Driver:
    """
    Browser management
    """
    def __init__(self, profile):
        self.profile = profile
        self.chrome_options = None
        self.driver = None
        self.action = None

    def setup(self, log_path='./data/logs/', headless=True):
        """
        Browser configuration
        """
        self.chrome_options = Options()

        # Anti bot detection
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        # Language Browser
        self.chrome_options.add_argument('--lang=fr-FR')

        # Maximize Browser
        self.chrome_options.add_argument('--start-maximized')

        # Headless Mode
        if headless:
            self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("window-size=1400,2100")


        # Optimize CPU
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-renderer-backgrounding")
        self.chrome_options.add_argument("--disable-background-timer-throttling")
        self.chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        self.chrome_options.add_argument("--disable-client-side-phishing-detection")
        self.chrome_options.add_argument("--disable-crash-reporter")
        self.chrome_options.add_argument("--disable-oopr-debug-crash-dump")
        self.chrome_options.add_argument("--no-crash-upload")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-low-res-tiling")
        self.chrome_options.add_argument("--log-level=3")
        self.chrome_options.add_argument("--silent")

        # Disable save password
        prefs = {'credentials_enable_service': False,
                'profile.password_manager_enabled': False}
        self.chrome_options.add_experimental_option('prefs', prefs)

        # Set profile
        self.chrome_options.add_argument(f'user-data-dir=./data/profiles/{self.profile}')

        self.driver = webdriver.Chrome('./ChromeDriver/chromedriver',options=self.chrome_options, service_args=[f'--log-path={log_path}ChromeDriver.log'])
        self.action = ActionChains(self.driver)
        return self.driver, self.action

    def get_driver(self):
        """
        Get Driver
        """
        return self.driver

    def get_action(self):
        """
        Get action
        """
        return self.action
