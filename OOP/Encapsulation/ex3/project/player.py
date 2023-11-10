class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        res = [f"Player: {self.__name}", f"Sprint: {self.__sprint}", f"Dribble: {self.__dribble}", f"Passing: {self.__passing}", f"Shooting: {self.__shooting}"]
        return "\n".join(res)

    @property
    def name(self):
        return self.__name

    @property
    def sprint(self):
        return self.__sprint

    @property
    def dribble(self):
        return self.__dribble

    @property
    def passing(self):
        return self.__passing

    @property
    def shooting(self):
        return self.__shooting
