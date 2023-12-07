from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    TYPE_ = "KneePad"
    PROTECTION = 120
    PRICE = 15.0
    INCREASE = 1.2
    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self):
        self.price *= self.INCREASE
