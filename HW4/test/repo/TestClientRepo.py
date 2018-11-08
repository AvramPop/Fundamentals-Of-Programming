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
        self.assertEqual(self.clientRepo.getList(), testClientRepo.getList())
        testClientRepo.addClient(Client("bani"))
        self.assertEqual(self.clientRepo.getList(), testClientRepo.getList())
        testClientRepo.addClient(Client("Ancu"))
        self.assertEqual(self.clientRepo.getList(), testClientRepo.getList())

    def test_addClient(self):
        self.clientRepo.addClient(Client("damo"))
        self.assertEqual(((self.clientRepo.getList())[0]).getClientId(), 0)
        self.assertEqual(((self.clientRepo.getList())[0]).getName(), "damo")
        testClientRepo = ClientRepo()
        self.assertEqual(((testClientRepo.getList())[0]).getClientId(), 0)
        self.assertEqual(((testClientRepo.getList())[0]).getName(), "damo")
        with self.assertRaises(TypeError):
            self.clientRepo.addClient([])

    def test_removeClient(self):
        self.clientRepo.removeClientWithId(0)
        self.assertEqual(len(self.clientRepo.getList()), 0)
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientRepo.removeClientWithId(5)

    def test_updateMovie(self):
        testClient1 = Client("ancu")
        testClient1.setClientId(0)
        testClient2 = Client("Ancu")
        testClient2.setClientId(1)
        self.clientRepo.updateClientWithId(0, Client("ancu"))
        self.assertEqual(self.clientRepo.getList(), [testClient1, testClient2])
