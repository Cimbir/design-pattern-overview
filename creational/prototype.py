from typing import Protocol


class Prototype(Protocol):
    def clone(self) -> 'Prototype':
        pass
    
class Plant(Prototype):
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
        
    def __init__(self, plant: 'Plant') -> None:
        self.name = plant.name
        self.color = plant.color
        
    def clone(self) -> 'Plant':
        return Plant(self.name, self.color)
    
class Tree(Plant):
    def __init__(self, name: str, color: str, height: int) -> None:
        super().__init__(name, color)
        self.height = height
        
    def __init__(self, tree: 'Tree') -> None:
        super().__init__(tree)
        self.height = tree.height
        
    def clone(self) -> 'Tree':
        return Tree(self)
    
class Bush(Plant):
    def __init__(self, name: str, color: str, width: int) -> None:
        super().__init__(name, color)
        self.width = width
        
    def __init__(self, bush: 'Bush') -> None:
        super().__init__(bush)
        self.width = bush.width
        
    def clone(self) -> 'Bush':
        return Bush(self)
    

class Garden:
    def __init__(self) -> None:
        self.plants = []
        
    def add_plant(self, plant: Prototype) -> None:
        self.plants.append(plant.clone())
        
    def reuse_garden(self) -> list[Plant]:
        return [plant.clone() for plant in self.plants]
    
    
garden = Garden()
garden.add_plant(Plant("Rose", "Red"))
garden.add_plant(Tree("Oak", "Green", 10))
garden.add_plant(Bush("Rose", "Red", 5))
reused = garden.reuse_garden()
print(reused)
reused[0].name = "Lily"
print(reused)

reused = garden.reuse_garden()
print(reused)