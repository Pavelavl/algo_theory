import tasks as T
import pytest

@pytest.mark.parametrize("numbers, expected", [
    ([1,2,3,4,5],25)
])

def test_operations(numbers, expected):
    assert T.three.find_expression(numbers, 25) == expected

@pytest.mark.parametrize('radius, expected_area', [
    (42, 131.9469),
])

def test_area_circle(radius, expected_area):
    assert T.two.area_calc(radius) == expected_area

@pytest.mark.parametrize('point, radius, expected_status', [
    ((23, 34), 42, True),
    ((30, 30), 42, False),
])

def test_point_in_circle(point, radius, expected_status):
    assert T.two.point_in_circle(point, radius) == expected_status

@pytest.mark.parametrize("my_favorite_movies, expected_output", [
    ('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее', "Терминатор,\nНазад в будущее,\nПятый элемент,\nЧужие."),
    ('Один дома, Интерстеллар, Властелин колец, Ишак Олег', "Один дома,\nИшак Олег,\nИнтерстеллар,\nВластелин колец."),
    ('Гарри Поттер, Звездные войны, Трансформеры, Выживание в Тамбове', "Гарри Поттер,\nВыживание в Тамбове,\nЗвездные войны,\nТрансформеры."),
])

def test_favorite_films(my_favorite_movies, expected_output):
    assert  T.four.search_films(my_favorite_movies) == expected_output

@pytest.mark.parametrize("my_family_height", [
    [['Отец', 180], ['Мать', 165], ['Я', 175], ['Брат', 185], ['Сестра', 160]],
    [['Дедушка', 170], ['Бабушка', 155], ['Отец', 180], ['Мама', 165], ['Я', 175], ['Сестра', 160], ['Брат', 185]],
    [['Дедушка', 170], ['Бабушка', 155], ['Отец', 180], ['Мама', 165], ['Я', 175], ['Сестра', 160], ['Брат', 185], ['Кузен', 170], ['Тётя', 165]]
])
def test_father_height(my_family_height):
    assert T.five.get_father_height(my_family_height) == "Рост отца - 180 см"

@pytest.mark.parametrize("my_family_height", [
    [['Отец', 180], ['Мать', 165], ['Я', 175], ['Брат', 185], ['Сестра', 160]],
])
def test_family_height(my_family_height):
    assert T.five.get_family_height(my_family_height) == "Общий рост моей семьи - "+str(865)+" см"

@pytest.mark.parametrize("zoo, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']),
])

def test_new_animal(zoo, expected_output):
    assert T.six.new_animal(zoo, 1, 'bear') == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']

@pytest.mark.parametrize("zoo, new_animals, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['rooster', 'ostrich', 'lark'], ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']),
])

def test_new_animals(zoo, new_animals, expected_output):
    assert T.six.new_animals(zoo, new_animals) == expected_output

@pytest.mark.parametrize("zoo, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], ['lion', 'kangaroo', 'monkey']),
])

def test_free_the_beast(zoo, expected_output):
    assert T.six.free_the_beast(zoo, 'elephant') == expected_output

@pytest.mark.parametrize("zoo, animal, expected_output", [
    (['lion', 'kangaroo', 'elephant', 'monkey'], 'lion', '1'),
    (['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark'], 'lark', '7'),
])

def test_get_animal_cage(zoo, animal, expected_output):
    assert T.six.get_animal_index_but_for_normal_peoples(zoo, animal) == zoo.index(animal)+1

# Почему-то в словаре и листе разные длины у песен, отсюда была ошибка в тесте
@pytest.mark.parametrize("song_list, songs, expected", [
    ([['World in My Eyes', 4.86],
      ['Sweetest Perfection', 4.43],
      ['Personal Jesus', 4.56],['Halo', 4.9],
      ['Waiting for the Night', 6.07],['Enjoy the Silence', 4.20],
      ['Policy of Truth', 4.76],['Blue Dress', 4.29],['Clean', 5.83]
      ], ["Halo", "Enjoy the Silence", "Clean"],14.93,),
    ([['World in My Eyes', 4.86],
      ['Sweetest Perfection', 4.43],
      ['Personal Jesus', 4.56],['Halo', 4.9],
      ['Waiting for the Night', 6.07],['Enjoy the Silence', 4.20],
      ['Policy of Truth', 4.76],['Blue Dress', 4.29],['Clean', 5.83]
      ], ["Sweetest Perfection", "Policy of Truth", "Blue Dress"], 13.48)
])

def test_get_sound_time_from_song_list(song_list, songs, expected):
    actual = T.seven.get_sound_time_from_song_list(song_list, songs)
    assert round(actual, 2) == expected

@pytest.mark.parametrize("song_dict, songs, expected", [
    ({
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68 }, ["Halo", "Enjoy the Silence", "Clean"], 14.58),
    ({
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68 }, ["Sweetest Perfection", "Policy of Truth", "Blue Dress"], 13.49)
])

def test_get_sound_time_from_song_dict(song_dict, songs, expected):
    actual = T.seven.get_sound_time_from_song_dict(song_dict, songs)
    assert round(actual, 2) == expected

@pytest.mark.parametrize("secret_message, expected_ans", [
    ([
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а'], "в бане веник дороже денег")
])

def test_get_answer(secret_message, expected_ans):
    assert T.eight.get_answer(secret_message) == expected_ans

@pytest.mark.parametrize("tuple_1, tuple_2, expected_output", [
    (('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', ),
     ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', ),
     {'одуванчик', 'подсолнух', 'мак', 'гладиолус', 'ромашка', 'роза', 'клевер'}),
    ((),(), set())
])

def test_make_a_set(tuple_1, tuple_2, expected_output):
    set1 = T.nine.make_a_set(tuple_1)
    set2 = T.nine.make_a_set(tuple_2)
    assert T.nine.union_the_sets(set1, set2) == expected_output

@pytest.mark.parametrize("tuple_1, tuple_2, expected_output", [
    (('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', ),
     ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', ),
     {'одуванчик', 'подсолнух', 'мак', 'гладиолус', 'ромашка', 'роза', 'клевер'}),
    ((),(), set())
])

def test_union_the_sets(tuple_1, tuple_2, expected_output):
    set1 = set(tuple_1)
    set2 = set(tuple_2)
    assert T.nine.union_the_sets(set1, set2) == set1.union(set2)

@pytest.mark.parametrize('tuple_1, tuple_2, expected_output', [
    (('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', ),
     ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', ), {'клевер', 'мак'}),
    ((), (), set())
])

def test_get_unique_elem(tuple_1, tuple_2, expected_output):
    assert T.nine.get_unique_set_elem(set(tuple_2), set(tuple_1)) == expected_output