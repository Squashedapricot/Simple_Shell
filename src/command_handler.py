from custom_commands import hello
from custom_commands import water


def handle_custom_commands(command):
    if command.strip().lower() == "hello":
        print(hello())
        return True
    elif command.strip().lower() == "water":
        print(water())
        return True
    return False
