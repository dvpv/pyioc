class User:
    name: str
    id: str

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def __eq__(self, __o: object) -> bool:
        return __o.name == self.name and __o.id == self.id

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"
