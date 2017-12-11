from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_source,get_highlights_source

@main.route('/')
def index():
    '''
    view root page function return the index page with all its data
    '''
    #getting news from various categories
    general_source = get_news_source('general')
    entertainment_source  = get_news_source('entertainment')
    technology_source = get_news_source('technology')
    business_source = get_news_source('business')
    title = 'Home - News Highlights'
    return render_template('index.html',title = title,general = general_source,entertainment = entertainment_source,technology = technology_source,business = business_source)

@main.route('/source/<id>')
def source(id):
    '''
    views function that returns the source page and its data
    '''
    #Getting highlights in respect to sources chosen
    highlights = get_highlights_source(id)
    title = f'{id} - Top News'

    return render_template('source.html',title = title, highlights = highlights)

