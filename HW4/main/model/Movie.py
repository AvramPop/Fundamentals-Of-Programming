from main.Exception import AlreadySetException


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
        """
        Return movie id

        :return movieId: the id if it is set
        :raises TypeError: if the id is not set
        """
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

    def hasIdSet(self):
        return not (self.__movieId is None)

    def setMovieId(self, movieId):
        """
        Set movieId to movieId, if not previously set. (Default None)

        :param movieId: (int > 0) the id to be set
        :raises ValueError: movieId not int > 0
        :raises SetIdNotNoneException: movieId already set
        """
        if self.__movieId is None:
            if type(movieId) != int:
                raise ValueError("invalid id")
            elif movieId < 0:
                raise ValueError
            else:
                self.__movieId = movieId
        else:
            raise AlreadySetException

    def __eq__(self, other: "Movie"):
        return self.__genre == other.getGenre() and self.__description == other.getDescription() and self.__title == other.getTitle() and self.__movieId == other.getMovieId()  # TODO id can be none and throw exception

    def __str__(self) -> str:
        return "Movie id: " + str(self.__movieId) + ", title: " + str(self.__title) + ", description: " + str(
            self.__description) + ", genre: " + str(self.__genre)
