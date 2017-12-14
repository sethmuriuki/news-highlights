import unittest
from app.models import Highlights

class TestHighlights(unittest.TestCase):
    '''
    test case to test the behavior of the highlights model
    Args: 
        unittest.testcase - creates test cases
    '''

    def setup(self):
        '''
        function that runs before each test case
        '''
        self.new_highlights = Highlights()


