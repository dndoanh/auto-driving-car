from handlers.simulation_handler import SimulationHandler


def test_create_field_with_invalid_input(monkeypatch, capfd):
    inputs = iter(["10 10a", "10 10"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "Invalid width and height of the field."
    handler = SimulationHandler()
    handler.create_field()
    output, err = capfd.readouterr()
    assert expected_output in output


def test_create_car_with_invalid_name_input(monkeypatch, capfd):
    inputs = iter(["", "A"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "Invalid name of the car."
    handler = SimulationHandler()
    handler._input_car_name()
    output, err = capfd.readouterr()
    assert expected_output in output


def test_create_car_with_invalid_position_direction(monkeypatch, capfd):
    inputs = iter(["1 2a N", "1 2 N"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "Invalid position or direction of the car."
    handler = SimulationHandler()
    handler._input_car_position_direction("A")
    output, err = capfd.readouterr()
    assert expected_output in output


def test_create_car_with_invalid_commands(monkeypatch, capfd):
    inputs = iter(["AFFFR", "FFFRLFF"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "Invalid commands of the car."
    handler = SimulationHandler()
    handler._input_car_commands("A")
    output, err = capfd.readouterr()
    assert expected_output in output


def test_invalid_selection(monkeypatch, capfd):
    inputs = iter(["3", "1"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = "Invalid selection. Please try again."
    handler = SimulationHandler()
    handler._input_selection("Please select an option:")
    output, err = capfd.readouterr()
    assert expected_output in output


def test_run_simulation_single_car(monkeypatch, capfd):
    inputs = iter(["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "2", "2"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = [
        "Welcome to Auto Driving Car Simulation!",
        "Please enter the width and height of the simulation field in x y format:",
        "You have created a field of 10 x 10.",
        "Please choose from the following options:",
        "[1] Add a car to field",
        "[2] Run simulation",
        "Please enter the name of the car:",
        "Please enter initial position of car A in x y Direction format:",
        "Please enter the commands for car A:",
        "Your current list of cars are:",
        "- A, (1,2) N, FFRFFFFRRL",
        "After simulation, the result is:",
        "- A, (5,4) S",
        "[1] Start over",
        "[2] Exit",
        "Thank you for running the simulation. Goodbye!",
    ]
    handler = SimulationHandler()
    handler.run()
    output, err = capfd.readouterr()
    for line in expected_output:
        assert line in output


def test_run_simulation_multiple_cars_without_collision(monkeypatch, capfd):
    inputs = iter(["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "1", "B", "5 7 S", "FFFLFRFRFF", "2", "2"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = [
        "Welcome to Auto Driving Car Simulation!",
        "Please enter the width and height of the simulation field in x y format:",
        "You have created a field of 10 x 10.",
        "Please choose from the following options:",
        "[1] Add a car to field",
        "[2] Run simulation",
        "Please enter the name of the car:",
        "Please enter initial position of car A in x y Direction format:",
        "Please enter the commands for car A:",
        "Your current list of cars are:",
        "- A, (1,2) N, FFRFFFFRRL",
        "- B, (5,7) S, FFFLFRFRFF",
        "After simulation, the result is:",
        "- A, (5,4) S",
        "- B, (4,3) W",
        "[1] Start over",
        "[2] Exit",
        "Thank you for running the simulation. Goodbye!",
    ]
    handler = SimulationHandler()
    handler.run()
    output, err = capfd.readouterr()
    for line in expected_output:
        assert line in output


def test_run_simulation_multiple_cars_with_collision(monkeypatch, capfd):
    inputs = iter(["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "1", "B", "7 8 W", "FFLFFFFFFF", "2", "2"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    expected_output = [
        "Welcome to Auto Driving Car Simulation!",
        "Please enter the width and height of the simulation field in x y format:",
        "You have created a field of 10 x 10.",
        "Please choose from the following options:",
        "[1] Add a car to field",
        "[2] Run simulation",
        "Please enter the name of the car:",
        "Please enter initial position of car A in x y Direction format:",
        "Please enter the commands for car A:",
        "Your current list of cars are:",
        "- A, (1,2) N, FFRFFFFRRL",
        "- B, (7,8) W, FFLFFFFFFF",
        "After simulation, the result is:",
        "- A, collides with B at (5,4) at step 7",
        "- B, collides with A at (5,4) at step 7",
        "[1] Start over",
        "[2] Exit",
        "Thank you for running the simulation. Goodbye!",
    ]
    handler = SimulationHandler()
    handler.run()
    output, err = capfd.readouterr()
    for line in expected_output:
        assert line in output
