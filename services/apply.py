class ApplyService:
    def __init__(self, commands):
        self.commands = commands

    def run_commands(self):
        for command in self.commands:
            command.run()