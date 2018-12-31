from src.AIService import AIService
from src.Console import Console
from src.GameService import GameService
from src.Repository import Repository
from src.UserService import UserService
from src.Validator import Validator


class Main:

    def __init__(self) -> None:
        super().__init__()
        userPiecesRepository = Repository()
        aiPiecesRepository = Repository()
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        userPiecesService = UserService(userPiecesRepository, validator)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        gameService = GameService(userPiecesService, aiPiecesService)
        self.console = Console(userPiecesService, aiPiecesService, gameService)

    def run(self):
        print("Hello World!")
        self.console.run()


main = Main()
main.run()
