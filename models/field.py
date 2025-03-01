from models.car import Car


class Field:
    def __init__(self, field_x: int, field_y: int) -> None:
        """Initialize field object.
        Args:
            field_x (int): width of the field.
            field_y (int): height of the field.
        """
        self.field_x = field_x
        self.field_y = field_y
        self.cars = []

    def __str__(self) -> str:
        return "\n".join([str(car) for car in self.cars])

    @property
    def result(self) -> str:
        return "\n".join([car.status for car in self.cars])

    def is_outside_field(self, car) -> bool:
        """Check whether the car is outside the field or not.
        Args:
            car (Car): the car going to check
        """
        return car.x < 0 or car.x > self.field_x - 1 or car.y < 0 or car.y > self.field_y - 1

    def is_duplicated(self, car) -> bool:
        """Check whether the car is duplicated or not.
        Args:
            car (Car): the car going to check
        """
        return any([c for c in self.cars if c.name == car.name or (c.x == car.x and c.y == car.y)])

    def add_car(self, car: Car) -> None:
        """Add a car to the field.
        Args:
            car (Car): the car is going to be added to the field.
        """
        if self.is_outside_field(car):
            raise ValueError("Invalid car's position. The car's position must be with the field boundary.")
        if self.is_duplicated(car):
            raise ValueError("Invalid car's name or position. The car's name or position must be unique.")
        self.cars.append(car)

    def update_status(self) -> None:
        """Do update status for each car in the field."""
        for car in self.cars:
            car.collided_cars = [c for c in self.cars if c.name != car.name and c.x == car.x and c.y == car.y]

    def run_simulation(self) -> None:
        """Run simulation."""
        if len(self.cars) == 0:
            return
        max_steps = max([len(car.steps) for car in self.cars])
        for i in range(max_steps):
            for car in self.cars:
                car.move(self.field_x, self.field_y)
            self.update_status()
