from survey import AnonymousSurvey

# DEFINE A QUESTION, AND MAKE A SURVEY.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# SHOW THE QUESTION, AND STORE RESPONSES TO THE QUESTION.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#SHOW THE SURVEY RESULTST.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()