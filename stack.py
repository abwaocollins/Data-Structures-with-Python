from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        self.container.pop()
    def peek(self):
        self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size_of_stack(self):
        return len(self.container)
    def items(self):
        print("Items in stack")
        for i in self.container:
            print(i)
        return
    def reverse_string(self,data):
        data_list = data.split()
        count = len(data_list) - 1
        while count > -1:
            self.push(data_list[count])
            count = count - 1
        return " ".join(self.container)

    def is_balanced(self,data):
        dic = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        for i in data:
            for k,v in dic.items():
                if i == k:
                    self.push(i)
                
        print(self.container)

        for i in data:
            for k,v in dic.items():
                if i == v and len(self.container) > 0:
                    self.pop()
        return self.is_empty()

new_stack = Stack()
# new_stack.push("Barry")
# new_stack.push("Collins")
# new_stack.push("Stephen")
# new_stack.pop()
# new_stack.peek()
# print("The stack is empty", new_stack.is_empty())
# print(f"The stack has {new_stack.size_of_stack()} items")
# new_stack.items()

# print("Reversed string: ", new_stack.reverse_string("Barry is a fool"))
print(f"Paranthesis balance {new_stack.is_balanced('boy {(({))}')}")