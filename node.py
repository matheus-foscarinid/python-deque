class Node:
  def __init__(self, value: any) -> None:
    self.value: any = value
    self.next: Node = None
    self.prev: Node = None

  # Retorna uma representação em string do Node
  def __str__(self) -> str:
    return str(self.value)