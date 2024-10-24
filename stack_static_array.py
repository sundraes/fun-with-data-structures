# stack(static array_LIFO)
class Stack:
    SIZE = 5
    def __init__(self):
        self.data = [None] * self.SIZE   #to put into the stack
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.SIZE - 1
    
    def push(self, item):
        if self.is_full():
            print('stack is full')
        else:
            self.top += 1
            self.data[self.top] = item 
    
    def pop(self):
        if self.is_empty():
            return 'cannot pop from empty stack'
        item = self.data[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            return 'cannot pop from empty stack'
        return self.data[self.top]
    
    def display(self):
        if self.is_empty():
            print('empty stack')
        else:
            for i in range(self.top, -1, -1):
                print(self.data[i], end=' ')
            print()         
                        
# Main
stack = Stack()  # Will run line 3 and 4 
print(stack.data)
print(stack.top)


stack.display()    
stack.push(15)
stack.push(20)
print(stack.data)
print(stack.top)
print(f"top item: {stack.peek()}")
stack.display()
print(stack.pop())   # show what has been removed
print(stack.pop())   # removes the remaining item
print(stack.pop())   # check if we have an empty stack and the command is working
stack.display()
print(stack.peek())
