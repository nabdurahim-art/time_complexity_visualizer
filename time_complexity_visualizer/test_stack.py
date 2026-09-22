import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_new_stack_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_push(self):
        stack = Stack()

        stack.push(10)

        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)

    def test_push_multiple_items(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 30)

    def test_pop(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)

        result = stack.pop()

        self.assertEqual(result, 20)
        self.assertEqual(stack.size(), 1)

    def test_pop_follows_lifo(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_pop_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.pop())

    def test_peek(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)

    def test_peek_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.peek())

    def test_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

        stack.push(10)

        self.assertFalse(stack.is_empty())

        stack.pop()

        self.assertTrue(stack.is_empty())

    def test_size(self):
        stack = Stack()

        self.assertEqual(stack.size(), 0)

        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.size(), 2)

        stack.pop()

        self.assertEqual(stack.size(), 1)


if __name__ == "__main__":
    unittest.main()
