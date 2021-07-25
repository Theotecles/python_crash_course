import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """TESTS FOR 'NAME_FUNCTION.PY'"""

    def test_first_last_name(self):
        """DO NAMES LIKE 'JANIS JOPLIN' WORK?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """DO NAMES LIKE 'WOLFGANG AMADEUS MOZART' WORK?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()