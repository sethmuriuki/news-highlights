class Sources:
    '''
    source class  to to defines source objects
    '''
    
    def __init__(self,id,name,description,url,category):
        '''
        __init__ method to define the properties of a source object
        '''

        self.id = id
        self.name = name 
        self.descrption = description
        self.url = url 
        self.category = category


class Highlights:
     '''
     Highlights class to define highlights objects
     '''

     def __init__(self,authour,title,description,url,image,date):

        '''
        __init__ method to define highlights properties
        '''

        self.authour = authour
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date