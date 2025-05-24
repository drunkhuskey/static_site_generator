from textnode import TextType, TextNode
import re


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "__", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("invalid Markdown syntax")
            for i in range(0, len(split_text)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            sections = [node.text]
            for image in images:
                last = str(sections.pop())
                sections.extend(last.split(f"![{image[0]}]({image[1]})", 1))
            for i in range(0, len(images)):
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
                new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
            if sections[-1] != "":
                new_nodes.append(TextNode(sections[-1], TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            sections = [node.text]
            for link in links:
                last = str(sections.pop())
                sections.extend(last.split(f"[{link[0]}]({link[1]})", 1))
            for i in range(0, len(links)):
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
                new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
            if sections[-1] != "":
                new_nodes.append(TextNode(sections[-1], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links