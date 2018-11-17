from unittest import TestCase

from main.controller.ClientController import ClientController
from main.repo.ClientRepo import ClientRepo


class TestClientController(TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()
        self.clientController = ClientController(self.clientRepo)

    def tearDown(self):
        self.clientRepo.clean()

    def test_addClient(self):
        pass
