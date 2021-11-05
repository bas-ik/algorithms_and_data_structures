from stack.Stack import Stack


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):

    def insert(self, root, key):

        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)
        root.h = 1 + max(self.get_height(root.l),
                         self.get_height(root.r))

        b = self.get_bal(root)

        if b > 1 and key < root.l.value:
            return self.right_rotate(root)

        if b < -1 and key > root.r.value:
            return self.left_rotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.left_rotate(root.l)
            return self.right_rotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.right_rotate(root.r)
            return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.r
        T2 = y.l
        y.l = z
        z.r = T2
        z.h = 1 + max(self.get_height(z.l),
                      self.get_height(z.r))
        y.h = 1 + max(self.get_height(y.l),
                      self.get_height(y.r))
        return y

    def right_rotate(self, z):
        y = z.l
        T3 = y.r
        y.r = z
        z.l = T3
        z.h = 1 + max(self.get_height(z.l),
                      self.get_height(z.r))
        y.h = 1 + max(self.get_height(y.l),
                      self.get_height(y.r))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.h

    def get_bal(self, root):
        if not root:
            return 0
        return self.get_height(root.l) - self.get_height(root.r)

    # КЛП
    @staticmethod
    def pre_order(root):

        # Base CAse
        res = []
        if root is None:
            return
        nodeStack = []
        nodeStack.append(root)
        while (len(nodeStack) > 0):
            node = nodeStack.pop()
            res.append(node.value)

            if node.r is not None:
                nodeStack.append(node.r)
            if node.l is not None:
                nodeStack.append(node.l)
        return res

    # ЛКП
    @staticmethod
    def in_order(root):
        current = root
        stack = []
        done = 0
        res = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.l

            elif (stack):
                current = stack.pop()
                res.append(current.value)
                current = current.r

            else:
                break

        print()
        return res

    # ЛПК
    @staticmethod
    def post_order(root):

        stack = []
        res = []
        while (True):
            while (root != None):
                stack.append(root)
                stack.append(root)
                root = root.l

            if (len(stack) == 0):
                return res

            root = stack.pop()

            if len(stack) > 0 and stack[-1] == root:
                root = root.r
            else:
                res.append(root.value)
                root = None

    def print_current_level(self, root, level, res):
        if root is None:
            return
        if level == 1:
            res.append(root.value)
        elif level > 1:
            self.print_current_level(root.l, level - 1, res)
            self.print_current_level(root.r, level - 1, res)

    def breadth_first_search(self, root):
        res = []
        h = self.get_height(root)
        for i in range(1, h + 1):
            # print()
            self.print_current_level(root, i, res)
        return res

    @staticmethod
    def sort_sequence(seq):
        Tree = AVLTree()
        a = None
        for i in seq:
            a = Tree.insert(a, i)
        return AVLTree.in_order(a)


if __name__ == "__main__":
    Tree = AVLTree()
    root = None

    root = Tree.insert(root, 1)
    root = Tree.insert(root, 2)
    root = Tree.insert(root, 3)
    root = Tree.insert(root, 4)
    root = Tree.insert(root, 5)
    root = Tree.insert(root, 6)

    # Preorder Traversal
    print("Preorder traversal of the",
          "constructed AVL tree is")
    print(f"in_order: {AVLTree.in_order(root)}")
    print("pre_order: ", AVLTree.pre_order(root))
    print("post-order:", AVLTree.post_order(root))
    print("в глубину:", Tree.breadth_first_search(root))
    seq = [5, 4, 3, 10, 2, 1]
    print(AVLTree.sort_sequence(seq))
