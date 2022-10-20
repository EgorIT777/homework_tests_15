import unittest

from task_05_movie.main import add_favorite_film


class Test05AddFavoriteFilm(unittest.TestCase):
    def test_add_favorite_film(self):
        """
        Проверяем обычный кейс. При вводе ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
         должны получить (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
        """
        lst = []
        print('введите фильмы')
        while True:
            s = input()
            if not s: break
            lst.append(s)
        return lst


if __name__ == '__main__':
    unittest.main()
