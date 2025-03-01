from handlers.simulation_handler import SimulationHandler


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


def test_run_simulation_multiple_cars(monkeypatch, capfd):
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
