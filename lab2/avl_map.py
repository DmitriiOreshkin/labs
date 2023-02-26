class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.l = None
        self.r = None
        self.h = 1


class AVLMap(object):

    def __init__(self, root=None) -> None:

        self.root = root

    def __del__(self):

        self.root = None

    def set(self, key, value):

        self.root = self._set(self.root, key, value)

    def _set(self, root, key, value):

        if not root:
            return Node(key, value)
        elif key < root.key:
            root.l = self._set(root.l, key, value)
        elif key == root.key:
            root.value = value
        else:
            root.r = self._set(root.r, key, value)

        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.key:
            return self.rRotate(root)

        if b < -1 and key > root.r.key:
            return self.lRotate(root)

        if b > 1 and key > root.l.key:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.key:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))

        return y

    def getHeight(self, root):

        if not root:
            return 0

        return root.h

    def getBal(self, root):

        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def get(self, key):

        if self.root != None:
            return self._get(self.root, key)

        return False

    def _get(self, cur_node, key):

        if key == cur_node.key:
            return cur_node.value
        elif key < cur_node.key and cur_node.l is not None:
            return self._get(cur_node.l, key)
        elif key > cur_node.key and cur_node.r is not None:
            return self._get(cur_node.r, key)

        return None

    def change(self, key, value):

        if self.root != None:
            return self._change(self.root, key, value)
        return False

    def _change(self, cur_node, key, value):

        if key == cur_node.key:
            cur_node.value = value
            return True
        elif key < cur_node.key and cur_node.l is not None:
            return self._change(cur_node.l, key, value)
        elif key > cur_node.key and cur_node.r is not None:
            return self._change(cur_node.r, key, value)

        return None

    def delete(self):

        if not self.root:
            return None

        self.root.l = self._delete(self.root.l)
        self.root.r = self._delete(self.root.r)
        self.root = None

    def _delete(self, cur_node):

        if not cur_node:
            return None

        cur_node.l = self._delete(cur_node.l)
        cur_node.r = self._delete(cur_node.r)

        return None

    def inspect(self):

        if not self.root:
            return

        print("{0} ".format(self.root.value), end="")
        self._inspect(self.root.l)
        self._inspect(self.root.r)

    def _inspect(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self._inspect(root.l)
        self._inspect(root.r)
