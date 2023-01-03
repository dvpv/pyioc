from typing import List
from src.movie import Movie
from src.movie_finder import MovieFinder
import yaml


class FileMovieFinder(MovieFinder):
    __file: str = None

    def set_file(self, file: str) -> None:
        self.__file = file

    def get_movies(self) -> List[Movie]:
        d = yaml.safe_load(open(self.__file, "r"))
        return [Movie.from_dict(movie_dict) for movie_dict in d["movies"]]
