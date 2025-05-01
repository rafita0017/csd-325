# This is the FAIL version for Step 6 (language is required)
def city_country(city, country, population=None, language=None):
    """Return a formatted city-country string, with optional population but required language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Calls
print(city_country('santiago', 'chile', language='spanish'))
print(city_country('paris', 'france', 2148000, 'french'))
print(city_country('tokyo', 'japan', 13960000, 'japanese'))
 