from main.repo.MovieRepo import MovieRepo


class MovieController:

    def __init__(self, movieRepo) -> None:
        self.__movieRepo = movieRepo

    def getRepo(self):
        return self.__movieRepo

    def addMovie(self, movie):
        self.__movieRepo.addMovie(movie)

    def getMovieWithId(self, movieId):
        return self.__movieRepo.getMovieWithId(movieId)

    def hasMovieWithId(self, movieId):
        return self.__movieRepo.hasMovieWithId(movieId)

    def getMovieList(self):
        return self.__movieRepo.getList()

    def removeMovieWithId(self, movieId):
        self.__movieRepo.removeMovieWithId(movieId)

    def updateMovieWithId(self, movieId, updatedMovie):
        self.__movieRepo.updateMovieWithId(movieId, updatedMovie)

    def populateRepo(self):
        self.__movieRepo.populate()
