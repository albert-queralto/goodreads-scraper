from selenium.webdriver.common.by import By


class MainPagePointers(object):
    MORE_BOOK_LISTS = (By.LINK_TEXT, "More book lists")
    
class ListopiaPointers(object):
    X_BUTTON = (By.CLASS_NAME, 'gr-iconButton')
    BEST_BOOKS_EVER = (By.LINK_TEXT, 'Best Books Ever')