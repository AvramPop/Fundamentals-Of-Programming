from unittest import TestCase

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
        self.assertEqual(self.rentalRepo.getList(), testRentalRepo.getList())
        testRentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021)))
        self.assertEqual(self.rentalRepo.getList(), testRentalRepo.getList())
        testRentalRepo.addRental(Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2022)))
        self.assertEqual(self.rentalRepo.getList(), testRentalRepo.getList())

    def test_addRental(self):
        self.rentalRepo.addRental(Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020)))
        self.assertEqual((self.rentalRepo.getList()[0]).getRentalId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getMovieId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getClientId(), 0)
        self.assertEqual((self.rentalRepo.getList()[0]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getList()[0]).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalRepo.getList()[1]).getRentalId(), 1)
        self.assertEqual((self.rentalRepo.getList()[1]).getMovieId(), 1)
        self.assertEqual((self.rentalRepo.getList()[1]).getClientId(), 1)
        self.assertEqual((self.rentalRepo.getList()[1]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalRepo.getList()[1]).getDueDate(), Date(7, 9, 2020))
        testRentalRepo = RentalRepo()
        self.assertEqual((testRentalRepo.getList()[0]).getRentalId(), 0)
        self.assertEqual((testRentalRepo.getList()[0]).getMovieId(), 0)
        self.assertEqual((testRentalRepo.getList()[0]).getClientId(), 0)
        self.assertEqual((testRentalRepo.getList()[0]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((testRentalRepo.getList()[0]).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((testRentalRepo.getList()[1]).getRentalId(), 1)
        self.assertEqual((testRentalRepo.getList()[1]).getMovieId(), 1)
        self.assertEqual((testRentalRepo.getList()[1]).getClientId(), 1)
        self.assertEqual((testRentalRepo.getList()[1]).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((testRentalRepo.getList()[1]).getDueDate(), Date(7, 9, 2020))
        with self.assertRaises(TypeError):
            self.rentalRepo.addRental("dfsaas")

    def test_removeRental(self):
        self.rentalRepo.removeRentalWithId(2)
        self.assertEqual(len(self.rentalRepo.getList()), 2)
        testRental1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020))
        testRental1.setRentalId(0)
        testRental2 = Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020))
        testRental2.setRentalId(1)
        self.assertEqual(self.rentalRepo.getList(), [testRental1, testRental2])

    def test_updateRental(self):
        self.rentalRepo.updateRentalWithId(0, Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021)))
        testRental1 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021))
        testRental1.setRentalId(0)
        testRental2 = Rental(1, 1, Date(5, 4, 2018), Date(7, 9, 2020))
        testRental2.setRentalId(1)
        testRental3 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020))
        testRental3.setRentalId(2)
        testRental4 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2021))
        testRental4.setRentalId(3)
        testRental5 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2022))
        testRental5.setRentalId(4)
        testRental6 = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020))
        testRental6.setRentalId(5)
        self.assertEqual(self.rentalRepo.getList(), [testRental1, testRental2, testRental3, testRental4, testRental5, testRental6])
