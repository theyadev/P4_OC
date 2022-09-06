"""Custom input function."""


def custom_input(string: str):
    """Ask for input until answer is not empty."""
    res = None
    while not res or res == "":
        res = input(string)

    return res
