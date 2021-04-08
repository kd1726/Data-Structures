class Node:
    def __init__(self,data=None):
        self.data=None
        self.right_child = None
        self.left_child = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def append(self,data):
        if self.root==None:
            self.root = Node(data)
        else:
            return self._append(self.root,data)

    def _append(self,cur_node,data):
        if data>cur_node.data:
            if cur_node.right_child==None:
                cur_node.right_child = Node(data)
                cur_node.right_child.parent = cur_node
            else:
                return self._append(cur_ndoe.right_child,data)
        if data<cur_node.data:
            if cur_node.left_child==None:
                cur_node.left_child=Node(data)
                cur_node.left_child.parent = cur_node
            else:
                return self._append(cur_ndoe.left_child,data)

        else:
            return "No duplicates in this tree!"
