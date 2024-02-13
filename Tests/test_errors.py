import unittest
from Src.error_proxy import error_proxy


class test_errors(unittest.TestCase):

    def test_set_error_message(self):
        error = error_proxy("Test", "test")

        assert error.is_error == True

    def test_set_exeption(self):
        error = error_proxy()

        try:
            result = 1 / 0
        except Exception as ex:
            error.set_error(ex)

        assert error.is_error == True