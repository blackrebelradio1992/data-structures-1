c
lass Stack_demo:
    def __init__(self):
        self.str_items = []

    # push - add item to top
    def push(self, item):
        self.str_items.append(item)

    # pop - remove and return item from top
    def pop(self):
        if not self.is_empty():
            return self.str_items.pop()
        else:
            return "Stack is empty"

    # peek - return top item
    def peek(self):
        if not self.is_empty():
            return self.str_items[-1]
        else:
            return "Stack is empty"

    # size - return the number of items
    def size(self):
        return len(self.str_items)

    # is_empty - True if no items, False otherwise
    def is_empty(self):
        return len(self.str_items) == 0

# Create a Stack_demo object
stack = Stack_demo()

# Test the stack operations
print("Is the stack empty?", stack.is_empty())

stack.push("apple")
stack.push("banana")
stack.push("cherry")

print("Is the stack empty?", stack.is_empty())
print("Stack size:", stack.size())
print("Top item:", stack.peek())
print("Popped item:", stack.pop())
print("Stack size:", stack.size())
