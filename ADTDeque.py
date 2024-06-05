class ADTDeque(ABC):
  # Verifica se o deque está vazio
  @abstractmethod
  def is_empty(self) -> bool: ...

  # Insere um valor no início do deque
  @abstractmethod
  def insert_first(self, value: Any) -> None: ...

  # Insere um valor no final do deque
  @abstractmethod
  def insert_last(self, value: Any) -> None: ...

  # Remove e retorna o valor do início do deque
  @abstractmethod
  def remove_first(self) -> Any: ...

  # Remove e retorna o valor do final do deque
  @abstractmethod
  def remove_last(self) -> Any: ...

  # Retorna o valor do início do deque sem remover
  @abstractmethod
  def peek_first(self) -> Any: ...

  # Retorna o valor do final do deque sem remover
  @abstractmethod
  def peek_last(self) -> Any: ...

  # Retorna o número de elementos no deque
  @abstractmethod
  def __len__(self) -> int: ...

  # Retorna uma representação em string do deque
  @abstractmethod
  def __str__(self) -> str: ...

  # Retorna um iterador para o deque
  @abstractmethod
  def __iter__(self) -> Iterator: ...