from unittest import TestCase
from main.dao.ClientDAO import ClientDAO
from main.Exception import AlreadySetException


class TestClient(TestCase):
    def setUp(self):
        self.client = ClientDAO("Dani")

    def tearDown(self):
        self.client = None

    def test_init(self):
        with self.assertRaises(ValueError):
            testClient = ClientDAO(1)
        with self.assertRaises(ValueError):
            testClient = ClientDAO([])
        self.assertEqual(self.client.getName(), "Dani", 'client name got wrong')
        self.assertRaises(TypeError, lambda: self.client.getId(), 'default client id not None')

    def test_setClientId(self):
        self.client.setClientId(5)
        self.assertEqual(self.client.getId(), 5, "client id set wrong")

    def test_setWrongId(self):
        self.assertRaises(ValueError, lambda: self.client.setClientId(-3))
        self.assertRaises(ValueError, lambda: self.client.setClientId([]))
        self.assertRaises(ValueError, lambda: self.client.setClientId("asd"))
        self.assertRaises(ValueError, lambda: self.client.setClientId(3.5))
        self.assertRaises(ValueError, lambda: self.client.setClientId({}))

    def test_setClientIdSecondTime(self):
        self.client.setClientId(6)
        with self.assertRaises(AlreadySetException):
            self.client.setClientId(9)
