from typing import Protocol



def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b



def print_base(result: int) -> None:
    print(f"Result: {result}")
    
def print_hex(result: int) -> None:
    print(f"Result: {hex(result)}")

    

class Operator:
    def __init__(self, operation: callable, print_result: callable):
        self.operation = operation
        self.print_result = print_result
    
    def operate(self, a: int, b: int) -> None:
        self.print_result(self.operation(a, b))
        

class OperatorFactory(Protocol):
    def create_operator(self) -> Operator:
        pass
    
    
class BaseOperatorFactory(OperatorFactory):
    def __init__(self, operation: callable, print_result: callable):
        super().__init__()
        self.operation = operation
        self.print_result = print_result
    
    def create_operator(self) -> Operator:
        return Operator(self.operation, self.print_result)
    
    
    
factory = BaseOperatorFactory(add, print_base)
operator = factory.create_operator()
operator.operate(1, 2)

factory = BaseOperatorFactory(subtract, print_hex)
operator = factory.create_operator()
operator.operate(1, 2)
