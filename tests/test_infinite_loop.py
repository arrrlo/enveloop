import unittest

from enveloop import limit_recursion_to


class TestInfiniteLoop(unittest.TestCase):

    def setUp(self):
        pass

    def test_limit_recursion_to(self):

        limit_no = 10
        str_ = 'bar '

        @limit_recursion_to(limit_no, lambda a: f'{a}-finished')
        def foo(a):
            return f'{a}{foo(a)}'

        self.assertEqual(foo(str_), f'{str_*(limit_no+1)}-finished')

        @limit_recursion_to(limit_no)
        def foo(a):
            from_foo = foo(a)
            if not from_foo:
                from_foo = ''
            return f'{a}{from_foo}'

        self.assertEqual(foo(str_), str_*limit_no)

        list_ = list()

        @limit_recursion_to(limit_no)
        def foo(a):
            list_.append(str_)
            foo(a)

        foo(str_)

        self.assertEqual(list_, [str_] * limit_no)
