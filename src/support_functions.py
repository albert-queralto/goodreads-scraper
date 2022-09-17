import re

class StringProcessing(object):
    
    def get_stars_ratings(text):
        stripped_text = text.split(' — ')
        stars = float(re.findall(r'\d+\.\d+', stripped_text[0])[0])
        ratings = int(stripped_text[1].split(' rating')[0].replace(',', ''))
        return stars, ratings