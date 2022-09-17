





class BasePage(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        
class Navigation(BasePage):
    def open_chrome_session(self):
        while True:
            try:
                self.driver.get(f"{self.base_url}")
                print(f"{self.base_url}")