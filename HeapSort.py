def heapSort(a):
    # giai doan 1: từ heap là một nữa sau, bổ sung dần về bên trái để được full heap
    Left = (len(a) // 2) - 1
    Right = len(a) - 1
    while Left >= 0:
        bosung(a, Left, Right)
        Left -= 1

    # giai đoạn 2: từ full heap, rút ra phần tử đầu tiên, đổi với phần tử cuối
    # bổ sung lại phần tử cuối vào heap (giảm đi 1 phần tử)
    while Right >= 1:
        t = a[0]
        a[0] = a[Right]
        a[Right] = t
        Right -= 1
        bosung(a, 0, Right)
        
        
def bosung(a, left, right):
    cha = a[left]
    index_cha = left
    index_trai = 2 * index_cha + 1
    is_heap = False
    while index_trai <= right and not is_heap:
        index_max = index_trai
        if index_trai + 1 <= right and a[index_max] < a[index_trai + 1]:
            index_max = index_trai + 1
        if cha >= a[index_max]:
            is_heap = True
        else:
            a[index_cha] = a[index_max]
            index_cha = index_max
            index_trai = 2 * index_cha + 1
    a[index_cha] = cha
    
    
if __name__ == "__main__":
    a = [44, 55, 12, 42, 94, 18, 6, 67]
    heapSort(a) # quickSort(a, 0, len(a)-1)
    print(a)