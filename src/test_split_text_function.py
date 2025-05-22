import unittest

from textnode import TextNode, TextType
from splitfunctions import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_case = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_case)
        
    def test_bold_split(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_case = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_case)
        
    def test_italic_split(self):
        node = TextNode("This is text with a __italic block__ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.ITALIC)
        test_case = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_case)

    def test_no_split(self):
        node = TextNode("**This is text with a bold block word**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_case = [
            TextNode("**This is text with a bold block word**", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, test_case)
        
    def test_multiple_nodes_split(self):
        nodes = [
            TextNode("This is text with a **bold block** word", TextType.TEXT),
            TextNode("This is more text with a **bold block** word also", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        test_case = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is more text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word also", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_case)
        
    def test_multiple_bold_split(self):
        node = TextNode("This is text with a **bold block** word and **bold block 2** another", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_case = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word and ", TextType.TEXT),
            TextNode("bold block 2", TextType.BOLD),
            TextNode(" another", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, test_case)

if __name__ == "__main__":
    unittest.main()