import re

class StringProcessing(object):
    
    def get_stars_ratings(text):
        stripped_text = text.split(' — ')
        stars = float(re.findall(r'\d+\.\d+', stripped_text[0])[0])
        ratings = int(stripped_text[1].split(' rating')[0].replace(',', ''))
        return stars, ratings
    
    def get_scores(text):
        return int(text.split('score: ')[1].split('</a>')[0].replace(',', ''))
    
    def get_votes(text):
        return int(text.split(' people voted')[0].split('>')[1].replace(',', ''))