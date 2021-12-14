class Player:
    counter = 0

    def __init__(
        self,
        username: str
    ) -> None:
        self.id = Player.counter
        self.username = username
        self.score = 0

        Player.counter += 1


    def __repr__(self) -> str:
        return f'You are {self.username} and your score is {self.score} points'