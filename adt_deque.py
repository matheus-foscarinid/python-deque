from abc import ABC, abstractmethod

class ADTDeque(ABC):
  # Verifica se o deque está vazio
  @abstractmethod
  def is_empty(self) -> bool: ...

  # Insere um valor no início do deque
  @abstractmethod
  def insert_first(self, value: object) -> None: ...

  # Insere um valor no final do deque
  @abstractmethod
  def insert_last(self, value: object) -> None: ...

  # Remove e retorna o valor do início do deque
  @abstractmethod
  def remove_first(self) -> object: ...

  # Remove e retorna o valor do final do deque
  @abstractmethod
  def remove_last(self) -> object: ...

  # Retorna o valor do início do deque sem remover
  @abstractmethod
  def peek_first(self) -> object: ...

  # Retorna o valor do final do deque sem remover
  @abstractmethod
  def peek_last(self) -> object: ...

  # Retorna o número de elementos no deque
  @abstractmethod
  def __len__(self) -> int: ...

  # Retorna uma representação em string do deque
  @abstractmethod
  def __str__(self) -> str: ...

  # Retorna um iterador para os elementos do deque
  @abstractmethod
  def __iter__(self) -> object: ...



