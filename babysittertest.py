import unittest
from babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_starttime_cannot_be_before_5(self):
        self.assertEqual("start time cannot be before 5pm", Babysitter.calculate(self.babysitter, 16))
