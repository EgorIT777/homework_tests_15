import unittest

from task_06_word_analysis.main import count_number_unique_letters


class Test06CountNumberUniqueLetters(unittest.TestCase):
    def test_main_privet(self):
        """
        Проверяем обычный кейс. При вводе "привет"  должны получить "Кол-во уникальных букв: 6"
        """
        word = input('Введите слово: ')
        word_list = list(word)
        unique_letters = 0

        for i in word_list:
            same_letters = 0
            for j in word_list:
                if j == i:
                    same_letters += 1
            if same_letters == 1:
                unique_letters += 1


    def test_main_lava(self):
        """
        Проверяем обычный кейс. При вводе "лава"  должны получить "Кол-во уникальных букв: 2"
        """



if __name__ == '__main__':
    unittest.main()
