import unittest
from generate_page import extract_title

#TEST GENERATE PAGE
class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        text = "# Hello World"
        title = extract_title(text)
        self.assertEqual(title, "Hello World")

    def test_extract_empty_title(self):
        text = ""
        self.assertRaises(Exception, extract_title, text)

    def test_extract_title_with_children(self):
        text = "# Hello World **with bold**"
        title = extract_title(text)
        self.assertEqual(title, "Hello World with bold")

if __name__ == "__main__":
    unittest.main()
