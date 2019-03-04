import unittest
from unittest.mock import mock_open, patch
from jvpm.ClassFile import OpCodes


class TestOpCodes(unittest.TestCase):
    def test_not_implemented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)

    def test_iadd_simple(self):
	    testiadd = OpCodes()
	    testiadd.stack.append(2)
	    testiadd.stack.append(2)
	    testiadd.iadd()
	    self.assertEqual(testiadd.stack.pop(), 4) 
    def test_iand_simple(self):
	    testiand = OpCodes()
	    testiand.stack.append(5)    
	    testiand.stack.append(3)    
	    testiand.iand()             
	    self.assertEqual(testiand.stack.pop(), 1) 
    def test_iconst_m1_simple(self):
	    testiconst_m1 = OpCodes()       
	    testiconst_m1.iconst_m1  
	    self.assertEqual(testiconst_m1.stack.pop(), -1) 
    def test_iconst_0_simple(self):
	    testiconst_0 = OpCodes()
	    testiconst_0.iconst_0    
	    self.assertEqual(testiconst_0.stack.pop(), 0) 
    def test_iconst_1_simple(self):
	    testiconst_1 = OpCodes()
	    testiconst_1.iconst_1    
	    self.assertEqual(testiconst_1.stack.pop(), 1) 
    def test_iconst_2_simple(self):
	    testiconst_2 = OpCodes()
	    testiconst_2.iconst_2   
	    self.assertEqual(testiconst_2.stack.pop(), 2) 
    def test_iconst_3_simple(self):
	    testiconst_3 = OpCodes()
	    testiconst_3.iconst_3    
	    self.assertEqual(testiconst_3.stack.pop(), 3) 
    def test_iconst_4_simple(self):
	    testiconst_4 = OpCodes()
	    testiconst_4.iconst_4    
	    self.assertEqual(testiconst_4.stack.pop(), 4) 
    def test_iconst_5_simple(self):
	    testiconst_5 = OpCodes()
	    testiconst_5.iconst_5   
	    self.assertEqual(testiconst_5.stack.pop(), 5) 
