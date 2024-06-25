from adt_deque import ADTDeque
from linked_deque import LinkedDeque

def test_deque_methods():
  deque: ADTDeque = LinkedDeque()

  for i in range(10):
    deque.insert_last(i)

  print('Deque preenchido: ', deque)

  deque.remove_first()
  print('Removendo o primeiro elemento: ', deque)
  
  deque.insert_first(0)
  print('Adicionando o primeiro elemento de volta: ', deque)

  deque.remove_last()
  print('Removendo o último elemento: ', deque)

  first_item = deque.peek_first()
  last_item = deque.peek_last()

  print('Primeiro elemento do deque: ', first_item)
  print('Último elemento do deque: ', last_item)
  print('Tamanho da Deque: ', len(deque))
  
  print('Iterando sobre o deque: ', end='')
  
  for item in deque:
    print(item, end=', ')

def test_empty_deque():
  deque: ADTDeque = LinkedDeque()
  print('Deque vazio: ', deque)
  
  print('Tamanho da Deque vazia: ', len(deque))
  print('Deque vazio? ', deque.is_empty())
  
  try:
    print('Tentando remover o primeiro elemento da Deque vazia...')
    deque.remove_first()
  except Exception as e:
    print('Erro:', e)
  
  
if __name__ == '__main__':
  test_deque_methods()
  test_empty_deque()