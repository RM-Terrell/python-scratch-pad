# --- Sample functions ---
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def get_status_code(status):
    if status == "OK":
        return 200
    return 404


def negative(input_number: int) -> int:
    if input_number == 0:
        return 0
    elif input_number < 0:
        return input_number
    else:
        return input_number * -1


# -------------------------
