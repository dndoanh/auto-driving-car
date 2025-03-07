import utils.messages as msg
from handlers.io.console_io_handler import ConsoleIOHandler
from handlers.io.io_handler import IOHandler
from models.car import Car
from models.field import Field
from utils.validation import validate_car_commands, validate_car_name, validate_car_position_direction, validate_field_width_height, validate_menu_selection


class SimulationHandler:

    def __init__(self, io_handler: IOHandler = None) -> None:
        """Initialize the simulation handler.
        Args:
            io_handler(IOHandler): to handle input and output. Use ConsoleIOHandler by default.
        """
        if io_handler is None:
            io_handler = ConsoleIOHandler()
        self.io_handler: IOHandler = io_handler
        self.field: None | Field = None

    def run(self) -> None:
        """Main function to handle the simulation."""
        self.create_field()
        while True:
            self._display_list_cars()
            selection = self._input_selection(msg.MSG_MENU_ADD_CAR)
            if selection == "1":
                self.create_car()
            else:
                self.run_simulation()
                break
        self.start_over()

    def run_simulation(self) -> None:
        """Start run the simulation after created field and cars."""
        if len(self.field.cars) > 0:
            self.io_handler.output_handler(f"{msg.MSG_LIST_CARS}\n{str(self.field)}")
            self.field.run_simulation()
            self._display_simulation_result()

    def create_field(self) -> None:
        """Create an instance of field with given width and height."""
        self.io_handler.output_handler(msg.MSG_WELCOME)
        is_valid_field_xy = False
        while not is_valid_field_xy:
            self.io_handler.output_handler(msg.MSG_INPUT_FIELD)
            field_xy_str = self.io_handler.input_handler()
            is_valid, field_x, field_y = validate_field_width_height(field_xy_str)
            if not is_valid:
                self.io_handler.output_handler(msg.MSG_OUTPUT_FIELD_INVALID)
            else:
                self.field = Field(field_x, field_y)
                self.io_handler.output_handler(msg.MSG_OUTPUT_FIELD.format(field_x=field_x, field_y=field_y))
                is_valid_field_xy = True

    def create_car(self) -> None:
        """To create a car with io_handler inputs."""
        name = self._input_car_name()
        x, y, direction = self._input_car_position_direction(name)
        commands = self._input_car_commands(name)
        try:
            car = Car(name, x, y, direction, commands)
            self.field.add_car(car)
        except ValueError as e:
            self.io_handler.output_handler(str(e))

    def _input_car_name(self) -> str:
        """Input name for car."""
        is_valid_car_name = False
        car_name = None
        while not is_valid_car_name:
            self.io_handler.output_handler(msg.MSG_INPUT_CAR_NAME)
            name_str = self.io_handler.input_handler()
            is_valid, car_name = validate_car_name(name_str)
            if not is_valid:
                self.io_handler.output_handler(msg.MSG_OUTPUT_CAR_NAME_INVALID)
            else:
                is_valid_car_name = True
        return car_name

    def _input_car_position_direction(self, car_name: str) -> tuple:
        """Input position(x,y) and direction for car."""
        is_valid_car_position_direction = False
        x, y, direction = None, None, None
        while not is_valid_car_position_direction:
            self.io_handler.output_handler(msg.MSG_INPUT_CAR_POSITION_DIRECTION.format(car_name=car_name))
            position_direction_str = self.io_handler.input_handler()
            is_valid, x, y, direction = validate_car_position_direction(position_direction_str)
            if not is_valid:
                self.io_handler.output_handler(msg.MSG_OUTPUT_CAR_POSITION_DIRECTION_INVALID)
            else:
                is_valid_car_position_direction = True
        return x, y, direction

    def _input_car_commands(self, car_name: str) -> str:
        """Input commands for car."""
        is_valid_car_commands = False
        commands = None
        while not is_valid_car_commands:
            self.io_handler.output_handler(msg.MSG_INPUT_CAR_COMMANDS.format(car_name=car_name))
            commands_str = self.io_handler.input_handler()
            is_valid, commands = validate_car_commands(commands_str)
            if not is_valid:
                self.io_handler.output_handler(msg.MSG_OUTPUT_CAR_COMMANDS_INVALID)
            else:
                is_valid_car_commands = True
        return commands

    def _input_selection(self, menu_str) -> str:
        """Input selection from the menu."""
        is_valid_selection = False
        selection = None
        while not is_valid_selection:
            self.io_handler.output_handler(menu_str)
            selection_str = self.io_handler.input_handler()
            is_valid, selection = validate_menu_selection(selection_str)
            if not is_valid:
                self.io_handler.output_handler(msg.MSG_SELECTION_INVALID)
            else:
                is_valid_selection = True
        return selection

    def _display_list_cars(self) -> None:
        """Display current list of cars."""
        if len(self.field.cars) > 0:
            self.io_handler.output_handler(f"{msg.MSG_LIST_CARS}\n{str(self.field)}")

    def _display_simulation_result(self) -> None:
        """Display the result after run simulation."""
        self.io_handler.output_handler(f"{msg.MSG_RESULT}\n{self.field.result}")

    def start_over(self) -> None:
        """Display menu to select start over or exit."""
        selection = self._input_selection(msg.MSG_MENU_START_OVER)
        if selection == "1":
            self.run()
        else:
            self.io_handler.output_handler(msg.MSG_GOODBYE)
