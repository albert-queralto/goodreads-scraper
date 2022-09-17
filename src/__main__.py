import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class BookScraping(unittest.TestCase):
    
    def driver_config(self):
        self.driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)
        self.base_url = 'http://goodreads.com/'