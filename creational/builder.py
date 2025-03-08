from typing import Any, Protocol


class Mech:
    def __init__(self):
        self.extensions = []
        self.power = 0
        
    def add_extension(self, extension: str, power: int) -> None:
        self.extensions.append(extension)
        self.power += power

class MechBlueprint:
    def __init__(self):
        self.extensions = []

    def add_extension(self, extension: str) -> None:
        self.extensions.append(extension)

    def get_info(self) -> str:
        return f"Mech with {', '.join(self.extensions)} extensions"
    

class Builder(Protocol):
    def reset(self) -> None:
        pass
    
    def add_extension(self, extension: str, power: int) -> None:
        pass
    
    def get_mech(self) -> Any:
        pass
    
class MechBuilder(Builder):
    def __init__(self) -> None:
        self.mech = Mech()
        
    def reset(self) -> None:
        self.mech = Mech()
        
    def add_extension(self, extension: str, power: int) -> None:
        self.mech.add_extension(extension, power)
        
    def get_mech(self) -> Mech:
        return self.mech
    
class MechBlueprintBuilder(Builder):
    def __init__(self) -> None:
        self.blueprint = MechBlueprint()
    
    def reset(self) -> None:
        self.blueprint = MechBlueprint()
        
    def add_extension(self, extension: str, power: int) -> None:
        self.blueprint.add_extension(extension)
        
    def get_mech(self) -> MechBlueprint:
        return self.blueprint
    

class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder
        
    def construct_mech(self, extensions: list[tuple[str, int]]) -> None:
        self.builder.reset()
        for extension, power in extensions:
            self.builder.add_extension(extension, power)
            
    def get_mech(self) -> Any:
        return self.builder.get_mech()
    
    
extensions = [('laser', 10), ('rocket', 20)]
    
director = Director(MechBuilder())
director.construct_mech(extensions)
mech = director.get_mech()
print('power:',mech.power)

director = Director(MechBlueprintBuilder())
director.construct_mech(extensions)
blueprint = director.get_mech()
print(blueprint.get_info())