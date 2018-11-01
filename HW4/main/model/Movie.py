class Movie:
    """
    Models a movie having a <movieId> (int), <title> (string),
    <description> (string) and <genre> (string)
    """

    def __init__(self, title, description, genre) -> None:
        self.__movieId = None

        try:
            self.__title = str(title)
        except ValueError as ve:
            raise ve

        try:
            self.__description = str(description)
        except ValueError as ve:
            raise ve

        try:
            self.__genre = str(genre)
        except ValueError as ve:
            raise ve

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
        if type(movieId) != int or movieId <= 0:
            raise ValueError("invalid id")
        else:
            self.__movieId = movieId
