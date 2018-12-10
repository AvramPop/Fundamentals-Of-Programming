import configparser

from src.controller.ClientController import ClientController
from src.controller.MovieController import MovieController
from src.controller.RentalController import RentalController
from src.repo.binary.ClientBinaryRepository import ClientBinaryRepository
from src.repo.binary.MovieBinaryRepository import MovieBinaryRepository
from src.repo.binary.RentalBinaryRepository import RentalBinaryRepository
from src.repo.file.ClientFileRepository import ClientFileRepository
from src.repo.file.MovieFileRepository import MovieFileRepository
from src.repo.file.RentalFileRepository import RentalFileRepository
from src.repo.inmemory.ClientRepo import ClientRepo
from src.repo.inmemory.MovieRepo import MovieRepo
from src.repo.inmemory.RentalRepo import RentalRepo
from src.ui.Console import Console
from src.undo.Stack import Stack
from src.undo.UndoRunner import UndoRunner


class Main:

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")
        if config['DEFAULT']["repository"] == "inmemory":
            self.clientController = ClientController(ClientRepo())
            self.movieController = MovieController(MovieRepo())
            self.rentalController = RentalController(RentalRepo())
            self.clientController.populateRepoWithMany()
            self.movieController.populateRepoWithMany()
            self.rentalController.populateRepo(self.movieController.getRepo(),
                                               self.clientController.getRepo())  # TODO do these really update as they should? remove checking seems wrong
        elif config['DEFAULT']["repository"] == "textfile":
            self.clientController = ClientController(ClientFileRepository(config['DEFAULT']["clients"]))
            self.movieController = MovieController(MovieFileRepository(config['DEFAULT']["movies"]))
            self.rentalController = RentalController(RentalFileRepository(config['DEFAULT']["rentals"]))
        elif config['DEFAULT']["repository"] == "binary":
            self.clientController = ClientController(ClientBinaryRepository(config['DEFAULT']["clients"]))
            self.movieController = MovieController(MovieBinaryRepository(config['DEFAULT']["movies"]))
            self.rentalController = RentalController(RentalBinaryRepository(config['DEFAULT']["rentals"]))
        self.undoStack = Stack()
        self.commandsStack = Stack()
        self.redoStack = Stack()
        self.undoRunner = UndoRunner()

    def main(self):
        console = Console(self.clientController, self.movieController, self.rentalController, self.undoStack, self.commandsStack, self.redoStack, self.undoRunner)
        console.run()
        print("bye")


main = Main()
main.main()
