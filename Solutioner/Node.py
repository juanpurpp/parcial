from functools import cmp_to_key

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def similar(a, b):
  coincidences = 0
  for index,char in enumerate(a):
    if(b[index] == char): coincidences += 1
  return coincidences

class Node:
  def __init__(self, literal_state, father):
    self.literal_state = literal_state
    self.father = father

  def get_choices(self):
    result = []
    # sample of literal_state xxx_ooo .
    # other samples
    # xx_oxoo

    #x_xoxoo
    state = self.literal_state
    length = len(state)
    space_index = state.find('_')
    if(space_index != 0):
      frog = state[space_index - 1]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index-1) #new_state[space_index -1] = '_'
      result.append(Node(new_state, self))
    if(space_index > 1):
      frog = state[space_index - 2]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index-2) 
      result.append(Node(new_state, self))
    if(space_index != length-1):
      frog = state[space_index + 1]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index+1) 
      result.append(Node(new_state, self))
    if(space_index < length-2):
      frog = state[space_index + 2]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index+2) 
      result.append(Node(new_state, self))
    return result

  def get_choices_with_h(self, final_state, b=4):
    result = []
    # sample of literal_state xxx_ooo .
    # other samples
    # xx_oxoo

    #x_xoxoo
    state = self.literal_state
    length = len(state)
    space_index = state.find('_')
    if(space_index != 0):
      frog = state[space_index - 1]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index-1) #new_state[space_index -1] = '_'
      result.append(Node(new_state, self))
    if(space_index > 1):
      frog = state[space_index - 2]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index-2) 
      result.append(Node(new_state, self))
    if(space_index != length-1):
      frog = state[space_index + 1]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index+1) 
      result.append(Node(new_state, self))
    if(space_index < length-2):
      frog = state[space_index + 2]
      new_state = state
      new_state = replacer(new_state, frog, space_index) #new_state[space_index] = frog
      new_state = replacer(new_state, '_', space_index+2) 
      result.append(Node(new_state, self))
    result = sorted(result, key=cmp_to_key(lambda a,b: self.get_h(b) - self.get_h(a)),)
    
    result = result[0:b]
    return result

  def get_h(self, final_state):
    #using hamming
    print('fs', self.literal_state)
    print('ss', final_state)
    return similar(self.literal_state, str(final_state))

  def __str__(self):
    return self.literal_state
  
  def get_father(self):
    return self.father
  
  def __eq__(self, other):
    if(other is None): return False
    return self.literal_state == other.literal_state
    
  def print_path(self):
    current_state = self
    length = 0
    while current_state != None:
      print(current_state)
      current_state = current_state.get_father()
      length+=1
    print(' Final path length: '+str(length))