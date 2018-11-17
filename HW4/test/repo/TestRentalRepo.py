from unittest import TestCase

from main.Exception import DatesNotOrderedException
from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class TestRentalRepo(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(Movie("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(Movie("Avatar", "lovely1", "Romance1"))
        self.movieRepo.addMovie(Movie("TestMovie", "lovely1", "Romance1"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(Client("dani"))
        self.clientRepo.addClient(Client("ancu"))
        self.rentalRepo = RentalRepo()
        self.rentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.rentalRepo.addRental(Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.printer = Printer()

    def tearDown(self):
        self.rentalRepo.clean()
        self.clientRepo.clean()
        self.movieRepo.clean()

    def test_addRental(self):
        self.rentalRepo.addRental(Rental(1, 2, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.assertEqual((self.rentalRepo.getList()[0]).getId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getClientId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getMovieId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getList()[0]).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalRepo.getList()[2]).getId(), 2)
        self.assertEqual((self.rentalRepo.getList()[2]).getMovieId(), 2)
        self.assertEqual((self.rentalRepo.getList()[2]).getClientId(), 1)
        self.assertEqual((self.rentalRepo.getList()[2]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getList()[2]).getDueDate(), Date(7, 9, 2020))

    def test_removeRental(self):
        self.rentalRepo.removeRentalWithId(1)
        self.assertEqual(len(self.rentalRepo.getList()), 1)
        testRental1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        testRental1.setRentalId(0)
        self.assertEqual(self.rentalRepo.getList(), [testRental1])

    def test_updateRental(self):
        self.rentalRepo.updateRentalWithId(0, Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021), self.movieRepo,
                                                     self.clientRepo))
        testRental1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021), self.movieRepo, self.clientRepo)
        testRental1.setRentalId(0)
        testRental2 = Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        testRental2.setRentalId(1)
        testRentalList = [testRental1, testRental2]
        self.assertEqual(self.rentalRepo.getList(), testRentalList)
