from unittest import TestCase
from Package1.Worker import Worker
import datetime

class TestWorker(TestCase):
    def setUp(self):
        print("setup:")
        self.gilad = Worker("Gilad", "Levy", 1999, 8, 12, "135, rothschild, tel-aviv", "IL")
        self.roy = Worker("Roy", "Segal", 1998, 7, 26, "1, dvoranit, ness-ziona", "IL")

    def tearDown(self):
        print("teardown^")

    def test_full_name(self):
        self.assertTrue(self.gilad.full_name() == "Gilad Levy")

    def test_age(self):
        # self.assertEqual(self.gilad.birth_year, datetime.datetime.now().year)
        # self.assertGreater(self.gilad.birth_year, datetime.datetime.now().year)
        # self.assertLess(self.gilad.birth_year, datetime.datetime.now().year)

    def test_days_to_birthday(self):

            self.assertGreater(self.gilad.birth_month, datetime.datetime.now().month)
        # if self.assertEqual(self.gilad.birth_month, datetime.datetime.now().month):
        #     self.assertGreater(self.gilad.birth_day, datetime.datetime.now().day)




        # if self.assertEqual(self.gilad.birth_month, datetime.datetime.now().month):
        #     self.assertGreater(self.gilad.birth_day, datetime.datetime.now().day)

        # self.assertLessEqual(self.gilad.birth_month, datetime.datetime.now().month)
        # self.assertLess(self.gilad.birth_day, datetime.datetime.now().day)
        #
        # self.assertEqual(self.gilad.birth_month, datetime.datetime.now().month)
        # self.assertEqual(self.gilad.birth_day, datetime.datetime.now().day)



    def test_greet(self):
        pass

    def test_location(self):
        pass

