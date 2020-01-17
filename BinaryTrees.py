class Node:
    def __init__(self,value):
        self.value=value 
        self.left_child=None
        self.right_child =None 

class Queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.insert(0,item)


    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return len(self.items)






class BinaryTree:
    def __init__(self,root):
        self.root=Node(root) 


    def print_tree( self,traverse_type):
        if traverse_type=="preorder":
            return self.pre_order(tree.root,"") 
        elif traverse_type=="inorder":
            return self.in_order(tree.root,"")
        elif traverse_type=="postorder":
            return self.post_order(tree.root,"") 
        elif traverse_type=="levelorder":
            return self.level_order(tree.root,"")             


    def pre_order(self,start,traversal):
        '''root left-childe ,right-child'''
        if start:
            traversal +=(str(start.value)+"-")  
            traversal=self.pre_order(start.left_child,traversal)
            traversal =self.pre_order(start.right_child,traversal) 

        return traversal 

    def in_order(self,start,traversal):
        '''Left -root- right'''
        if start:
            traversal+=self.in_order(start.left_child,traversal)  
            traversal+=(str(start.value)+"-")
            traversal=self.in_order(start.right_child,traversal)
        return traversal


    def   post_order(self,start,traversal):
        if start:
            traversal+=self.post_order(start.left_child,traversal)
            traversal+=self.post_order(start.right_child,traversal) 
            traversal+= (str(start.value)+"-") 
        return traversal

    def level_order(self,start,traversal):
        if start is None:
            return 
        queue= Queue()
        queue.enqueue(start)
        traversal=""
        while len(queue)>0:
            traversal+=str(queue.peek())+" -"
            node = queue.dequeue()
            if node.left_child:
                queue.enqueue(node.left_child)
            if node.right_child:
                queue.enqueue(node.right_child) 
        return traversal            




if __name__=="__main__":
    tree = BinaryTree(1)
    tree.root.left_child=Node(2)
    tree.root.right_child=Node(3)
    tree.root.left_child.right_child=Node(8)
    tree.root.right_child.left_child=Node(7)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    print(tree.print_tree("levelorder"))



#tree traversal 
#inorder,postorder and preorder
#preorder: root-left-right

 

  