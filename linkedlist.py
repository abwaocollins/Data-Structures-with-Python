class Node:
    def __init__(self, data = None, next = None ):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print_items(self):
        if self.head is None:
            print("The linkedlist is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.next
        print(llstr)

    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_list_values(self, datalist):
        self.head = None
        for i in datalist:
            self.insert_end(i)
    def len_of_linkedlist(self):
        count = 0
        itr = self.head

        while itr:
            count = count + 1
            itr = itr.next
        
        return count

    def del_at(self,index):
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head

        while itr:
            if count == (index - 1):
                itr.next = itr.next.next
                break
            count = count + 1
            itr = itr.next
    def insert_at(self,index,data):
        if index < 0 or index > self.len_of_linkedlist():
            print("Sorry, index is out of range")

        if index == 0:
            self.head = self.insert_beginning(data)

        count = 0

        itr = self.head

        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            count = count + 1
            itr = itr.next

    def insert_after_value(self,data_after, data):
        if self.head.data == data_after:
            new_node = Node(data,self.head.next)
            self.head.next = new_node
        itr = self.head

        while itr:
            if itr.data == data_after:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break

            itr = itr.next

    def remove_by_value(self,data):

        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head


        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next



instance_link = linkedlist()
# instance_link.insert_beginning(20)
# instance_link.insert_beginning(65)
# instance_link.insert_beginning(78)
# instance_link.insert_end(55)
instance_link.insert_list_values([21,23,45,66])
instance_link.print_items()
# instance_link.del_at(2)
# instance_link.insert_at(3,77)
# instance_link.insert_after_value(23,42)
instance_link.remove_by_value(21)
instance_link.remove_by_value(66)
instance_link.print_items()

print("length",instance_link.len_of_linkedlist())