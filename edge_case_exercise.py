def move(my_list, direction=None):
    if direction == 'right':
      if index_of_one == -1:
        return my_list
      else:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    else direction == 'left':
      if index_of_one == 0:
        return my_list
      elif:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
    
    return my_list
