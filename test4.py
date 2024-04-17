from one_hot_encoder import fit_transform
import pytest


def test_correct_countries():
    """
    Проверим, работает ли fit_transform так, как мы ожидаем на примере
    """
    countries = ['Russia', 'USA', 'England', 'Denmark']
    expected = [
        ('Russia', [0, 0, 0, 1]),
        ('USA', [0, 0, 1, 0]),
        ('England', [0, 1, 0, 0]),
        ('Denmark', [1, 0, 0, 0])
    ]
    assert fit_transform(countries) == expected


def test_correct_furniture():
    """
    Проверим, работает ли fit_transform так, как мы ожидаем на примере
    """
    furniture = ['bed', 'armchair', 'desk', 'bookshelf', 'table']
    expected = [
        ('bed', [0, 0, 0, 0, 1]),
        ('armchair', [0, 0, 0, 1, 0]),
        ('desk', [0, 0, 1, 0, 0]),
        ('bookshelf', [0, 1, 0, 0, 0]),
        ('table', [1, 0, 0, 0, 0])
    ]
    assert fit_transform(furniture) == expected


def test_correct_clothes():
    """
    Проверим, работает ли fit_transform так, как мы ожидаем на примере
    """
    clothes = ['T-shirt', 'dress', 'sweater', 'skirt', 'jeans']
    expected = [
        ('T-shirt', [0, 0, 0, 0, 1]),
        ('dress', [0, 0, 0, 1, 0]),
        ('sweater', [0, 0, 1, 0, 0]),
        ('skirt', [0, 1, 0, 0, 0]),
        ('jeans', [1, 0, 0, 0, 0])
    ]
    assert fit_transform(clothes) == expected


def test_correct_seasons():
    """
    Проверим, работает ли fit_transform так, как мы ожидаем на примере
    """
    seasons = ['winter', 'spring', 'summer', 'autumn']
    expected = [
        ('winter', [0, 0, 0, 1]),
        ('spring', [0, 0, 1, 0]),
        ('summer', [0, 1, 0, 0]),
        ('autumn', [1, 0, 0, 0])
    ]
    assert fit_transform(seasons) == expected


def test_types():
    """
    Проверим, ожидаемый ли тип результата fit_transform
    """
    meals = ['breakfast', 'lunch', 'dinner']
    res = fit_transform(meals)
    assert isinstance(res, list)
    assert isinstance(res[0], tuple)


def test_empty():
    """
    Тест с перехватом исключения
    """
    with pytest.raises(TypeError):
        fit_transform()
