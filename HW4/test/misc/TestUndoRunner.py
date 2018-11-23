from unittest import TestCase

from main.Constants import Constants
from main.Exception import ObjectNotInCollectionException
from main.Stack import Stack
from main.UndoRunner import UndoRunner
from main.controller.ClientController import ClientController
from main.controller.MovieController import MovieController
from main.controller.RentalController import RentalController
from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class TestUndoRunner(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.movieController = MovieController(MovieRepo())
        self.clientController = ClientController(ClientRepo())
        self.rentalController = RentalController(RentalRepo())
        self.clientController.populateRepo()
        self.movieController.populateRepo()
        self.rentalController.populateRepo(self.movieController.getRepo(), self.clientController.getRepo())
        self.undoRunner = UndoRunner()
        self.printer = Printer()

    def tearDown(self):
        self.stack = None
        self.movieController = None
        self.clientController = None
        self.rentalController = None

    def test_addOppositeCommandToStack(self):
        self.undoRunner.addCommandToUndo(["add", "Dani"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "remove", "12"], "add client doesn't work")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "add", "5", "Dave"], "remove client doesn't work")
        self.undoRunner.addCommandToUndo(["update", "5", "AAA"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "update", "5", "Dave"], "update client doesn't work")
        self.undoRunner.addCommandToUndo(["add", "a", "a", "a"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "remove", "12"], "add movie doesn't work")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "add", "5", "Pluto", "war!", "children"], "remove movie doesn't work")
        self.undoRunner.addCommandToUndo(["update", "5", "a", "a", "a"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "update", "5", "Pluto", "war!", "children"], "update movie doesn't work")
        self.undoRunner.addCommandToUndo(["rent", "1", "1", "2", "2", "2055"], self.rentalController, self.stack, "rental")
        self.assertEqual(self.stack.pop(), ["rental", "remove", "11"], "rental doesn't work")
        self.undoRunner.addCommandToUndo(["return", "0", "0"], self.rentalController, self.stack, "rental")
        self.assertEqual(self.stack.pop(), ["rental", "returnedDateToNone", "0"], "return doesn't work")

    def test_undoAddClient(self):
        self.undoRunner.addCommandToUndo(["add", "Da"], self.clientController, self.stack, "client")
        self.clientController.addClient(Client("Da"))
        self.undoRunner.addCommandToUndo(["add", "Iani"], self.clientController, self.stack, "client")
        self.clientController.addClient(Client("Iani"))  # 14
        self.assertEqual(len(self.clientController.getRepo().getList()), 14)
        self.assertEqual(self.clientController.getClientWithId(13).getName(), "Iani")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getRepo().getList()), 13)
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientController.getClientWithId(13)

    def test_undoAddMovie(self):
        self.undoRunner.addCommandToUndo(["add", "a", "a", "a"], self.movieController, self.stack, "movie")
        self.movieController.addMovie(Movie("a", "a", "a"))
        self.undoRunner.addCommandToUndo(["add", "b", "b", "b"], self.movieController, self.stack, "movie")

        self.movieController.addMovie(Movie("b", "b", "b"))
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
        self.undoRunner.addCommandToUndo(["remove", "11"], self.clientController, self.stack, "client")
        self.clientController.removeClientWithId(11, self.rentalController.getRepo())
        self.assertEqual(len(self.clientController.getClientList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getClientList()), 12)
        self.assertEqual(self.clientController.getClientWithId(11).getName(), "Anisoara")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.clientController, self.stack, "client")
        self.clientController.removeClientWithId(5, self.rentalController.getRepo())
        self.assertEqual(len(self.clientController.getClientList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.clientController.getClientList()), 12)
        self.assertEqual(self.clientController.getClientWithId(5).getName(), "Dave")

    def test_undoRemoveMovie(self):
        self.undoRunner.addCommandToUndo(["remove", "11"], self.movieController, self.stack, "movie")
        self.movieController.removeMovieWithId(11, self.rentalController.getRepo())
        self.assertEqual(len(self.movieController.getMovieList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.movieController.getMovieList()), 12)
        self.assertEqual(self.movieController.getMovieWithId(11).getTitle(), "Stars")
        self.undoRunner.addCommandToUndo(["remove", "5"], self.movieController, self.stack, "movie")
        self.movieController.removeMovieWithId(5, self.rentalController.getRepo())
        self.assertEqual(len(self.movieController.getMovieList()), 11)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.movieController.getMovieList()), 12)
        self.assertEqual(self.movieController.getMovieWithId(5).getTitle(), "Pluto")

    def test_undoUpdateClient(self):
        updatedClient = Client("aaa")
        updatedClient.setClientId(0)
        self.undoRunner.addCommandToUndo(["update", "0", "aaa"], self.clientController, self.stack, "client")
        self.clientController.updateClientWithId(0, updatedClient)
        self.assertEqual(self.clientController.getClientWithId(0).getName(), "aaa")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(self.clientController.getClientWithId(0).getName(), "Dani")

    def test_undoUpdateMovie(self):
        updatedMovie = Movie("a", "a", "a")
        updatedMovie.setMovieId(0)
        self.undoRunner.addCommandToUndo(["update", "0", "a", "a", "a"], self.movieController, self.stack, "movie")

        self.movieController.updateMovieWithId(0, updatedMovie)
        self.assertEqual(self.movieController.getMovieWithId(0).getTitle(), "a")
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(self.movieController.getMovieWithId(0).getTitle(), "Titanic")

    def test_undoRent(self):
        self.undoRunner.addCommandToUndo(["rent", "1", "1", "1", "1", "2555"], self.rentalController, self.stack, "rental")

        self.rentalController.rentMovieByClientUntilDate(1, 1, Date(1, 1, 2555), self.movieController.getRepo(), self.clientController.getRepo())
        self.assertEqual(len(self.rentalController.getRentalList()), 12)
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertEqual(len(self.rentalController.getRentalList()), 11)

    def test_undoReturn(self):
        constants = Constants()
        self.undoRunner.addCommandToUndo(["return", "0", "0"], self.rentalController, self.stack, "rental")
        self.rentalController.returnMovieByClient(0, 0)
        self.assertEqual(self.rentalController.getRentalWithId(0).getReturnedDate(), constants.currentDay())
        self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.stack)
        self.assertIsNone(self.rentalController.getRentalWithId(0).getReturnedDate())
