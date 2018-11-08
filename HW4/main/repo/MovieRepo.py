from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException
from main.model.Movie import Movie


class MovieRepo:
    __shared_state = {}
    __movieList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasMovieWithId(self, movieId):
        """
        Checks whether there is a movie with movieId
        """
        for movie in self.__movieList:
            if movie.getMovieId() == movieId:
                return True
        return False

    # def getMovieIdByTitle(self, title):
    #     for movie in self.__movieList:
    #         if movie.getTitle() == title:
    #             return movie.getMovieId()
    #     raise ObjectNotInCollectionException

    # def hasMovieWithTitle(self, title):
    #     for movie in self.__movieList:
    #         if movie.getTitle() == title:
    #             return True
    #     return False

    # def getMovieWithTitle(self, title):
    #     for movie in self.__movieList:
    #         if movie.getTitle() == title:
    #             return movie
    #     raise ObjectNotInCollectionException

    # def removeMovieWithTitle(self, title):
    #     """
    #     Removes movie with title title from repo
    #     """
    #     indexOfMovieToRemoveInList = -1
    #     for i in range(0, len(self.__movieList)):
    #         if (self.__movieList[i]).getTitle() == title:
    #             indexOfMovieToRemoveInList = i
    #
    #     if indexOfMovieToRemoveInList == -1:
    #         raise ObjectNotInCollectionException
    #     else:
    #         del self.__movieList[indexOfMovieToRemoveInList]

    # def updateMovieWithTitle(self, movieTitle, updatedMovie):
    #     """
    #     Update movie with movieTitle to updatedMovie
    #     """
    #     movieFound = False
    #     for i in range(0, len(self.__movieList)):
    #         if self.__movieList[i].getTitle() == movieTitle:
    #             movieId = self.__movieList[i].getMovieId()
    #             self.__movieList[i] = updatedMovie
    #             self.__movieList[i].setMovieId(movieId)
    #             movieFound = True
    #     if not movieFound:
    #         raise ObjectNotInCollectionException

    def addMovie(self, movie):  # TODO check unicity
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
        # if updatedMovie.hasIdSet():
        #     if updatedMovie.getMovieId() != movieId:
        #         raise UpdatingObjectWithDifferentIdException
        #
        # try:
        #     self.removeMovieWithId(movieId)
        # except ObjectNotInCollectionException as objectNotInCollectionException:
        #     raise objectNotInCollectionException
        #
        # if not updatedMovie.hasIdSet():
        #     updatedMovie.setMovieId(movieId)
        # self.addMovie(updatedMovie)

    def __sortMovieList(self):
        for i in range(0, len(self.__movieList) - 1):
            for j in range(i + 1, len(self.__movieList)):
                if (self.__movieList[j]).getMovieId() < self.__movieList[i].getMovieId():
                    auxMovie = self.__movieList[j]
                    self.__movieList[j] = self.__movieList[i]
                    self.__movieList[i] = auxMovie

    # def printMovieList(self):
    #     for movie in self.__movieList:
    #         print(str(movie))

    # def cleanMovieList(self):
    #     self.__movieList = []

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

