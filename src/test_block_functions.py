import unittest

from blockfunctions import BlockType, block_to_block_type


class TestBlockFunctions(unittest.TestCase):
    def test_block_paragraph(self):
        block = "This is a regular paragraph block."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH) 
         
    def test_block_heading_one(self):
        block = "# This is a heading block."
        self.assertEqual(block_to_block_type(block), BlockType.HEADING) 
        
    def test_block_heading_six(self):
        block = "###### This is also a heading block."
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
    def test_block_heading_seven(self):
        block = "####### This is a regular paragraph block despite excessive #."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_block_code(self):
        block = "```This is a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
    def test_block_paragraph_with_code(self):
        block = "'''This is a regular paragraph block despite code start."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_block_quote(self):
        block = ">This is a quote block."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
    def test_block_unordered_list(self):
        block = "- This is an unordered list block.\n- Another line."
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
    def test_block_ordered_list(self):
        block = "1. This is a heading paragraph block.\n2. Another element"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
    def test_block_paragraph_with_bad_ordered_list(self):
        block = "2. This is a regular paragraph block despite index start.\n2. still bad."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()