from unittest import TestCase

from main.Constants import Constants
from main.Exception import DatesNotOrderedException, ClientHasMoviesNotReturnedException, MovieNotAvailableException, \
    MovieNotCurrentlyRentedByClientException
from main.controller.RentalController import RentalController
from main.dao.ClientDAO import ClientDAO
from main.Date import Date
from main.dao.MovieDAO import MovieDAO
from main.dao.RentalDAO import RentalDAO
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class TestRentalController(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(MovieDAO("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(MovieDAO("Avatar", "lovely1", "Romance1"))
        self.movieRepo.addMovie(MovieDAO("TestMovie", "lovely1", "Romance1"))
        self.movieRepo.addMovie(MovieDAO("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(MovieDAO("Avatar", "lovely1", "Romance1"))
        self.movieRepo.addMovie(MovieDAO("TestMovie", "lovely1", "Romance1"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(ClientDAO("dani"))
        self.clientRepo.addClient(ClientDAO("ancu"))
        self.clientRepo.addClient(ClientDAO("dani1"))
        self.clientRepo.addClient(ClientDAO("ancu1"))
        self.clientRepo.addClient(ClientDAO("dani2"))
        self.clientRepo.addClient(ClientDAO("ancu2"))
        self.rentalRepo = RentalRepo()
        self.rentalRepo.addRental(RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.rentalRepo.addRental(RentalDAO(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.printer = Printer()
        self.constants = Constants()
        self.rentalController = RentalController(self.rentalRepo)

    def tearDown(self):
        self.movieRepo.clean()
        self.clientRepo.clean()
        self.rentalRepo.clean()

    def test_rent(self):
        printer = Printer()
        with self.assertRaises(DatesNotOrderedException):
            self.rentalController.rentMovieByClientUntilDate(0, 0, Date(1, 1, 1999), self.movieRepo, self.clientRepo)
        self.rentalController.getRepo().addRental(
            RentalDAO(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo))
        printer.printList(self.rentalController.getRepo().getList())
        with self.assertRaises(ClientHasMoviesNotReturnedException):
            self.rentalController.rentMovieByClientUntilDate(3, 3, Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        with self.assertRaises(MovieNotAvailableException):
            self.rentalController.rentMovieByClientUntilDate(0, 4, Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        self.rentalController.rentMovieByClientUntilDate(5, 5, Date(5, 5, 2025), self.movieRepo, self.clientRepo)

        # printer.printList(self.rentalController.getRepo().getList())
        rentalTest1 = RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest1.setRentalId(0)
        rentalTest2 = RentalDAO(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest2.setRentalId(1)
        rentalTest3 = RentalDAO(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo)
        rentalTest3.setRentalId(2)
        rentalTest4 = RentalDAO(5, 5, self.constants.currentDay(), Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        rentalTest4.setRentalId(3)
        self.assertEqual(self.rentalController.getRentalList(), [rentalTest1, rentalTest2, rentalTest3, rentalTest4])
        with self.assertRaises(MovieNotAvailableException):
            self.rentalController.rentMovieByClientUntilDate(5, 5, Date(5, 5, 2025), self.movieRepo, self.clientRepo)

    def test_return(self):
        printer = Printer()
        self.rentalController.getRepo().addRental(
            RentalDAO(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo))
        printer.printList(self.rentalController.getRentalList())
        with self.assertRaises(MovieNotCurrentlyRentedByClientException):
            self.rentalController.returnMovieByClient(2, 5)
        self.rentalController.returnMovieByClient(1, 1)
        rentalTest1 = RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest1.setRentalId(0)
        rentalTest2 = RentalDAO(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest2.setRentalId(1)
        constants = Constants()
        rentalTest2.setReturnedDate(constants.currentDay())
        rentalTest3 = RentalDAO(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo)
        rentalTest3.setRentalId(2)

        self.assertEqual(self.rentalController.getRentalList(), [rentalTest1, rentalTest2, rentalTest3])



