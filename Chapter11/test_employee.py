import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """A TEST FOR THE CLASS EMPLOYEE"""

    def setUp(self):
        """
        CREATE AND EMPLOYEE AND TEST THE DEFAULT AND CUSTOM RAISE
        """
        first = 'brian'
        last = 'mochtyak'
        salary = 81000
        self.my_employee = Employee(first, last, salary)

    def test_give_default_raise(self):
        """TEST THAT A DEFAULT RAISE IS GIVEN PROPERLY"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 86000)

    def test_give_custom_raise(self):
        """TEST THAT A RAISE WITH A CUSTOM AMMOUNT WORKS PROPERLY"""
        self.my_employee.give_raise(9000)
        self.assertEqual(self.my_employee.salary, 90000)

if __name__ == '__main__':
    unittest.main()