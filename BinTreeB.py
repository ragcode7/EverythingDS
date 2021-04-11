#Implement the standard Binary Tree ADT - along with a few custom functions . Your ADT should have the following operations
#Preorder - PR
#Level order - L
#Depth of a node U (where U is the index position) - D
#Height of a node U (where U is the index position) - H
#Check if 2 values U and V are cousins - CC
#Check if given tree is a Full binary tree - FB
#Check if given tree is a Complete binary tree - CB
#Convert the given tree into its Mirror - CM

import math
from collections import deque

class BinaryTree:
    #@start-editable@
    class node:
        def __init__(self):
            self.parent=None
            self.leftchild=None
            self.rightchild=None
        
    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0
    
    

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False
    
    def preorderTraverse(self, v):
        current = v
        if current is None:
            return
        print(current.element,end=" ")
        self.preorderTraverse(current.leftchild)
        self.preorderTraverse(current.rightchild)
    
    def inorderTraverse(self, v):
        current = v
        if current is None:
            return
        self.inorderTraverse(current.leftchild)
        print(current.element,end=" ")
        self.inorderTraverse(current.rightchild)
    
    def postorderTraverse(self, v):
        current = v
        if current is None:
            return
        self.postorderTraverse(current.leftchild)
        self.postorderTraverse(current.rightchild)
        print(current.element,end=" ")
    
    def levelorderTraverse(self, v):
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
            print(i,end=" ")
    
    def findDepth(self, u):
        current=u
        if self.isRoot(current):
            return 0
        else:
            d = 1 + self.findDepth(current.parent)
            return d
    
    def findHeight(self, u):
        if u is None:
            return -1
        else :
            lH = self.findHeight(u.leftchild)
            rH = self.findHeight(u.rightchild)

            if (lH > rH):
                return lH+1
            else:
                return rH+1

    def isFull(self, v):
        if v is None:
            return True
        if v.leftchild is None and v.rightchild is None:
            return True
        if v.leftchild is not None and v.rightchild is not None:
            return(self.isFull(v.leftchild) and self.isFull(v.rightchild))
        return False
    
    def isComplete(self,v):
        if v is None:
            return False
        queue = deque()
        queue.append(v)
        flag = False
        while queue:
            front = queue.popleft()
            if flag and (front.leftchild or front.rightchild):
                return False
            if front.leftchild is None and front.rightchild:
                return False
            if front.leftchild:
                queue.append(front.leftchild)
            else:
                flag = True
            if front.rightchild:
                queue.append(front.rightchild)
            else:
                flag = True
        return True
    
    def convertMirror(self, v):
        if(v==None):
            return
        else:
            temp=v
            self.convertMirror(v.leftchild)
            self.convertMirror(v.rightchild)
            temp=v.leftchild
            v.leftchild=v.rightchild
            v.rightchild=temp

    

        
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
        
    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz



def main():
    tree = BinaryTree()
    #arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "IN"):
            tree.inorderTraverse(tree.root)
            print()
        elif (operation[0] == "PR"):
            tree.preorderTraverse(tree.root)
            print()
        elif (operation[0] == "PO"):
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
        elif (operation[0] == "CC"):
            u = int(operation[1])
            v = int(operation[2])
            print(tree.checkCousins(nlist,u,v))
        elif (operation[0] == "FB"):
            print(tree.isFull(tree.root))
        elif (operation[0] == "CB"):
            print(tree.isComplete(tree.root))
        elif (operation[0] == "CM"):
            tree.convertMirror(tree.root)
            tree.preorderTraverse(tree.root)

        inputs -= 1

if __name__ == '__main__':
    main()

"""
Sample Input:
0 1 2 3 4 5 6 7 8
12
IN
PR
PO
D 4
H 3
L
CC 4 7
CC 4 8
FB
CB
PR
CM
Sample Output:
8 4 2 5 1 6 3 7 
1 2 4 8 5 3 6 7 
8 4 5 2 6 7 3 1 
2
1
1 2 3 4 5 6 7 8 
True
False
False
True
1 2 4 8 5 3 6 7 
1 3 7 6 2 5 4 8
"""
