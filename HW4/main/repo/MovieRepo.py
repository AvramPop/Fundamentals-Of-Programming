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

    def populateWithFew(self):
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

    def populateWithMany(self):
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
        self.addMovie(Movie("crocodile", "out of ideas", "romance"))
        self.addMovie(Movie("belly", "adventurous", "drama"))
        self.addMovie(Movie("Allowable", "nice", "action"))
        self.addMovie(Movie("Hobby", "genial", "drama"))
        self.addMovie(Movie("Mary", "vary romantic", "romance"))
        self.addMovie(Movie("Robot", "children stuff", "children"))
        self.addMovie(Movie("Marsss", "war!", "children"))
        self.addMovie(Movie("Glutton", "adventurous", "children"))
        self.addMovie(Movie("Henry VIII", "nice", "action"))
        self.addMovie(Movie("Genial", "boring", "action"))
        self.addMovie(Movie("Appeell", "no comment", "romance"))
        self.addMovie(Movie("Android", "silence", "romance"))
        self.addMovie(Movie("A1", "out of ideas", "romance"))
        self.addMovie(Movie("A2", "adventurous", "drama"))
        self.addMovie(Movie("A3", "nice", "action"))
        self.addMovie(Movie("A4", "genial", "drama"))
        self.addMovie(Movie("A5", "vary romantic", "romance"))
        self.addMovie(Movie("A6", "children stuff", "children"))
        self.addMovie(Movie("A7", "war!", "children"))
        self.addMovie(Movie("A8", "adventurous", "children"))
        self.addMovie(Movie("A9", "nice", "action"))
        self.addMovie(Movie("A21", "boring", "action"))
        self.addMovie(Movie("A22", "no comment", "romance"))
        self.addMovie(Movie("A23", "silence", "romance"))
        self.addMovie(Movie("A24", "out of ideas", "romance"))
        self.addMovie(Movie("A25", "adventurous", "drama"))
        self.addMovie(Movie("A26", "nice", "action"))
        self.addMovie(Movie("A27", "genial", "drama"))
        self.addMovie(Movie("BY1", "vary romantic", "romance"))
        self.addMovie(Movie("BY12", "children stuff", "children"))
        self.addMovie(Movie("BY13", "war!", "children"))
        self.addMovie(Movie("BY14", "adventurous", "children"))
        self.addMovie(Movie("BY15", "nice", "action"))
        self.addMovie(Movie("BY16", "boring", "action"))
        self.addMovie(Movie("BY17", "no comment", "romance"))
        self.addMovie(Movie("BY18", "silence", "romance"))
        self.addMovie(Movie("BY9", "out of ideas", "romance"))
        self.addMovie(Movie("BY122", "adventurous", "drama"))
        self.addMovie(Movie("BY123", "nice", "action"))
        self.addMovie(Movie("BY133", "genial", "drama"))
        self.addMovie(Movie("BY144", "vary romantic", "romance"))
        self.addMovie(Movie("BY155", "children stuff", "children"))
        self.addMovie(Movie("BY166", "war!", "children"))
        self.addMovie(Movie("BY177", "adventurous", "children"))
        self.addMovie(Movie("BY188", "nice", "action"))
        self.addMovie(Movie("BY199", "boring", "action"))
        self.addMovie(Movie("BY1000", "no comment", "romance"))
        self.addMovie(Movie("MaBY1inland", "silence", "romance"))
        self.addMovie(Movie("BY~~1", "out of ideas", "romance"))

    def clean(self):
        self.__movieList = []
