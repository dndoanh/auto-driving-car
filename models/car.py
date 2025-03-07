import utils.constants as consts


class Car:
    def __init__(self, name: str, x: int, y: int, direction: str, commands: str) -> None:
        """Initialize car object.

        Args:
            name (str): name of car.
            x (int): x-axis of car's position.
            y (int): y-axis of car's position.
            commands (str): commands of car.
        """
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.steps = list(commands)
        self.collided_cars = []
        self.moved_steps = 0

    @property
    def is_collided(self) -> bool:
        """Indicate the car whether got collision or not.

        Returns:
            (bool) a boolean value to indicate where the car got collision or not.
        """
        return len(self.collided_cars) > 0

    def __str__(self) -> str:
        """
        Returns: a string to represent the initial properties of the car.
        """
        return f"- {self.name}, ({self.x},{self.y}) {self.direction}, {self.commands}"

    @property
    def status(self) -> str:
        """
        Returns: a string to represent the status of the car.
        If the car got collision, display collided car along with position.
        """
        if self.is_collided:
            collided_car_names = ",".join([c.name for c in self.collided_cars])
            return f"- {self.name}, collides with {collided_car_names} at ({self.x},{self.y}) at step {self.moved_steps}"
        else:
            return f"- {self.name}, ({self.x},{self.y}) {self.direction}"

    def turn_left(self) -> None:
        """Do turn left.

        Returns: None.
        """
        if self.direction == consts.DIRECTION_NORTH:
            self.direction = consts.DIRECTION_WEST
        elif self.direction == consts.DIRECTION_EAST:
            self.direction = consts.DIRECTION_NORTH
        elif self.direction == consts.DIRECTION_SOUTH:
            self.direction = consts.DIRECTION_EAST
        else:
            self.direction = consts.DIRECTION_SOUTH

    def turn_right(self) -> None:
        """Do turn right.

        Returns: None.
        """
        if self.direction == consts.DIRECTION_NORTH:
            self.direction = consts.DIRECTION_EAST
        elif self.direction == consts.DIRECTION_EAST:
            self.direction = consts.DIRECTION_SOUTH
        elif self.direction == consts.DIRECTION_SOUTH:
            self.direction = consts.DIRECTION_WEST
        else:
            self.direction = consts.DIRECTION_NORTH

    def go_forward(self) -> None:
        """Do go forward.

        Returns: None.
        """
        if self.direction == consts.DIRECTION_NORTH:
            self.y += 1
        elif self.direction == consts.DIRECTION_EAST:
            self.x += 1
        elif self.direction == consts.DIRECTION_SOUTH:
            self.y -= 1
        else:
            self.x -= 1

    def _possible_go_forward(self, field_x: int, field_y: int) -> bool:
        """Check whether the car is possible to go forward or not.
        If the step is go forward and car tries to move beyond the boundary of the field, impossible to go forward.
        Returns:
            (bool)
        """
        if (
            (self.direction == consts.DIRECTION_NORTH and self.y == field_y - 1)
            or (self.direction == consts.DIRECTION_EAST and self.x == field_x - 1)
            or (self.direction == consts.DIRECTION_SOUTH and self.y == 0)
            or (self.direction == consts.DIRECTION_WEST and self.x == 0)
        ):
            return False
        else:
            return True

    def move(self, field_x: int, field_y: int) -> None:
        """Take one step to move.
        If the step is go forward and car tries to move beyond the boundary of the field, do not move.
        If the car got collision, do not move.
        Returns: None
        """
        if self.is_collided or len(self.steps) == 0:
            return
        self.moved_steps += 1
        step = self.steps.pop(0)
        if step == consts.COMMAND_LEFT:
            self.turn_left()
        elif step == consts.COMMAND_RIGHT:
            self.turn_right()
        else:
            if self._possible_go_forward(field_x, field_y):
                self.go_forward()
