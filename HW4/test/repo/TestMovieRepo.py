from unittest import TestCase

from main.Exception import ObjectNotInCollectionException
from main.dao.MovieDAO import MovieDAO
from main.repo.MovieRepo import MovieRepo
from main.ui.Printer import Printer


class TestMovieRepo(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()

    def tearDown(self):
        self.movieRepo.clean()

    def test_addMovie(self):
        self.movieRepo.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieRepo.addMovie(MovieDAO("titanic", "description", "genre"))
        self.assertEqual((self.movieRepo.getList()[0]).getId(), 0)
        self.assertEqual((self.movieRepo.getList()[0]).getTitle(), "dani")
        self.assertEqual((self.movieRepo.getList()[0]).getDescription(), "great")
        self.assertEqual((self.movieRepo.getList()[0]).getGenre(), "nice")
        self.assertEqual((self.movieRepo.getList()[1]).getId(), 1)
        self.assertEqual((self.movieRepo.getList()[1]).getTitle(), "titanic")
        self.assertEqual((self.movieRepo.getList()[1]).getDescription(), "description")
        self.assertEqual((self.movieRepo.getList()[1]).getGenre(), "genre")

    def test_removeMovie(self):
        self.movieRepo.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieRepo.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieRepo.removeMovieWithId(1)
        self.assertEqual(len(self.movieRepo.getList()), 1)
        testMovie = MovieDAO("dani", "great", "nice")
        testMovie.setMovieId(0)
        self.assertEqual(self.movieRepo.getList(), [testMovie])
        with self.assertRaises(ObjectNotInCollectionException):
            self.movieRepo.removeMovieWithId(5)

    def test_updateMovie(self):
        self.movieRepo.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieRepo.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieRepo.updateMovieWithId(0, MovieDAO("ancu", "nice", "great"))
        testMovie1 = MovieDAO("ancu", "nice", "great")
        testMovie1.setMovieId(0)
        testMovie2 = MovieDAO("titanic", "description", "genre")
        testMovie2.setMovieId(1)
        self.assertEqual(self.movieRepo.getList(), [testMovie1, testMovie2])


