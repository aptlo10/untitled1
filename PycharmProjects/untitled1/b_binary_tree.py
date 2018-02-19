from node import Node

class BST(object):
    def __init__(self):
        self.rootNode=None;


    def insert(self,data):
        if not self.rootNode:
            self.rootNode=Node(data)

        else:
            self.rootNode.insert(data)


    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()
    def traveseorder(self):
        if self.rootNode:
            self.rootNode.traversorder()