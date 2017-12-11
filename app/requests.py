import urllib.request,json
from models import Sources, Highlights


api_key = None

def configure_request(app):

    '''
    function that takes in application instance and replace None variables to application configuration object
    '''

    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']

def get_news_source(category):
    '''
    function that gets the json response to the url request
    '''

    get_news_url = 'https://newsapi.org/v1/sources'.fomart(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']

            source_results process_results(source_results_list)

            return source_results

