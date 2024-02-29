import unittest
from Utils.typecheck import typecheck
from Utils.instance import instance_checker
from Src.exeptions import argument_exception
from Src.Models import *

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


    def test_set_checher_limit(self):
        @typecheck(expression = lambda x: x['b'] <= 4)
        def smth(a:int, b:int = 0):
            return a+b

        assert smth(4) == 4
        self.assertRaises(argument_exception, smth,4, 5)

    def test_list_annotations(self):
        @typecheck
        def smth(lst: list[int]):
            return sum(lst)

        assert smth([1,2,3]) == 6
        self.assertRaises(argument_exception, smth, ['a','b','c'])

    def test_instance(self):

        assert instance_checker(5, int) == True
        assert instance_checker(5, int | float) == True
        assert instance_checker(5, str) == False
        assert instance_checker([1,2,3], list) == True
        assert instance_checker([1,2,3], list[int]) == True
        assert instance_checker([1, 'a', 3], list[int]) == False

    def test_attrworker_getattrs(self):
        gramm = unit_model.create_gramm()
        assert gramm.getattrs() == {'head'}

    def test_attrworker_getattrsnames(self):
        gramm = unit_model.create_gramm()
        assert gramm.get_by_attr('head') is not None

    def test_attrworker_getattrsvalues(self):
        gramm = unit_model.create_gramm()
        assert gramm.get_attr_values('head') is not None

    def test_attrworker_getattrskeys(self):
        gramm = unit_model.create_gramm()
        assert gramm.get_attr_keys('head') is not None