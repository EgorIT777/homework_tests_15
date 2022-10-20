import unittest
from task_04_videocards.main import select_video_cards


class Test04SelectVideoCards(unittest.TestCase):
    def test_select_video_cards(self):
        """
        Проверяем обычный кейс. [3070, 2060, 3090, 3070, 3090]  должны получить [3070, 2060, 3070]
        """
        old_video_cards = []
        quantity_video_cards = int(input('Кол-во видеокарт: '))
        for i in range(quantity_video_cards):
            id_video_cards = int(input(f'{i + 1} Видеокарта: '))
            old_video_cards.append(id_video_cards)
        return old_video_cards





    def test_select_video_cards_no_result(self):
        """
        Проверяем обычный кейс. [3070, 3070]  должны получить []
        """





if __name__ == '__main__':
    unittest.main()
