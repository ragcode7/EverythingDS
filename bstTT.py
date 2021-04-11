import math
class BinarySearchTree:
    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0
        self.mylist = []
    def findElement(self,e,curnode):
        while curnode != None:
            if curnode.element == e:
                return curnode
            if e > curnode.element:
                if curnode.rightchild == None:
                    return None
                else:
                    curnode = curnode.rightchild
            elif e < curnode.element:
                if curnode.leftchild == None:
                    return None
                else:
                    curnode = curnode.leftchild
    def insertElement(self,e):
        temp = self.root
        if temp == None:
            self.root = self.node()
            self.root.element = e
            self.sz+=1
        else:
            while temp:
                if e < temp.element and temp.leftchild != None:
                    temp = temp.leftchild
                    continue
                elif e < temp.element and temp.leftchild == None:
                    temp.leftchild = self.node()
                    temp.leftchild.element = e
                    temp.leftchild.parent = temp
                    self.sz+=1
                    break
                elif e > temp.element and temp.rightchild != None:
                    temp = temp.rightchild
                    continue
                elif e > temp.element and temp.rightchild == None:
                    temp.rightchild = self.node()
                    temp.rightchild.element = e
                    temp.rightchild.parent = temp
                    self.sz+=1
                    break
    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print(curnode.element,end=",")
        if (curnode.rightchild!=None):
            self.inorderTraverse(curnode.rightchild)
    def returnNextInorder(self,v):
        while(v.leftchild!=None):
            v = v.leftchild
        return v
    def deleteElement(self,e):
        nodetobedeleted = self.findElement(e,self.root)
        if(nodetobedeleted == None):
            print("Error, element not found")
            return -1
        currnode = self.node()
        currnode.element = e
        parent = None
        x = self.root
        while(x!=None and x.element!=e):
            parent = x
            if(e<x.element):
                x = x.leftchild
            else:
                x = x.rightchild
        if(self.isExternal(x)):
            if(parent.leftchild==x):
                parent.leftchild = None
            else:
                parent.rightchild = None
        elif(x.leftchild!=None and x.rightchild!=None):
            successor = self.returnNextInorder(x.rightchild)
            value = successor.element
            self.deleteElement(successor.element)
            x.element = value
        else:
            if(x.leftchild!=None):
                child = x.leftchild
            else:
                child = x.rightchild
            x.element = child.element
            if(x.leftchild!=None):
                x.leftchild = None
            else:
                x.rightchild = None
            self.sz-=1
        return
    def createTree(self, items):
        self.sz=len(items)
        mid = int(math.floor(len(items)/2))
        self.insertElement(items[mid])
        del items[mid]
        if (len(items)>1):
            self.createTree(items[0:mid])
            self.createTree(items[mid:len(items)+1])
        else:
            if (len(items)==1):
                self.insertElement(items[0])
            return
    def isExternal(self,curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False
    def getChildren(self, curnode):
        children = []
        #if curnode.leftchild!= None:
        children.append(curnode.leftchild)
        #if curnode.rightchild!= None:
        children.append(curnode.rightchild)
        return children
    def isExternal(self, curnode):
        if (curnode.leftchild==None and curnode.rightchild ==None):
            return True
        else:
            return False
    def preorderTraverse(self,v):
        curnode = v
        print (curnode.element,end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.preorderTraverse(curnode.rightchild)
        return
    def postorderTraverse(self,v):
        curnode = v
        if curnode:
            self.postorderTraverse(curnode.leftchild)
            self.postorderTraverse(curnode.rightchild)
            print(curnode.element, end=",")
        return
    def findDepthIter(self,v):
        if v==self.root:
            return 0
        else:
            return 1+self.findDepthIter(v.parent)
    def findDepth(self,v):
        return self.findDepthIter(self.findElement(v.element,self.root))
    def findHeightIter(self,v):
        if self.isExternal(v):
            return 0
        else:
            h=0
            if(v.leftchild!=None):
                h=max(h,self.findHeightIter(v.leftchild))
            if(v.rightchild!=None):
                h=max(h,self.findHeightIter(v.rightchild))
            return 1+h
    def findHeight(self,v):
        return self.findHeightIter(self.findElement(v.element,self.root))
    def finRange(self,low,high):
        elements = []
        for element in range(low, high+1):
            if self.findElement(element,self.root) != None:
                elements.append(element)
        return elements
    def returnInorderTraverse(self,v):
        temp = v
        if(temp.leftchild!=None):
            self.returnInorderTraverse(temp.leftchild)
        self.templist.append(temp.element)
        if(temp.rightchild!=None):
            self.returnInorderTraverse(temp.rightchild)
    def findMedian(self):
        self.templist = []
        self.returnInorderTraverse(self.root)
        l = len(self.templist)
        if(l%2==0):
            add = self.templist[int(l/2)-1]
            add += (self.templist[int(l/2)])
            midd = (add/2)
            if(midd-int(midd)==0):
                return int(midd)
            else:
                return midd
        else:
            return self.templist[int(l/2)]
def testbst():
    ds = BinarySearchTree()
    arr = list(map(int, input().split()))
    ds.createTree(arr)
    ds.preorderTraverse(ds.root)
    print()
    inputs = int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="M"):
            ds.preorderTraverse(ds.root)
            print()
            print(ds.findMedian())
        elif(operation[0]=="R"):
            print(ds.finRange(int(operation[1]),int(operation[2])))
        elif(operation[0]=="I"):
            ds.insertElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="Pre"):
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="In"):
            ds.inorderTraverse(ds.root)
            print()
        elif(operation[0] == "F"):
            temp = ds.findElement(int(operation[1]),ds.root)
            if (temp == None):
                print(False)
            else:
                print(True)
        elif(operation[0]=="D"):
            ds.deleteElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        inputs-=1
def main():
    testbst()

if __name__ == '__main__':
    main()
