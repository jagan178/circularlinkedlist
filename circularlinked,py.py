class Nodee:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circularlist:
    def __init__(self):
        self.head = None
        self.temp = None
        self.tail = None

    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            value = int(input("Enter a value: "))
            newnode = Nodee(value)
            if self.head is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                self.tail = newnode
            self.tail.next = self.head

    def display(self):
        self.temp = self.head
        while self.temp.next != self.head:
            print(self.temp.data)
            self.temp = self.temp.next
        print(self.temp.data)

    def insertfront(self):
        data = int(input("Enter value to insert at front: "))
        newnode = Nodee(data)
        newnode.next = self.head
        self.head = newnode
        self.tail.next = self.head

    def insertend(self):
        newnode = Nodee(int(input("Enter value to insert at end: ")))
        self.tail.next = newnode
        self.tail = newnode
        newnode.next = self.head

    def insertmiddle(self):
        posi = int(input("Enter position to insert: "))
        newnode = Nodee(int(input("Enter value to insert at middle: ")))
        self.temp = self.head
        prev = None
        i = 1
        while i < posi:
            prev = self.temp
            self.temp = self.temp.next
            i += 1
        newnode.next = self.temp
        prev.next = newnode

    def delfront(self):
        self.temp = self.head
        self.head = self.head.next
        self.tail.next = self.head
        del self.temp

    def delend(self):
        self.temp = self.head
        prev = None
        while self.temp.next != self.head:
            prev = self.temp
            self.temp = self.temp.next
        prev.next = self.head
        self.tail = prev
        del self.temp

    def delmiddle(self):
        posi = int(input("Enter position to delete: "))
        self.temp = self.head
        prev = None
        i = 1
        while i < posi:
            prev = self.temp
            self.temp = self.temp.next
            i += 1
        prev.next = self.temp.next
        del self.temp

    def count(self):
        count = 1
        self.temp = self.head
        while self.temp.next != self.head:
            count += 1
            self.temp = self.temp.next
        print(count)

    def search(self):
        item = int(input("Enter the search element: "))
        self.temp = self.head
        while self.temp:
            if self.temp.data == item:
                print(f"{item} found ")
                return
            self.temp = self.temp.next
        print(f"{item} is not in the list")

obj = Circularlist()
obj.create()
obj.display()
obj.insertfront()
obj.display()
obj.insertend()
obj.display()
obj.insertmiddle()
obj.display()
obj.delfront()
obj.display()
obj.delend()
obj.display()
obj.delmiddle()
obj.display()
obj.count()
obj.search()
