def get_city_country(city, country, population=''):
    """A FUNCTION THAT FORMATS THE NAMES OF A CITY AND COUNTRY"""
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted