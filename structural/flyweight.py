from dataclasses import dataclass


@dataclass(frozen=True)
class TreeType:
    name: str = ""
    color: str = ""
    texture: str = ""
    
class TreeTypeFactory:
    _stored_types: list[TreeType] = []
    
    def get_type(self, name: str, color: str, texture: str) -> TreeType:
        for tree_type in self._stored_types:
            if (tree_type.name == name and tree_type.color == color and tree_type.texture == texture):
                return tree_type
        new_type = TreeType(name, color, texture)
        self._stored_types.append(new_type)
        return new_type
    
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self._x = x
        self._y = y
        self._tree_type = tree_type
        
    def draw(self):
        print(f"Drawing tree at ({self._x}, {self._y}) with type {self._tree_type.name}")
        
class Forest:
    def __init__(self):
        self._trees = []
        
    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = TreeTypeFactory().get_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)
        
    def draw(self):
        for tree in self._trees:
            tree.draw()
            
forest = Forest()
forest.plant_tree(1, 2, "Oak", "Green", "Rough")
forest.plant_tree(3, 4, "Oak", "Green", "Rough")
forest.plant_tree(5, 6, "Pine", "Green", "Smooth")
forest.plant_tree(7, 8, "Pine", "Green", "Smooth")
forest.draw()