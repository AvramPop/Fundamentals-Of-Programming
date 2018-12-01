from unittest import TestCase

from src.Exception import ObjectNotInCollectionException
from src.dao.ClientDAO import ClientDAO
from src.repo.file.ClientFileRepository import ClientFileRepository
from src.ui.Printer import Printer


class TestClientFileRepository(TestCase):
    def setUp(self):
        self.clientFileRepository = ClientFileRepository("/home/dani/Desktop/code/faculta/Fundamentals-Of-Programming/HW4/test/repo/file/clientTest.txt")

    def tearDown(self):
        self.clientFileRepository.cleanFile()

    def test_addClient(self):
        self.clientFileRepository.addClient(ClientDAO("damo"))
        self.assertEqual(((self.clientFileRepository.getList())[0]).getId(), 0)
        self.assertEqual(((self.clientFileRepository.getList())[0]).getName(), "damo")

    def test_removeClient(self):
        self.clientFileRepository.addClient(ClientDAO("damo"))
        self.clientFileRepository.addClient(ClientDAO("ancu"))
        self.clientFileRepository.removeClientWithId(1)
        self.assertEqual(len(self.clientFileRepository.getList()), 1)
        testClient = ClientDAO("damo")
        testClient.setClientId(0)
        self.assertEqual(self.clientFileRepository.getList(), [testClient])
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientFileRepository.removeClientWithId(5)

    def test_updateClient(self):
        self.clientFileRepository.addClient(ClientDAO("damo"))
        self.clientFileRepository.addClient(ClientDAO("ancu"))
        testClient1 = ClientDAO("ancu")
        testClient1.setClientId(0)
        testClient2 = ClientDAO("ancu")
        testClient2.setClientId(1)
        self.clientFileRepository.updateClientWithId(0, ClientDAO("ancu"))
        self.assertEqual(self.clientFileRepository.getList(), [testClient1, testClient2])

    def test_getList(self):
        client1 = ClientDAO("aaa")
        client1.setClientId(1)
        client2 = ClientDAO("bb")
        client2.setClientId(2)
        client3 = ClientDAO("958")
        client3.setClientId(4)
        self.clientFileRepository.addClientWithId(client1)
        self.clientFileRepository.addClientWithId(client2)
        self.clientFileRepository.addClientWithId(client3)
        self.assertEqual(self.clientFileRepository.getList(), [client1, client2, client3])

    def test_hasClientWithId(self):
        client1 = ClientDAO("aaa")
        client1.setClientId(1)
        client2 = ClientDAO("bb")
        client2.setClientId(2)
        client3 = ClientDAO("958")
        client3.setClientId(3)
        self.clientFileRepository.addClientWithId(client1)
        self.clientFileRepository.addClientWithId(client2)
        self.clientFileRepository.addClientWithId(client3)
        self.assertEqual(self.clientFileRepository.hasClientWithId(1), True)
        self.assertEqual(self.clientFileRepository.hasClientWithId(4), False)

