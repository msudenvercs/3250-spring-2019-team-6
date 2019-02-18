import unittest
# unittest


class ClassFile:
    def __init__(self, file='jvpm/test.class'):
        with open(file, 'rb') as binary_file:
            # the byte string being stored in self.data to be parsed
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            # self.constant_pool = self.get_constant_pool()
            # self.constant_table =  self.get_constant_pool_table()
            # self.access_flags = self.get_access_flags()
            # self.this_class = self.get_this_class()
            # self.superclass = self.get_super_class()
            # self.interface_count = self.get_interface_count()
            # self.cp_and_ic = self.interface_count + self.constant_pool
            # self.interface_table = self.get_interface_table()
            # self.field_count = self.get_field_count()
            # self.cp_ic_fc = self.cp_and_ic + self.field_count
            # self.field_table = self.get_field_table()
            # self.method_count = self.get_method_count()
            # self.cp_ic_fc_mc = self.cp_ic_fc + self.method_count
            # self.method_table = self.get_method_table()
            # self.attribute_count = self.get_attribute_count()
            # self.attribute_table = self.get_attribute_table()

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

    # def get_constant_pool_table(self):
    #     constant = self.data[10:(10+self.constant_pool)]
    #     # for i in range(self.constant_pool):
    #     #    constant += format(self.data[i + 10], '02X')
    #     return constant
    #
    # def get_access_flags(self):
    #     return self.data[10 + self.constant_pool-1:11 + self.constant_pool]
    #
    # def get_this_class(self):
    #     return self.data[12 + self.constant_pool] + self.data[13 + self.constant_pool]
    #
    # def get_super_class(self):
    #     return self.data[14 + self.constant_pool] + self.data[15 + self.constant_pool]
    #
    # def get_interface_count(self):
    #     return self.data[16 + self.constant_pool] + self.data[17 + self.constant_pool]
    #
    # def get_interface_table(self):
    #     interface = ""
    #     for i in range(self.interface_count):
    #         interface += format(self.data[i + 18 + self.constant_pool], '02X')
    #     return interface
    #
    # def get_field_count(self):
    #     return self.data[18 + self.cp_and_ic] + self.data[19 + self.cp_and_ic]
    #
    # def get_field_table(self):
    #     field = self.data[self.cp_and_ic+20:(self.field_count+self.cp_ic_fc+20)]
    #     # for i in range(self.field_count):
    #     #    field += format(self.data[i + 20 + self.cp_and_ic], '02X')
    #     return field
    #
    # def get_method_count(self):
    #     return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]
    #
    # def get_method_table(self):
    #     method = self.data[22+self.cp_ic_fc:22+self.cp_ic_fc_mc]
    #     # for i in range(self.method_count):
    #     #    method += format(self.data[i + 22 + self.cp_ic_fc], '02X')
    #     return method
    #
    # def get_attribute_count(self):
    #     return self.data[22 + self.cp_ic_fc_mc] + self.data[23 + self.cp_ic_fc_mc]
    #
    # def get_attribute_table(self):
    #     attribute = self.data[(24+self.cp_ic_fc_mc):(24+self.cp_ic_fc_mc+self.attribute_count)]
    #     # for i in range(self.attribute_count):
    #     #    attribute += format(self.data[i + 24 + self.cp_ic_fc_mc], '02X')
    #     return attribute
    #
    # def print_self(self):
    #     print(self)
    #     print("Magic: ", self.magic)
    #     print("Minor version: ", self.minor)
    #     print("Major version: ", self.major)
    #     print("Constant pool: ", self.constant_pool)
    #     print("Constant pool: ", self.constant_pool)
    #     print("Constant table: ", "[%s]" % ", ".join(map(str, self.constant_table)))
    #     print("Access flags: ", hex(self.access_flags[0]), hex(self.access_flags[1]))
    #     print("This class: ", self.this_class)
    #     print("Superclass: ", self.superclass)
    #     print("Interface count: ", self.interface_count)
    #     print("Cp + Ic: ", self.cp_and_ic)
    #     print("Field count: ", self.field_count)
    #     print("Cp + Ic + fc: ", self.cp_ic_fc)
    #     print("Field table: ", "[%s]" % ", ".join(map(str, self.field_table)))
    #     print("Method count: ", self.method_count)
    #     print("Cp + IC + Fc + Mc: ", self.cp_ic_fc_mc)
    #     print("Method table: ", "[%s]" % ", ".join(map(str, self.method_table)))
    #     print("Attribute count: ", self.attribute_count)
    #     print("Attribute table: ", "[%s]" % ", ".join(map(str, self.attribute_table)))

#
# if '__main__' == __name__:
#     ClassFile()


class OpCodes:
    def __init__(self):
        self.table = {0x00: self.not_implemented}

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        return self.table[value]()


# classy = ClassFile()
# classy.print_self()
