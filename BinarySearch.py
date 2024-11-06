def binary_search(x, a):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        if x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # khong tim thay x

def insert(x, a):
    a.append(x)  # Step 1: Append x at the end
    i = len(a) - 2
    while i >= 0 and x < a[i]:  # Step 2: Shift elements to the right
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = x  # Step 3: Locate x in the correct position

def remove(x, a):
    index = binary_search(x, a)
    if index == -1:
        return  # x is not in the list
    for j in range(index + 1, len(a)):  # Shift elements to the left
        a[j - 1] = a[j]
    a.pop(-1)  # Remove the last element

# Testing the functions
a = [1, 2, 4, 6, 8, 10, 15, 20, 25]
x = 6
print(binary_search(x, a))  # Should print the index of x

b = [1, 2, 4, 6, 8, 10, 15, 20, 25]
insert(0, b)
print('=>', b)  # Should print the list with 0 inserted in the correct position

c = [1, 2, 4, 6, 8, 10, 15, 20, 25, 26, 30, 25]
remove(10, c)
print("=>", c)  # Should print the list with 10 removed
