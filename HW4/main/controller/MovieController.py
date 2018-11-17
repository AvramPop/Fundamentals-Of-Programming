from main.Utils import stringsPartiallyMatch
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

    def removeMovieWithId(self, movieId):   # TODO approve just if not rented
        self.__movieRepo.removeMovieWithId(movieId)

    def updateMovieWithId(self, movieId, updatedMovie):
        self.__movieRepo.updateMovieWithId(movieId, updatedMovie)

    def populateRepo(self):
        self.__movieRepo.populate()
        
    def listOfMoviesWithTitle(self, movieTitleToFind):
        movieListWithPartialTitleCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getTitle(), movieTitleToFind):
                movieListWithPartialTitleCorresponding.append(movie)
        return movieListWithPartialTitleCorresponding

    def listOfMoviesWithGenre(self, movieGenreToFind):
        movieListWithPartialGenreCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getGenre(), movieGenreToFind):
                movieListWithPartialGenreCorresponding.append(movie)
        return movieListWithPartialGenreCorresponding

    def listOfMoviesWithDescription(self, movieDescriptionToFind):
        movieListWithPartialDescriptionCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getDescription(), movieDescriptionToFind):
                movieListWithPartialDescriptionCorresponding.append(movie)
        return movieListWithPartialDescriptionCorresponding
