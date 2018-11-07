from unittest import TestCase

from main.Exception import DatesNotOrderedException, ObjectNotInCollectionException, AlreadySetException
from main.model.Client import Client
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.model.Date import Date
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo


class TestRental(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(Movie("Titanic", "lovely", "Romance"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(Client("dani"))
        self.rental = Rental(0, 0, Date(5, 4, 2018), Date(7, 9, 2020))

    def tearDown(self):
        self.rental = None
        self.clientRepo = None
        self.movieRepo = None  # TODO be sure it clears everything, be sure don't have residual values when populating

    def test_init(self):
        self.assertEqual(self.rental.getMovieId(), 0)
        self.assertEqual(self.rental.getClientId(), 0)
        self.assertEqual(self.rental.getRentedDate(), Date(5, 4, 2018))
        self.assertEqual(self.rental.getDueDate(), Date(7, 9, 2020))
        self.assertRaises(TypeError, lambda: self.rental.getRentalId(), 'default rental id not None')
        self.assertRaises(TypeError, lambda: self.rental.getReturnedDate(), 'default returned date not None')
        with self.assertRaises(ValueError):
            testRental = Rental("s", 0, Date(22, 4, 1995), Date(22, 4, 1996))
        with self.assertRaises(ValueError):
            testRental = Rental(-5, 0, Date(22, 4, 1995), Date(22, 4, 1996))
        with self.assertRaises(ValueError):
            testRental = Rental(0, [], Date(22, 4, 1995), Date(22, 4, 1996))
        with self.assertRaises(ValueError):
            testRental = Rental(0, -99, Date(22, 4, 1995), Date(22, 4, 1996))
        with self.assertRaises(ValueError):
            testRental = Rental(0, 0, 9, Date(22, 4, 1996))
        with self.assertRaises(ValueError):
            testRental = Rental(0, 0, Date(22, 4, 1995), "date")
        with self.assertRaises(DatesNotOrderedException):
            testRental = Rental(0, 0, Date(22, 4, 1995), Date(22, 4, 1994))
        with self.assertRaises(ObjectNotInCollectionException):
            testRental = Rental(1, 0, Date(22, 4, 1995), Date(22, 4, 1996))
        with self.assertRaises(ObjectNotInCollectionException):
            testRental = Rental(0, 1, Date(22, 4, 1995), Date(22, 4, 1996))

    def test_setWrongId(self):
        self.assertRaises(ValueError, lambda: self.rental.setRentalId(-3))
        self.assertRaises(ValueError, lambda: self.rental.setRentalId(5.5))
        self.assertRaises(ValueError, lambda: self.rental.setRentalId("dasas"))
        self.assertRaises(ValueError, lambda: self.rental.setRentalId([]))
        self.assertRaises(ValueError, lambda: self.rental.setRentalId({}))
        self.assertRaises(ValueError, lambda: self.rental.setRentalId((5, 3)))

    def test_setRentalIdSecondTime(self):
        self.rental.setRentalId(5)
        with self.assertRaises(AlreadySetException):
            self.rental.setRentalId(9)

    def test_setRentalId(self):
        with self.assertRaises(ValueError):
            self.rental.setRentalId(-9)
        with self.assertRaises(ValueError):
            self.rental.setRentalId("dsaa")
        self.rental.setRentalId(5)
        self.assertEqual(self.rental.getRentalId(), 5, "rental id set wrong")

    def test_setReturnedDate(self):
        with self.assertRaises(ValueError):
            self.rental.setReturnedDate("dfsaasd")
        self.rental.setReturnedDate(Date(22, 4, 1996))
        self.assertEqual(self.rental.getReturnedDate(), Date(22, 4, 1996))

    def test_setReturnedDateSecondTime(self):
        self.rental.setReturnedDate(Date(22, 4, 1996))
        with self.assertRaises(AlreadySetException):
            self.rental.setReturnedDate(Date(22, 4, 1996))

