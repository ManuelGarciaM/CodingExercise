import unittest

from printer import get_alphbet_dict, repeat_n_times


class TestPrinter(unittest.TestCase):
    def test_get_alpahbet_dict(self):
        alphabet_dict = get_alphbet_dict()

        self.assertEqual(alphabet_dict['a'], 1)
        self.assertEqual(alphabet_dict['z'], 26)
        self.assertEqual(alphabet_dict['e'], 5)

    def test_repeat_n_times(self):
        alphabet_dict = get_alphbet_dict()

        a_input = repeat_n_times('a', alphabet_dict['a'])

        self.assertEqual(a_input, 'a')

        e_input = repeat_n_times('e', alphabet_dict['e'])

        self.assertEqual(e_input, 'eeeee')

        z_input = repeat_n_times('z', alphabet_dict['z'])

        self.assertEqual(len(z_input), 26)

    def test_repeat_n_times_uppercase(self):
        alphabet_dict = get_alphbet_dict()

        a_input = repeat_n_times('A', alphabet_dict['a'])

        self.assertEqual(a_input, 'A')

        e_input = repeat_n_times('E', alphabet_dict['e'])

        self.assertEqual(e_input, 'EEEEE')

        z_input = repeat_n_times('Z', alphabet_dict['z'])

        self.assertEqual(len(z_input), 26)


if __name__ == '__main__':
    unittest.main()
