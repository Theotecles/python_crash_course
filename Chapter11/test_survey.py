import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """TESTS FOR THE CLASS ANONYMOUSSURVEY"""

    def setUp(self):
        """
        CREATE A SURVEY AND A SET OF RESPONSES FOR USE IN ALL TEST METHODS
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """TEST THAT A SINGLE RESPONSE IS STORED PROPERLY."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """TEST THAT THREE INDIVIDUAL RESPONSES ARE STORED PROPERLY"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()