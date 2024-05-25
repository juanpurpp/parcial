from Solutioner.Node import Node

class Solutioner:
  def __init__(self, init_state):
    self.init_state = init_state
  
  def start_breadth(self, final_state):
    print('---- STARTING BEAM ----')
    final = Node(final_state,None)
    queue = []
    checked = []
    current_state = Node(self.init_state, None)
    checked.append(current_state)
    iterations = 1
    while(not(current_state == final)):
      iterations+=1
      choices = current_state.get_choices()
      for choice in choices:
        if choice not in checked:
          checked.append(choice)
          queue.append(choice)
      current_state = queue.pop(0)
      print(current_state)
    
    print('\n\n\n-------------------------------------------------------------\n\n\n')
    print(' Resutlts: ')
    print(' iterations: '+ str(iterations))
    print('\n\n\n-------------------------------------------------------------\n\n\n')
    print(' Final path: ')
    current_state.print_path()

  def start_beam(self, final_state, b=4):
    print('---- STARTING BEAM ----')
    final = Node(final_state,None)
    queue = []
    checked = []
    current_state = Node(self.init_state, None)
    checked.append(current_state)
    iterations = 1
    while(not(current_state == final) and len(queue) !=0):
      iterations+=1
      choices = current_state.get_choices_with_h(final_state,b)
      for choice in choices:
        if choice not in checked:
          checked.append(choice)
          queue.append(choice)
      current_state = queue.pop(0)
      print(current_state)
    
    print('\n\n\n-------------------------------------------------------------\n\n\n')
    print(' Resutlts: ')
    print(' iterations: '+ str(iterations))
    print('\n\n\n-------------------------------------------------------------\n\n\n')
    print(' Final path: ')
    current_state.print_path()
      
      