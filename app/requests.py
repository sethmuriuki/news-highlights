import urllib.request,json
from models import Sources, Highlights


api_key = None

def configure_request(app):

    '''
    function that takes in application instance and replace None variables to application configuration object
    '''

    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']


    