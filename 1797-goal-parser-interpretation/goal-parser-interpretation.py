class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("G", "G").replace("()", "o").replace("(al)", "al")
