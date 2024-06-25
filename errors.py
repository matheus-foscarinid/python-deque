class UnderflowError(Exception):
  def __init__(self, message = "Underflow error occurred"):
    super().__init__(message)