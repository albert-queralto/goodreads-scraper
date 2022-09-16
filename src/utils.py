
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locator import *

class BasePage(object):
    
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
class NavigationFunctions(BasePage):
    
    def open_chrome_session(self):
        while True:
            try:
                self.drive.get(f"{self.base_url}")
                print(f"{self.base_url}")
                break
            except TimeoutException as timeout:
                print(f"{timeout}")
                print("Page will be reloaded.")
                
    def navigate_to_lists_page(self):
        link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.MORE_BOOK_LISTS))