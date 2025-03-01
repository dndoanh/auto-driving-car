import pytest

from utils.validation import validate_car_commands, validate_car_name, validate_car_position_direction, validate_field_width_height, validate_menu_selection


@pytest.mark.parametrize(
    "field_xy, is_valid",
    [
        (None, (False, None, None)),
        ("", (False, None, None)),
        ("10", (False, None, None)),
        ("10a 10", (False, None, None)),
        ("10 10a", (False, None, None)),
        ("10 10 10", (False, None, None)),
        ("0 10", (False, None, None)),
        ("10 -1", (False, None, None)),
        ("0 0", (False, None, None)),
        ("11.8 10", (False, None, None)),
        ("11 22.7", (False, None, None)),
        ("10 10", (True, 10, 10)),
    ],
)
def test_validate_field_width_height(field_xy, is_valid):
    result = validate_field_width_height(field_xy)
    assert result == is_valid


@pytest.mark.parametrize(
    "name_str, is_valid",
    [
        (None, (False, None)),
        ("", (False, None)),
        ("   ", (False, None)),
        (" A  ", (True, "A")),
        ("A", (True, "A")),
    ],
)
def test_validate_car_name(name_str, is_valid):
    result = validate_car_name(name_str)
    assert result == is_valid


@pytest.mark.parametrize(
    "position_direction_str, is_valid",
    [
        (None, (False, None, None, None)),
        ("", (False, None, None, None)),
        ("1 2", (False, None, None, None)),
        ("1 2a N", (False, None, None, None)),
        ("1a 2 N", (False, None, None, None)),
        ("1 2 N A", (False, None, None, None)),
        ("-1 2 N", (False, None, None, None)),
        ("1 -2 N", (False, None, None, None)),
        ("1 2 A", (False, None, None, None)),
        ("1 2 N", (True, 1, 2, "N")),
        ("1 2 E", (True, 1, 2, "E")),
        ("1 2 S", (True, 1, 2, "S")),
        ("1 2 W", (True, 1, 2, "W")),
    ],
)
def test_validate_car_position_direction(position_direction_str, is_valid):
    result = validate_car_position_direction(position_direction_str)
    assert result == is_valid


@pytest.mark.parametrize(
    "commands_str, is_valid",
    [
        (None, (False, None)),
        ("", (False, None)),
        ("FF ", (False, None)),
        ("AFFFRL", (False, None)),
        ("FFFRLFF", (True, "FFFRLFF")),
    ],
)
def test_validate_car_commands(commands_str, is_valid):
    result = validate_car_commands(commands_str)
    assert result == is_valid


@pytest.mark.parametrize(
    "selection_str, is_valid",
    [
        (None, (False, None)),
        ("", (False, None)),
        ("3", (False, None)),
        ("1", (True, "1")),
        ("2", (True, "2")),
    ],
)
def test_validate_menu_selection(selection_str, is_valid):
    result = validate_menu_selection(selection_str)
    assert result == is_valid
