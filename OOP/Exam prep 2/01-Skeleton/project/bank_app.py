from project.clients.base_client import BaseClient
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from typing import List


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Adult": Adult, "Student": Student}
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        self.given_loans = 0
        self.given_sum = 0
    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._find_client(client_id)
        if client._TYPE == "Student" and loan_type != "StudentLoan":
            raise Exception("Inappropriate loan type!")
        if client._TYPE == "Adult" and loan_type != "MortgageLoan":
            raise Exception("Inappropriate loan type!")
        loan = self._find_loan(loan_type)
        self.loans.remove(loan)
        client.loans.append(loan)
        self.given_loans += 1
        self.given_sum += loan.amount
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._find_client(client_id)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed = 0
        for l in self.loans:
            if l._TYPE == loan_type:
                l.increase_interest_rate()
                changed += 1
        return f"Successfully changed {changed} loans."

    def increase_clients_interest(self, min_rate: float):
        changed = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                changed += 1
        return f"Number of clients affected: {changed}."

    def get_statistics(self):
        avg = 0
        if self.clients:
            avg = sum([c.interest for c in self.clients]) / len(self.clients)
        res = f"""Active Clients: {len(self.clients)}
Total Income: {sum([c.income for c in self.clients]):.2f}
Granted Loans: {self.given_loans}, Total Sum: {self.given_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}
Average Client Interest Rate: {avg:.2f}"""
        return res

    def _find_client(self, client_id):
        res = [c for c in self.clients if client_id == c.client_id]
        if res:
            return res[0]
        return None

    def _find_loan(self, loan_type):
        res = [l for l in self.loans if loan_type == l._TYPE]
        if res:
            return res[0]
        return None
