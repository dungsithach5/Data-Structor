def binary_search(x,a):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        if x < a[mid]:
            right = mid - 1
        else:
            left = mid+1
    return -1 # khong tim thay x

def insert(x,a):
    # i = 0
    n = len(a)
    # a.append(-1)
    # while i <= n - 1 and x > a[i]:  #Step 1: find position for x
    #     i += 1
    # for j in range(i+1, n+1): #Step 2: shift right
    #     a[j] = a[j-1]
    a.insert(0,x)
    i = n - 1
    while i>= 0 and x < a[i]:
        a[i+1] = a[i]
        i-= 1
    a[i+1] = x #Step 3: locate x
    a.pop(0)
    
def remove(x,a):
        # i = a.index(x)
    # del a[i]
    index = binary_search(x,a)
    if index == -1:
        return
    for j in range(index+1, len(a)):
        a[j-1] = a[j]
    a.pop(-1)
    
a = [1,2,4,6,8,10,15,20,25]
x = 6
print(binary_search(x,a))

b = [1,2,4,6,8,10,15,20,25]
insert(0,b)
print('=>',b)

c = [1,2,4,6,8,10,15,20,25,26,30,25]
remove(10,c)
print("=>", c)
