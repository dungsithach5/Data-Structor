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
    postfix = ''

    for char in expression:
        if char.isdigit():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.top() != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty()) and (precedence.get(char, 0) <= precedence.get(stack.top(), 0)):
                postfix += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

def infix_to_prefix(infix):
  prefix = []
  stack = []

  formatted_expression = format_expression(infix)
  reversed_expression = reversed(formatted_expression.split())

  for token in reversed_expression:
    if is_operand(token):
      prefix.append(token)
    elif token == ")":
      stack.append(token)
    elif token == "(":
      while stack and stack[-1] != ")":
        prefix.append(stack.pop())
      stack.pop()  
    else:
      while stack and get_priority(token) <= get_priority(stack[-1]):
        prefix.append(stack.pop())
      stack.append(token)

  while stack:
    prefix.append(stack.pop())

  return " ".join(prefix[::-1])




if __name__ == "__main__":
    expression = "5+2*(3-4)"
    print("Input Expression:", expression)
    postfix_expression = infix_to_suffix(expression)
    print("Postfix Expression:", postfix_expression)
