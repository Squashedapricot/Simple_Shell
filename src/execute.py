import subprocess


def execute_system_command(User_input):
    try:
        result = subprocess.run(
            User_input,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return result.stdout + result.stderr

    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

    except Exception as e:
        return f"Unexpected error: {str(e)}"
