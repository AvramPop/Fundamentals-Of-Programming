class MovieRepo:
    __shared_state = {}

    def __init__(self):
        self.__movieList = []
        self.__dict__ = self.__shared_state

    def hasMovieWithId(self, movieId):
        return True  # TODO rally change this please
