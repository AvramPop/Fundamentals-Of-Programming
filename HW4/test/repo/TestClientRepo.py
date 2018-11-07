from unittest import TestCase

from main.Exception import ObjectNotInCollectionException
from main.model.Client import Client
from main.repo.ClientRepo import ClientRepo


class TestClientRepo(TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()

    def tearDown(self):
        self.clientRepo = None

    def test_uniqueInstance(self):
        testClientRepo = ClientRepo()
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())
        testClientRepo.addClient(Client("bani"))
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())
        testClientRepo.addClient(Client("Ancu"))
        self.assertEqual(self.clientRepo.getClientList(), testClientRepo.getClientList())

    def test_addClient(self):
        self.clientRepo.addClient(Client("damo"))
        self.assertEqual(((self.clientRepo.getClientList())[0]).getClientId(), 0)
        self.assertEqual(((self.clientRepo.getClientList())[0]).getName(), "damo")
        testClientRepo = ClientRepo()
        self.assertEqual(((testClientRepo.getClientList())[0]).getClientId(), 0)
        self.assertEqual(((testClientRepo.getClientList())[0]).getName(), "damo")
        with self.assertRaises(TypeError):
            self.clientRepo.addClient([])

    def test_removeClient(self):
        self.clientRepo.removeClientWithId(0)
        self.assertEqual(len(self.clientRepo.getClientList()), 0)
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientRepo.removeClientWithId(5)

    def test_updateMovie(self):
        self.clientRepo.printClientList()
        testClient1 = Client("ancu")
        testClient1.setClientId(0)
        testClient2 = Client("Ancu")
        testClient2.setClientId(1)
        self.clientRepo.updateClientWithId(0, Client("ancu"))
        self.clientRepo.printClientList()
        self.assertEqual(self.clientRepo.getClientList(), [testClient1, testClient2])
