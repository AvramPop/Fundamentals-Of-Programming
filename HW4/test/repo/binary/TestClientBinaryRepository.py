from unittest import TestCase

from src.Exception import ObjectNotInCollectionException
from src.dao.ClientDAO import ClientDAO
from src.repo.binary.ClientBinaryRepository import ClientBinaryRepository


class TestClientBinaryRepository(TestCase):
    def setUp(self):
        self.clientBinaryRepository = ClientBinaryRepository("clientsTest.pickle")

    def tearDown(self):
        self.clientBinaryRepository.cleanFile()

    def test_addClient(self):
        self.clientBinaryRepository.addClient(ClientDAO("damo"))
        self.assertEqual(((self.clientBinaryRepository.getList())[0]).getId(), 0)
        self.assertEqual(((self.clientBinaryRepository.getList())[0]).getName(), "damo")

    def test_removeClient(self):
        self.clientBinaryRepository.addClient(ClientDAO("damo"))
        self.clientBinaryRepository.addClient(ClientDAO("ancu"))
        self.clientBinaryRepository.removeClientWithId(1)
        self.assertEqual(len(self.clientBinaryRepository.getList()), 1)
        testClient = ClientDAO("damo")
        testClient.setClientId(0)
        self.assertEqual(self.clientBinaryRepository.getList(), [testClient])
        with self.assertRaises(ObjectNotInCollectionException):
            self.clientBinaryRepository.removeClientWithId(5)

    def test_updateClient(self):
        self.clientBinaryRepository.addClient(ClientDAO("damo"))
        self.clientBinaryRepository.addClient(ClientDAO("ancu"))
        testClient1 = ClientDAO("ancu")
        testClient1.setClientId(0)
        testClient2 = ClientDAO("ancu")
        testClient2.setClientId(1)
        self.clientBinaryRepository.updateClientWithId(0, ClientDAO("ancu"))
        self.assertEqual(self.clientBinaryRepository.getList(), [testClient1, testClient2])

    def test_getList(self):
        client1 = ClientDAO("aaa")
        client1.setClientId(1)
        client2 = ClientDAO("bb")
        client2.setClientId(2)
        client3 = ClientDAO("958")
        client3.setClientId(4)
        self.clientBinaryRepository.addClientWithId(client1)
        self.clientBinaryRepository.addClientWithId(client2)
        self.clientBinaryRepository.addClientWithId(client3)
        self.assertEqual(self.clientBinaryRepository.getList(), [client1, client2, client3])

    def test_hasClientWithId(self):
        client1 = ClientDAO("aaa")
        client1.setClientId(1)
        client2 = ClientDAO("bb")
        client2.setClientId(2)
        client3 = ClientDAO("958")
        client3.setClientId(3)
        self.clientBinaryRepository.addClientWithId(client1)
        self.clientBinaryRepository.addClientWithId(client2)
        self.clientBinaryRepository.addClientWithId(client3)
        self.assertEqual(self.clientBinaryRepository.hasClientWithId(1), True)
        self.assertEqual(self.clientBinaryRepository.hasClientWithId(4), False)


