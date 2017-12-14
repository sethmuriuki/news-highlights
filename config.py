import os

class Config:
    '''
    General configurations parent class 
    '''

    NEWS_API_BASE_URL = "https://newsapi.org/v1/sources?language=en&category={}"
    NEWS_API_KEY = '937b10b0c16b4f408a44526714103037'

class ProdConfig(Config):
    pass



class DevConfig(Config):
   
   DEBUG = True
   
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
