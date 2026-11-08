class ApplyService:
    def __init__(self, commands:list):
        self.commands = commands

    def run_commands(self):
        for command in self.commands:
            command.execute()