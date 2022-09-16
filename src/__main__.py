import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriver
import scraper
import utils

class BookScraperSearch(unittest.TestCase):
    
    def configuration(self):
        self.driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(20)
        self.base_url = 'https://www.goodreads.com/'
        
    def web_scraper(self):
        page_navigator = utils.NavigationFunctions(driver=self.driver, base_url=self.base_url)
        page_navigator.open_chrome_session()
        
    
    
    
    def close_driver(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')