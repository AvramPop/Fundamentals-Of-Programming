from unittest import TestCase

from main.controller.MovieController import MovieController
from main.repo.MovieRepo import MovieRepo


class TestMovieController(TestCase):
    def setUp(self):
        self.movieRepo = MovieRepo()
        self.movieController = MovieController(self.movieRepo)

    def tearDown(self):
        self.movieRepo.clean()

    def test_addMovie(self):
        pass
