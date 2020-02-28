class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

# O(n)
  def reverse_list(self):
    # TO BE COMPLETED
    prev_node = None
    current_node = self.head
    while current_node is not None:
      next_node = current_node.get_next()
      current_node.set_next(prev_node)
      prev_node = current_node
      current_node = next_node
    self.head = prev_node

    # We want a prev, current, and next node to cycle through the list

    # the current node should have the starting point of the head

    # the prev node should start at None because before we change over
    # the current node we will be storing the value of the current node
    # in the prev node to use as a reference point for the next node

    # then if we'd want to move everything over we need to make the prev
    # node the current node and the current node needs to become the
    # next node so that we can loop through the node until the node wants
    # the node to become the node through the node

    # then set the head to become the prev node to reset the node

    # node