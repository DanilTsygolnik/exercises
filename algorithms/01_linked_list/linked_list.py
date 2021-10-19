class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

   #def print_all_nodes(self):
   #    node = self.head
   #    while node != None:
   #        print(node.value)
   #        node = node.next

    def print_all_nodes(self, as_list=False):
        node = self.head
        nodes_values = []
        while node != None:
            if as_list == False:
                print(node.value)
            nodes_values.append(node.value)
            node = node.next
        if as_list:
            return nodes_values

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # ++ approved
    def find_all(self, val):
        results = None
        node = self.head
        while node is not None:
            if node.value == val:
                if results == None:
                    results = []
                results.append(node)
            node = node.next
        return results

    # ready for approval
    def delete(self, val, remove_all=True):
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            if curr_node.value == val:
                if curr_node is self.tail:
                    if prev_node == None:
                        self.clean()
                        break
                    prev_node.next = None
                    self.tail = prev_node
                elif curr_node.next.value != val:
                    if prev_node is None:
                        self.head = curr_node.next
                    else:
                        prev_node.next = curr_node.next
                        if remove_all == False:
                            break
                else:
                    if remove_all == False:
                        if prev_node is None:
                            self.head = curr_node.next
                        else:
                            prev_node.next = curr_node.next
                        break
            else:
                prev_node = curr_node
            curr_node = curr_node.next

    # ready for approval
    def clean(self):
        self.head = None
        self.tail = None
 
    # ready for approval
    def len(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    # ready for approval
    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            node = self.head
            while node is not None:
                if node is afterNode:
                    if node is self.tail:
                        newNode.next = None
                        self.tail = newNode
                    else:
                        newNode.next = node.next
                    node.next = newNode
                    break
                node = node.next
