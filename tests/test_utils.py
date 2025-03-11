from src.utils import echo, get_flag_by_country
from src.instead_of_db import countries


# echo function tests:
def test_echo_with_int():
    assert echo(0) == 0


def test_echo_with_negative_int():
    assert echo(-1) == -1


def test_echo_with_float():
    assert echo(0.1) == 0.1


def test_echo_int_addition():
    assert echo(1 + 2) == 3


def test_echo_int_subtraction():
    assert echo(1 - 2) == -1


def test_echo_int_devision():
    assert echo(21 / 7) == 3


def test_echo_int_multiplication():
    assert echo(3 * 7) == 21


def test_echo_int_floor_division():
    assert echo(19 // 10) == 1


def test_echo_int_division_remainder():
    assert echo(19 % 10) == 9


def test_echo_with_string():
    assert echo("str") == "str"


def test_echo_with_list():
    assert echo([0, 1]) == [0, 1]


def test_echo_with_tuple():
    assert echo((0, 1)) == (0, 1)


def test_echo_with_set():
    assert echo({0, 1}) == {0, 1}


def test_echo_with_dictionary():
    assert echo({"a": 0, "b": 1}) == {"a": 0,"b": 1}


def test_echo_without_data():
    assert echo() is None


def test_echo_with_none():
    assert echo(None) is None


# get_flag_by_country function tests:
def test_get_flag_by_country_success():
    assert get_flag_by_country(countries, "djibouti") == "🇩🇯"


def test_get_flag_without_country():
    assert get_flag_by_country(countries) is None


def test_get_flag_without_countries():
    try:
        get_flag_by_country()
    except TypeError as e:
        assert str(e) == "get_flag_by_country() missing 1 required positional argument: 'countries'"


def test_get_nonexistent_flag():
    assert get_flag_by_country(countries, "brightland") is None
