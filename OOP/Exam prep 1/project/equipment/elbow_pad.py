from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    TYPE_ = "ElbowPad"
    PROTECTION = 90
    PRICE = 25.0
    INCREASE = 1.1
    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self):
        self.price *= self.INCREASE
