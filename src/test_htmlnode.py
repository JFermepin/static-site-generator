import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode

#HTML NODE TESTS
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", None, {"class": "text"})
        node2 = HTMLNode("div", "This is a text node", None, {"class": "text"})
        self.assertEqual(node, node2)

    def test_different_tag_type(self):
        node = HTMLNode("div", "This is a text node", None, {"class": "text"})
        node2 = HTMLNode("a", "Google", None, {"class": "link", "href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("div", "This is a text node", None, {"class": "text"})
        self.assertEqual(node.props_to_html(), ' class="text"')

#LEAF NODE TESTS
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#PARENT NODE TESTS
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_many_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_one_node = ParentNode("span", [grandchild_node])
        child_two_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_one_node, child_two_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()