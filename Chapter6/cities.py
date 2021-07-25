# CREATE A DICTIONARY OF THREE CITIES
cities = {
    'cincinnati': {
        'country': 'us',
        'population': 1746000,
        'fact': 'known as the queen city'
    },
    'new york': {
        'country': 'us',
        'population': 18804000,
        'fact': 'largest city in the us'
    },
    'paris': {
        'country': 'france',
        'population': 11017000,
        'fact': 'known as the city of light'
    }
}

# PRINT THE NAME OF EACH CITY AND ALL OF THE INFORMATION ABOUT IT

for city, city_info in cities.items():
    print(f"\n{city.title()}")
    print(f"\t{city.title()} is located in {city_info['country'].title()}, has a population of {city_info['population']} and is {city_info['fact']}.")