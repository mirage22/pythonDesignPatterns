# Command
# =======
# a request is wrapped under an object as command and passed
# to invoker object.

from abc import ABC


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        pass


class CommandImplementationOne(Command):
    def __init__(self, receiver):
        super().__init__(receiver)
        self.receiver = receiver

    def process(self):
        print('command one')
        self.receiver.perform_action('one')


class CommandImplementationTwo(Command):
    def __init__(self, receiver):
        super().__init__(receiver)
        self.receiver = receiver

    def process(self):
        print('command two')
        self.receiver.perform_action('two')


class Receiver:
    def perform_action(self, text):
        print('Action performed in receiver. %s' % text)


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


## Client code
receiver = Receiver()
cmdOne = CommandImplementationOne(receiver)
cmdTwo = CommandImplementationTwo(receiver)

invoker = Invoker()
invoker.command(cmdOne)
invoker.execute()

invoker.command(cmdTwo)
invoker.execute()
