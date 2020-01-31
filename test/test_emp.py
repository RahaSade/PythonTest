import unittest
import calc
from employee import Employee  # look at how I import and give access to employee class


# always remember that the tests are not going to be run in order
class TestEmployee(unittest.TestCase):  # always remember to create a class first
    # use this setUp function to do something before all the test methods
    @classmethod
    def setUpClass(cls) -> None:
        print('setUp Class')

    # use this setUp function to do something after all the test methods
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    # use this setUp function to do something at the first step of running each test method
    def setUp(self):
        self.emp_1 = Employee('raha', 'sadeghi', 50000)
        self.emp_2 = Employee('Aty', 'Shadi', 60000)

    # # use this setUp function to do something at the last steps of running each test method
    def tearDown(self) -> None:
        pass

    def test_email(self):
        # emp_1 = Employee('Corey', 'Schafer', 50000) #as you already define them in setup there is no need to redefine them
        # emp_2 = Employee('Sue', 'Smit', 60000)
        self.assertEqual(self.emp_1.email, 'raha.sadeghi@email.com')

    def test_fullName(self):
        # emp1 = Employee('raha', 'sadeghi', 5000)
        self.assertEqual(self.emp_1.fullname, 'raha sadeghi')
