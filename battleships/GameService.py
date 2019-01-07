class GameService:

    def __init__(self, shipRepo0, shipRepo1,
                                  hitRepo, shipValidator, hitValidator) -> None:
        self.__shipRepo0 = shipRepo0
        self.__shipRepo1 = shipRepo1
        self.__hitRepo = hitRepo
        self.__shipValidator = shipValidator
        self.__hitValidator = hitValidator
