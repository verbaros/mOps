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

    def test_union(self):
        a = ms.Set(0, 2, 4, 6, 8)
        b = ms.Set(1, 3, 5, 7, 9)
        result = ms.union(a, b)
        aResult = ms.Set(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertListEqual(aResult.items(), result.items())

    def test_intersection(self):
        a = ms.Set(0, 2, 4, 6, 8, 10, 12)
        b = ms.Set(0, 3, 6, 9, 12)
        result = ms.intersection(a, b)
        aResult = ms.Set(0, 6, 12)
        self.assertListEqual(aResult.items(), result.items())

    def test_set_diffrence(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(2, 3, 5, 7, 8, 9)
        aResult = ms.Set(1, 4, 6)
        result = ms.SetD(a, b)
        self.assertListEqual(aResult.items(), result.items())

    def test_set_diffrence_properties(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(9, 2, 3, 8, 5, 7)
        c = ms.Set(5, 3, 8)
        self.assertListEqual(ms.SetD(c, ms.I(a, b)).items(), ms.U(ms.SetD(c, a), ms.SetD(c, b)).items())
        self.assertListEqual(ms.SetD(c, ms.U(a, b)).items(), ms.I(ms.SetD(c, a), ms.SetD(c, b)).items())
        self.assertListEqual(ms.SetD(c, ms.SetD(b, a)).items(), ms.U(ms.I(c, a), ms.SetD(c, b)).items())
        self.assertListEqual(ms.SetD(c, ms.SetD(c, a)).items(), ms.I(c, a).items())
        self.assertListEqual(ms.SetD(ms.I(b, c), a).items(), ms.I(b, ms.SetD(c, a)).items())
        self.assertListEqual(ms.I(ms.SetD(b, a), c).items(), ms.SetD(ms.I(b, c), a).items())
        self.assertListEqual(ms.U(ms.SetD(b, a), c).items(), ms.SetD(ms.U(b, c), ms.SetD(a, c)).items())
        self.assertListEqual(ms.SetD(a, a).items(), ms.Set().items())
        self.assertListEqual(ms.SetD(ms.EmptySet, a).items(), ms.Set().items())
        self.assertListEqual(ms.SetD(a, ms.EmptySet).items(), a.items())

    def test_symmetric_diffrence(self):
        a = ms.Set(1, 2, 3)
        b = ms.Set(1, 2, 4)
        aResult = ms.Set(3, 4)
        result = ms.SymD(a, b)
        self.assertListEqual(aResult.items(), result.items())

    def test_symmetric_diffrence_properties(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(9, 2, 3, 8, 5, 7)
        c = ms.Set(5, 3, 8)
        self.assertListEqual(ms.SymD(a, b).items(), ms.U(ms.SetD(a, b), ms.SetD(b, a)).items())
        self.assertListEqual(ms.SymD(a, b).items(), ms.SetD(ms.U(a, b), ms.I(a, b)).items())
        self.assertListEqual(ms.U(a, b).items(), ms.SymD(ms.SymD(a, b), ms.I(a, b)).items())
        self.assertListEqual(ms.SymD(a, b).items(), ms.SymD(b, a).items())
        self.assertListEqual(ms.SymD(ms.SymD(a, b), c).items(), ms.SymD(a, ms.SymD(b, c)).items())
        self.assertListEqual(ms.SymD(a, ms.Set()).items(), a.items())
        self.assertListEqual(ms.SymD(a, a).items(), ms.Set())

    def test_cartesian_product(self):
        a = ms.Set(1, 2, 3)
        b = ms.Set(1, 2, 4)
        aResult = ms.Set((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 4), (2, 4), (3, 4))
        result = ms.CarP(a, b)
        self.assertListEqual(aResult.items(), result.items())

    def test_power_set(self):
        a = ms.Set(1, 2, 3)
        aResult = ms.Set(ms.Set(), ms.Set(1), ms.Set(1, 2), ms.Set(1, 2, 3), ms.Set(1, 3), ms.Set(2), ms.Set(2, 3),
                         ms.Set(3))
        result = ms.PwrS(a)
        self.assertListEqual(aResult.items(), result.items())

    def test_power_set_properties(self):
        a = [1, 2, 3]
        self.assertEqual(len(ms.PwrS(a)), 2 ** len(a))
