"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list.
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    if self.tail is None:
      first_node = Node(value)
      self.head = first_node
      self.tail = first_node
    else:
      newest_node = Node(value)
      self.tail.next_node = newest_node
      self.tail = newest_node
      self.tail.next_node = None

  def remove_head(self):
    if self.head:
      current_head = self.head
      self.head = self.head.get_next()
      self.tail = None
      return current_head.value

  def contains(self, value):
    if self.head:
      search_node = self.head
      while search_node is not None:
        if search_node.value == value:
          return True
        search_node = search_node.next_node
      return False

  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current_head = self.head.get_next()
    while current_head:
      if current_head.value > max_value:
        max_value = current_head.value
      current_head = current_head.next_node
    return max_value
