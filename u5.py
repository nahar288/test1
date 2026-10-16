import unittest
import main

class TestString(unittest.TestCase):
    def test_reverse(self):
        r1 = main.reverse("omen")
        self.assertEqual(r1, "nemo")
        self.assertNotEqual(r1, "omen")

    def test_vowels(self):
        r2 = main.vowels("hello")
        self.assertEqual(r2, 2)
        self.assertTrue(r2 > 0)
        self.assertFalse(r2 == 0)
        self.assertIn(r2, [3, 2, 4])
        self.assertIsInstance(r2, int)

    def test_words(self):
        r3 = main.words("I hate Python")
        self.assertEqual(r3, 3)

    
    def test_error(self):
        with self.assertRaises(TypeError):
            main.reverse(123)
        with self.assertRaises(TypeError):
            main.vowels(None)
        with self.assertRaises(TypeError):
            main.words(45)
        

if __name__ == "__main__":
    unittest.main()
