class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    
    def upHeap(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.upHeap(self.currentSize)

    def downHeap(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.downHeap(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  
            self.downHeap(i)
            i = i - 1

    def update(self, k1, k2):
        #@start-editable@
        for i in range(self.currentSize+1):
            if(self.heapList[i]==k1):
                self.heapList[i]=k2
                if(k1>k2):
                    self.upHeap(i)
                else:
                    self.downHeap(i)
                return
	    #@end-editable@


    def checkHeap(self, alist):
        #@start-editable@
        checkl = alist
        for i in range(int(((len(checkl)) - 2)/2) + 1):
            if checkl[2*i + 1] < checkl[i]:
                return False
            if (2*i + 2 < (len(checkl)) and checkl[2*i + 2] < checkl[i]):
                return False
        return True
	    #@end-editable@


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
        elif (operation[0] == "U"):
            heap.update(int(operation[1]),int(operation[2]))
            heap.printHeap()
        elif (operation[0] == "C"):
            arraySize = operation[1]
            arr = list(map(int, input().split()))
            print(heap.checkHeap(arr))
        inputs -= 1
        
if __name__ == '__main__':
    main()