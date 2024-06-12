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

    def test_remove_last_empty(self):
        with self.assertRaises(Exception):
            self.deque.remove_last()

    def test_remove_last_when_length_is_1(self):
        self.deque.insert_first(1)
        self.assertEqual(self.deque.remove_last().value, 1)
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(str(self.deque), '[  ]')

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.insert_first(1)
        self.assertFalse(self.deque.is_empty())

    def test_len(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.insert_first(1)
        self.assertEqual(len(self.deque), 1)

    def test_multi_cases(self):
        self.deque.insert_first(1)
        self.deque.insert_first(2)
        self.deque.insert_last(3)
        self.deque.insert_last(4)
        
        self.assertEqual(str(self.deque), '[ 2 1 3 4 ]')
        self.assertEqual(self.deque.remove_first().value, 2)
        self.assertEqual(self.deque.remove_last().value, 4)
        self.assertEqual(self.deque.remove_first().value, 1)
        self.assertEqual(self.deque.remove_last().value, 3)
        self.assertEqual(self.deque.is_empty(), True)
        self.assertEqual(str(self.deque), '[  ]')


if __name__ == '__main__':
    unittest.main()