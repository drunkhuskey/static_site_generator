import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()