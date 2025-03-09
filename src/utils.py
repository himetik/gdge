def echo(x=None):
    return x


def get_flag_by_country(countries, country=None):
    if not country:
        return None
    return countries.get(country.lower())
