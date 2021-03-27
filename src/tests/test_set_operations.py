import unittest
import mOps.sets as ms
import mOps.logic as ml
import mOps.core.number_generators as ng



class TestSetOperations(unittest.TestCase):

    def test_function_alias(self):
        self.assertEqual(ms.U, ms.union)
        self.assertEqual(ms.I, ms.intersection)
        self.assertEqual(ms.SetD, ms.set_diffrence)
        self.assertEqual(ms.SymD, ms.symmetric_diffrence)
        self.assertEqual(ms.CarP, ms.cartesian_product)
        self.assertEqual(ms.PwrS, ms.power_set)

    def test_set_equality_unsorted(self):
        a = ms.Set(0, 2, 4)
        b = ms.Set(0, 4, 2)
        self.assertTrue(a == b)

    def test_set_equality_multiset(self):
        a = ms.Set(1, 2, 4)
        b = ms.Set(1, 2, 2, 4, 4, 4, 4 )
        self.assertTrue(a == b)

    def test_set_inequality(self):
        a = ms.Set(0, 2, 4)
        b = ms.Set(1, 4, 2)
        self.assertTrue(a != b)

    def test_union(self):
        a = ms.Set(0, 2, 4, 6, 8)
        b = ms.Set(1, 3, 5, 7, 9)
        result = ms.union(a, b)
        aResult = ms.Set(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertTrue(aResult == result)

    def test_intersection(self):
        a = ms.Set(0, 2, 4, 6, 8, 10, 12)
        b = ms.Set(0, 3, 6, 9, 12)
        result = ms.intersection(a, b)
        aResult = ms.Set(0, 6, 12)
        self.assertTrue(aResult == result)

    def test_set_diffrence(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(2, 3, 5, 7, 8, 9)
        aResult = ms.Set(1, 4, 6)
        result = ms.SetD(a, b)
        self.assertTrue(aResult == result)

    def test_set_diffrence_properties(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(9, 2, 3, 8, 5, 7)
        c = ms.Set(5, 3, 8)
        self.assertTrue(ms.SetD(c, ms.I(a, b)) == ms.U(ms.SetD(c, a), ms.SetD(c, b)))
        self.assertTrue(ms.SetD(c, ms.U(a, b)) == ms.I(ms.SetD(c, a), ms.SetD(c, b)))
        self.assertTrue(ms.SetD(c, ms.SetD(b, a)) == ms.U(ms.I(c, a), ms.SetD(c, b)))
        self.assertTrue(ms.SetD(c, ms.SetD(c, a)) == ms.I(c, a))
        self.assertTrue(ms.SetD(ms.I(b, c), a) == ms.I(b, ms.SetD(c, a)))
        self.assertTrue(ms.I(ms.SetD(b, a), c) == ms.SetD(ms.I(b, c), a))
        self.assertTrue(ms.U(ms.SetD(b, a), c) == ms.SetD(ms.U(b, c), ms.SetD(a, c)))
        self.assertTrue(ms.SetD(a, a) == ms.Set())
        self.assertTrue(ms.SetD(ms.Set(), a) == ms.Set())
        self.assertTrue(ms.SetD(a, ms.Set()) == a)

    def test_symmetric_diffrence(self):
        a = ms.Set(1, 2, 3)
        b = ms.Set(1, 2, 4)
        aResult = ms.Set(3, 4)
        result = ms.SymD(a, b)
        self.assertTrue(aResult == result)

    def test_symmetric_diffrence_properties(self):
        a = ms.Set(1, 2, 3, 4, 5, 6)
        b = ms.Set(9, 2, 3, 8, 5, 7)
        c = ms.Set(5, 3, 8)
        self.assertTrue(ms.SymD(a, b) == ms.U(ms.SetD(a, b), ms.SetD(b, a)))
        self.assertTrue(ms.SymD(a, b) == ms.SetD(ms.U(a, b), ms.I(a, b)))
        self.assertTrue(ms.U(a, b) == ms.SymD(ms.SymD(a, b), ms.I(a, b)))
        self.assertTrue(ms.SymD(a, b) == ms.SymD(b, a))
        self.assertTrue(ms.SymD(ms.SymD(a, b), c) == ms.SymD(a, ms.SymD(b, c)))
        self.assertTrue(ms.SymD(a, ms.Set()) == a)
        self.assertTrue(ms.SymD(a, a) == ms.Set())

    def test_cartesian_product(self):
        a = ms.Set(1, 2, 3)
        b = ms.Set(1, 2, 4)
        aResult = ms.Set((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 4), (2, 4), (3, 4))
        result = ms.CarP(a, b)
        self.assertTrue(aResult == result)

    def test_power_set(self):
        a = ms.Set(1, 2, 3)
        aResult = ms.Set(ms.Set(), ms.Set(1), ms.Set(1, 2), ms.Set(1, 2, 3), ms.Set(1, 3), ms.Set(2), ms.Set(2, 3),
                         ms.Set(3))
        result = ms.PwrS(a)
        self.assertTrue(aResult == result)

    def test_power_set_properties(self):
        a = [1, 2, 3]
        self.assertEqual(len(ms.PwrS(a)), 2 ** len(a))

    def test_generator(self):
        ms.Set().fromGenerator(ng.isPrime, ml.OR, ng.isEven)
