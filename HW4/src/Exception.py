class AlreadySetException(Exception):
    pass


class ObjectNotInCollectionException(Exception):
    pass


class ObjectAlreadyInCollectionException(Exception):
    pass


class InvalidDateFormatException(Exception):
    pass


class DatesNotOrderedException(Exception):
    pass


class UpdatingObjectWithDifferentIdException(Exception):
    pass


class ConstantNotFoundException(Exception):
    pass


class ClientHasMoviesNotReturnedException(Exception):
    pass


class IdNotSetException(Exception):
    pass


class MovieNotAvailableException(Exception):
    pass


class MovieNotCurrentlyRentedByClientException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class MovieCurrentlyRentedException(Exception):
    pass


class EmptyStackException(Exception):
    pass
