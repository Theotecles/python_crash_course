# CREATE A FUNCTION CALLED CITY_COUNTRY
def city_country(city, country):
    """PRINT OUT A CITY COUNTRY COMBINATION"""
    output = f"{city}, {country}"
    return output.title()

combo1 = city_country('cincinnati', 'united states')
print(combo1)
combo2 =city_country('paris', 'france')
print(combo2)
combo3 = city_country('toronto', 'canada')
print(combo3)