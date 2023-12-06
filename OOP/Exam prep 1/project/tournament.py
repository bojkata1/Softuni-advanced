from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type == "KneePad":
            self.equipment.append(KneePad())
        elif equipment_type == "ElbowPad":
            self.equipment.append(ElbowPad())
        else:
            raise Exception("Invalid equipment type!")
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)
        elif team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
        else:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        for i in range(len(self.equipment)-1, -1, -1):
            if self.equipment[i].__class__.__name__ == equipment_type:
                eq = self.equipment[i]
                break
        for team in self.teams:
            if team_name == team.name:
                team_obj = team
                break
        if team_obj.budget >= eq.price:
            team_obj.budget -= eq.price
            team_obj.equipment.append(eq)
            self.equipment.remove(eq)
            return f"Successfully sold {equipment_type} to {team_obj.name}."
        else:
            raise "Budget is not enough!"

    def remove_team(self, team_name: str):
        for team in self.teams:
            if team.name == team_name:
                team = team
                break
        else:
            raise Exception("No such team!")
        if team.wins != 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team.name}."
    def increase_equipment_price(self, equipment_type: str):
        changed = 0
        for eq in self.equipment:
            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                changed += 1
        return f"Successfully changed {changed}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        for team in self.teams:
            if team.name == team_name1:
                team1 = team
            if team.name == team_name2:
                team2 = team
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        power1 = team1.advantage
        power2 = team2.advantage
        for eq in team1.equipment:
            power1 += eq.protection
        for eq in team2.equipment:
            power2 += eq.protection
        if power1 > power2:
            team1.win()
            winner = team1
        elif power1 < power2:
            team2.win()
            winner = team2
        else:
            return "No winner in this game."
        return f"The winner is {winner.name}."

    def get_statistics(self):
        res = f"Tournament: {self.name}\n" \
              f"Number of Teams: {len(self.teams)}\nTeams:\n"
        sorted_list = sorted(self.teams, key=lambda x: x.wins)
        for team in self.teams:
            res += team.get_statistics()
        return res




