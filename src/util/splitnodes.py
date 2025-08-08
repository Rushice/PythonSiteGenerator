
from .extractmarkdown import extract_markdown_images, extract_markdown_links
from ..textnode import TextNode, TextType

# For now assume all nodes are plain text
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):

  new_nodes: list[TextNode] = []
  for node in old_nodes:
    # if node is not TEXT type add to new list
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue

    chunks = node.text.split(delimiter)
    # check if there is a matching delimiter
    # if length of chunks can be divided by 2, there isnt a matching delimiter e.g. 1"2"3"4 < 4 chunks have only 3 delimiters, odd index chunks will be converted
    if len(chunks)%2 == 0:
      raise Exception("There is a missing delimiter")

    for i in range(0, len(chunks)):
      new_node = TextNode(chunks[i],TextType.TEXT)
      if i % 2 != 0:
        new_node.text_type = text_type
      new_nodes.append(new_node)

  return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
  new_nodes:list[TextNode] = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    new_nodes.extend(split_node_image(node))
  return new_nodes

def split_node_image(node: TextNode, node_list: list[TextNode]=None):
  if node_list is None:
    node_list = []
  # find image match
  matches = extract_markdown_images(node.text)
  # no match append node
  if len(matches) == 0:
    node_list.append(node)
    return node_list

  # split the text with the first match
  match = matches[0]
  curr_match = f"![{match[0]}]({match[1]})"
  splits = node.text.split(curr_match,1) # split once
  if len(splits[0]) > 0:
    split_node_image(TextNode(splits[0],TextType.TEXT),node_list)

  node_list.append(TextNode(match[0],TextType.IMAGE,match[1]))
  if len(splits[1]) > 0:
    split_node_image(TextNode(splits[1],TextType.TEXT),node_list)

  return node_list



def split_nodes_link(old_nodes: list[TextNode]):
  new_nodes:list[TextNode] = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    new_nodes.extend(split_node_link(node))
  return new_nodes

def split_node_link(node: TextNode, node_list: list[TextNode]=None):
  if node_list is None:
    node_list = []
  # find image match
  matches = extract_markdown_links(node.text)
  # no match append node
  if len(matches) == 0:
    node_list.append(node)
    return node_list

  # split the text with the first match
  match = matches[0]
  curr_match = f"[{match[0]}]({match[1]})"
  splits = node.text.split(curr_match,1) # split once
  if len(splits[0]) > 0:
    split_node_link(TextNode(splits[0],TextType.TEXT),node_list)

  node_list.append(TextNode(match[0],TextType.LINK,match[1]))
  if len(splits[1]) > 0:
    split_node_link(TextNode(splits[1],TextType.TEXT),node_list)

  return node_list


def text_to_textnodes(text):
  nodes = [TextNode(text,TextType.TEXT)]
  nodes = split_nodes_delimiter(nodes, "**",TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_",TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`",TextType.CODE)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
  return nodes
