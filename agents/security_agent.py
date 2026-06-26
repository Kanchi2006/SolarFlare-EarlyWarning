def validate_input(value):

    if value < 0:
        return False

    if value > 10000:
        return False

    return True