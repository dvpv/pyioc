from src.movie_finder import MovieFinder


class MovieLister:
    __finder: MovieFinder = None

    def set_finder(self, finder: MovieFinder) -> None:
        self.__finder = finder

    def list_movies(self) -> None:
        movies = self.__finder.get_movies()
        for movie in movies:
            print(
                f"{movie.get_title()}({movie.get_year()}), rating: {movie.get_rating()*'*'}"
            )
