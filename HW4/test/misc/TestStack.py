from unittest import TestCase

from src.Exception import EmptyStackException
from src.undo.Stack import Stack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.pop(), "b")

    def test_pop(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.pop(), "b")
        self.assertEqual(self.stack.pop(), "a")
        with self.assertRaises(EmptyStackException):
            self.stack.pop()
