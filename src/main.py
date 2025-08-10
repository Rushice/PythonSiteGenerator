
from email.mime import base
import os
import shutil
import sys

from src.util.markdowntohtml import markdown_to_html_node
from src.util.markdowntoblocks import BlockType, block_to_block_type, markdown_to_blocks

def main():
  basepath = "/"
  if len(sys.argv) > 1:
    basepath = sys.argv[1]

  public_path = "docs"
  reset_build_dir(public_path, "static")
  generate_pages_recursive("content","template.html", public_path, basepath)

def reset_build_dir(public_path, static_path):

  if not os.path.exists(static_path) or not os.path.isdir(static_path):
    raise Exception("Static dir path does not exists or its not a directory")

  if os.path.exists(public_path) and os.path.isdir(public_path):
    shutil.rmtree(public_path)

  copy_to_path(static_path,public_path)


def copy_to_path(source, dest):
  # check if source is valid
  if os.path.exists(source) == False:
    raise Exception("Source path does not exist")

  if os.path.exists(dest) == False:
    os.mkdir(dest)
  for item in os.listdir(source):
    item_path = os.path.join(source,item)
    print(f"curr: {item_path}")
    if os.path.isfile(item_path):
      shutil.copy(item_path,dest)
    else:
      dest_dir = os.path.join(dest,item)
      copy_to_path(item_path,dest_dir)

def extract_title(markdown):
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    if block_to_block_type(block) is BlockType.HEADING:
      if block.startswith("# "):
        return block[2:].strip()

def generate_page(from_path,template_path,dest_path,basepath):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  dirs_to_create = os.path.dirname(dest_path)
  if len(dirs_to_create) > 0:
    os.makedirs(dirs_to_create,exist_ok=True)
  with open(from_path, 'r') as source_file, open(template_path, 'r') as template_file, open(dest_path,'w') as dest_file:
    source_contents = source_file.read()
    template_contents = template_file.read()

    source_html = markdown_to_html_node(source_contents).to_html()
    page_title = extract_title(source_contents)

    template_contents = template_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", source_html).replace("href=\"/",f"href=\"{basepath}").replace("src=\"/",f"src=\"{basepath}")

    dest_file.write(template_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
  if os.path.exists(dir_path_content) == False:
    raise Exception("Source path does not exist")

  if os.path.exists(dest_dir_path) == False:
    os.mkdir(dest_dir_path)

  for item in os.listdir(dir_path_content):
    item_path = os.path.join(dir_path_content,item)
    dest_dir = os.path.join(dest_dir_path,item)

    if os.path.isfile(item_path):
      dest_dir = dest_dir.replace(".md",".html")
      generate_page(item_path,template_path,dest_dir,basepath)
    else:
      generate_pages_recursive(item_path,template_path,dest_dir,basepath)

if __name__ == "__main__":
  main()