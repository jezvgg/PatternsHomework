import unittest
from Utils.typecheck import typecheck
from Src.exeptions import argument_exception

class test_utils(unittest.TestCase):

    def test_annotation_checker(self):
        @typecheck
        def smth(a:int, b:int):
            return a+b
        
        assert smth(5,5) == 10
        self.assertRaises(argument_exception, smth, 'a', 'b')


    def test_limits_checher(self):
        @typecheck(expression=lambda x: x['a']<5)
        def smth(a: int, b:int):
            return a+b
        
        assert smth(2,2) == 4
        self.assertRaises(argument_exception, smth, 'a', 'b')
        self.assertRaises(argument_exception, smth, 6, 5)