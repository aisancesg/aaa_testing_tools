from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_1(self):
        countries = ['Russia', 'USA', 'England', 'Denmark']
        expected = [
            ('Russia', [0, 0, 0, 1]),
            ('USA', [0, 0, 1, 0]),
            ('England', [0, 1, 0, 0]),
            ('Denmark', [1, 0, 0, 0])
        ]
        self.assertEqual(fit_transform(countries), expected)

    def test_2(self):
        meals = ['breakfast', 'lunch', 'dinner']
        incorrect_res = [
            ('breakfast', [0, 1, 0]),
            ('lunch', [0, 0, 1]),
            ('dinner', [1, 0, 0])
        ]
        self.assertNotEqual(fit_transform(meals), incorrect_res)

    def test_3(self):  # с перехватом исключения
        clothes = ['T-shirt', 'dress', 'sweater', 'skirt', 'jeans']
        res = [
            ('sweater', [0, 0, 0, 0, 1]),
            ('skirt', [0, 0, 0, 1, 0]),
            ('jeans', [0, 0, 1, 0, 0]),
            ('T-shirt', [0, 1, 0, 0, 0]),
            ('dress', [1, 0, 0, 0, 0])
        ]
        transformed_clothes = fit_transform(clothes)
        try:
            self.assertEqual(transformed_clothes, res)
        except AssertionError:
            print(f'\n AssertionError in test_3: '
                  f'\n input: {clothes}, '
                  f'\n expected: {res}, '
                  f'\n got: {transformed_clothes}')

    def test_4(self):
        furniture = ['bed', 'armchair', 'desk', 'bookshelf', 'table']
        res = [
            ('desk', [0, 0, 1, 0, 0]),
            ('bookshelf', [0, 1, 0, 0, 0]),
            ('table', [1, 0, 0, 0, 0]),
            ('bed', [0, 0, 0, 0, 1]),
            ('armchair', [0, 0, 0, 1, 0])
        ]
        self.assertNotIn(fit_transform(furniture), res)


if __name__ == '__main__':
    unittest.main()
