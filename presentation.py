from adt_deque import ADTDeque
from linked_deque import LinkedDeque

if __name__ == '__main__':
    list: ADTDeque = LinkedDeque()

    for i in range(10):
        list.insert_last(i)

    print('Lista preenchida: ', list)

    list.remove_first()
    print('Removendo o primeiro elemento: ', list)
    
    list.insert_first(0)
    print('Adicionando o primeiro elemento de volta: ', list)

    list.remove_last()
    print('Removendo o último elemento: ', list)

    first_item = list.peek_first()
    last_item = list.peek_last()

    print('Primeiro elemento da lista: ', first_item)
    print('Último elemento da lista: ', last_item)
    print('Tamanho da lista: ', len(list))