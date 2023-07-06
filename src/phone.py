from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim: int):
        super().__init__(name, price, quantity)
        self.__sim = sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__sim})"

    @property
    def number_of_sim(self):
        return self.__sim

    @number_of_sim.setter
    def number_of_sim(self, new):
        if new > 0 and isinstance(new, int):
            self.__sim = new
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
