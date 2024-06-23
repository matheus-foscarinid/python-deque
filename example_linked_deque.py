from linked_deque import LinkedDeque

class Task:
  def __init__(self, task_id, priority):
    self.task_id = task_id
    # True para alta prioridade, False para baixa
    self.priority = priority

  def __str__(self):
    return f"Task ID: {self.task_id}, Priority: {'High' if self.priority else 'Low'}"

def insert_by_priority(task_deque, new_task):
  # Adiciona tarefa de alta prioridade ao início
  if new_task.priority:
    task_deque.insert_first(new_task)
  # Adiciona tarefa de baixa prioridade ao final
  else:
    task_deque.insert_last(new_task)  

def execute_tasks(task_deque):
  while not task_deque.is_empty():
      # Remove e obtém a tarefa do início do deque
      current_task = task_deque.remove_first()  
      print(f"Executing {current_task}")

def example():
    task_deque = LinkedDeque()

    # Criação de tarefas
    simple_task = Task(1, False)
    simple_task_2 = Task(2, False)
    simple_task_3 = Task(4, False)
    important_task = Task(3, True)
    important_task_2 = Task(5, True)

    # Adiciona tarefas ao deque por prioridade
    insert_by_priority(task_deque, simple_task)
    insert_by_priority(task_deque, important_task)
    insert_by_priority(task_deque, simple_task_2)
    insert_by_priority(task_deque, simple_task_3)
    insert_by_priority(task_deque, important_task_2)

    # Executa tarefas
    execute_tasks(task_deque)

example()