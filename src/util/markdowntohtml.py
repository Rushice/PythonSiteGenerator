
from src.leafnode import LeafNode
from src.util.splitnodes import text_to_textnodes
from src.util.textnodeconverter import text_node_to_html_node
from src.parentnode import ParentNode
from src.util.markdowntoblocks import BlockType, block_to_block_type, markdown_to_blocks


def markdown_to_html_node(markdown):
  # Split the markdown to blocks
  blocks = markdown_to_blocks(markdown)
  children_nodes = []

  for block in blocks:
    child_block = create_html_node_of_block_type(block)
    children_nodes.append(child_block)

  node = ParentNode("div",children_nodes)
  return node

"""
    Quote blocks should be surrounded by a <blockquote> tag.
    Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
    Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
    Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
    Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
    Paragraphs should be surrounded by a <p> tag.

"""
def create_html_node_of_block_type(block:str) -> ParentNode:
  block_type = block_to_block_type(block)
  match block_type:
    case BlockType.QUOTE:
      lines = block.splitlines()
      lines = [l[2:] for l in lines]
      text = " ".join(lines)
      leaf_nodes = get_leaf_nodes(text)
      return ParentNode("blockquote",leaf_nodes)

    case BlockType.UNORDERED_LIST:
      items = get_list_items(block,2)
      return ParentNode("ul",items)

    case BlockType.ORDERED_LIST:
      items = get_list_items(block,3)
      return ParentNode("ol",items)

    case BlockType.CODE:
      lines = block.splitlines(True)
      text = "".join(lines[1:len(lines)-1])
      leaf_nodes = LeafNode("code",text)
      return ParentNode("pre",[leaf_nodes])

    case BlockType.HEADING:
      i = 0
      while block[i] == '#':
        i += 1
      block = block[i+1:]
      leaf_nodes = get_leaf_nodes(block)
      tag = f"h{i}"
      return ParentNode(tag,leaf_nodes)

    case BlockType.PARAGRAPH:
      block = block.replace('\n',' ')
      leaf_nodes = get_leaf_nodes(block)
      return ParentNode("p",leaf_nodes)

  pass

def get_leaf_nodes(markdown)->list[LeafNode]:
  text_nodes = text_to_textnodes(markdown)
  leaf_nodes = []
  for node in text_nodes:
    leaf_node = text_node_to_html_node(node)
    leaf_nodes.append(leaf_node)

  return leaf_nodes

def get_list_items(markdown, offset) -> list[list[LeafNode]]:
  item_nodes = []
  lines = markdown.splitlines()
  for i in range(len(lines)):
    lines[i] = lines[i][offset:]
    item_nodes.append(get_leaf_nodes(lines[i]))

  parent_nodes = []
  for item in item_nodes:
    parent_nodes.append(ParentNode("li",item))

  return parent_nodes
