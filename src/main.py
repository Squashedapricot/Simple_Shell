from execute import execute_system_command
from command_handler import handle_custom_commands


def simple_shell():
    while True:
        User_input = input("myshell> ")

        if User_input.lower() in ["exit", "quit"]:
            print("Bye.")
            break
        if handle_custom_commands(User_input):
            continue
        else:
            output = execute_system_command(User_input)
            print(output)


if __name__ == "__main__":
    simple_shell()
