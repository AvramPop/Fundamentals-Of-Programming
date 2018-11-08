from main.repo.MovieRepo import MovieRepo


class MovieController:
    __movieRepo = MovieRepo()
    __movieRepo.populate()

    def addMovie(self, movie):
        self.__movieRepo.addMovie(movie)

    def getMovieWithId(self, movieId):
        return self.__movieRepo.getMovieWithId(movieId)

    def getMovieList(self):
        return self.__movieRepo.getList()

    def removeMovieWithId(self, movieId):
        self.__movieRepo.removeMovieWithId(movieId)

    def updateMovieWithId(self, movieId, updatedMovie):
        self.__movieRepo.updateMovieWithId(movieId, updatedMovie)
