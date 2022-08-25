def custom_input(string: str):
    res = None
    while not res or res == "":
        res = input(string)

    return res
