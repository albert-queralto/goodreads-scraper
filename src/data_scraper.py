import re
from bs4 import BeautifulSoup

from font_code_pointers import *
from navigation import *
from support_functions import *

class BestBooksEverPageScraper(BasePage):
    
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        
        self.best_books_ever = {
                                'position':[], 'title':[], 'author':[], 'book_id':[], 'stars':[], 'ratings':[], 'score':[],
                                'people_voted':[]
                                }
        
    def get_all_book_pages(self):
        while True:
            try:
                self.get_best_books_info(self.best_books_ever)
                print(self.best_books_ever)
                self.driver.implicitly_wait(5)
                if Navigation.navigate_next_page(self) == False:
                    break
            except Exception as e:
                print(e)
                break
        return self.best_books_ever
    
    def get_best_books_info(self, dictionary: dict):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        
        if soup is not None:
            for book in soup.find_all('tr'):
                try:
                    dictionary['position'].append(book.find(BestBooksEverPointers.POSITION_ORDER[0], class_=BestBooksEverPointers.POSITION_ORDER[1]).text.strip())
                    dictionary['title'].append(book.find(BestBooksEverPointers.BOOK_TITLE[0], class_=BestBooksEverPointers.BOOK_TITLE[1]).text.strip())
                    dictionary['author'].append(book.find(BestBooksEverPointers.AUTHOR_NAME[0], class_=BestBooksEverPointers.AUTHOR_NAME[1]).text.strip())
                    dictionary['book_id'].append(book.find(BestBooksEverPointers.BOOK_TITLE[0], class_=BestBooksEverPointers.BOOK_TITLE[1]).get('href').split('/')[-1])
                    
                    stars, ratings = StringProcessing.get_stars_ratings(book.find(BestBooksEverPointers.STARS_RATINGS[0], class_=BestBooksEverPointers.STARS_RATINGS[1]).text)
                    dictionary['stars'].append(stars)
                    dictionary['ratings'].append(ratings)
                    
                    score = StringProcessing.get_scores(str(book.find(BestBooksEverPointers.SCORE[0], text=re.compile(BestBooksEverPointers.SCORE[1]))))
                    dictionary['score'].append(score)
                    
                    votes = StringProcessing.get_votes(str(book.find(BestBooksEverPointers.VOTES[0], text=re.compile(BestBooksEverPointers.VOTES[1]))))
                    dictionary['people_voted'].append(votes)
                    
                except Exception as e:
                    print(e)
                    continue
            return dictionary
        else:
            print('Soup object is None')
            return None