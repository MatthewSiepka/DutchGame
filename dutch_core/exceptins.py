class IllegalMove(NameError):
    def __init__(self, user_name, message):
        super().__init__("Move performed by " + user_name + " is illegal, move: " + message)

