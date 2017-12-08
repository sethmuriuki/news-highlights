import os

class config:
    '''
    General configurations parent class 
    '''

    NEWS_API_BASE_URL = "https://newsapi.org/v1/sources?language=en&category={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig:



class DevConfig:
