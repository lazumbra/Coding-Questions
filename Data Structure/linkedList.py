class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):

        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):

        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print('The node does not exist')
            return

        newNode = Node(data)

        newNode.next = prev_node.next
        prev_node.next = newNode

    def delete_node(self, key):

        current_node = self.head

        if current_node.data == key:
            self.head = current_node.next
            current_node = None
            return   

        prev = None
        while current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return    
        
        prev.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        count = 0
        prev = None
        while count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        
        if cur_node == None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        current_node = self.head

        count = 0

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def len_recursive(self, node):

        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)





llist = LinkedList()
llist.append("A")
llist.append('B')
llist.append('C')
llist.append('D')

print(llist.len_recursive(llist.head))

#llist.delete_node("B")
#llist.delete_node_at_pos(1)
llist.print_list()
print('\n')

llist.insert_after_node(llist.head.next, 'E')
llist.print_list()