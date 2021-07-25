# CREATE A FUNCTION CALLED DESCRIBE CITY
def describe_city(city, country='United States'):
    """PRINTS A SIMPLE SENTENCE ABOUT THE CITY AND THE COUNTRY IT IS LOCATED IN"""
    print(f"{city.title()} is located in the country, {country.title()}")

describe_city('cincinnati')
describe_city('chicago')
describe_city('paris', 'france')