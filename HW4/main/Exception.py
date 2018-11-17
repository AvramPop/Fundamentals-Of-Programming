class AlreadySetException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class ObjectNotInCollectionException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class ObjectAlreadyInCollectionException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class InvalidDateFormatException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class DatesNotOrderedException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class UpdatingObjectWithDifferentIdException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class ConstantNotFoundException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class ClientHasMoviesNotReturnedException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class IdNotSetException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class MovieNotAvailableException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class MovieNotCurrentlyRentedByClientException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class MovieCurrentlyRentedException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
