class Node(object):
    def __init__(self,data):
        self.d=data
        self.left_child=None
        self.right_child=None

    def insert(self,data):
        if data<self.d:
            if not self.left_child:
                   self.left_child=Node(data)

            else:
               self.left_child.insert(data)


        else:
            if not self.right_child:
                self.right_child=Node(data)

            else:
                self.right_child.insert(data)


    def traversorder(self):
            if self.left_child is not None:
             self.left_child.traversorder()

            print(self.d)

            if self.right_child is not None:
                 self.right_child.traversorder()


"""
    def getmin(self):
        if self.left_child is None:
            return self.d
        else:
            return self.left_child.getmin()

    def getmax(self):
        if self.right_child is None:
            return  self.d
        else:
            return self.right_child.getmax()
"""
