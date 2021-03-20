import unittest
import mOps.sets as ms


class TestSetOperations(unittest.TestCase):

    def test_function_alias(self):
        self.assertEqual(ms.U, ms.union)
        self.assertEqual(ms.I, ms.intersection)
        self.assertEqual(ms.SetD, ms.set_diffrence)
        self.assertEqual(ms.SymD, ms.symmetric_diffrence)
        self.assertEqual(ms.CarP, ms.cartesian_product)
        self.assertEqual(ms.PwrS, ms.power_set)


    def test_union_sorted(self):
        a = [0, 2, 4, 6, 8]
        b = [1, 3, 5, 7, 9]
        result = ms.union(a, b)
        aResult = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(aResult, result)

    def test_union_unsorted(self):
        a = [0, 2, 4, 6, 8]
        b = [1, 3, 5, 7, 9]
        result = ms.union(a, b, sort=False)
        aResult = list(set(a + b))
        self.assertListEqual(aResult, result)

    def test_union_non_iter(self):
        a = 0
        b = [1, 3, 5, 7, 9]
        try:
            ms.union(a, b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_intersection(self):
        a = [0, 2, 4, 6, 8, 10, 12]
        b = [0, 3, 6, 9, 12]
        result = ms.intersection(a, b)
        aResult = [0, 6, 12]
        self.assertListEqual(aResult, result)

    def test_intersection_non_iter(self):
        a = 0
        b = [1, 3, 5, 7, 9]
        try:
            ms.intersection(a, b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_set_diffrence(self):
        a = [1, 2, 3, 4, 5, 6]
        b = [2, 3, 5, 7, 8, 9]
        aResult = [1, 4, 6]
        result = ms.SetD(a, b)
        self.assertListEqual(aResult, result)

    def test_set_diffrence_non_iter(self):
        a = 0
        b = [1, 3, 5, 7, 9]
        try:
            ms.SetD(a, b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_set_diffrence_properties(self):
        a = [1, 2, 3, 4, 5, 6]
        b = [9, 2, 3, 8, 5, 7]
        c = [5, 3, 8]
        self.assertListEqual(ms.SetD(c, ms.I(a, b)), ms.U(ms.SetD(c, a), ms.SetD(c, b)))
        self.assertListEqual(ms.SetD(c, ms.U(a, b)), ms.I(ms.SetD(c, a), ms.SetD(c, b)))
        self.assertListEqual(ms.SetD(c, ms.SetD(b, a)), ms.U(ms.I(c, a), ms.SetD(c, b)))
        self.assertListEqual(ms.SetD(c, ms.SetD(c, a)), ms.I(c, a))
        self.assertListEqual(ms.SetD(ms.I(b, c), a), ms.I(b, ms.SetD(c, a)))
        self.assertListEqual(ms.I(ms.SetD(b, a), c), ms.SetD(ms.I(b, c), a))
        self.assertListEqual(ms.U(ms.SetD(b, a), c), ms.SetD(ms.U(b, c), ms.SetD(a, c)))
        self.assertListEqual(ms.SetD(a, a), ms.EmptySet)
        self.assertListEqual(ms.SetD(ms.EmptySet, a), ms.EmptySet)
        self.assertListEqual(ms.SetD(a, ms.EmptySet), a)

    def test_symmetric_diffrence(self):
        a = [1, 2, 3]
        b = [1, 2, 4]
        aResult = [3, 4]
        result = ms.SymD(a, b)
        self.assertListEqual(aResult, result)

    def test_symmetric_diffrence_non_iter(self):
        a = 0
        b = [1, 3, 5, 7, 9]
        try:
            ms.SetD(a, b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_symmetric_diffrence_properties(self):
        a = [1, 2, 3, 4, 5, 6]
        b = [9, 2, 3, 8, 5, 7]
        c = [5, 3, 8]
        self.assertListEqual(ms.SymD(a, b), ms.U(ms.SetD(a, b), ms.SetD(b, a)))
        self.assertListEqual(ms.SymD(a, b), ms.SetD(ms.U(a, b), ms.I(a, b)))
        self.assertListEqual(ms.U(a, b), ms.SymD(ms.SymD(a, b), ms.I(a, b)))
        self.assertListEqual(ms.SymD(a, b), ms.SymD(b, a))
        self.assertListEqual(ms.SymD(ms.SymD(a, b), c), ms.SymD(a, ms.SymD(b, c)))
        self.assertListEqual(ms.SymD(a, ms.EmptySet), a)
        self.assertListEqual(ms.SymD(a, a), ms.EmptySet)

    def test_cartesian_product(self):
        a = [1, 2, 3]
        b = [1, 2, 4]
        aResult = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 4), (2, 4), (3, 4)]
        result = ms.CarP(a, b)
        self.assertListEqual(aResult, result)

    def test_cartesian_product_non_iter(self):
        a = 0
        b = [1, 3, 5, 7, 9]
        try:
            ms.CarP(a, b)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_power_set(self):
        a = [1, 2, 3]
        aResult = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        result = ms.PwrS(a)
        self.assertListEqual(aResult, result)

    def test_power_set_non_iter(self):
        a = 0
        try:
            ms.PwrS(a)
            self.fail('Set must be iterable')
        except TypeError:
            self.assertTrue(True)

    def test_power_set_properties(self):
        a = [1, 2, 3]
        self.assertEqual(len(ms.PwrS(a)), 2**len(a))