from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    type = BlockType.PARAGRAPH
    if block[0] == "#" and block[:7] != "#######":
        stripped = block.strip("#")
        if stripped[0] == " ":
            type = BlockType.HEADING
    if block[:3] == "```" and block [-3:] == "```":
        type = BlockType.CODE
    line_split = block.split("\n")
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    ordered_list_index = 1
    for line in line_split:
        if line[0] != ">":
            is_quote = False
        if line[0:2] != "- ":
            is_unordered_list = False
        if line[0:3] != f"{ordered_list_index}. ":
            is_ordered_list = False
        ordered_list_index += 1
    if is_quote: type = BlockType.QUOTE
    if is_unordered_list: type = BlockType.UNORDERED_LIST
    if is_ordered_list: type = BlockType.ORDERED_LIST
    return type