import unittest

from translator import englishToFrench, frenchToEnglish

class TestWatson(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    
    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_e2f_1(self):
        self.assertNotEqual(englishToFrench(''),'Bonjour')
    
    def test_f2e_1(self):
        self.assertNotEqual(frenchToEnglish(''),'Hello')


if __name__ == "__main__":
    unittest.main()
    