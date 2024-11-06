def quickSort(a, left, right):
    mid = (left + right) // 2
    i = left
    j = right
    pivot = a[mid]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1
    if left < j:
        quickSort(a, left, j)
    if i < right:
        quickSort(a, i, right)
        
if __name__ == "__main__":
    a = [44, 55, 12, 42, 94, 18, 6, 67]
    quickSort(a, 0, len(a)-1)
    print(a)