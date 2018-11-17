from unittest import TestCase

from main.Exception import ObjectNotInCollectionException
from main.model.Client import Client
from main.repo.ClientRepo import ClientRepo
from main.ui.Printer import Printer


class TestClientRepo(TestCase):
    def setUp(self):
        self.clientRepo = ClientRepo()

    def tearDown(self):
        self.clientRepo.clean()

    def test_addClient(self):
        printer = Printer()
        printer.printList(self.clientRepo.getList())
        print("aaaaaaaaaaaaaaa")
        self.clientRepo.addClient(Client("damo"))
        self.assertEqual(((self.clientRepo.getList())[0]).getId(), 0)
        self.assertEqual(((self.clientRepo.getList())[0]).getName(), "damo")

    def test_removeClient(self):
        printer = Printer()
        printer.printList(self.clientRepo.getList())
        print("bbbbb")
        self.clientRepo.addClient(Client("damo"))
        self.clientRepo.addClient(Client("ancu"))
        self.clientRepo.removeClientWithId(1)
        self.assertEqual(len(self.clientRepo.getList()), 1)
        testClient = Client("damo")
        testClient.setClientId(0)
        self.assertEqual(self.clientRepo.getList(), [testClient])
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientRepo.removeClientWithId(5)

    def test_updateClient(self):
        printer = Printer()
        printer.printList(self.clientRepo.getList())
        print("ccccccccccc")
        self.clientRepo.addClient(Client("damo"))
        self.clientRepo.addClient(Client("ancu"))
        testClient1 = Client("ancu")
        testClient1.setClientId(0)
        testClient2 = Client("ancu")
        testClient2.setClientId(1)
        self.clientRepo.updateClientWithId(0, Client("ancu"))
        self.assertEqual(self.clientRepo.getList(), [testClient1, testClient2])
