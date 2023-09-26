class Node :
    def __init__(self , value = None, next = None):
        self.value = value
        self.next = next

class linked_list :
    def __init__(self):
        self.head = None
    def insert_at_begining(self , value):
        node = Node(value , self.head)
        self.head = node
    def print(self):
        list = []
        if self.head is None :
            print("empty list")
            return
        else :
            itr = self.head
            while itr :
                list.append(itr.value)
                itr = itr.next
        print(list)

    def insert_at_end(self , value):
        if self.head is None:
            self.head = Node(value)
            return
        else :
            itr = self.head
            while itr.next :
                itr = itr.next
            itr.next= Node(value)
    def insert_values(self , data_list):
        for data in data_list :
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr :
            counter +=1
            itr = itr.next
        return counter
    def remove_at_index(self , index):
        if index<0 or index >= self.get_length() :
            print("invalid index")
            return
        if index ==0 :
            self.head = self.head.next
            return
        itr = self.head
        for i in range(index-1):
            itr = itr.next
        itr.next = itr.next.next
    def insert_at_index(self , index , value):
        if index<0 or index >= self.get_length() :
            print("invalid index")
            return
        if index ==0 :
            self.insert_at_begining(value)
            return
        if index == self.get_length():
            self.insert_at_end(value)
            return
        itr = self.head
        for i in range(index-1):
            itr = itr.next
        node = Node(value , itr.next)
        itr.next = node

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        while itr :
            if itr.value == data_after:
                node = Node(data_to_insert , itr.next)
                itr.next = node
                return
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.value == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next :
            if itr.next.value == data:
                itr.next = itr.next.next
                break
            itr = itr.next



ll= linked_list()
ll.insert_at_begining(1)
ll.insert_at_begining(2)
ll.insert_at_end(3)
ll.insert_values([4,5,6])

print("*" * 30 + " after insertion " + "*" * 30)
ll.print()

print("*" * 30 + " the length of the list  " + "*" * 30)
print(ll.get_length())

print("*" * 30 + " after insert at index  " + "*" * 30)
ll.insert_at_index(2,100)
ll.print()

ll.remove_at_index(2)
print("*" * 30 + " after remove at index   " + "*" * 30)
ll.print()

print("*" * 30 + " insert after value  " + "*" * 30)
ll.insert_after_value(3 , 200)

ll.print()
print("*" * 30 + " remove by value  " + "*" * 30)
ll.remove_by_value(200)
ll.print()


