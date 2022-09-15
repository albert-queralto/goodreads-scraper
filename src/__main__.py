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