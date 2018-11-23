from unittest import TestCase

from main.Stack import Stack
from main.UndoRunner import UndoRunner
from main.controller.ClientController import ClientController
from main.controller.MovieController import MovieController
from main.controller.RentalController import RentalController
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo


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

    def tearDown(self):
        self.stack = None
        self.movieController = None
        self.clientController = None
        self.rentalController = None

    def test_addOppositeCommandToStack(self):
        self.undoRunner.addCommand(["add", "Dani"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "remove", "12"], "add client doesn't work")
        self.undoRunner.addCommand(["remove", "5"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "add", "5", "Dave"], "remove client doesn't work")
        self.undoRunner.addCommand(["update", "5", "AAA"], self.clientController, self.stack, "client")
        self.assertEqual(self.stack.pop(), ["client", "update", "5", "Dave"], "update client doesn't work")
        self.undoRunner.addCommand(["add", "a", "a", "a"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "remove", "12"], "add movie doesn't work")
        self.undoRunner.addCommand(["remove", "5"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "add", "5", "Pluto", "war!", "children"], "remove movie doesn't work")
        self.undoRunner.addCommand(["update", "5", "a", "a", "a"], self.movieController, self.stack, "movie")
        self.assertEqual(self.stack.pop(), ["movie", "update", "5", "Pluto", "war!", "children"], "update movie doesn't work")
        self.undoRunner.addCommand(["rent", "1", "1", "2", "2", "2055"], self.rentalController, self.stack, "rental")
        self.assertEqual(self.stack.pop(), ["rental", "remove", "11"], "rental doesn't work")
        self.undoRunner.addCommand(["return", "0", "0"], self.rentalController, self.stack, "rental")
        self.assertEqual(self.stack.pop(), ["rental", "returnedDateToNone", "0"], "return doesn't work")
