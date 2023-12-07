from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500.0
    ADVANTAGE = 145
    TYPE_ = "IndoorTeam"
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.wins += 1
        self.advantage += self.ADVANTAGE
