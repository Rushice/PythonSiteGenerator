from ..htmlnode import HTMLNode
from .markdowntoblocks import BlockType, block_to_block_type, markdown_to_blocks


def markdown_to_html_node(markdown):
  # Split the markdown to blocks
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    block_type = block_to_block_type(block)
    html_node: HTMLNode = None
    match block_type:
      case BlockType.PARAGRAPH:
        pass
  pass