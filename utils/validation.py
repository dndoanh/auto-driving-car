import utils.constants as consts


def validate_field_width_height(field_xy_str: str) -> tuple:
    """Validate the width and height of the field.
    Args:
        field_xy_str (str): the width and height of the field in x y format.
    Returns:
         (tuple) the value to indicate whether the width and height of the field is valid or not.
    """
    if not field_xy_str:
        return False, None, None
    field_xy = field_xy_str.split()
    if len(field_xy) != 2:
        return False, None, None
    try:
        field_x, field_y = int(field_xy[0]), int(field_xy[1])
        if field_x <= 0 or field_y <= 0:
            return False, None, None
        return True, field_x, field_y
    except ValueError:
        return False, None, None


def validate_car_name(name_str: str) -> tuple:
    """Validate the name of the car.
    Args:
        name_str (str): given input string
    Returns:
        (tuple) the value to indicate the name of the car is valid or not.
    """
    if name_str is None:
        return False, None
    name_str = name_str.strip()
    return (True, name_str) if name_str != "" else (False, None)


def validate_car_position_direction(position_direction_str: str) -> tuple:
    """Validate the position and direction of the car.
    Args:
        position_direction_str (str): given input string
    Returns:
        (tuple) the value to indicate the position and direction of the car is valid or not.
    """
    if position_direction_str is None:
        return False, None, None, None
    position_direction = position_direction_str.split()
    if len(position_direction) != 3:
        return False, None, None, None
    try:
        x, y, direction = int(position_direction[0]), int(position_direction[1]), position_direction[2]
        if x < 0 or y < 0:
            return False, None, None, None
        if direction not in [consts.DIRECTION_NORTH, consts.DIRECTION_EAST, consts.DIRECTION_SOUTH, consts.DIRECTION_WEST]:
            return False, None, None, None
        return True, x, y, direction
    except ValueError:
        return False, None, None, None


def validate_car_commands(commands_str: str) -> tuple:
    """Validate the commands of the car.
    Args:
        commands_str (str): given input string
    Returns:
        (tuple) the value to indicate the commands of the car is valid or not.
    """
    if commands_str is None or commands_str == "":
        return False, None
    commands = [c for c in list(commands_str) if c not in [consts.COMMAND_LEFT, consts.COMMAND_RIGHT, consts.COMMAND_FORWARD]]
    return (False, None) if any(commands) else (True, commands_str)


def validate_menu_selection(selection_str: str) -> tuple:
    """Validate selection  of the menu.
    Args:
        selection_str (str): given input string
    Returns:
        (tuple) the value to indicate the selection of the menu is valid or not.
    """
    if selection_str is None or selection_str == "":
        return False, None
    return (True, selection_str) if selection_str in ["1", "2"] else (False, None)
