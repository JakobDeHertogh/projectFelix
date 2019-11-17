import unittest

class TestAlwaysWork(unittest.TestCase):
    '''
    Dit is een voorbeeld van een test in Python. Je kan tests runnen in VS Code 
    via "RightClick->Run Current Test File" of het commando 
    ---      python -m pytest -v tests   ---
    Alle tests worden ook automatisch uitgevoerd telkens je code pusht via Git. 
    Faalt je code een van deze tests, dan wordt hij niet gedeployed op de server!
    '''

    def setup(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_one_equals_one(self):
        self.assertEqual(1,1)