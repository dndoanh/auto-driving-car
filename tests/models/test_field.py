import pytest

from models.car import Car
from models.field import Field


@pytest.mark.parametrize("field_x, field_y", [(10, 10)])
def test_initialization(field_x, field_y):
    field = Field(field_x, field_y)
    assert isinstance(field, Field)
    assert field.field_x == field_x
    assert field.field_y == field_y
    assert field.cars == []


@pytest.mark.parametrize("field_x, field_y, car, car2", [(10, 10, Car("A", 1, 2, "N", "FFRLRF"), Car("B", 7, 8, "W", "RFRLRF"))])
def test_add_car(field_x, field_y, car, car2):
    field = Field(field_x, field_y)
    field.add_car(car)
    field.add_car(car2)
    assert field.cars == [car, car2]


@pytest.mark.parametrize(
    "field_x, field_y, car",
    [
        (10, 10, Car("A", -1, 2, "N", "FFRLRF")),
        (10, 10, Car("A", 1, -2, "N", "FFRLRF")),
        (10, 10, Car("A", 11, 8, "N", "FFRLRF")),
        (10, 10, Car("A", 5, 22, "N", "FFRLRF")),
    ],
)
def test_add_car_with_position_beyond_the_field(field_x, field_y, car):
    field = Field(field_x, field_y)
    with pytest.raises(ValueError):
        field.add_car(car)


@pytest.mark.parametrize(
    "field_x, field_y, car, car2",
    [
        (10, 10, Car("A", 1, 2, "N", "FFRLRF"), Car("A", 5, 8, "W", "RFRLRF")),
        (10, 10, Car("A", 1, 2, "N", "FFRLRF"), Car("B", 1, 2, "E", "RFRLRF")),
    ],
)
def test_add_car_with_duplication(field_x, field_y, car, car2):
    field = Field(field_x, field_y)
    with pytest.raises(ValueError):
        field.add_car(car)
        field.add_car(car2)


@pytest.mark.parametrize("field_x, field_y, car, field_str, result", [(10, 10, Car("A", 1, 2, "N", "FFRFFFFRRL"), "- A, (1,2) N, FFRFFFFRRL", "- A, (5,4) S")])
def test_run_simulation_single_car(field_x, field_y, car, field_str, result):
    field = Field(field_x, field_y)
    field.add_car(car)
    assert str(field) == field_str
    field.run_simulation()
    assert field.result == result


@pytest.mark.parametrize(
    "field_x, field_y, car, car2, field_str, result",
    [
        (
            10,
            10,
            Car("A", 1, 2, "N", "FFRFFFFRRL"),
            Car("B", 7, 8, "W", "FFLFFRFFFF"),
            "- A, (1,2) N, FFRFFFFRRL\n- B, (7,8) W, FFLFFRFFFF",
            "- A, (5,4) S\n- B, (1,6) W",
        ),
        (
            10,
            10,
            Car("A", 1, 2, "N", "FFRFFFFRRL"),
            Car("B", 7, 8, "W", "FFLFFFFFFF"),
            "- A, (1,2) N, FFRFFFFRRL\n- B, (7,8) W, FFLFFFFFFF",
            "- A, collides with B at (5,4) at step 7\n- B, collides with A at (5,4) at step 7",
        ),
    ],
)
def test_run_simulation_multiple_car(field_x, field_y, car, car2, field_str, result):
    field = Field(field_x, field_y)
    field.add_car(car)
    field.add_car(car2)
    assert str(field) == field_str
    field.run_simulation()
    assert field.result == result
