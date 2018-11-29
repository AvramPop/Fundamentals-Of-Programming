from unittest import TestCase

from src.controller.ClientController import ClientController
from src.repo.inmemory.ClientRepo import ClientRepo


class TestClientController(TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()
        self.clientController = ClientController(self.clientRepo)

    def tearDown(self):
        self.clientRepo.clean()

    def test_addClient(self):
        pass
