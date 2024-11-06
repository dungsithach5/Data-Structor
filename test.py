class mystack:
    def __init__(self,size):
        self.arr = [None]*size
        self.top = -1
        
    def push(self,x):
       
            self.top += 1
            self.arr[self.top] = x
        
            
    def pop(self):

            self.top -= 1
            x= self.arr[self.top]         
            return x
        
    def is_empty(self):
            return self.top == -1
        
def to_binary(n):
    binary = []
    s = mystack(100)
    while n>0:
        cc =n%2  #chia stack
        
        s.push(cc) 
        n = n //2 #chia lay phan du      
    while not(s.is_empty()):
        binary.append(s.pop())    
    return binary
def evaluate_suffix(suff):
    for x in suff:
        if x in ['+','-','*','/']:
            a = s.pop()
            b = s.pop()
            if x == '+':
                Value = a+b
            elif x == '-':
                Value = a-b
            elif x == '*':
                Value = a*b
            elif x == '/':
                Value = a/b
            s.push(Value)
        else:
            s.push(x)
    
    return Value

print(evaluate_suffix([1,2,3,'+',4,'*','+']))
           
print(to_binary(233))           
s = mystack(10)
s.push(1),s.push(2),s.push(3),s.push(4),s.push(5),s.push(6),s.push(7),s.push(8),s.push(9),s.push(10)
print(s.pop(),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()),print(s.pop()))