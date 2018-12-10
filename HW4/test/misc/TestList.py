from unittest import TestCase

from src.List import List, sortList, filterList, sortListByObjectAttribute
from src.dao.ClientDAO import ClientDAO


class TestList(TestCase):
    def setUp(self):
        self.testList = List([5, 4, 10, 50])

    def tearDown(self):
        del self.testList

    def test_getItem(self):
        self.assertEqual(self.testList[0], 5)
        self.assertEqual(self.testList[-1], 50)
        with self.assertRaises(IndexError):
            a = self.testList[5]

    def test_setItem(self):
        self.assertEqual(self.testList[0], 5)
        self.testList[0] = 1000
        self.assertEqual(self.testList[0], 1000)
        self.assertEqual(self.testList[-1], 50)
        self.testList[-1] = 500
        self.assertEqual(self.testList[-1], 500)
        with self.assertRaises(IndexError):
            self.testList[5] = 0

    def test_equals(self):
        list1 = [5, 4, 10, 50]
        self.assertEqual(list1, self.testList)
        list1 = List([5, 4, 10, 50])
        self.assertEqual(list1, self.testList)
        list1 = {}
        self.assertNotEqual(list1, self.testList)
        list1 = [5, 4, 10]
        self.assertNotEqual(list1, self.testList)
        list1 = List([5, 4, 10, 51])
        self.assertNotEqual(list1, self.testList)

    def test_deleteItem(self):
        self.assertEqual(len(self.testList), 4)
        del self.testList[0]
        self.assertEqual(len(self.testList), 3)
        self.assertEqual(self.testList[0], 4)

    def test_iter(self):
        newList = []
        for element in self.testList:
            newList.append(element)
        self.assertEqual(newList, self.testList)

        listIterator = iter(self.testList)
        self.assertEqual(next(listIterator), 5)
        self.assertEqual(next(listIterator), 4)
        self.assertEqual(next(listIterator), 10)
        self.assertEqual(next(listIterator), 50)
        with self.assertRaises(StopIteration):
            next(listIterator)

    def test_append(self):
        self.assertEqual(len(self.testList), 4)
        self.testList.append(80)
        self.assertEqual(len(self.testList), 5)
        self.assertEqual(self.testList[4], 80)

    def test_insert(self):
        self.assertEqual(len(self.testList), 4)
        self.testList.insert(2, 888)
        self.assertEqual(len(self.testList), 5)
        self.assertEqual(self.testList[2], 888)
        self.assertEqual(self.testList[3], 10)

    def test_sort(self):
        sortList(self.testList, lambda a, b: True if a < b else False)
        self.assertEqual(self.testList, [4, 5, 10, 50])
        testList = List()
        sortList(testList, lambda a, b: True if a < b else False)
        self.assertEqual(testList, [])
        testList = List([1, 2, 3])
        sortList(testList, lambda a, b: True if a < b else False)
        self.assertEqual(testList, [1, 2, 3])
        testList = List([1, -2, -3])
        sortList(testList, lambda a, b: True if a < b else False)
        self.assertEqual(testList, [-3, -2, 1])

    def test_sortByAttribute(self):
        client1 = ClientDAO("a")
        client1.setClientId(1)
        client2 = ClientDAO("b")
        client2.setClientId(0)
        testList = [client1, client2]
        sortListByObjectAttribute(testList, lambda a, b: True if a < b else False, lambda a: a.getId())
        self.assertEqual(testList, [client2, client1])
        sortListByObjectAttribute(testList, lambda a, b: True if a > b else False, lambda a: a.getId())
        self.assertEqual(testList, [client1, client2])

    def test_filter(self):
        self.assertEqual(filterList(self.testList, lambda a: True if a % 2 == 0 else False), [4, 10, 50])
        self.assertEqual(filterList(List([1, -2, -3]), lambda a: True if a % 2 == 0 else False), [-2])

