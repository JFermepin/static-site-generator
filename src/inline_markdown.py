import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if images == []:
            new_nodes.append(old_node)
            continue
        split_old_text = old_node.text
        split_nodes = []
        for i in range(len(images)):
            alt_text, url = images[i]
            split_old_text = split_old_text.split(f"![{alt_text}]({url})", 1)
            if len(split_old_text) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if i == len(images) - 1:
                split_nodes.append(TextNode(split_old_text[0], TextType.TEXT))
                split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                if len(split_old_text[1]) > 0:
                    split_nodes.append(TextNode(split_old_text[1], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_old_text[0], TextType.TEXT))
                split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                split_old_text = split_old_text[1]

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if links == []:
            new_nodes.append(old_node)
            continue
        split_old_text = old_node.text
        split_nodes = []
        for i in range(len(links)):
            anchor, url = links[i]
            split_old_text = split_old_text.split(f"[{anchor}]({url})", 1)
            if len(split_old_text) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if i == len(links) - 1:
                split_nodes.append(TextNode(split_old_text[0], TextType.TEXT))
                split_nodes.append(TextNode(anchor, TextType.LINK, url))
                if len(split_old_text[1]) > 0:
                    split_nodes.append(TextNode(split_old_text[1], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_old_text[0], TextType.TEXT))
                split_nodes.append(TextNode(anchor, TextType.LINK, url))
                split_old_text = split_old_text[1]

        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_image(split_nodes_link([text_node])), "`", TextType.CODE), "**", TextType.BOLD), "_", TextType.ITALIC)