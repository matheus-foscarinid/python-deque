from adt_deque import ADTDeque
from node import Node
from errors import UnderflowError

class LinkedDeque(ADTDeque):
  def __init__(self) -> None:
    self._head: Node = None
    self._tail: Node = None
    self._count: int = 0

  # Complexidade: O(1)
  def __len__(self) -> int:
    return self._count

  # Complexidade: O(n)
  def __str__(self) -> str:
    values_str = " ".join([str(elm) for elm in self])
    return "[ " + values_str + " ]"

  # Complexidade: O(n)
  def __iter__(self) -> object:
    current = self._head
    while current:
      yield current.value
      current = current.next

  # Complexidade: O(1)
  def is_empty(self) -> bool:
    return self._count == 0

  # Complexidade: O(1)
  def insert_first(self, value: object) -> None:
    new_node = Node(value)
    if self.is_empty():
      self._head = self._tail = new_node
    else:
      new_node.next = self._head
      self._head.prev = new_node
      self._head = new_node
    self._count += 1

  # Complexidade: O(1)
  def insert_last(self, value: object) -> None:
    new_node = Node(value)

    if self.is_empty():
      self._head = self._tail = new_node
    else:
      new_node.prev = self._tail
      self._tail.next = new_node
      self._tail = new_node

    self._count += 1

  # Complexidade: O(1)
  def peek_first(self) -> object:
    if self.is_empty():
      raise UnderflowError()
    return self._head.value

  # Complexidade: O(1)
  def peek_last(self) -> object:
    if self.is_empty():
      raise UnderflowError()
    return self._tail.value

  # Complexidade: O(1)
  def remove_first(self) -> object:
    if self.is_empty():
      raise UnderflowError()

    first_node = self._head

    if self._head == self._tail:
      self._head = self._tail = None
    else:
      self._head = self._head.next
      self._head.prev = None

    self._count -= 1
    return first_node

  # Complexidade: O(1)
  def remove_last(self) -> object:
    if self.is_empty():
      raise UnderflowError()

    last_node = self._tail

    if self._head == self._tail:
      self._head = self._tail = None
    else:
      self._tail = self._tail.prev
      self._tail.next = None

    self._count -= 1
    return last_node
