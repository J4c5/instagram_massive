# logic - a class that will contain the necessary stores for Email, Email Code...etc. much faster!
# code:
def new():
    class storage:
        def __init__(self) -> None:
            self.Username = ""
            self.Name     = ""
            self.Email    = ""
            self.Pass     = ""
            self.Code     = ""
    
    return storage()

class Storage:
    def __init__(self) -> None:
        self.New = new