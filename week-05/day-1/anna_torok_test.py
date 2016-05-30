import unittest
from anna_torok_work import anagram, count_letters

class TestTwoAnagrams(unittest.TestCase):

    def test_two_string_anagrams_true(self):
        self.assertTrue(anagram('mary', 'yram'))

    def test_two_string_anagrams_false(self):
        self.assertFalse(anagram('albert', 'rokalb'))

    def test_number_and_string_anagrams_false(self):
        self.assertFalse(anagram('10001', 'amadeus'))

    def test_number_and_number_anagrams_false(self):
        self.assertTrue(anagram('10001', '00101'))

    def test_two_string_with_uppercase_anagrams_false(self):
        self.assertFalse(anagram('Kalman', 'mankal'))

    def test_empty_strings_anagrams_true(self):
        self.assertTrue(anagram('', ''))

    def test_two_strings_with_hypen_nagrams_true(self):
        self.assertTrue(anagram('al-ma', '-lama'))

    def test_two_strings_with_space_anagrams_true(self):
        self.assertTrue(anagram(' lomha', 'ha lom'))

    def test_count_letters(self):
        self.assertEqual(count_letters('almafa'), count_letters('lamaaf'))

    def test_count_with_hypen_letters(self):
        self.assertEqual(count_letters('lomha-macska'), count_letters('-scakmahomal'))

    def test_count__with_not_letters(self):
        self.assertNotEqual(count_letters('lomham1acska'), count_letters('scakmahomal3d'))

    def test_count__with_uppercase_letters(self):
        self.assertEqual(count_letters('lomhaMacska'), count_letters('scAkmahomal'))

    def test_count__empty_letters(self):
        self.assertEqual(count_letters(''), {})


if __name__  == '__main__':
     unittest.main()
