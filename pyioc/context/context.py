from abc import ABC, abstractmethod
from typing import Any


class Context(ABC):
    @abstractmethod
    def get_nut(self, id: str) -> Any:
        pass
