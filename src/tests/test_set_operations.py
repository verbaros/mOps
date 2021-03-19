import unittest
import mOps.sets.operations.operations as ms


class TestSetOperations(unittest.TestCase):

    def test_function_alias(self):
        self.assertEqual(ms.U, ms.union)
        self.assertEqual(ms.I, ms.intersection)

    def test_union_sorted(self):
        a = [0,2,4,6,8]
        b = [1,3,5,7,9]
        result = ms.union(a,b)
        aResult = [0,1,2,3,4,5,6,7,8,9]
        self.assertListEqual(aResult,result)

    def test_union_unsorted(self):
        a = [0,2,4,6,8]
        b = [1,3,5,7,9]
        result = ms.union(a,b,sort=False)
        aResult = a+b
        self.assertListEqual(aResult,result)

    def test_union_non_iter(self):
        a = 0
        b = [1,3,5,7,9]
        try:
            ms.union(a,b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_intersection(self):
        a = [0,2,4,6,8,10,12]
        b = [0,3,6,9,12]
        result = ms.intersection(a,b)
        aResult = [0,6,12]
        self.assertListEqual(aResult,result)
            
    def test_intersection_non_iter(self):
        a = 0
        b = [1,3,5,7,9]
        try:
            ms.intersection(a,b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)
