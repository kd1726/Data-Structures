class Node:
    def __init__(self,data=None):
        self.data=data
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
                return self._append(cur_node.right_child,data)
        if data<cur_node.data:
            if cur_node.left_child==None:
                cur_node.left_child=Node(data)
                cur_node.left_child.parent = cur_node
            else:
                return self._append(cur_node.left_child,data)

        else:
            return "No duplicates in this tree!"

    def height(self):
        height=0
        cur_node = self.root
        if cur_node==None:
            return height
        else:
            return self._height(self.root,height)

    def _height(self,cur_node,height):
        if cur_node!=None:
            left_height = self._height(cur_node.left_child,height+1)
            right_height = self._height(cur_node.right_child,height+1)
            return max(left_height,right_height)
        return height

    def print_tree(self):
        if self.root==None:
            return "Cannot print a tree that doesn't exist"
        else:
            ask = input("In order (ino), Pre order (pro) or post order (pto)").lower()
            if ask=="ino":
                return self._print_in_order_tree(self.root)
            elif ask=="pro":
                return self._print_pre_order_tree(self.root)
            elif ask=="pto":
                return self._print_post_order_tree(self.root)
            else:
                return self._print_in_order_tree(self.root)

    def _print_in_order_tree(self,cur_node):
        if cur_node!=None:
            self._print_in_order_tree(cur_node.left_child)
            print(cur_node.data)
            self._print_in_order_tree(cur_node.right_child)
            return


    def _print_pre_order_tree(self,cur_node):
        if cur_node!=None:
            print(cur_node.data)
            self._print_pre_order_tree(cur_node.left_child)
            self._print_pre_order_tree(cur_node.right_child)
            return

    def _print_post_order_tree(self,cur_node):
        if cur_node!=None:
            self._print_post_order_tree(cur_node.left_child)
            self._print_post_order_tree(cur_node.right_child)
            print(cur_node.data)
            return


    def search(self,data):
        cur_node = self.root
        if cur_node==None:
            return "No results if there is no tree!"
        else:
            return self._search(self.root,data)

    def _search(self,cur_node,data):
        if data>cur_node.data:
            if cur_node.right_child!=None:
                return self._search(cur_node.right_child,data)
            else:
                return "No result found in tree."
        elif data<cur_node.data:
            if cur_node.left_child!=None:
                return self._search(cur_node.left_child,data)
            else:
                return "No result found in tree."
        elif data==cur_node.data:
            return f"{cur_node.data} has been found in the tree"
        else:
            return "No result found in tree."

    def find(self,data):
        cur_node = self.root
        if cur_node==None:
            return "No results if there is no tree!"
        else:
            return self._find(self.root,data)

    def _find(self,cur_node,data):
        if data>cur_node.data:
            if cur_node.right_child!=None:
                return self._find(cur_node.right_child,data)
            else:
                return None
        elif data<cur_node.data:
            if cur_node.left_child!=None:
                return self._find(cur_node.left_child,data)
            else:
                return None
        elif data==cur_node.data:
            return cur_node
        else:
            return None

    def delete_value(self,data):
        if self.find(data)==None:
            return "You cannot delete something that doesn't exist"
        else:
            ask = input(f"You are deleting {self.find(data).data} from your tree. Continue? (y/n)").lower()
            if ask=="y":
                return self._delete_node(self.find(data))
            else:
                return "Operation aborted"

    def _delete_node(self,node):

        def min_value_node(node):
            cur =  node
            while cur.left_child!=None:
                cur = cur.left_child
            return cur

        def getChildren(node):
            c =0
            if node.left_child!=None:
                c+=1
            if node.right_child!=None:
                c+=1
            return c

        parent = node.parent
        children = getChildren(node)

        if children==0:
            if parent.left_child==node:
                parent.left_child=None
            else:
                parent.right_child=None

        if children==1:
            if node.left_child!=None:
                child = node.left_child
            else:
                child = node.right_child

            if parent.left_child==node:
                parent.left_child = child
                node.left_child = None
            else:
                parent.right_child=child
                node.right_child=None
            child.parent = parent

        if children==2:
            successor = min_value_node(node.right_child)

            node = successor

            self._delete_node(successor)
        return
