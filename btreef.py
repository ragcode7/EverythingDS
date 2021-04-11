#@start-editable@

import math
from collections import deque
#@end-editable@

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
            

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0
        

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild==None and curnode.rightchild==None):
            return (True)
        else:
            return (False)

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False   	

    def inorderTraverse(self, v):
        #@start-editable@

        current = v
        if current is None:
            return
        self.inorderTraverse(current.leftchild)
        print(current.element,end=",")
        self.inorderTraverse(current.rightchild)
	    #@end-editable@
        

    def preorderTraverse(self, v):
        #@start-editable@

        current = v
        if current is None:
            return
        print(current.element,end=",")
        self.preorderTraverse(current.leftchild)
        self.preorderTraverse(current.rightchild)
	    #@end-editable@
       

    def postorderTraverse(self, v):
        #@start-editable@

        current = v
        if current is None:
            return
        self.postorderTraverse(current.leftchild)
        self.postorderTraverse(current.rightchild)
        print(current.element,end=",")
	    #@end-editable@
        

    def levelorderTraverse(self, v):
        #@start-editable@

        list_of_nodes = []
        traversal_queue = deque([self.root])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.element)
            if node.leftchild:
                traversal_queue.append(node.leftchild)
            if node.rightchild:
                traversal_queue.append(node.rightchild)
        for i in list_of_nodes:
            print(i,end=",")
	    #@end-editable@
       

    def findDepth(self, v):
        #@start-editable@

        current=v
        if self.isRoot(current):
            return 0
        else:
            d = 1 + self.findDepth(current.parent)
            return d
	    #@end-editable@
    	

    def findHeight(self, v):
        #@start-editable@

        if v is None:
            return -1 
        else :
            lH = self.findHeight(v.leftchild)
            rH = self.findHeight(v.rightchild)

            if (lH > rH):
                return lH+1
            else:
                return rH+1
	    #@end-editable@
    	

    # delete leaves in the tree
    def delLeaves(self, v):
        #@start-editable@

        if v==None:
            return None
        if v.leftchild==None and v.rightchild==None:
            return None
        v.leftchild=self.delLeaves(v.leftchild)
        v.rightchild=self.delLeaves(v.rightchild)
        return v

	    #@end-editable@
        
    # returns true if tree is proper
    def isProper(self, v):
        #@start-editable@

        if v is None:
            return True
        if v.leftchild is None and v.rightchild is None:
            return True
        if v.leftchild is not None and v.rightchild is not None:
            return(self.isProper(v.leftchild) and self.isProper(v.rightchild))
        return False    
	    #@end-editable@
        
    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        #@start-editable@

        if(v==None):
            return
        else:
            temp=v
            self.mirror(v.leftchild)
            self.mirror(v.rightchild)
            temp=v.leftchild
            v.leftchild=v.rightchild
            v.rightchild=temp
            
    def p(self,v,s):
        if v is None:
            return (s == 0)
        else:
            a = 0
            ss = s - v.element
            if(v.leftchild == None and v.rightchild == None and ss == 0):
                return True
            if v.leftchild is not None:
                a = a or self.p(v.leftchild,ss)
            if v.rightchild is not None:
                a = a or self.p(v.rightchild,ss)
            if(a == 0):
                return False
            return a
	    #@end-editable@
        

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz=len(nodelist)
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element,end=" ");
            else:
                print(None)


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    #determine whether there exists a root-to-leaf path whose nodes sum is equal to a specified integer
    def root2leafsum(self, k):
        #@start-editable@

        x = self.p(self.root,k)
        print(x)

	    #@end-editable@
        

    #determine the value of the leaf node in a given binary tree that is the terminal node of a path of least value from the root of the binary tree to any leaf. The value of a path is the sum of values of nodes along that path.
    def leastleaf(self):
        #@start-editable@

        value=0
        if self.root is None:
            return 0
        value=value+self.root.element
        if(self.root.leftchild is None and self.root.rightchild is None):
            return self.root.element
        value=self.leastleaf(self.root.leftchild)+self.leastleaf(self.root.rightchild)
        return(self.value)
	    #@end-editable@
        

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              tree.inorderTraverse(tree.root)
              print()
         elif (operation[0] == "P"):
              tree.preorderTraverse(tree.root)
              print()
         elif (operation[0] == "Post"):
              tree.postorderTraverse(tree.root)
              print()
         elif (operation[0] == "L"):
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == "D"):
              pos = int(operation[1])
              print(tree.findDepth(nlist[pos]))
         elif (operation[0] == "H"):
              pos = int(operation[1])
              print(tree.findHeight(nlist[pos]))
         elif (operation[0] == "IP"):
              print(tree.isProper(tree.root))
         elif (operation[0] == 'M'):
              tree.mirror(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'DL'):
              tree.delLeaves(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'RL'):
              tree.root2leafsum(int(operation[1]))
              print()
         elif (operation[0] == 'ML'):
              tree.leastleaf()
              print()
         inputs -= 1

if __name__ == '__main__':
    main()