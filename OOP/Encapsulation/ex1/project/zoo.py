class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum([w.salary for w in self.workers])
        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = sum([a.money_for_care for a in self.animals])
        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(repr(animal))
        res = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        res.extend(lions)
        res.append(f"----- {len(tigers)} Tigers:")
        res.extend(tigers)
        res.append(f"----- {len(cheetahs)} Cheetahs:")
        res.extend(cheetahs)
        return "\n".join(res)

    def workers_status(self):
        res = [f"You have {len(self.workers)} workers"]
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            if worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            if worker.__class__.__name__ == "Vet":
                vets.append(repr(worker))
        res.append(f"----- {len(keepers)} Keepers:")
        res.extend(keepers)
        res.append(f"----- {len(caretakers)} Caretakers:")
        res.extend(caretakers)
        res.append(f"----- {len(vets)} Vets:")
        res.extend(vets)
        return "\n".join(res)
