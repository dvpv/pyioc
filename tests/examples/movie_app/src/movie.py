class Movie:
    @staticmethod
    def from_dict(d: dict):
        return Movie(
            title=d["title"],
            year=d["year"],
            rating=d["rating"],
        )

    def __init__(self, title: str, year: int, rating: int):
        self.__title = title
        self.__year = year
        self.__rating = rating

    def get_title(self) -> str:
        return self.__title

    def get_year(self) -> int:
        return self.__year

    def get_rating(self) -> int:
        return self.__rating
