from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException
from main.Utils import sortListById
from main.dao.MovieDAO import MovieDAO


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
        if type(movie).__name__ == 'MovieDAO':
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

    def getList(self):  # caution use
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
        self.addMovie(MovieDAO("Titanic", "adventurous", "drama"))
        self.addMovie(MovieDAO("Avatar", "nice", "action"))
        self.addMovie(MovieDAO("Silence", "genial", "drama"))
        self.addMovie(MovieDAO("Mars", "vary romantic", "romance"))
        self.addMovie(MovieDAO("Narnia", "children stuff", "children"))
        self.addMovie(MovieDAO("Pluto", "war!", "children"))
        self.addMovie(MovieDAO("Conrad", "adventurous", "children"))
        self.addMovie(MovieDAO("Henry", "nice", "action"))
        self.addMovie(MovieDAO("Genie", "boring", "action"))
        self.addMovie(MovieDAO("China", "no comment", "romance"))
        self.addMovie(MovieDAO("Mainland", "silence", "romance"))
        self.addMovie(MovieDAO("Stars", "out of ideas", "romance"))

    def populateWithMany(self):
        self.addMovie(MovieDAO("Titanic", "adventurous", "drama"))
        self.addMovie(MovieDAO("Avatar", "nice", "action"))
        self.addMovie(MovieDAO("Silence", "genial", "drama"))
        self.addMovie(MovieDAO("Mars", "vary romantic", "romance"))
        self.addMovie(MovieDAO("Narnia", "children stuff", "children"))
        self.addMovie(MovieDAO("Pluto", "war!", "children"))
        self.addMovie(MovieDAO("Conrad", "adventurous", "children"))
        self.addMovie(MovieDAO("Henry", "nice", "action"))
        self.addMovie(MovieDAO("Genie", "boring", "action"))
        self.addMovie(MovieDAO("China", "no comment", "romance"))
        self.addMovie(MovieDAO("Mainland", "silence", "romance"))
        self.addMovie(MovieDAO("crocodile", "out of ideas", "romance"))
        self.addMovie(MovieDAO("belly", "adventurous", "drama"))
        self.addMovie(MovieDAO("Allowable", "nice", "action"))
        self.addMovie(MovieDAO("Hobby", "genial", "drama"))
        self.addMovie(MovieDAO("Mary", "vary romantic", "romance"))
        self.addMovie(MovieDAO("Robot", "children stuff", "children"))
        self.addMovie(MovieDAO("Marsss", "war!", "children"))
        self.addMovie(MovieDAO("Glutton", "adventurous", "children"))
        self.addMovie(MovieDAO("Henry VIII", "nice", "action"))
        self.addMovie(MovieDAO("Genial", "boring", "action"))
        self.addMovie(MovieDAO("Appeell", "no comment", "romance"))
        self.addMovie(MovieDAO("Android", "silence", "romance"))
        self.addMovie(MovieDAO("A1", "out of ideas", "romance"))
        self.addMovie(MovieDAO("A2", "adventurous", "drama"))
        self.addMovie(MovieDAO("A3", "nice", "action"))
        self.addMovie(MovieDAO("A4", "genial", "drama"))
        self.addMovie(MovieDAO("A5", "vary romantic", "romance"))
        self.addMovie(MovieDAO("A6", "children stuff", "children"))
        self.addMovie(MovieDAO("A7", "war!", "children"))
        self.addMovie(MovieDAO("A8", "adventurous", "children"))
        self.addMovie(MovieDAO("A9", "nice", "action"))
        self.addMovie(MovieDAO("A21", "boring", "action"))
        self.addMovie(MovieDAO("A22", "no comment", "romance"))
        self.addMovie(MovieDAO("A23", "silence", "romance"))
        self.addMovie(MovieDAO("A24", "out of ideas", "romance"))
        self.addMovie(MovieDAO("A25", "adventurous", "drama"))
        self.addMovie(MovieDAO("A26", "nice", "action"))
        self.addMovie(MovieDAO("A27", "genial", "drama"))
        self.addMovie(MovieDAO("BY1", "vary romantic", "romance"))
        self.addMovie(MovieDAO("BY12", "children stuff", "children"))
        self.addMovie(MovieDAO("BY13", "war!", "children"))
        self.addMovie(MovieDAO("BY14", "adventurous", "children"))
        self.addMovie(MovieDAO("BY15", "nice", "action"))
        self.addMovie(MovieDAO("BY16", "boring", "action"))
        self.addMovie(MovieDAO("BY17", "no comment", "romance"))
        self.addMovie(MovieDAO("BY18", "silence", "romance"))
        self.addMovie(MovieDAO("BY9", "out of ideas", "romance"))
        self.addMovie(MovieDAO("BY122", "adventurous", "drama"))
        self.addMovie(MovieDAO("BY123", "nice", "action"))
        self.addMovie(MovieDAO("BY133", "genial", "drama"))
        self.addMovie(MovieDAO("BY144", "vary romantic", "romance"))
        self.addMovie(MovieDAO("BY155", "children stuff", "children"))
        self.addMovie(MovieDAO("BY166", "war!", "children"))
        self.addMovie(MovieDAO("BY177", "adventurous", "children"))
        self.addMovie(MovieDAO("BY188", "nice", "action"))
        self.addMovie(MovieDAO("BY199", "boring", "action"))
        self.addMovie(MovieDAO("BY1000", "no comment", "romance"))
        self.addMovie(MovieDAO("MaBY1inland", "silence", "romance"))
        self.addMovie(MovieDAO("BY~~1", "out of ideas", "romance"))

    def clean(self):
        self.__movieList = []
