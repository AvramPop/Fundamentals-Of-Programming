from main.Exception import MovieCurrentlyRentedException
from main.Utils import stringsPartiallyMatch
from main.repo.MovieRepo import MovieRepo


class MovieController:

    def __init__(self, movieRepo) -> None:
        self.__movieRepo = movieRepo

    def getRepo(self):
        """
        Get controller's repo
        """
        return self.__movieRepo

    def addMovieWithId(self, movie):
        """
        Add movie to controller
        """
        self.__movieRepo.addMovieWithId(movie)

    def addMovie(self, movie):
        """
        Add movie to controller
        """
        self.__movieRepo.addMovie(movie)

    def getMovieWithId(self, movieId):
        return self.__movieRepo.getMovieWithId(movieId)

    def hasMovieWithId(self, movieId):
        return self.__movieRepo.hasMovieWithId(movieId)

    def getMovieList(self):
        return self.__movieRepo.getList()

    def removeMovieWithId(self, movieId, rentalRepo):
        if not self.__isMovieRented(movieId, rentalRepo):
            self.__movieRepo.removeMovieWithId(movieId)
        else:
            raise MovieCurrentlyRentedException

    def updateMovieWithId(self, movieId, updatedMovie):
        self.__movieRepo.updateMovieWithId(movieId, updatedMovie)

    def populateRepoWithFew(self):
        self.__movieRepo.populateWithFew()

    def populateRepoWithMany(self):
        self.__movieRepo.populateWithMany()
        
    def listOfMoviesWithTitle(self, movieTitleToFind):
        """
        Get movies having title
        """
        movieListWithPartialTitleCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getTitle(), movieTitleToFind):
                movieListWithPartialTitleCorresponding.append(movie)
        return movieListWithPartialTitleCorresponding

    def listOfMoviesWithGenre(self, movieGenreToFind):
        """
        Get movies having genre
        """
        movieListWithPartialGenreCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getGenre(), movieGenreToFind):
                movieListWithPartialGenreCorresponding.append(movie)
        return movieListWithPartialGenreCorresponding

    def listOfMoviesWithDescription(self, movieDescriptionToFind):
        """
        Get movies having description
        """
        movieListWithPartialDescriptionCorresponding = []
        for movie in self.getMovieList():
            if stringsPartiallyMatch(movie.getDescription(), movieDescriptionToFind):
                movieListWithPartialDescriptionCorresponding.append(movie)
        return movieListWithPartialDescriptionCorresponding

    def __isMovieRented(self, movieId, rentalRepo):
        for rental in rentalRepo.getList():
            if rental.getMovieId() == movieId and rental.getReturnedDate() is None:
                return True
        return False

