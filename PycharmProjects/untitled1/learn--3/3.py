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
                    print ('|{:>5}|'.format(""),"--",key,end="")

                    return
                else:
                    # return self.add_node(key,node = self.root.left)
                    return self.add_node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    print ('{:<15}|'.format(""),"++",key)
                    return key
                else:
                    # return self.add_node(key,node = self.root.right)
                    return self.add_node(key, node=node.right)


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
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(15)
t.add_node(5)
t.add_node(17)
t.add_node(2)

