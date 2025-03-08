from typing import Protocol


class Item(Protocol):
    def price(self) -> float:
        pass
    
    def weight(self) -> float:
        pass
    
class Valuable(Item):
    def __init__(self, price: float, weight: float):
        self._price = price
        self._weight = weight
        
    def price(self) -> float:
        return self._price
    
    def weight(self) -> float:
        return self._weight
    
class Box(Item):
    def __init__(self):
        self.items = []
        
    def add_item(self, item: Item):
        self.items.append(item)
        
    def price(self) -> float:
        return sum(item.price() for item in self.items)
    
    def weight(self) -> float:
        return sum(item.weight() for item in self.items)
    
val1 = Valuable(10, 1)
val2 = Valuable(20, 2)
box1 = Box()
box1.add_item(val1)
box1.add_item(val2)
val3 = Valuable(30, 3)
box2 = Box()
box2.add_item(val3)
box2.add_item(box1)
print("box2 price:", box2.price())
print("box2 weight:", box2.weight())