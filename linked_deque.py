from adt_deque import ADTDeque
from node import Node

# LinkedDeque class implementation
class LinkedDeque(ADTDeque):
  def __init__(self) -> None:
    self._head: Node = None
    self._tail: Node = None
    self._count: int = 0

  def __len__(self) -> int:
    return self._count

  def __str__(self) -> str:
    values_str = " ".join([str(elm) for elm in self])
    return "[ " + values_str + " ]"

  def __iter__(self) -> object:
    current = self._head
    while current is not None:
      yield current.value
      current = current.next

  def is_empty(self) -> bool:
    return self._count == 0

  def insert_first(self, value: any) -> None:
    new_node = Node(value)
    if self.is_empty():
      self._head = self._tail = new_node
    else:
      new_node.next = self._head
      self._head.prev = new_node
      self._head = new_node
    self._count += 1

  def insert_last(self, value: any) -> None:
    new_node = Node(value)

    if self.is_empty():
      self._head = self._tail = new_node
    else:
      new_node.prev = self._tail
      self._tail.next = new_node
      self._tail = new_node

    self._count += 1

  def peek_first(self) -> any:
    return self._head.value

  def peek_last(self) -> any:
    return self._tail.value

  def remove_first(self) -> any:
    if self.is_empty():
      raise UnderflowError()

    first_node = self._head
    self._head = self._head.next
    self._count -= 1
    return first_node

  def remove_last(self) -> any:
    if self.is_empty():
      raise UnderflowError()

    last_node = self._tail
    self._tail = self._tail.prev
    self._count -= 1
    return last_node
