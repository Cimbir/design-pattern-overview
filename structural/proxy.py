from typing import Protocol


class Database(Protocol):
    def get_all(self) -> list[str]:
        pass
    
    def get_by_index(self, ind: int) -> str:
        pass
    
    def insert(self, data: str):
        pass
    
class DefaultDatabase(Database):
    def __init__(self):
        self.data = []
        
    def get_all(self) -> list[str]:
        return self.data
    
    def get_by_index(self, ind: int) -> str:
        return self.data[ind]
    
    def insert(self, data: str):
        self.data.append(data)
        
class DatabaseProxy(Database):
    def __init__(self, database: Database):
        self._database = database
        self._info = None
        self._should_reset = False
        
    def get_all(self) -> list[str]:
        if self._info is None or self._should_reset:
            print("Pulled")
            self._info = self._database.get_all()
            self._should_reset = False
        return self._info
    
    def get_by_index(self, ind: int) -> str:
        if self._info is None or self._should_reset:
            print("Pulled")
            self._info = self._database.get_all()
            self._should_reset = False
        return self._info[ind]
    
    def insert(self, data: str):
        print("Added")
        self._database.insert(data)
        self._should_reset = True
        
database = DefaultDatabase()
database_proxy = DatabaseProxy(database)
database_proxy.insert("Hello")
database_proxy.insert("World")
print(database_proxy.get_all())
print(database_proxy.get_by_index(0))
database_proxy.insert("!")
print(database_proxy.get_all())
print(database_proxy.get_by_index(0))
print(database_proxy.get_by_index(1))
print(database_proxy.get_by_index(2))