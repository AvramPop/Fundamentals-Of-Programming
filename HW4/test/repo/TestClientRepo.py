from unittest import TestCase
from main.model.Client import Client
from main.repo.ClientRepo import ClientRepo


class TestClientRepo(TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()
        self.clientRepo.addClient(Client("dani"))

    def tearDown(self):
        self.clientRepo = None

    def test_uniqueInstance(self):
        testClientRepo = ClientRepo()
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())
        testClientRepo.addClient(Client("dani"))
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())
        testClientRepo.addClient(Client("Ancu"))
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())
