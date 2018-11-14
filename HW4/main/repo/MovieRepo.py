from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException
from main.model.Movie import Movie


class MovieRepo:

    def __init__(self) -> None:
        self.__movieList = []

    def hasMovieWithId(self, movieId):
        """
        Checks whether there is a movie with movieId
        """
        for movie in self.__movieList:
            if movie.getMovieId() == movieId:
                return True
        return False

    def addMovie(self, movie):
        """
        Add movie to repo
        """
        if type(movie).__name__ == 'Movie':
            if not self.hasMovieWithId(movie.getMovieId()):
                movie.setMovieId(self.__maximumIndexInMovieList() + 1)
                self.__movieList.append(movie)
                self.__sortMovieList()
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError


    def __maximumIndexInMovieList(self):
        maximumIndex = -1
        for movie in self.__movieList:
            if movie.getMovieId() > maximumIndex:
                maximumIndex = movie.getMovieId()
        return maximumIndex

    def getList(self):
        return self.__movieList

    def getMovieWithId(self, movieId):
        for movie in self.__movieList:
            if movie.getMovieId() == movieId:
                return movie
        raise ObjectNotInCollectionException

    def removeMovieWithId(self, movieId):
        """
        Remove movie with movieId from repo
        """
        indexOfMovieToRemoveInList = -1
        for i in range(0, len(self.__movieList)):
            if (self.__movieList[i]).getMovieId() == movieId:
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
            if (self.__movieList[i]).getMovieId() == movieId:
                indexOfMovieToUpdateInList = i

        if indexOfMovieToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            updatedMovie.setMovieId(movieId)
            self.__movieList[indexOfMovieToUpdateInList] = updatedMovie


    def __sortMovieList(self):
        for i in range(0, len(self.__movieList) - 1):
            for j in range(i + 1, len(self.__movieList)):
                if (self.__movieList[j]).getMovieId() < self.__movieList[i].getMovieId():
                    auxMovie = self.__movieList[j]
                    self.__movieList[j] = self.__movieList[i]
                    self.__movieList[i] = auxMovie

    def populate(self):
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
