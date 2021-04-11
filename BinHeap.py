
class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
	
   """ since heap can be represented by a single list- constructor - initialize list and attribute currentSize to keep 
	track of the size of the heap.
   """

    """ Easiest way would be to add an item to a list by simply appending the item to the end of list. it can 
	 maintain complete tree property. however, it will likely violate heap order property. 
	Regain the property by comparing the newly added item with its parent.If newly added guy is less than parent,
	we swap it.
    """
	
    """ This method defines the upheap function when inserting an element. upheapp a new item as far up in the tree 
	as it needs to go to maintain the heap property. Here is where our wasted element in heapList is important. 
	Notice that we can compute the parent of any node by using simple integer division. The parent of the current node 
	can be computed by dividing the index of the current node by 2.
    """
    def upHeapp(self,i):
        #@start-editable@
        while i//2 >0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
	    #@end-editable@
   """
   Once a new item is appended to the tree, upHeapp takes over and positions the new item properly. 
   """

    def insert(self,k):
        #@start-editable@
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.upHeapp(self.currentSize)
	    #@end-editable@

    """ This method defines the downheap function when removing min
    """

    def downHeap(self,i):
        #@start-editable@
        while (i * 2) <= self.currentSize:
            minc = self.minChild(i)
            if self.heapList[i] > self.heapList[minc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minc]
                self.heapList[minc] = tmp
            i = minc
	    #@end-editable@
   """Since the heap property requires that the root of the tree be the smallest item in the tree,
 finding the minimum item is relatively easy. The hard part of delMin is restoring full compliance with the 
heap structure and heap order properties after the root has been removed. We can restore our heap 
in two steps. First, we will restore the root item by taking the last item in the list and moving 
it to the root position. Moving the last item maintains our heap structure property. 
However, we have probably destroyed the heap order property of our binary heap. Second, we will 
restore the heap order property by pushing the new root node down the tree to its proper position 

In order to maintain the heap order property, all we need to do is swap the root with its 
smallest child less than the root. After the initial swap, we may repeat the swapping process 
with a node and its children until the node is swapped into a position on the tree where it 
is already less than both children.
"""

    def minChild(self,i):
        #@start-editable@
        if (2*i) + 1 > self.currentSize:
            return (2*i)
        else:
            if self.heapList[2*i] < self.heapList[(2*i)+1]:
                return (2*i)
            else:
                return (2*i) + 1
	    #@end-editable@
    def delMin(self):
        #@start-editable@
        rm = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.downHeap(1)
        return rm
	    #@end-editable@
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  #// \label{lst:bh:loop}
            self.downHeap(i)
            i = i - 1
    #create a method to print the contents of the heap in level order
    def printHeap(self):
        print(self.heapList)
def main():
    heap = BinHeap()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    heap.buildHeap(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              heap.insert(int(operation[1]))
              heap.printHeap()
         elif (operation[0] == "R"):
              heap.delMin()
              heap.printHeap()
         inputs -= 1

if __name__ == '__main__':
    main()
