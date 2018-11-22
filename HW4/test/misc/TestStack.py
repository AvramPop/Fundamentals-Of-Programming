from unittest import TestCase

from main.Stack import Stack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEquals(self.stack.pop(), "b")

    def test_pop(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEquals(self.stack.pop(), "b")
        self.assertEquals(self.stack.pop(), "a")
        with self.assertRaises(IndexError):
            self.stack.pop()
