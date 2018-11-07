from unittest import TestCase
from main.model.Movie import Movie
from main.Exception import AlreadySetException


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Titanic", "lovely", "romance")

    def tearDown(self):
        self.movie = None

    def test_init(self):
        with self.assertRaises(ValueError):
            testMovie = Movie(1, "dfa", "fasd")
        with self.assertRaises(ValueError):
            testMovie = Movie("asd", [], "fasd")
        with self.assertRaises(ValueError):
            testMovie = Movie("sdf", "fsda", 6.5)
        with self.assertRaises(ValueError):
            testMovie = Movie(1, "dfa", [])
        with self.assertRaises(ValueError):
            testMovie = Movie(1, [], {"6": 5})
        self.assertEqual(self.movie.getTitle(), "Titanic", 'movie title got wrong')
        self.assertEqual(self.movie.getDescription(), "lovely", 'movie description got wrong')
        self.assertEqual(self.movie.getGenre(), "romance", 'movie genre got wrong')
        self.assertRaises(TypeError, lambda: self.movie.getMovieId(), 'default movie id not None')

    def test_setMovieId(self):
        self.movie.setMovieId(5)
        self.assertEqual(self.movie.getMovieId(), 5, "movie id set wrong")

    def test_setWrongId(self):
        self.assertRaises(ValueError, lambda: self.movie.setMovieId(-3))
        self.assertRaises(ValueError, lambda: self.movie.setMovieId(5.5))
        self.assertRaises(ValueError, lambda: self.movie.setMovieId("dasas"))
        self.assertRaises(ValueError, lambda: self.movie.setMovieId([]))
        self.assertRaises(ValueError, lambda: self.movie.setMovieId({}))
        self.assertRaises(ValueError, lambda: self.movie.setMovieId((5, 3)))

    def test_setMovieIdSecondTime(self):
        self.movie.setMovieId(5)
        with self.assertRaises(AlreadySetException):
            self.movie.setMovieId(9)
