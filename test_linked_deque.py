import unittest

from linked_deque import LinkedDeque

class TestLinkedDeque(unittest.TestCase):
    def setUp(self):
        self.deque = LinkedDeque()

    def test_insert_first(self):
        self.deque.insert_first(1)
        self.assertEqual(self.deque.peek_first(), 1)

    def test_insert_last(self):
        self.deque.insert_last(1)
        self.assertEqual(self.deque.peek_last(), 1)

    def test_remove_first(self):
        self.deque.insert_first(1)
        self.assertEqual(self.deque.remove_first().value, 1)

    def test_remove_last(self):
        self.deque.insert_last(1)
        self.assertEqual(self.deque.remove_last().value, 1)

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.insert_first(1)
        self.assertFalse(self.deque.is_empty())

    def test_len(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.insert_first(1)
        self.assertEqual(len(self.deque), 1)

if __name__ == '__main__':
    unittest.main()