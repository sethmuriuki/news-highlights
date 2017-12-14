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

    get_news_url = "https://newsapi.org/v1/sources".fomart(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']

            source_results = process_results(source_results_list)

            return source_results


def process_results(news_list):
    '''
    function to process new list dictonary and turn them to objects
    
    Args:
        news_list:a list of dictionaries that has news sources

    Return:
        news_results:A list of news objects
    '''

    news_results = []
    for source_item in news_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')


        news_source = Sources(id,name,description,url,category)
        news_results.append(news_source)

    return news_results

def get_highlights_sources(id):
    '''
    function that gets the json response to the url request
    '''

    get_highlights_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_responce = json.loads(get_highlights_data)

        highlights_results = None
        if get_highlights_responce['highlights']:
            highlights_results_list = get_highlights_response
            highlights_results = Process_highlights(highlights_results_list)

def Process_highlights(highlights_list):
    '''
    processes highlights results and changes them to object list

    Args:
        highlight_list:dictionaries that contain highlight details

    Returns:
        highlights_results:a list of highlights objects
    '''

    highlights_results = [] 

    for highlights_item in highlights_list:
         author = highlights_item.get('author')
         title = highlights_item.get('title')
         description = highlights_item.get('descripiton')
         url = highlights_item.get('url')
         image = highlights_item.get('urlToImage')
         date = highlights_item.get('publishedAt')


         if date:
             highlights_object = Highlights(author,title,description,url,image,date)
             highlights_results.append(highlights_object)