from unittest import TestCase

from src.Exception import ObjectNotInCollectionException
from src.dao.MovieDAO import MovieDAO
from src.repo.binary.MovieBinaryRepository import MovieBinaryRepository


class TestMovieBinaryRepository(TestCase):
    def setUp(self):
        self.movieBinaryRepository = MovieBinaryRepository("moviesTest.pickle")

    def tearDown(self):
        self.movieBinaryRepository.cleanFile()

    def test_addMovie(self):
        self.movieBinaryRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieBinaryRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(0)).getId(), 0)
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(0)).getTitle(), "dani")
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(0)).getDescription(), "great")
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(0)).getGenre(), "nice")
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(1)).getId(), 1)
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(1)).getTitle(), "titanic")
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(1)).getDescription(), "description")
        self.assertEqual((self.movieBinaryRepository.getMovieWithId(1)).getGenre(), "genre")

    def test_removeMovie(self):
        self.movieBinaryRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieBinaryRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieBinaryRepository.removeMovieWithId(1)
        self.assertEqual(len(self.movieBinaryRepository.getList()), 1)
        testMovie = MovieDAO("dani", "great", "nice")
        testMovie.setMovieId(0)
        self.assertEqual(self.movieBinaryRepository.getList(), [testMovie])
        with self.assertRaises(ObjectNotInCollectionException):
            self.movieBinaryRepository.removeMovieWithId(5)

    def test_updateMovie(self):
        self.movieBinaryRepository.addMovie(MovieDAO("dani", "great", "nice"))
        self.movieBinaryRepository.addMovie(MovieDAO("titanic", "description", "genre"))
        self.movieBinaryRepository.updateMovieWithId(0, MovieDAO("ancu", "nice", "great"))
        testMovie1 = MovieDAO("ancu", "nice", "great")
        testMovie1.setMovieId(0)
        testMovie2 = MovieDAO("titanic", "description", "genre")
        testMovie2.setMovieId(1)
        self.assertEqual(self.movieBinaryRepository.getList(), [testMovie1, testMovie2])

    def test_getList(self):
        movie1 = MovieDAO("aaa", "aaa", "aaa")
        movie1.setMovieId(1)
        movie2 = MovieDAO("bb", "bb", "bb")
        movie2.setMovieId(2)
        movie3 = MovieDAO("958", "958", "958")
        movie3.setMovieId(4)
        self.movieBinaryRepository.addMovieWithId(movie1)
        self.movieBinaryRepository.addMovieWithId(movie2)
        self.movieBinaryRepository.addMovieWithId(movie3)
        self.assertEqual(self.movieBinaryRepository.getList(), [movie1, movie2, movie3])

    def test_hasClientWithId(self):
        movie1 = MovieDAO("aaa", "aaa", "aaa")
        movie1.setMovieId(1)
        movie2 = MovieDAO("bb", "bb", "bb")
        movie2.setMovieId(2)
        movie3 = MovieDAO("958", "958", "958")
        movie3.setMovieId(3)
        self.movieBinaryRepository.addMovieWithId(movie1)
        self.movieBinaryRepository.addMovieWithId(movie2)
        self.movieBinaryRepository.addMovieWithId(movie3)
        self.assertEqual(self.movieBinaryRepository.hasMovieWithId(1), True)
        self.assertEqual(self.movieBinaryRepository.hasMovieWithId(4), False)




