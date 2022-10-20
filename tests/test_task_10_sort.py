import unittest

from task_10_sort.main import sort_list


class Test10Sort(unittest.TestCase):
    def test_sort_list(self):
        """
        Проверяем обычный кейс. При вводе [1, 4, -3, 0, 10] должны получить [-3, 0, 1, 4, 10]
        """
        original_list = []

        for i in range(len(original_list)):
            for cur_elem in range(i, len(original_list)):
                if original_list[i] > original_list[cur_elem]:
                    original_list[cur_elem], original_list[i] = original_list[i], original_list[cur_elem]
        return original_list
        sorted_list = sort_list([1, 4, -3, 0, 10])
        self.assertEqual(sorted_list, [-3, 0, 1, 4, 10])


if __name__ == '__main__':
    unittest.main()
