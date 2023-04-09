from collections import deque

class Node:
    def __init__(self, key, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class BTreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if not self.root:
            self.root = Node(key, val)
            return
        dq = deque()
        dq.append(self.root)
        while dq:
            curr = dq.popleft()
            if not curr.left:
                curr.left = Node(key, val)
                break
            else:
                dq.append(curr.left)
            if not curr.right:
                curr.right = Node(key, val)
                break
            else:
                dq.append(curr.right)

    def delete_deepest_node(self, deepest_node):
        dq = deque()
        dq.append(self.root)
        while dq:
            curr = dq.popleft()
            if curr is deepest_node:
                curr = None
                return
            if curr.right:
                if curr.right is deepest_node:
                    curr.right = None
                    return
                else:
                    dq.append(curr.right)
            if curr.left:
                if curr.left is deepest_node:
                    curr.left = None
                    return
                else:
                    dq.append(curr.left)

    def delete(self, key):
        if not self.root:
            return
        if not self.root.left and not self.root.right:
            if self.root.key == key:
                self.root = None
                return
        dq = deque()
        dq.append(self.root)
        req_key_node = None
        curr = None
        while dq:
            curr = dq.popleft()
            if curr.key == key:
                req_key_node = curr
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        if req_key_node:
            deepest_key = curr.key
            self.delete_deepest_node(curr)
            req_key_node.key = deepest_key

    def inorder(self, curr):
        ans = []
        if curr.left:
            ans = self.inorder(curr.left)
        ans.append(curr)
        if curr.right:
            ans = ans + self.inorder(curr.right)
        return ans

    def postorder(self, curr):
        ans = []
        if curr.left:
            ans = self.postorder(curr.left)
        if curr.right:
            ans = ans + self.postorder(curr.right)
        ans.append(curr)
        return ans

    def preorder(self, curr):
        ans = []
        if curr:
            ans.append(curr)
            ans = ans + self.preorder(curr.left)
            ans = ans + self.preorder(curr.right)
        return ans

    def search(self, key):
        dq = []
        dq.append(self.root)
        while dq:
            curr = dq.pop()
            if curr.key == key:
                return curr.val
            if curr.left:
                if curr.left.key == key:
                    return curr.left.val
                else:
                    dq.append(curr.left)
            if curr.right:
                if curr.right.key == key:
                    return curr.right.val
                else:
                    dq.append(curr.right)
