
from abc import ABC, abstractmethod


class HTMLNode(ABC):
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag: str = tag
    self.value: str = value
    self.children: list[HTMLNode] = children
    self.props: dict = props

  @abstractmethod
  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
    if self.props == None:
      return ""

    result = []

    for key,value in self.props.items():
      result.append(f" {key}=\"{value}\"")

    return "".join(result)

  def __repr__(self):
    return f"HTMLNode({self.tag},{self.value},{self.children},{self.props_to_html()})"