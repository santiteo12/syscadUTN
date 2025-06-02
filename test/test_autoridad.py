from app import create_app
import os

class AutoridadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_contenxt = self.app-context()
        self.app_contenxt.push()

    def tearDown(self):
        self.app_contenxt.pop()