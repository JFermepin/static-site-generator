import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://another-example.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()