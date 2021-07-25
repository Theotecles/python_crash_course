class AnonymousSurvey:
    """COLLECT ANONYMOUS ANSWERS TO A SURVEY QUESTION."""

    def __init__(self, question):
        """STORE A QUESTION AND PREPARE TO STORE RESPONSES."""
        self.question = question
        self.responses = []

    def show_question(self):
        """SHOW THE SURVEY QUESTION."""
        print(self.question)

    def store_response(self, new_response):
        """STORE A SINGLE RESPONSE TO THE SURVEY."""
        self.responses.append(new_response)

    def show_results(self):
        """SHOW ALL THE RESPONSES THAT AHVE BEEN GIVEN."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")