import unittest
from babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_starttime_cannot_be_before_5pm(self):
        self.assertEqual("start time cannot be before 5pm or after 3am", Babysitter.calculate(self.babysitter, 16, 20))

    def test_starttime_cannot_be_after_3am(self):
        self.assertEqual("start time cannot be before 5pm or after 3am", Babysitter.calculate(self.babysitter, 4, 20))

    def test_valid_starttime(self):
        self.assertNotEqual("start time cannot be before 5pm or after 3am", Babysitter.calculate(self.babysitter, 17, 20))

    def test_paid_12hr_start_to_bedtime(self):
        self.assertEqual(60, Babysitter.calculate(self.babysitter, 17, 22))

    def test_paid_12hr_start_to_endtime(self):
        self.assertEqual(48, Babysitter.calculate(self.babysitter, 17, 21))

    def test_paid_8hr_bedtime_to_midnight(self):
        self.assertEqual(16, Babysitter.calculate(self.babysitter, 22, 24))

    def test_endtime_cannot_be_after_4am(self):
        self.assertEqual("end time cannot be before 6pm or after 4am", Babysitter.calculate(self.babysitter, 20, 5))

    def test_endtime_cannot_be_before_6pm(self):
        self.assertEqual("end time cannot be before 6pm or after 4am", Babysitter.calculate(self.babysitter, 17, 17))

    def test_paid_16hr_bedtime_to_midnight(self):
        self.assertEqual(64, Babysitter.calculate(self.babysitter, 24, 4))
