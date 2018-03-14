from unittest import TestCase

from day_12.example import super_sum


class TestExample(TestCase):
    def setUp(self):
        self.data = [1, 2]

    def tearDown(self):
        pass

    def test_sum_one_plus_two_eq_three(self):
        # given
        expected = 3
        result = super_sum(*self.data)
        self.assertEqual(result, expected)

    def test_sum_two_plus_two_eq_four(self):
        # given
        expected = 4
        result = super_sum(*self.data)
        self.assertEqual(result, expected)

    def test_sum_raises_valueerr_for_int_and_str(self):
        a = 'abc'
        b = 3
        with self.assertRaises(TypeError):
            super_sum(a, b)

    def test_sum_adds_3_numbers(self):
        data = [1, 2, 3]
        expected = 6
        result = super_sum(*data)
        self.assertEqual(result, expected)

