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
        movie.setMovieId(len(self.__movieList))
        self.__movieList.append(movie)

    def getMovieList(self):
        return self.__movieList
