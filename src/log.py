# logic - display logs, warnings and errors, simple.
# code:
def Log(text):
    print(f"log - {text}")

def Warning(text):
    print(f"Warning - {text}")

def Error(text):
    print("Error - {text}")
    exit(1)

class Console:
    def __init__(self) -> None:
        self.Log = Log
        self.Warning = Warning
        self.Error = Error