class Stack:
    def __init__(self, size):
        self.items = [] ;
        self.size = size
        self.indx=-1

    def is_empty(self):
        """
        Check The List items if it is empty.
        Returns true if empty false if not.
        """
        # Write code here
        if stack.indx == -1:
            return True
        return False



    def is_full(self):
        """
        Check if The stack is full.
        Returns true if full
        returns false if not full.
        """
        # Write code here
        if stack.indx== stack.size-1 :
            return True
        return False

    def push(self, data):
        """
        Pushes value to stack if stack is empty. 
        
        Args:
        data: The value to be pushed.
        """
        if not self.is_full():
            # Write code here
            stack.items.append(data)
            stack.indx=stack.indx+1

    def pop(self):
        """ 
        Pushes the top value out of stack.
        """
        if not self.is_empty():
            # Write code here
            stack.items.pop()
            stack.indx=stack.indx-1

    def status(self):
        # Write code here
        for i in range(0, len(stack.items)):
             print(stack.items[i],end="\n")
             

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
