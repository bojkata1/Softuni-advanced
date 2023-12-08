from project.clients.base_client import BaseClient


class Student(BaseClient):
    INIT_INTEREST = 2.0
    INCREASE = 1.0
    _TYPE = "Student"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INIT_INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INCREASE
