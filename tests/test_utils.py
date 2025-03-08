from src.utils import echo


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
