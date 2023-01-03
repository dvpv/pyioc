from abc import ABC, abstractmethod
from typing import List
from src.movie import Movie


class MovieFinder(ABC):
    @abstractmethod
    def get_movies(self) -> List[Movie]:
        pass
