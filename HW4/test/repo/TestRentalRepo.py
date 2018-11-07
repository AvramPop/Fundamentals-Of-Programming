from unittest import TestCase

from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo


class TestRentalRepo(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(Movie("Titanic", "lovely", "Romance"))
        self.movieRepo.addMovie(Movie("Avatar", "lovely1", "Romance1"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(Client("dani"))
        self.clientRepo.addClient(Client("ancu"))
        self.rentalRepo = RentalRepo()
        self.rentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020)))

    def tearDown(self):
        self.rentalRepo = None
        self.clientRepo = None
        self.movieRepo = None  # TODO be sure it clears everything, be sure don't have residual values when populating

    def test_uniqueInstance(self):
        testRentalRepo = RentalRepo()
        self.assertEqual(self.rentalRepo.getRentalList(), testRentalRepo.getRentalList())
        testRentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021)))
        self.assertEqual(self.rentalRepo.getRentalList(), testRentalRepo.getRentalList())
        testRentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2022)))
        self.assertEqual(self.rentalRepo.getRentalList(), testRentalRepo.getRentalList())

    def test_addRental(self):
        self.rentalRepo.addRental(Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020)))
        self.assertEqual((self.rentalRepo.getRentalList()[0]).getRentalId(), 0)
        self.assertEqual((self.rentalRepo.getRentalList()[0]).getMovieId(), 0)
        self.assertEqual((self.rentalRepo.getRentalList()[0]).getClientId(), 0)
        self.assertEqual((self.rentalRepo.getRentalList()[0]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getRentalList()[0]).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalRepo.getRentalList()[1]).getRentalId(), 1)
        self.assertEqual((self.rentalRepo.getRentalList()[1]).getMovieId(), 1)
        self.assertEqual((self.rentalRepo.getRentalList()[1]).getClientId(), 1)
        self.assertEqual((self.rentalRepo.getRentalList()[1]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getRentalList()[1]).getDueDate(), Date(7, 9, 2020))
        with self.assertRaises(TypeError):
            (self.rentalRepo.getRentalList()[0]).getReturnedDate()
        testRentalRepo = RentalRepo()
        self.assertEqual((testRentalRepo.getRentalList()[0]).getRentalId(), 0)
        self.assertEqual((testRentalRepo.getRentalList()[0]).getMovieId(), 0)
        self.assertEqual((testRentalRepo.getRentalList()[0]).getClientId(), 0)
        self.assertEqual((testRentalRepo.getRentalList()[0]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((testRentalRepo.getRentalList()[0]).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((testRentalRepo.getRentalList()[1]).getRentalId(), 1)
        self.assertEqual((testRentalRepo.getRentalList()[1]).getMovieId(), 1)
        self.assertEqual((testRentalRepo.getRentalList()[1]).getClientId(), 1)
        self.assertEqual((testRentalRepo.getRentalList()[1]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((testRentalRepo.getRentalList()[1]).getDueDate(), Date(7, 9, 2020))
        print(str(self.rentalRepo.getRentalList()[1]))
        with self.assertRaises(TypeError):
            self.rentalRepo.addRental("dfsaas")
