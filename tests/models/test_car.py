import pytest

from models.car import Car


@pytest.mark.parametrize("name, x, y, direction, commands", [("A", 1, 2, "N", "FFRLFF")])
def test_initialization(name, x, y, direction, commands):
    car = Car(name, x, y, direction, commands)
    assert isinstance(car, Car)
    assert car.name == name
    assert car.x == x
    assert car.y == y
    assert car.direction == direction
    assert car.commands == commands
    assert car.steps == list(commands)
    assert car.collided_cars == []
    assert not car.is_collided
    assert car.moved_steps == 0
    assert str(car) == f"- {name}, ({x},{y}) {direction}, {commands}"


@pytest.mark.parametrize("name, x, y, direction, commands, moved_steps", [("A", 1, 2, "N", "FFRLFF", 7)])
def test_status(name, x, y, direction, commands, moved_steps):
    car = Car(name, x, y, direction, commands)
    car.moved_steps = moved_steps
    assert car.status == f"- {name}, ({x},{y}) {direction}"
    car2 = Car("B", 1, 2, "E", "LFRLRF")
    car.collided_cars = [car2]
    assert car.status == f"- {name}, collides with B at ({x},{y}) at step {moved_steps}"
    car3 = Car("C", 1, 2, "W", "RRRLRF")
    car.collided_cars = [car2, car3]
    assert car.status == f"- {name}, collides with B,C at ({x},{y}) at step {moved_steps}"


@pytest.mark.parametrize(
    "name, x, y, direction, commands, car_str",
    [
        ("A", 1, 2, "N", "FFRLFF", "- A, (1,2) W, FFRLFF"),
        ("A", 1, 2, "E", "FFRLFF", "- A, (1,2) N, FFRLFF"),
        ("A", 1, 2, "S", "FFRLFF", "- A, (1,2) E, FFRLFF"),
        ("A", 1, 2, "W", "FFRLFF", "- A, (1,2) S, FFRLFF"),
    ],
)
def test_turn_left(name, x, y, direction, commands, car_str):
    car = Car(name, x, y, direction, commands)
    car.turn_left()
    assert str(car) == car_str


@pytest.mark.parametrize(
    "name, x, y, direction, commands, car_str",
    [
        ("A", 1, 2, "N", "FFRLFF", "- A, (1,2) E, FFRLFF"),
        ("A", 1, 2, "E", "FFRLFF", "- A, (1,2) S, FFRLFF"),
        ("A", 1, 2, "S", "FFRLFF", "- A, (1,2) W, FFRLFF"),
        ("A", 1, 2, "W", "FFRLFF", "- A, (1,2) N, FFRLFF"),
    ],
)
def test_turn_right(name, x, y, direction, commands, car_str):
    car = Car(name, x, y, direction, commands)
    car.turn_right()
    assert str(car) == car_str


@pytest.mark.parametrize(
    "name, x, y, direction, commands, car_str",
    [
        ("A", 1, 2, "N", "FFRLFF", "- A, (1,3) N, FFRLFF"),
        ("A", 1, 2, "E", "FFRLFF", "- A, (2,2) E, FFRLFF"),
        ("A", 1, 2, "S", "FFRLFF", "- A, (1,1) S, FFRLFF"),
        ("A", 1, 2, "W", "FFRLFF", "- A, (0,2) W, FFRLFF"),
    ],
)
def test_go_forward(name, x, y, direction, commands, car_str):
    car = Car(name, x, y, direction, commands)
    car.go_forward()
    assert str(car) == car_str


@pytest.mark.parametrize(
    "field_x, field_y, name, x, y, direction, commands, car_str, moved_steps",
    [
        (10, 10, "A", 1, 2, "N", "LFRLFF", "- A, (1,2) W, LFRLFF", 1),
        (10, 10, "A", 1, 2, "N", "RFRLFF", "- A, (1,2) E, RFRLFF", 1),
        (10, 10, "A", 1, 2, "N", "FFRLFF", "- A, (1,3) N, FFRLFF", 1),
    ],
)
def test_move(field_x, field_y, name, x, y, direction, commands, car_str, moved_steps):
    car = Car(name, x, y, direction, commands)
    car.move(field_x, field_y)
    assert str(car) == car_str
    assert car.moved_steps == moved_steps


@pytest.mark.parametrize(
    "field_x, field_y, name, x, y, direction, commands, car_str, moved_steps",
    [
        (10, 10, "A", 1, 9, "N", "F", "- A, (1,9) N, F", 1),
        (10, 10, "A", 9, 6, "E", "F", "- A, (9,6) E, F", 1),
        (10, 10, "A", 1, 0, "S", "F", "- A, (1,0) S, F", 1),
        (10, 10, "A", 0, 2, "W", "F", "- A, (0,2) W, F", 1),
    ],
)
def test_do_not_move(field_x, field_y, name, x, y, direction, commands, car_str, moved_steps):
    car = Car(name, x, y, direction, commands)
    for i in range(2):
        car.move(field_x, field_y)
    assert str(car) == car_str
    assert car.moved_steps == moved_steps


@pytest.mark.parametrize(
    "field_x, field_y, car, car2, moved_steps, car_str", [(10, 10, Car("A", 1, 2, "N", "FFRLFF"), Car("B", 1, 2, "E", "LFRLRF"), 0, "- A, (1,2) N, FFRLFF")]
)
def test_do_not_move_if_got_collision(field_x, field_y, car, car2, moved_steps, car_str):
    car.collided_cars = [car2]
    car.move(field_x, field_y)
    assert car.moved_steps == moved_steps
    assert str(car) == car_str
