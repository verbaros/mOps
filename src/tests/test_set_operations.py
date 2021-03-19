import unittest
import mOps.sets.operations.operations as ms


class TestSetOperations(unittest.TestCase):
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
        a = "02468"
        b = [1,3,5,7,9]
        try:
            ms.union(a,b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)
            
