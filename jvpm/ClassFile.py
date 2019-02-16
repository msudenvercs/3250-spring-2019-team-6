import unittest
from unittest.mock import mock_open, patch

class ClassFile():
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            #the byte string being stored in self.data to be parsed
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            self.constant_pool = self.get_constant_pool()
            self.constant_table =  self.get_constant_pool_table()
            self.access_flags = self.get_access_flags()
            self.this_class = self.get_this_class()
            self.superclass = self.get_super_class()
            self.interface_count = self.get_interface_count()
            self.cp_and_ic = self.interface_count + self.constant_pool
            self.interface_table = self.get_interface_table()
            self.field_count = self.get_field_count()
            self.cp_ic_fc = self.cp_and_ic + self.field_count
            self.field_table = self.get_field_table()
            self.method_count = self.get_method_count()
            self.cp_ic_fc_mc = self.cp_ic_fc + self.method_count
            self.method_table = self.get_method_table()
            self.attribute_count = self.get_attribute_count()
            self.attribute_table = self.get_attribute_table()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

    def get_constant_pool(self):
        return self.data[8] + self.data[9]

    def get_constant_pool_table(self):
        constant = ""
        for i in range(self.constant_pool):
            constant += format(self.data[i + 10], '02X')
        return constant

    def get_access_flags(self):
        return self.data[10 + self.constant_pool] + self.data[11 + self.constant_pool]

    def get_this_class(self):
        return self.data[12 + self.constant_pool] + self.data[13 + self.constant_pool]

    def get_super_class(self):
        return self.data[14 + self.constant_pool] + self.data[15 + self.constant_pool]

    def get_interface_count(self):
        return self.data[16 + self.constant_pool] + self.data[17 + self.constant_pool]

    def get_interface_table(self):
        interface = ""
        for i in range(self.interface_count):
            interface += format(self.data[i + 18 + self.constant_pool], '02X')
        return interface

    def get_field_count(self):
        return self.data[18 + self.cp_and_ic] + self.data[19 + self.cp_and_ic]

    def get_field_table(self):
        field = ""
        for i in range(self.field_count):
            field += format(self.data[i + 20 + self.cp_and_ic], '02X')
        return field

    def get_method_count(self):
        return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]

    def get_method_table(self):
        method = ""
        for i in range(self.method_count):
            method += format(self.data[i + 22 + self.cp_ic_fc], '02X')
        return method

    def get_attribute_count(self):
        return self.data[22 + self.cp_ic_fc_mc] + self.data[23 + self.cp_ic_fc_mc]
        
    def get_attribute_table(self):
        attribute = ""
        for i in range(self.attribute_count):
            attribute += format(self.data[i + 24 + self.cp_ic_fc_mc], '02X')
        return attribute
		
    def printSelf(self):
        print(self)

 #       print(self.magic)
 #       print(self.minor)
 #       print(self.major)
 #       self.constant_pool)
 #       self.constant_table)
 #       self.access_flags)
 #       self.this_class)
 #       self.superclass)
 #       self.interface_count)
 #       self.cp_and_ic)
 #       self.field_count)
 #       self.cp_ic_fc)
 #       self.field_table)
 #       self.method_count)
 #       self.cp_ic_fc_mc
 #       self.method_table
 #       self.attribute_count
 #       self.attribute_table


class OpCodes():
    def __init__(self):
        self.table = {0x00: self.not_implemented}

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        return self.table[value]()

class TestClassFile(unittest.TestCase):
    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x01\x02\x03')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 1)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 5)

class TestOpCodes(unittest.TestCase):
    def test_not_implmented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
			
classy = ClassFile()
classy.printSelf()
