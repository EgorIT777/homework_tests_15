import unittest

from task_09_word_analysis_2.main import check_palindrome


class Test09CheckPalindrome(unittest.TestCase):
    def test_check_palindrome_madam(self):
        """
        Проверяем обычный кейс. При вводе "мадам" True
        """
        word = input('Введите слово: ')
        palindrome = 'Слово является палиндромом'
        not_palindrome = 'Слово не является палиндромом'
        for i in range(len(word) // 2):
            if word[i] == word[- 1 - i]:
                return palindrome
        else:
            return not_palindrome



    def test_check_palindrome_abccba(self):
        """
        Проверяем обычный кейс. При вводе "abccba" должны получить True
        """



    def test_check_palindromen_abbd(self):
        """
        Проверяем обычный кейс. При вводе "abbd" должны получить False
        """



if __name__ == '__main__':
    unittest.main()
