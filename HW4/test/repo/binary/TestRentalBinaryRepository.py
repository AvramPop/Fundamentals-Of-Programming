from unittest import TestCase

from src.Date import Date
from src.dao.RentalDAO import RentalDAO
from src.repo.binary.RentalBinaryRepository import RentalBinaryRepository


class TestRentalBinaryRepository(TestCase):
    def setUp(self):
        self.rentalBinaryRepository = RentalBinaryRepository("rentalsTest.pickle")

    def tearDown(self):
        self.rentalBinaryRepository.cleanFile()

    def test_addRental(self):
        rental0 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental0.setReturnedDate(Date(5, 7, 55555))
        self.rentalBinaryRepository.addRental(rental0)
        rental = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental.setRentalId(2)
        self.rentalBinaryRepository.addRentalWithId(rental)
        rental2 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental2.setRentalId(1)
        rental2.setReturnedDate(Date(5, 7, 55555))
        self.rentalBinaryRepository.addRentalWithId(rental2)
        self.assertEqual(len(self.rentalBinaryRepository.getList()), 3)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getId(), 0)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getMovieId(), 2)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getClientId(), 1)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(0)).getReturnedDate(), Date(5, 7, 55555))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(2)).getId(), 2)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(2)).getMovieId(), 2)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(2)).getClientId(), 1)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(2)).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(2)).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getId(), 1)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getMovieId(), 2)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getClientId(), 1)
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getRentedDate(), Date(5, 4, 2018))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getDueDate(), Date(7, 9, 2020))
        self.assertEqual((self.rentalBinaryRepository.getRentalWithId(1)).getReturnedDate(), Date(5, 7, 55555))

    def test_removeRental(self):
        rental = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental.setRentalId(2)
        self.rentalBinaryRepository.addRentalWithId(rental)
        self.rentalBinaryRepository.removeRentalWithId(2)
        self.assertEqual(len(self.rentalBinaryRepository.getList()), 0)

    def test_updateRental(self):
        rental = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        self.rentalBinaryRepository.addRental(rental)
        self.rentalBinaryRepository.updateRentalWithId(0, RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2021)))
        testRental1 = RentalDAO(0, 0, Date(5, 4, 2018), Date(7, 9, 2021))
        testRental1.setRentalId(0)
        self.assertEqual(self.rentalBinaryRepository.getList(), [testRental1])

    def test_getList(self):
        rental1 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental2 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental3 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        self.rentalBinaryRepository.addRental(rental1)
        self.rentalBinaryRepository.addRental(rental2)
        self.rentalBinaryRepository.addRental(rental3)
        self.assertEqual(self.rentalBinaryRepository.getList(), [rental1, rental2, rental3])

    def test_hasClientWithId(self):
        rental1 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental2 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        rental3 = RentalDAO(1, 2, Date(5, 4, 2018), Date(7, 9, 2020))
        self.rentalBinaryRepository.addRental(rental1)
        self.rentalBinaryRepository.addRental(rental2)
        self.rentalBinaryRepository.addRental(rental3)
        self.assertEqual(self.rentalBinaryRepository.hasRentalWithId(1), True)
        self.assertEqual(self.rentalBinaryRepository.hasRentalWithId(4), False)


