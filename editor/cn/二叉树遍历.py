class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = []

    def traversal(self, root):
        self.res = []
        self.inorder_traversal_recursion(root)
        print("递归-中序遍历")
        print(self.res)

        self.res = []
        self.preorder_traversal_recursion(root)
        print("递归-前序遍历")
        print(self.res)

        self.res = []
        self.postorder_traversal_recursion(root)
        print("递归-后序遍历")
        print(self.res)

        self.res = []
        self.inorder_traversal_iteration(root)
        print("迭代-中序遍历")
        print(self.res)

        self.res = []
        self.preorder_traversal_iteration(root)
        print("迭代-前序遍历")
        print(self.res)

        self.res = []
        self.postorder_traversal_iteration(root)
        print("迭代-后序遍历")
        print(self.res[::-1])

    def inorder_traversal_recursion(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.inorder_traversal_recursion(root.left)
        self.inorder_traversal_recursion(root.right)

    def preorder_traversal_recursion(self, root):
        if not root:
            return
        self.preorder_traversal_recursion(root.left)
        self.res.append(root.val)
        self.preorder_traversal_recursion(root.right)

    def postorder_traversal_recursion(self, root):
        if not root:
            return
        self.postorder_traversal_recursion(root.left)
        self.postorder_traversal_recursion(root.right)
        self.res.append(root.val)

    def inorder_traversal_iteration(self, root):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            self.res.append(cur.val)
            # 子节点入栈顺序 右--左
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    #访问元素和打印元素不一致
    def preorder_traversal_iteration(self, root):
        if not root:
            return
        #不要先压入root
        stack = []
        cur = root
        while cur or stack:
            #寻找最左元素
            if cur:
                stack.append(cur)
                cur = cur.left
            #访问元素，并开始遍历右子树
            else:
                cur = stack.pop()
                self.res.append(cur.val)
                cur = cur.right

    def postorder_traversal_iteration(self, root):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            self.res.append(cur.val)
            # 子节点入栈顺序 左--右，最后把结果反转，本质是中序遍历的反转
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    b.left = d
    b.right = e

    Solution().traversal(a)
