from src.dao.MovieDAO import MovieDAO
from src.repo.inmemory.MovieRepo import MovieRepo


class MovieFileRepository(MovieRepo):

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

    def __loadFileReadMode(self):
        self.__file = open(self.__fileName, "r")

    def __loadFileWriteMode(self):
        self.__file = open(self.__fileName, "w")

    def __closeFile(self):
        self.__file.close()

    def __loadRepo(self):
        self.__loadFileReadMode()
        for line in self.__file:
            splitLine = line.split()
            movieToAdd = MovieDAO(splitLine[1], splitLine[2], splitLine[3])
            movieToAdd.setMovieId(int(splitLine[0]))
            super().addMovieWithId(movieToAdd)
        self.__closeFile()

    def __storeRepo(self):
        print("storing repo")
        self.__loadFileWriteMode()
        self.__file.write("")
        for movie in super().getList():
            self.__file.write(self.movieToString(movie))
        self.__closeFile()

    def movieToString(self, movieDAO):
        string = str(movieDAO.getId()) + " " + movieDAO.getTitle() + " " + movieDAO.getDescription() + " " + movieDAO.getGenre() + "\n"
        # print(string)
        return string

    def cleanFile(self):
        self.__loadFileWriteMode()
        self.__file.write("")
        self.__closeFile()
