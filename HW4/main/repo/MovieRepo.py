from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException
from main.Utils import sortListById
from main.model.Movie import Movie


class MovieRepo:

    def __init__(self) -> None:
        self.__movieList = []

    def hasMovieWithId(self, movieId):
        """
        Checks whether there is a movie with movieId
        """
        for movie in self.__movieList:
            if movie.getId() == movieId:
                return True
        return False

    def addMovie(self, movie):
        """
        Add movie to repo
        """
        if type(movie).__name__ == 'Movie':
            if not self.hasMovieWithId(movie.getId()):
                movie.setMovieId(self.__maximumIndexInMovieList() + 1)
                self.__movieList.append(movie)
                # self.__sortMovieList()
                sortListById(self.__movieList)
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError

    def __maximumIndexInMovieList(self):
        maximumIndex = -1
        for movie in self.__movieList:
            if movie.getId() > maximumIndex:
                maximumIndex = movie.getId()
        return maximumIndex

    def getList(self):
        return self.__movieList

    def getMovieWithId(self, movieId):
        for movie in self.__movieList:
            if movie.getId() == movieId:
                return movie
        raise ObjectNotInCollectionException

    def removeMovieWithId(self, movieId):
        """
        Remove movie with movieId from repo
        """
        indexOfMovieToRemoveInList = -1
        for i in range(0, len(self.__movieList)):
            if (self.__movieList[i]).getId() == movieId:
                indexOfMovieToRemoveInList = i

        if indexOfMovieToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__movieList[indexOfMovieToRemoveInList]

    def updateMovieWithId(self, movieId, updatedMovie):
        """
        Update movie with movieId to updatedMovie
        """
        indexOfMovieToUpdateInList = -1
        for i in range(0, len(self.__movieList)):
            if (self.__movieList[i]).getId() == movieId:
                indexOfMovieToUpdateInList = i

        if indexOfMovieToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            if updatedMovie.getId() is None:
                updatedMovie.setMovieId(movieId)
            self.__movieList[indexOfMovieToUpdateInList] = updatedMovie

    def addMovieWithId(self, movie):
        self.__movieList.append(movie)
        sortListById(self.__movieList)

    def populateWithFew(self):  # TODO populate with many
        self.addMovie(Movie("Titanic", "adventurous", "drama"))
        self.addMovie(Movie("Avatar", "nice", "action"))
        self.addMovie(Movie("Silence", "genial", "drama"))
        self.addMovie(Movie("Mars", "vary romantic", "romance"))
        self.addMovie(Movie("Narnia", "children stuff", "children"))
        self.addMovie(Movie("Pluto", "war!", "children"))
        self.addMovie(Movie("Conrad", "adventurous", "children"))
        self.addMovie(Movie("Henry", "nice", "action"))
        self.addMovie(Movie("Genie", "boring", "action"))
        self.addMovie(Movie("China", "no comment", "romance"))
        self.addMovie(Movie("Mainland", "silence", "romance"))
        self.addMovie(Movie("Stars", "out of ideas", "romance"))

    def clean(self):
        self.__movieList = []
