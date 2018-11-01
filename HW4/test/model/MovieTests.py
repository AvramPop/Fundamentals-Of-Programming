from unittest import TestCase
from main.model.Movie import Movie


class MovieTests(TestCase):

    def setUp(self):
        self.movie = Movie("Titanic", "lovely", "romance")

    def tearDown(self):
        self.movie = None

    def test_movieTitleInitiation(self):
        self.assertEqual(self.movie.getTitle(), "Titanic", 'movie title got wrong')

    def test_movieDescriptionInitiation(self):
        self.assertEqual(self.movie.getDescription(), "lovely", 'movie description got wrong')

    def test_movieGenreInitiation(self):
        self.assertEqual(self.movie.getGenre(), "romance", 'movie genre got wrong')

    def test_defaultIdIsNone(self):
        self.assertRaises(TypeError, lambda: self.movie.getMovieId(), 'default movie id not None')

    def test_setMovieId(self):
        self.movie.setMovieId(5)
        self.assertEqual(self.movie.getMovieId(), 5, "movie id set wrong")
