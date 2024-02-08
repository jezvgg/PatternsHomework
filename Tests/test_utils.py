import unittest
from Utils.typecheck import typecheck

class test_utils(unittest.TestCase):

    def test_annotation_checker(self):
        @typecheck
        def smth(a:int, b:int):
            return a+b
        
        assert smth(5,5) == 10
        self.assertRaises(TypeError, smth, 'a', 'b')


    def test_limits_checher(self):
        @typecheck(expression=lambda x: x['a']<5)
        def smth(a: int, b:int):
            return a+b
        
        assert smth(2,2) == 4
        self.assertRaises(TypeError, smth, 'a', 'b')
        self.assertRaises(Exception, smth, 6, 5)