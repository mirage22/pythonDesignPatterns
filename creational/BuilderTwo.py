# an builder pattern example
class CommandBuilder(object):
    def __init__(self) -> None:
        self.commands = []

    def add_command(self, c):
        self.commands.append(c)
        return self

    def add_space_command(self, c):
        self.commands.append(" ")
        self.commands.append(c)
        return self

    def build(self):
        return "".join(self.commands)


def main():
    command_string = CommandBuilder().add_command("scp").add_space_command("file.txt").add_space_command("pi@0.0.0.0") \
        .add_command(":").add_command("/").build()
    print("COMMAND:" + command_string)


if __name__ == '__main__': main()
