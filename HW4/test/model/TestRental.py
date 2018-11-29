from unittest import TestCase

from src.Exception import DatesNotOrderedException, ObjectNotInCollectionException, AlreadySetException
from src.dao.ClientDAO import ClientDAO
from src.dao.MovieDAO import MovieDAO
from src.dao.RentalDAO import RentalDAO
from src.Date import Date
from src.repo.inmemory.ClientRepo import ClientRepo
from src.repo.inmemory.MovieRepo import MovieRepo


class TestRental(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieRepo.addMovie(MovieDAO("Titanic", "lovely", "Romance"))
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(ClientDAO("dani"))
        self.rental = RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2020), self.movieRepo, self.clientRepo)

    def tearDown(self):
        self.rental = None
        self.clientRepo = None
        self.movieRepo = None

    def test_init(self):
        self.assertEqual(self.rental.getMovieId(), 0)
        self.assertEqual(self.rental.getClientId(), 0)
        self.assertEqual(self.rental.getRentedDate(), Date(5, 4, 2018))
        self.assertEqual(self.rental.getDueDate(), Date(7, 9, 2020))
        self.assertRaises(TypeError, lambda: self.rental.getId(), 'default rental id not None')
        self.assertRaises(TypeError, lambda: self.rental.getReturnedDate(), 'default returned date not None')
        with self.assertRaises(ValueError):
            testRental = RentalDAO(0, "s", Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ValueError):
            testRental = RentalDAO(0, -5, Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ValueError):
            testRental = RentalDAO([], 0, Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ValueError):
            testRental = RentalDAO(-99, 0, Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ValueError):
            testRental = RentalDAO(0, 0, 9, Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ValueError):
            testRental = RentalDAO(0, 0, Date(22, 4, 1995), "date", self.movieRepo, self.clientRepo)
        with self.assertRaises(DatesNotOrderedException):
            testRental = RentalDAO(0, 0, Date(22, 4, 1995), Date(22, 4, 1994), self.movieRepo, self.clientRepo)
        with self.assertRaises(ObjectNotInCollectionException):
            testRental = RentalDAO(0, 1, Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)
        with self.assertRaises(ObjectNotInCollectionException):
            testRental = RentalDAO(1, 0, Date(22, 4, 1995), Date(22, 4, 1996), self.movieRepo, self.clientRepo)

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
        self.assertEqual(self.rental.getId(), 5, "rental id set wrong")

    def test_setReturnedDate(self):
        with self.assertRaises(ValueError):
            self.rental.setReturnedDate("dfsaasd")
        self.rental.setReturnedDate(Date(22, 4, 1996))
        self.assertEqual(self.rental.getReturnedDate(), Date(22, 4, 1996))

    def test_setReturnedDateSecondTime(self):
        self.rental.setReturnedDate(Date(22, 4, 1996))
        with self.assertRaises(AlreadySetException):
            self.rental.setReturnedDate(Date(22, 4, 1996))

