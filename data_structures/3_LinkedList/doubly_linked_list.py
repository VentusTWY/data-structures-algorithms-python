class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DDLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return

        itr=self.head
        listarr=[]
        while itr:
            listarr.append(itr.data)
            itr=itr.next
        print(listarr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    #     if self.head is None:
    #         self.head = Node(data, None)
    #         return

    #     itr = self.head

    #     while itr.next:
    #         itr = itr.next

    #     itr.next = Node(data, None)




if __name__ == '__main__':
    gg = DDLinkedList()
    gg.insert_values(["banana","mango","grapes","orange"])
    gg.print_backward()
    gg.print()


    # ll = LinkedList()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()




