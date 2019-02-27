import unittest
from unittest.mock import mock_open, patch
from jvpm.ClassFile import OpCodes


class TestOpCodes(unittest.TestCase):
    def test_not_implemented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
	def test_iadd_simple(self):
	    test1 = OpCodes()
		test1.stack.append(1)
		test1.stack.append(2)
		test1.idiv()
		self.assertEqual(test1.pop(), 2)
