from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INIT_INTEREST = 4.0
    INCREASE = 2.0
    _TYPE = "Adult"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INIT_INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INCREASE
