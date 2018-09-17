import unittest
import paramunittest


# 方案一
@paramunittest.parametrized(
    ('1', '2'),
    # (4, 3),
    ('2', '3'),
    (('4',), {'b': '5'}),
    ((), {'a': 5, 'b': 6}),
    {'a': 5, 'b': 6},
)
class TestFoo(paramunittest.ParametrizedTestCase):
    def setParameters(self, a, b):
        self.a = a
        self.b = b

    def testLess(self):
        self.assertLess(self.a, self.b)


# 方案二
@paramunittest.parametrized(
    ('1', '2'),
    # (4, 3),
    ('2', '3'),
    (('4',), {'b': '5'}),
    ((), {'a': 5, 'b': 6}),
    {'a': 5, 'b': 6},
)
class TestBar(unittest.TestCase):
    def setParameters(self, a, b):
        self.a = a
        self.b = b

    def testLess(self):
        self.assertLess(self.a, self.b)


if __name__ == "__main__":
    unittest.main(verbosity=2)