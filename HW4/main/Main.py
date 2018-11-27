from main.Stack import Stack
from main.UndoRunner import UndoRunner
from main.controller.ClientController import ClientController
from main.controller.MovieController import MovieController
from main.controller.RentalController import RentalController
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Console import Console


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
