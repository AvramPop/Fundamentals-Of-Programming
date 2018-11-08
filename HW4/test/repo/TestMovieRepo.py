from unittest import TestCase

from main.Exception import ObjectNotInCollectionException
from main.model.Movie import Movie
from main.repo.MovieRepo import MovieRepo


class TestMovieRepo(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()

    def tearDown(self):
        self.movieRepo = None

    def test_uniqueInstance(self):
        testMovieRepo = MovieRepo()
        self.assertEqual(self.movieRepo.getList(), testMovieRepo.getList())
        testMovieRepo.addMovie(Movie("title1", "desc1", "genre1"))
        self.assertEqual(self.movieRepo.getList(), testMovieRepo.getList())
        testMovieRepo.addMovie(Movie("title2", "desc2", "genre2"))
        self.assertEqual(self.movieRepo.getList(), testMovieRepo.getList())

    def test_addMovie(self):  # TODO watchout. the repo is borg
        self.movieRepo.addMovie(Movie("dani", "great", "nice"))
        self.movieRepo.addMovie(Movie("titanic", "description", "genre"))
        self.assertEqual((self.movieRepo.getList()[0]).getMovieId(), 0)
        self.assertEqual((self.movieRepo.getList()[0]).getTitle(), "dani")
        self.assertEqual((self.movieRepo.getList()[0]).getDescription(), "great")
        self.assertEqual((self.movieRepo.getList()[0]).getGenre(), "nice")
        self.assertEqual((self.movieRepo.getList()[1]).getMovieId(), 1)
        self.assertEqual((self.movieRepo.getList()[1]).getTitle(), "titanic")
        self.assertEqual((self.movieRepo.getList()[1]).getDescription(), "description")
        self.assertEqual((self.movieRepo.getList()[1]).getGenre(), "genre")
        testMovieRepo = MovieRepo()
        self.assertEqual((testMovieRepo.getList()[0]).getMovieId(), 0)
        self.assertEqual((testMovieRepo.getList()[0]).getDescription(), "great")
        self.assertEqual((testMovieRepo.getList()[0]).getTitle(), "dani")
        self.assertEqual((testMovieRepo.getList()[0]).getGenre(), "nice")
        self.assertEqual((testMovieRepo.getList()[1]).getMovieId(), 1)
        self.assertEqual((testMovieRepo.getList()[1]).getDescription(), "description")
        self.assertEqual((testMovieRepo.getList()[1]).getTitle(), "titanic")
        self.assertEqual((testMovieRepo.getList()[1]).getGenre(), "genre")
        with self.assertRaises(TypeError):
            self.movieRepo.addMovie("sdfa")

    def test_removeMovie(self):
        self.movieRepo.removeMovieWithId(1)
        self.assertEqual(len(self.movieRepo.getList()), 1)
        with self.assertRaises(ObjectNotInCollectionException):
            self.movieRepo.removeMovieWithId(5)

    def test_updateMovie(self):
        self.movieRepo.updateMovieWithId(0, Movie("ancu", "nice", "great"))
        testMovie1 = Movie("ancu", "nice", "great")
        testMovie1.setMovieId(0)
        testMovie2 = Movie("title1", "desc1", "genre1")
        testMovie2.setMovieId(1)
        testMovie3 = Movie("title2", "desc2", "genre2")
        testMovie3.setMovieId(2)
        self.assertEqual(self.movieRepo.getList(), [testMovie1, testMovie2, testMovie3])


