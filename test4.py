from one_hot_encoder import fit_transform
import pytest


def test_1():
    countries = ['Russia', 'USA', 'England', 'Denmark']
    expected = [
        ('Russia', [0, 0, 0, 1]),
        ('USA', [0, 0, 1, 0]),
        ('England', [0, 1, 0, 0]),
        ('Denmark', [1, 0, 0, 0])
    ]
    assert fit_transform(countries) == expected


def test_2():  # с перехватом исключения
    meals = ['breakfast', 'lunch', 'dinner']
    incorrect_res = [
        ('breakfast', [0, 1, 0]),
        ('lunch', [0, 0, 1]),
        ('dinner', [1, 0, 0])
    ]
    with pytest.raises(AssertionError):
        assert fit_transform(meals) == incorrect_res


def test_3():
    clothes = ['T-shirt', 'dress', 'sweater', 'skirt', 'jeans']
    expected = [
        ('T-shirt', [0, 0, 0, 0, 1]),
        ('dress', [0, 0, 0, 1, 0]),
        ('sweater', [0, 0, 1, 0, 0]),
        ('skirt', [0, 1, 0, 0, 0]),
        ('jeans', [1, 0, 0, 0, 0])
    ]
    assert fit_transform(clothes) == expected


def test_4():
    furniture = ['bed', 'armchair', 'desk', 'bookshelf', 'table']
    res = [
        ('desk', [0, 0, 1, 0, 0]),
        ('bookshelf', [0, 1, 0, 0, 0]),
        ('table', [1, 0, 0, 0, 0]),
        ('bed', [0, 0, 0, 0, 1]),
        ('armchair', [0, 0, 0, 1, 0])
    ]
    assert fit_transform(furniture) not in res
