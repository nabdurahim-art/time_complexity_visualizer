import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue(10)

        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 1)

    def test_enqueue_multiple_items(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.peek(), 10)

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)

        result = queue.dequeue()

        self.assertEqual(result, 10)
        self.assertEqual(queue.size(), 1)

    def test_dequeue_follows_fifo(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)

    def test_dequeue_empty_queue(self):
        queue = Queue()

        self.assertIsNone(queue.dequeue())

    def test_peek(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 2)

    def test_peek_empty_queue(self):
        queue = Queue()

        self.assertIsNone(queue.peek())

    def test_is_empty(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())

        queue.enqueue(10)

        self.assertFalse(queue.is_empty())

        queue.dequeue()

        self.assertTrue(queue.is_empty())

    def test_size(self):
        queue = Queue()

        self.assertEqual(queue.size(), 0)

        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.size(), 2)

        queue.dequeue()

        self.assertEqual(queue.size(), 1)


if __name__ == "__main__":
    unittest.main()
