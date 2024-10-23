# Basic lifetime of a shell

- **Initialize** : In this step, a typical shell would read and execute it's configuration files. These changes aspects of the shell's behaviors.

- **Interpret**: Next, the shell reads commands from stdin (which could be interactive, or a file) and executes them.
 
- **Terminate**: After its commands are executed, the executes any shutdown commands, free up any memory, and terminates

# Basic loop of a shell
- **Read**: Read the command from standard input.
- **Parse**: Separate the command string into a program and arguments,
- **Execute**: Run the parsed command.