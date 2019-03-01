import unittest
from unittest.mock import mock_open, patch
from jvpm.ClassFile import OpCodes


class TestOpCodes(unittest.TestCase):
    def test_not_implemented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
    def test_idiv_simple(self):
	    test1 = OpCodes()
	    test1.stack.append(2)
	    test1.stack.append(4)
	    test1.idiv()
	    self.assertEqual(test1.stack.pop(), 2)
    def test_imul_simple(self):
	    test2 = OpCodes()
	    test2.stack.append(2)
	    test2.stack.append(4)
	    test2.imul()
	    self.assertEqual(test2.stack.pop(), 8)
    def test_ineg_simple(self):
	    test3 = OpCodes()
	    test3.stack.append(5)
	    test3.ineg()
	    self.assertEqual(test3.stack.pop(), -5)
    def test_ior_simple(self):
	    test4 = OpCodes()
	    test4.stack.append(6)
		test4.stack.append(2)
		test4.ior()
		self.assertEqual(test4.stack.pop(), 7)
    def test_irem_simple(self):
	    test5 = OpCodes()
		test5.stack.append(3)
		test5.stack.append(7)
		test5.irem()
		self.assertEqual(test5.stack.pop(), 1)
