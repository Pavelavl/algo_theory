import pytest
import tasks as T

# Тесты для distance.py
def test_get_distance():
    distances = T.one.get_distance()
    assert int(distances['Moscow']['London']) == 145
    assert int(distances['Paris']['London']) == 42

# Тесты для circle.py
def test_area_calc():
    assert T.two.area_calc(42) == 131.9469

def test_point_in_circle():
    assert T.two.point_in_circle((23, 34), 42) == True
    assert T.two.point_in_circle((30, 30), 42) == False

# Тесты для favorite_movies.py
def test_search_films():
    expected_result = "Терминатор\nНазад в будущее\nПятый элемент\nЧужие"
    assert T.four.search_films(T.four.my_favorite_movies) == expected_result

# Тесты для garden.py
def test_union():
    garden_set = T.nine.set_from_tuple(T.nine.garden)
    meadow_set = T.nine.set_from_tuple(T.nine.meadow)
    expected_union = {"ромашка", "роза", "одуванчик", "гладиолус", "подсолнух", "клевер", "мак"}
    assert T.nine.union(garden_set, meadow_set) == expected_union

def test_get_similar_elem_from_set():
    garden_set = T.nine.set_from_tuple(T.nine.garden)
    meadow_set = T.nine.set_from_tuple(T.nine.meadow)
    expected_intersection = {"ромашка", "одуванчик"}
    assert T.nine.get_similar_elem_from_set(garden_set, meadow_set) == expected_intersection

# Тесты для my_family.py
def test_get_father_height():
    result = T.five.get_father_height(T.five.my_family_height)
    assert result == "dad's height - 175 sm"

def test_get_family_height():
    result = T.five.get_family_height(T.five.my_family_height)
    assert result == "total height - 530 sm"

# Тесты для operations.py
def test_find_expression():
    result = T.three.find_expression([1, 2, 3, 4, 5], 25)
    assert eval(result) == 25 if result else False

# Тесты для secret.py
def test_encode():
    expected_message = "в бане веник дороже денег"
    assert T.eight.encode(T.eight.secret_message) == expected_message

# Тесты для shopping.py
def test_find_min_prices():
    min_prices = T.ten.find_min_prices(T.ten.shops)
    assert min_prices['печенье'][0]['price'] == 9.99
    assert min_prices['пирожное'][0]['price'] == 59.99

# Тесты для songs_list.py
def test_total_songs_time_list():
    result = T.seven.total_songs_time_list(T.seven.violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
    assert round(result, 2) == 14.93

def test_total_songs_time_dict():
    result = T.seven.total_songs_time_dict(T.seven.violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    assert round(result) == 13

# Тесты для store.py
def test_calculate_store_cost():
    store_data = T.eleven.solve()
    assert store_data == ('Стол -', 54, 'шт, стоимость', 11762, 'руб', 'Диван -', 3, 'шт, стоимость', 3552, 'руб', 'Стул -', 105, 'шт, стоимость', 10311, 'руб')

# Тесты для zoo.py
def test_new_animal():
    zoo = ["lion", "kangaroo", "elephant", "monkey"]
    result = T.six.new_animal(zoo, 1, "bear")
    assert result == ["lion", "bear", "kangaroo", "elephant", "monkey"]

def test_get_animal_index_pretty():
    zoo = ["lion", "kangaroo", "elephant", "monkey", "rooster", "ostrich", "lark"]
    assert T.six.get_animal_index_pretty(zoo, "lion") == 1
    assert T.six.get_animal_index_pretty(zoo, "lark") == 7
