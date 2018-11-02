from main.Exception import SetToNotNoneException


class Movie:
    """
    Models a movie having a <movieId> (int, default None), <title> (string),
    <description> (string) and <genre> (string)
    """

    def __init__(self, title, description, genre) -> None:
        self.__movieId = None

        if type(title) == str:
            self.__title = title
        else:
            raise ValueError

        if type(description) == str:
            self.__description = description
        else:
            raise ValueError

        if type(genre) == str:
            self.__genre = genre
        else:
            raise ValueError

    def getMovieId(self):
        movieId = self.__movieId
        if movieId is None:
            raise TypeError("movieId not set. maybe not in list")
        return movieId

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getGenre(self):
        return self.__genre

    def setMovieId(self, movieId):
        """
        Set movieId to movieId, if not previously set. (Default None)

        :param movieId: (int > 0) the id to be set
        :raises ValueError: movieId not int > 0
        :raises SetIdNotNoneException: movieId already set
        """
        if self.__movieId is None:
            if type(movieId) != int or movieId <= 0:
                raise ValueError("invalid id")
            else:
                self.__movieId = movieId
        else:
            raise SetToNotNoneException
