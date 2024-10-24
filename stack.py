# Stack(using built-in functions)  LIFO  ( last in first out)
class Stack:     
  def __init__(self):
    self.data = []      # empty list

  def is_empty(self):
    return self.data == []

  def push(self, item):
    self.data.append(item)   # appending items into the list to the end of the list

  def pop(self):
    if self.is_empty(): # len(self.data) == 0: # if self.data == [] ( is also a possible command to follow through from line 4)
      return "cannot pop from empty stack"           # if its empty, it will return
    return self.data.pop()  # After removable of last item, return to the calling prog

  def display(self):
    if self.is_empty():
        print('empty stack')
    else:    
    #     for i in range(len(self.data)):   
        for i in range(len(self.data)-1, -1, -1):  # Reverse the order. Top value then lower value
          print(self.data[i], end=' ')
        print() 

# Main
stack = Stack()    # Will run line 3 and 4
stack.display()
stack.push(15)
stack.push(20)
stack.display()
print(stack.pop())   # show what has been removed

print(stack.pop())   # removes the remaining item
print(stack.pop())   # check if we have an empty stack and the command is working
stack.display()
