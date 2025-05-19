import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_node_creation(self):
        node = HTMLNode("tag", "value",)
        self.assertEqual(repr(node), "HTMLNode(tag, value, None, None)")
        
    def test_is_instance(self):
        node = HTMLNode("tag", "value", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertIsInstance(node, HTMLNode)
        
    def test_props_to_html(self):
        node = HTMLNode("tag", "value", None, {"href":"https://www.google.com", "target":"_blank"})
        props = node.props_to_html()
        self.assertEqual(props, " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_with(self):
        node = LeafNode("p", "Hello, world!", {"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), "<p href=\"https://www.google.com\">Hello, world!</p>")
        
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
        
    def test_empty_parent_node(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)


if __name__ == "__main__":
    unittest.main()