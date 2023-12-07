from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam
from typing import List


class Tournament:
    VALID_EQ_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQ_TYPES:
            raise Exception("Invalid equipment type!")
        new_eq = self.VALID_EQ_TYPES[equipment_type]()
        self.equipment.append(new_eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self._find_team_by_name(team_name)
        eq = self._find_last_equipment_by_type(equipment_type)
        if team.budget < eq.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(eq)
        team.equipment.append(eq)
        team.budget -= eq.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed = 0
        for eq in self.equipment:
            if eq.TYPE_ == equipment_type:
                eq.increase_price()
                changed += 1
        return f"Successfully changed {changed}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)
        if team1.TYPE_ != team2.TYPE_:
            raise Exception("Game cannot start! Team types mismatch!")
        power1 = team1.advantage + sum(x.protection for x in team1.equipment)
        power2 = team2.advantage + sum(x.protection for x in team2.equipment)
        if power1 > power2:
            winner = team1
        elif power1 < power2:
            winner = team2
        else:
            return "No winner in this game."
        winner.win()
        return f"The winner is {winner.name}."


    def _find_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if eq.TYPE_ == equipment_type]
        return collection[-1] if collection else None

    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        res = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"
        for t in sorted_teams:
            res += t.get_statistics()
        return res