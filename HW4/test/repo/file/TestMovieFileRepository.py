from unittest import TestCase

from src.Exception import ObjectNotInCollectionException
from src.dao.MovieDAO import MovieDAO
from src.repo.file.MovieFileRepository import MovieFileRepository
from src.ui.Printer import Printer


class TestMovieFileRepository(TestCase):
    def setUp(self):
        self.movieFileRepository = MovieFileRepository("/home/dani/Desktop/code/faculta/Fundamentals-Of-Programming/HW4/test/repo/file/movieTest.txt")

    def tearDown(self):
        self.movieFileRepository.cleanFile()

    def test_addMovie(self):
        self.movieFileRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieFileRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.assertEqual((self.movieFileRepository.getList()[0]).getId(), 0)
        self.assertEqual((self.movieFileRepository.getList()[0]).getTitle(), "dani")
        self.assertEqual((self.movieFileRepository.getList()[0]).getDescription(), "great")
        self.assertEqual((self.movieFileRepository.getList()[0]).getGenre(), "nice")
        self.assertEqual((self.movieFileRepository.getList()[1]).getId(), 1)
        self.assertEqual((self.movieFileRepository.getList()[1]).getTitle(), "titanic")
        self.assertEqual((self.movieFileRepository.getList()[1]).getDescription(), "description")
        self.assertEqual((self.movieFileRepository.getList()[1]).getGenre(), "genre")

    def test_removeMovie(self):
        printer = Printer()
        self.movieFileRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieFileRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieFileRepository.removeMovieWithId(1)

        self.assertEqual(len(self.movieFileRepository.getList()), 1)
        testMovie = MovieDAO("dani", "great", "nice")
        testMovie.setMovieId(0)
        self.assertEqual(self.movieFileRepository.getList(), [testMovie])
        with self.assertRaises(ObjectNotInCollectionException):
            self.movieFileRepository.removeMovieWithId(5)

    def test_updateMovie(self):
        self.movieFileRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieFileRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieFileRepository.updateMovieWithId(0, MovieDAO("ancu", "nice", "great"))
        testMovie1 = MovieDAO("ancu", "nice", "great")
        testMovie1.setMovieId(0)
        testMovie2 = MovieDAO("titanic", "description", "genre")
        testMovie2.setMovieId(1)
        self.assertEqual(self.movieFileRepository.getList(), [testMovie1, testMovie2])

    def test_getList(self):
        movie1 = MovieDAO("aaa", "aaa", "aaa")
        movie1.setMovieId(1)
        movie2 = MovieDAO("bb", "bb", "bb")
        movie2.setMovieId(2)
        movie3 = MovieDAO("958", "958", "958")
        movie3.setMovieId(4)
        self.movieFileRepository.addMovieWithId(movie1)
        self.movieFileRepository.addMovieWithId(movie2)
        self.movieFileRepository.addMovieWithId(movie3)
        self.assertEqual(self.movieFileRepository.getList(), [movie1, movie2, movie3])

    def test_hasClientWithId(self):
        movie1 = MovieDAO("aaa", "aaa", "aaa")
        movie1.setMovieId(1)
        movie2 = MovieDAO("bb", "bb", "bb")
        movie2.setMovieId(2)
        movie3 = MovieDAO("958", "958", "958")
        movie3.setMovieId(3)
        self.movieFileRepository.addMovieWithId(movie1)
        self.movieFileRepository.addMovieWithId(movie2)
        self.movieFileRepository.addMovieWithId(movie3)
        self.assertEqual(self.movieFileRepository.hasMovieWithId(1), True)
        self.assertEqual(self.movieFileRepository.hasMovieWithId(4), False)



