from unittest import TestCase

from src.Constants import Constants
from src.Exception import ObjectNotInCollectionException
from src.undo.Stack import Stack
from src.undo.UndoRunner import UndoRunner
from src.controller.ClientController import ClientController
from src.controller.MovieController import MovieController
from src.controller.RentalController import RentalController
from src.dao.ClientDAO import ClientDAO
from src.Date import Date
from src.dao.MovieDAO import MovieDAO
from src.repo.inmemory.ClientRepo import ClientRepo
from src.repo.inmemory.MovieRepo import MovieRepo
from src.repo.inmemory.RentalRepo import RentalRepo
from src.ui.Printer import Printer


class TestUndoRunner(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.movieController = MovieController(MovieRepo())
        self.clientController = ClientController(ClientRepo())
        self.rentalController = RentalController(RentalRepo())
        self.clientController.populateRepoWithFew()
        self.movieController.populateRepoWithFew()
        self.rentalController.populateRepo(self.movieController.getRepo(), self.clientController.getRepo())
        self.undoRunner = UndoRunner()
        self.printer = Printer()
        self.commandsStack = Stack()

    def tearDown(self):
        self.stack = None
        self.movieController = None
        self.clientController = None
        self.rentalController = None

    def test_addOppositeCommandToStack(self):
        self.undoRunner.addCommandToUndo(["add", "Dani"], self.clientController, self.stack, "client", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["client", "remove", "12"], "add client doesn't work")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.clientController, self.stack, "client", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["client", "add", "5", "Dave"], "remove client doesn't work")
        self.undoRunner.addCommandToUndo(["update", "5", "AAA"], self.clientController, self.stack, "client", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["client", "update", "5", "Dave"], "update client doesn't work")
        self.undoRunner.addCommandToUndo(["add", "a", "a", "a"], self.movieController, self.stack, "movie", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["movie", "remove", "12"], "add movie doesn't work")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.movieController, self.stack, "movie", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["movie", "add", "5", "Pluto", "war!", "children"], "remove movie doesn't work")
        self.undoRunner.addCommandToUndo(["update", "5", "a", "a", "a"], self.movieController, self.stack, "movie", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["movie", "update", "5", "Pluto", "war!", "children"], "update movie doesn't work")
        self.undoRunner.addCommandToUndo(["rent", "1", "1", "2", "2", "2055"], self.rentalController, self.stack, "rental", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["rental", "remove", "11"], "rental doesn't work")
        self.undoRunner.addCommandToUndo(["return", "0", "0"], self.rentalController, self.stack, "rental", self.commandsStack)
        self.assertEqual(self.stack.pop(), ["rental", "returnedDateToNone", "0"], "return doesn't work")

    def test_undoAddClient(self):
        self.undoRunner.addCommandToUndo(["add", "Da"], self.clientController, self.stack, "client", self.commandsStack)
        self.clientController.addClient(ClientDAO("Da"))
        self.undoRunner.addCommandToUndo(["add", "Iani"], self.clientController, self.stack, "client", self.commandsStack)
        self.clientController.addClient(ClientDAO("Iani"))  # 14
        self.assertEqual(len(self.clientController.getRepo().getList()), 14)
        self.assertEqual(self.clientController.getClientWithId(13).getName(), "Iani")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getRepo().getList()), 13)
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientController.getClientWithId(13)

    def test_undoAddMovie(self):
        self.undoRunner.addCommandToUndo(["add", "a", "a", "a"], self.movieController, self.stack, "movie", self.commandsStack)
        self.movieController.addMovie(MovieDAO("a", "a", "a"))
        self.undoRunner.addCommandToUndo(["add", "b", "b", "b"], self.movieController, self.stack, "movie", self.commandsStack)

        self.movieController.addMovie(MovieDAO("b", "b", "b"))
        self.printer.printList(self.movieController.getMovieList())
        print()
        self.assertEqual(len(self.movieController.getRepo().getList()), 14)
        self.assertEqual(self.movieController.getMovieWithId(13).getTitle(), "b")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.printer.printList(self.movieController.getMovieList())
        self.assertEqual(len(self.movieController.getRepo().getList()), 13)
        with self.assertRaises(ObjectNotInCollectionException):
            self.movieController.getMovieWithId(13)

    def test_undoRemoveClient(self):
        self.undoRunner.addCommandToUndo(["remove", "11"], self.clientController, self.stack, "client", self.commandsStack)
        self.clientController.removeClientWithId(11, self.rentalController.getRepo())
        self.assertEqual(len(self.clientController.getClientList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getClientList()), 12)
        self.assertEqual(self.clientController.getClientWithId(11).getName(), "Anisoara")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.clientController, self.stack, "client", self.commandsStack)
        self.clientController.removeClientWithId(5, self.rentalController.getRepo())
        self.assertEqual(len(self.clientController.getClientList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getClientList()), 12)
        self.assertEqual(self.clientController.getClientWithId(5).getName(), "Dave")

    def test_undoRemoveMovie(self):
        self.undoRunner.addCommandToUndo(["remove", "11"], self.movieController, self.stack, "movie", self.commandsStack)
        self.movieController.removeMovieWithId(11, self.rentalController.getRepo())
        self.assertEqual(len(self.movieController.getMovieList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.movieController.getMovieList()), 12)
        self.assertEqual(self.movieController.getMovieWithId(11).getTitle(), "Stars")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.movieController, self.stack, "movie", self.commandsStack)
        self.movieController.removeMovieWithId(5, self.rentalController.getRepo())
        self.assertEqual(len(self.movieController.getMovieList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.movieController.getMovieList()), 12)
        self.assertEqual(self.movieController.getMovieWithId(5).getTitle(), "Pluto")

    def test_undoUpdateClient(self):
        updatedClient = ClientDAO("aaa")
        updatedClient.setClientId(0)
        self.undoRunner.addCommandToUndo(["update", "0", "aaa"], self.clientController, self.stack, "client", self.commandsStack)
        self.clientController.updateClientWithId(0, updatedClient)
        self.assertEqual(self.clientController.getClientWithId(0).getName(), "aaa")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(self.clientController.getClientWithId(0).getName(), "Dani")

    def test_undoUpdateMovie(self):
        updatedMovie = MovieDAO("a", "a", "a")
        updatedMovie.setMovieId(0)
        self.undoRunner.addCommandToUndo(["update", "0", "a", "a", "a"], self.movieController, self.stack, "movie", self.commandsStack)

        self.movieController.updateMovieWithId(0, updatedMovie)
        self.assertEqual(self.movieController.getMovieWithId(0).getTitle(), "a")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(self.movieController.getMovieWithId(0).getTitle(), "Titanic")

    def test_undoRent(self):
        self.undoRunner.addCommandToUndo(["rent", "1", "1", "1", "1", "2555"], self.rentalController, self.stack, "rental", self.commandsStack)

        self.rentalController.rentMovieByClientUntilDate(1, 1, Date(1, 1, 2555), self.movieController.getRepo(), self.clientController.getRepo())
        self.assertEqual(len(self.rentalController.getRentalList()), 12)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.rentalController.getRentalList()), 11)

    def test_undoReturn(self):
        constants = Constants()
        self.undoRunner.addCommandToUndo(["return", "0", "0"], self.rentalController, self.stack, "rental", self.commandsStack)
        self.rentalController.returnMovieByClient(0, 0)
        self.assertEqual(self.rentalController.getRentalWithId(0).getReturnedDate(), constants.currentDay())
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertIsNone(self.rentalController.getRentalWithId(0).getReturnedDate())
