import unittest
from unittest.mock import mock_open, patch
from jvpm.ClassFile import ClassFile


class TestClassFile(unittest.TestCase):
    def setUp(self):
        #credit from https://stackoverflow.com/questions/1289894/how-do-i-mock-an-open-used-in-a-with-statement-using-the-mock-framework-in-pyth
        with patch("builtins.open", mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x01\x02\x03\x00\x00')) as m:
            # m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x01\x02\x03\x00\x00')
            #with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 1)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 5)

    def test_count_pool(self):
        self.assertEqual(self.cf.get_constant_pool(), 0)
