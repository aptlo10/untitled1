class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree():

    def __init__(self):
        self.root = None

    def add_node(self, key, node=None):

        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(key)

        else:

            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    print ("left",key)
                    return
                else:
                    # return self.add_node(key,node = self.root.left)
                    return self.add_node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    print ("right",key)
                    return key
                else:
                    # return self.add_node(key,node = self.root.right)
                    return self.add_node(key, node=node.right)

    def search(self, key, node=None):

        if node is None:
            node = self.root

        if self.root.key == key:
            print "key is at the root"
            return self.root

        else:
            if node.key == key:
                print "key exists"
                return node

            elif key < node.key and node.left is not None:
                print "left"
                return self.search(key, node=node.left)

            elif key > node.key and node.right is not None:
                print "right"
                return self.search(key, node=node.right)

            else:
                print "key does not exist"
                return None



    def tree_data(self, node=None):
        if node is None:
            node = self.root

        stack = []
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right


t = Tree()
t.add_node(10)
t.add_node(60)
t.add_node(25)
t.add_node(8)
t.add_node(30)
t.add_node(20)
t.add_node(40)