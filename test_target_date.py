import unittest

from target_date import date_nb_days


class DateNbDaysTest(unittest.TestCase):
    
    def test_sample(self):
        self.assertEqual(date_nb_days(4281, 5087, 2), "2024-07-03")
        
    def test_sample_second(self):
        self.assertEqual(date_nb_days(9999, 11427, 6), "2018-03-13")
        
    def test_sample_x(self):
        self.assertEqual(date_nb_days(4620, 5188, 2), "2021-09-19")
        self.assertEqual(date_nb_days(9999, 11427, 6), "2018-03-13")
        self.assertEqual(date_nb_days(3525, 4822, 3), "2026-04-18")
        self.assertEqual(date_nb_days(5923, 6465, 6), "2017-06-10")
        self.assertEqual(date_nb_days(4254, 4761, 8), "2017-05-22")
        self.assertEqual(date_nb_days(1244, 2566, 4), "2033-11-04")
        self.assertEqual(date_nb_days(6328, 7517, 5), "2019-05-25")
        self.assertEqual(date_nb_days(2920, 3834, 2), "2029-06-03")
        self.assertEqual(date_nb_days(7792, 8987, 4), "2019-07-09")
    


# testing(date_nb_days(4620, 5188, 2), "2021-09-19")
# testing(date_nb_days(9999, 11427, 6), "2018-03-13")
# testing(date_nb_days(3525, 4822, 3), "2026-04-18")
# testing(date_nb_days(5923, 6465, 6), "2017-06-10")
# testing(date_nb_days(4254, 4761, 8), "2017-05-22")
# testing(date_nb_days(1244, 2566, 4), "2033-11-04")
# testing(date_nb_days(6328, 7517, 5), "2019-05-25")
# testing(date_nb_days(2920, 3834, 2), "2029-06-03")
# testing(date_nb_days(7792, 8987, 4), "2019-07-09")
