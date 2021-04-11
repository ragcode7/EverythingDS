class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyQueue():
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def enqueue(self, data):
        node = Node(data)
        if self.last_node:
            self.last_node.next = node
        self.last_node = node
        if not self.first_node:
            self.first_node = self.last_node
        return

    def dequeue(self):
        if not self.first_node:
            print("Queue Empty Exception")
            return
        data = self.first_node.data
        self.first_node = self.first_node.next
        if not self.first_node:
            self.last_node = None
        return data

    def size(self):
        if not self.first_node:
            return 0
        else:
            size_count = 1
            current = self.first_node
            while current.next:
                size_count += 1
                current = current.next
            return size_count

    def front(self):
        if not self.first_node:
            print("Queue Empty Exception")
        return self.first_node.data

    def isEmpty(self):
        return self.first_node is None

    def printQueue(self):
        if (self.isEmpty()):
            print("Queue Empty")
        else:
            temp=self.first_node
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print()
        return
#driver code...
def testqueue():
        q1 = MyQueue()
        inputs=int(input())
        while inputs>0:
            command=input()
            operation=command.split()
            if(operation[0]=="S"):
                print(q1.size())
            elif(operation[0]=="I"):
                print(q1.isEmpty())
            elif(operation[0]=="E"):
                q1.enqueue(int(operation[1]))
                q1.printQueue()
            elif(operation[0]=="D"):
                print(q1.dequeue())
                q1.printQueue()
            elif(operation[0]=="F"):
                print(q1.front())
            inputs-=1

def main():
        testqueue()

if __name__ == '__main__':
        main()