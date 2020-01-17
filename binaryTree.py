class BinaryTree:
    def __init__(self,root):
        self.key=root 
        self.left_child=None 
        self.right_child=None 


    def insert_left(self,new_node):
        if self.left_child==None:
            self.left_child=BinaryTree(new_node)

        else:
            t=BinaryTree(new_node)
            t.left_child=self.left_child 
            self.left_child=t

    def insert_right(self,new_node):
        if self.right_child==None:
            self.right_child=self.left_child 
        else:
            t=BinaryTree(new_node)
            t.right_child=self.right_child
            self.right_child=t 

    def get_right_child(self):
        return self.right_child 


    def get_left_child(self):
        return self.left_child 


    def set_root_value(self,new_root):
        self.key= new_root

    def get_root_value(self):
        return self.key 


if __name__=="__main__":
    r = BinaryTree('a')
    print(r.get_root_value())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_value())    
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_value())
    r.get_right_child().set_root_value('hello')
    print(r.get_right_child().get_root_value())        


