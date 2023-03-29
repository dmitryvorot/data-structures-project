"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class TestCode(unittest.TestCase):
    #top = 'data0'
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')


    def test_pop(self):
        stack = Stack()
        stack.push('dataX')
        self.assertNotEqual(stack.pop(), None)

if __name__ == '__main__':
    unittest.main()