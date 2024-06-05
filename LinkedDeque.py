# LinkedDeque class implementation
class LinkedDeque(ADTDeque):
  def __init__(self) -> None:
    self._head: Node = None
    self._tail: Node = None
    self._count: int = 0