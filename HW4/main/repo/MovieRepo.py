from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException


class MovieRepo:
    __shared_state = {}
    __movieList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasMovieWithId(self, movieId):
        for movie in self.__movieList:
            if movie.getMovieId() == movieId:
                return True
        return False

    def addMovie(self, movie):
        if type(movie).__name__ == 'Movie':
            if not movie.hasIdSet():
                movie.setMovieId(len(self.__movieList))
            self.__movieList.append(movie)
            self.sortMovieList()
        else:
            raise TypeError

    def getMovieList(self):
        return self.__movieList

    def getMovieWithId(self, movieId):
        for movie in self.__movieList:
            if movie.getMovieId() == movieId:
                return movie
        raise ObjectNotInCollectionException

    def removeMovieWithId(self, movieId):
        indexOfMovieToRemoveInList = -1
        for i in range(0, len(self.__movieList)):
            if (self.__movieList[i]).getMovieId() == movieId:
                indexOfMovieToRemoveInList = i

        if indexOfMovieToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__movieList[indexOfMovieToRemoveInList]

    def updateMovieWithId(self, movieId, updatedMovie):
        if updatedMovie.hasIdSet():
            if updatedMovie.getMovieId() != movieId:
                raise UpdatingObjectWithDifferentIdException

        try:
            self.removeMovieWithId(movieId)
        except ObjectNotInCollectionException as objectNotInCollectionException:
            raise objectNotInCollectionException

        if not updatedMovie.hasIdSet():
            updatedMovie.setMovieId(movieId)
        self.addMovie(updatedMovie)

    def sortMovieList(self):
        for i in range(0, len(self.__movieList) - 1):
            for j in range(i + 1, len(self.__movieList)):
                if (self.__movieList[j]).getMovieId() < self.__movieList[i].getMovieId():
                    auxMovie = self.__movieList[j]
                    self.__movieList[j] = self.__movieList[i]
                    self.__movieList[i] = auxMovie

    def printMovieList(self):
        for movie in self.__movieList:
            print(str(movie))

    def cleanMovieList(self):
        self.__movieList = []
