from typing import Protocol


class Fashion(Protocol):
    def wear(self) -> str:
        pass
    
class Naked(Fashion):
    def wear(self) -> str:
        return "Wearing nothing"
    
class FashionDecorator(Fashion):
    def __init__(self, fashion: Fashion):
        self.fashion = fashion
        
    def wear(self) -> str:
        return self.fashion.wear()
    
class Shirt(FashionDecorator):
    def wear(self) -> str:
        return f"{self.fashion.wear()} and a shirt"
    
class Pants(FashionDecorator):
    def wear(self) -> str:
        return f"{self.fashion.wear()} and pants"
    
class Shoes(FashionDecorator):
    def wear(self) -> str:
        return f"{self.fashion.wear()} and shoes"
    
naked = Naked()
shirt = Shirt(naked)
pants = Pants(shirt)
shoes = Shoes(pants)
print(shoes.wear())