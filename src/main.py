from textnode import *

def main():
    test_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(test_node))
    

main()
