from unittest import TestCase

from main.Constants import Constants
from main.Exception import DatesNotOrderedException, ClientHasMoviesNotReturnedException, MovieNotAvailableException, \
    MovieNotCurrentlyRentedByClientException
from main.controller.RentalController import RentalController
from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class TestRentalController(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(Movie("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(Movie("Avatar", "lovely1", "Romance1"))
        self.movieRepo.addMovie(Movie("TestMovie", "lovely1", "Romance1"))
        self.movieRepo.addMovie(Movie("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(Movie("Avatar", "lovely1", "Romance1"))
        self.movieRepo.addMovie(Movie("TestMovie", "lovely1", "Romance1"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(Client("dani"))
        self.clientRepo.addClient(Client("ancu"))
        self.clientRepo.addClient(Client("dani1"))
        self.clientRepo.addClient(Client("ancu1"))
        self.clientRepo.addClient(Client("dani2"))
        self.clientRepo.addClient(Client("ancu2"))
        self.rentalRepo = RentalRepo()
        self.rentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
        self.rentalRepo.addRental(Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo))
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
            Rental(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo))
        printer.printList(self.rentalController.getRepo().getList())
        with self.assertRaises(ClientHasMoviesNotReturnedException):
            self.rentalController.rentMovieByClientUntilDate(3, 3, Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        with self.assertRaises(MovieNotAvailableException):
            self.rentalController.rentMovieByClientUntilDate(0, 4, Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        self.rentalController.rentMovieByClientUntilDate(5, 5, Date(5, 5, 2025), self.movieRepo, self.clientRepo)

        # printer.printList(self.rentalController.getRepo().getList())
        rentalTest1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest1.setRentalId(0)
        rentalTest2 = Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest2.setRentalId(1)
        rentalTest3 = Rental(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo)
        rentalTest3.setRentalId(2)
        rentalTest4 = Rental(5, 5, self.constants.currentDay(), Date(5, 5, 2025), self.movieRepo, self.clientRepo)
        rentalTest4.setRentalId(3)
        self.assertEqual(self.rentalController.getRentalList(), [rentalTest1, rentalTest2, rentalTest3, rentalTest4])
        with self.assertRaises(MovieNotAvailableException):
            self.rentalController.rentMovieByClientUntilDate(5, 5, Date(5, 5, 2025), self.movieRepo, self.clientRepo)

    def test_return(self):
        printer = Printer()
        self.rentalController.getRepo().addRental(
            Rental(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo))
        printer.printList(self.rentalController.getRentalList())
        with self.assertRaises(MovieNotCurrentlyRentedByClientException):
            self.rentalController.returnMovieByClient(2, 5)
        self.rentalController.returnMovieByClient(1, 1)
        rentalTest1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest1.setRentalId(0)
        rentalTest2 = Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)
        rentalTest2.setRentalId(1)
        constants = Constants()
        rentalTest2.setReturnedDate(constants.currentDay())
        rentalTest3 = Rental(3, 4, Date(5, 4, 2012), Date(7, 9, 2013), self.movieRepo, self.clientRepo)
        rentalTest3.setRentalId(2)

        self.assertEqual(self.rentalController.getRentalList(), [rentalTest1, rentalTest2, rentalTest3])



