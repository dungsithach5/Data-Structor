class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    output = []
    operator_stack = Stack()

    for char in infix_expression.split():
        if char.isdigit():
            output.append(char)
        elif char == '(':
            operator_stack.push(char)
        elif char == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Discard '('
        else:
            while not operator_stack.is_empty() and precedence[operator_stack.peek()] >= precedence[char]:
                output.append(operator_stack.pop())
            operator_stack.push(char)

    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return ' '.join(output)

# Biểu thức trung tố đầu vào
infix_expression = "( 1 + 5 ) + ( 3 - 2 ) * ( 8 / ( 4 - 1 ) ) - 2"

# Chuyển biểu thức trung tố thành biểu thức hậu tố
postfix_expression = infix_to_postfix(infix_expression)
print("Biểu thức hậu tố:", postfix_expression)
