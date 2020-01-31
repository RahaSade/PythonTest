import unittest

import App as App


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/testData.json')
