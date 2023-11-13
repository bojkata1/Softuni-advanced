from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from typing import List


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = next(subscription for subscription in self.subscriptions if subscription_id == subscription.id)
        trainer = next(trainer for trainer in self.trainers if subscription.trainer_id == trainer.id)
        plan = next(plan for plan in self.plans if plan.id == subscription.exercise_id)
        equipment = next(equipment for equipment in self.equipment if equipment.id == plan.equipment_id)
        customer = next(customer for customer in self.customers if customer.id == subscription.customer_id)
        return repr(subscription) + "\n" + repr(customer) + "\n" + repr(trainer) + "\n" + repr(equipment) + "\n" + repr(plan)
