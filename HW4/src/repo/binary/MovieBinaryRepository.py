import pickle

from src.repo.inmemory.MovieRepo import MovieRepo


class MovieBinaryRepository(MovieRepo):
    def __init__(self, fileName) -> None:
        super().__init__()
        self.__fileName = fileName
        self.__file = None

    def hasMovieWithId(self, movieId):
        self.__loadRepo()
        hasMovieWithId = super().hasMovieWithId(movieId)
        super().clean()
        return hasMovieWithId

    def addMovie(self, movie):
        self.__loadRepo()
        super().addMovie(movie)
        self.__storeRepo()
        super().clean()

    def getList(self):
        self.__loadRepo()
        movieList = super().getList()
        super().clean()
        return movieList

    def addMovieWithId(self, movie):
        self.__loadRepo()
        super().addMovieWithId(movie)
        self.__storeRepo()
        super().clean()

    def getMovieWithId(self, movieId):
        self.__loadRepo()
        movie = super().getMovieWithId(movieId)
        super().clean()
        return movie

    def removeMovieWithId(self, movieId):
        self.__loadRepo()
        super().removeMovieWithId(movieId)
        self.__storeRepo()
        super().clean()

    def updateMovieWithId(self, movieId, updatedMovie):
        self.__loadRepo()
        super().updateMovieWithId(movieId, updatedMovie)
        self.__storeRepo()
        super().clean()

    def __loadRepo(self):
        file = open(self.__fileName, "rb")
        try:
            readRepo = pickle.load(file)
        except EOFError:
            readRepo = []
        for movie in readRepo:
            super().addMovieWithId(movie)
        file.close()

    def __storeRepo(self):
        file = open(self.__fileName, "wb")
        pickle.dump(super().getList(), file)
        file.close()

    def cleanFile(self):
        file = open(self.__fileName, "wb")
        pickle.dump([], file)
        file.close()
