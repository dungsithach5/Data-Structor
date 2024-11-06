class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def search(self, x):
        t = self.root
        parent = None
        while t is not None and t.data != x:
            parent = t
            if t.data < x:
                t = t.right
            else:
                t = t.left
        return [parent, t]

    def insert(self, x):
        result = self.search(x)
        if result[1] is not None: # found x, not inserting
            return
        n = node(x)
        if result[0] is None: # tree is empty
            self.root = n
        elif x < result[0].data:
            result[0].left = n
        else:
            result[0].right = n

    def inorder(self):
        self.sub_inorder(self.root)

    def sub_inorder(self, t):
        if t is None:
            return
        self.sub_inorder(t.left)
        print(t.data, end=' ')
        self.sub_inorder(t.right)

    def remove(self, x):
        result = self.search(x)
        if result[1] is None:  # not found x!
            return
        t, parent = result[1], result[0] # nút cần xóa và cha
        if t.left != None and t.right != None: # 2 con, # quy về trường hợp xóa <= 1 con
            tcbp, chatcbp = t.left, t
            while tcbp.right is not None:
                chatcbp, tcbp = tcbp, tcbp.right
            t.data = tcbp.data
            t, parent = tcbp, chatcbp
        con_lai = t.left # xóa lá hoặc có chỉ 1 con
        if con_lai is None:
            con_lai = t.right
        if parent is None: # nối cha của t đến phần còn lại của t
            root = con_lai
        elif parent.right == t:
            parent.right = con_lai
        else:
            parent.left = con_lai


arr = [5, 3, 4, 2, 1, 7, 6, 8, 6.5,2.5, 2.3, 2.7, 2.2, 2.4, 2.6, 2.8, 6.2]
t = bst()
for x in arr:
    t.insert(x)
t.remove(5)
print('Sau khi xóa\n')
t.inorder()
# for x in arr:
#     print('\nChen ', x)
#     t.insert(x)
#     print('Cay ')
#     t.inorder()
