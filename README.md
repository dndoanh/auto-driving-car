## Auto Driving Car Simulation
### Setup
To create and activate a new virtual environment, run the following commands:
```commandline
python -m venv venv

.\venv\Scripts\activate
```
To install the necessary Python packages (include `--trusted-host` if required), run:
```commandline
pip install -r requirements.txt
```
## How to run
To run the code, use following command:
```commandline
python -m main
```
## Testing
To run unit tests, use:
```commandline
pytest .
```
To run unit tests with coverage, use:
```commandline
pytest --cov .
```
## Assumptions
1. Upon invalid input (e.g. invalid the width and height of the field; invalid car name, position, direction or commands; invalid menu selection), the program will prompt an error message for input again.
2. If a car is duplicated with same name or position, the program will prompt an error message for input again.
## Linting
For linting, use `black`, `isort` and `flake8`. To format the code, run the following commands:
```commandline
black --line-length=160 .

isort --profile=black --line-length=160 .

flake8 .
```

