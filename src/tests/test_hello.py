import unittest
import mOps as mo


class TestHello(unittest.TestCase):

    def test_hi(self):
        result = mo.hello(5)
        self.assertEqual(result,5*5)