import os
import glob


def hello():
    return "Hello! Welcome to the python shell"


def water():
    return "I like water"


def ls(patth="."):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory {path} does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access {path}.")
        return []
