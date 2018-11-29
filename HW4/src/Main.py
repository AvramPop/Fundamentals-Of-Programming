from src.undo.Stack import Stack
from src.undo.UndoRunner import UndoRunner
from src.controller.ClientController import ClientController
from src.controller.MovieController import MovieController
from src.controller.RentalController import RentalController
from src.repo.inmemory.ClientRepo import ClientRepo
from src.repo.inmemory.MovieRepo import MovieRepo
from src.repo.inmemory.RentalRepo import RentalRepo
from src.ui.Console import Console


class Main:

    def __init__(self) -> None:
        self.clientController = ClientController(ClientRepo())
        self.movieController = MovieController(MovieRepo())
        self.rentalController = RentalController(RentalRepo())
        self.clientController.populateRepoWithMany()
        self.movieController.populateRepoWithMany()
        # self.movieController.populateRepoWithFew()
        # self.clientController.populateRepoWithFew()
        self.rentalController.populateRepo(self.movieController.getRepo(),
                                           self.clientController.getRepo())  # TODO do these really update as they should? remove checking seems wrong
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
