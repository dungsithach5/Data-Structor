class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]




def infix_to_suffix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    suffix = ''

    for char in expression:
        if char.isalnum():
            suffix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.top() != '(':
                suffix += stack.pop()
            stack.pop() 
        else:
            while (not stack.is_empty()) and (precedence.get(char, 0) <= precedence.get(stack.top(), 0)):
                suffix += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        suffix += stack.pop()

    return suffix


def evaluate_infix(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid expression"

if __name__ == "__main__":
    E = input("Nhập biểu thức E: ")
    postfix_expression = infix_to_suffix(E)
    print(f"Eprefix: {postfix_expression}")
    value = evaluate_infix(E)
    print(f"Result: {value}")
    
    