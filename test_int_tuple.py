import pytest

# Тесты для int

# Параметризованный тест
@pytest.mark.parametrize('values, expected_results', [
    pytest.param(
        (45, 3.75, '6754', [10]), (True, False, False, False),
        id='first',
    ),
    pytest.param(
        (-5.555, -78, '-89.90', [-123]), (False, True, False, False),
        id='second',
    ),
])
def test_is_int(values, expected_results):
    res = tuple([isinstance(values[i], int) for i in range(len(values))])
    assert res == expected_results


# Негативный тест, не выдающий ошибку
def test_int_plus_list():
    try:
        assert 145 + [255]
    except TypeError:
        pass


def test_convert_to_int():
    assert int('-777') == -777



# Тесты для tuple

# Параметризованный тест
@pytest.mark.parametrize('tup, length', [
    pytest.param(
        (1, 2, 3, 4, 5, 6, 7), 7,
    ),
    pytest.param(
        (), 0,
    ),
    pytest.param(
        ('one', 'two', 'three', 'four', 'five'), 5,
    ),
])
def test_len_tuple(tup, length):
    assert len(tup) == length


# Негативный тест, не выдающий ошибку
def test_tuple_out_of_range():
    test_tuple = (-3, 'Simple is better than complex.', None)
    try:
        assert test_tuple[len(test_tuple)]
    except IndexError:
        pass


def test_merge_tuples():
    tup1 = ('Python - ', 'окрыляет;') 
    tup2 = ('Mail.ru - ', 'вдохновляет;')
    tup3 = ('Курение - ', 'убивает.') 
    assert tup1 + tup2 + tup3 == ('Python - ', 'окрыляет;',
                                  'Mail.ru - ', 'вдохновляет;',
                                  'Курение - ', 'убивает.')
