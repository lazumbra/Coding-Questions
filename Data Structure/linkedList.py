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

    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return
        
        prev1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev1 = curr_1
            curr_1 = curr_1.next

        prev2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev2 = curr_2
            curr_2 = curr_2.next
        
        #Checar se eu encontrei mesmo os valores
        #Se um ou outro valor for None sair da função
        #Pois não existe swap
        if not curr_1 or not curr_2:
            return
        
        #Alocar os ponteiros dos dois prev
        if prev1:
            prev1.next = curr_2
        else:
            self.head = curr_2

        if prev2:
            prev2.next = curr_1
        else:
            self.head = curr_1

        #Alocar os current
        curr_1.next, curr_2.next =  curr_2.next, curr_1.next
        print('cheguei aqui')






llist = LinkedList()
llist.append("A")
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')

llist.print_list()
print('vot')
llist.swap_nodes("B", "E")
print('\n')


llist.print_list()
print('terminei')
