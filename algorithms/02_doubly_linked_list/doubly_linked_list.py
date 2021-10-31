#pylint: disable=c0114,c0115,c0116,c0103
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def wipe_links(self):
        self.next = None
        self.prev = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def get_all_nodes(self, as_val=False):
        """
        Метод отладочного вывода значений всех узлов связного списка
        По умолчанию выводит на экран значение каждого узла
        При as_list=True возвращает список значений узлов
        """
        node = self.head
        nodes = []
        nodes_values = []
        while node is not None:
            nodes.append(node)
            nodes_values.append(node.value)
            node = node.next
        if as_val:
            return nodes_values
        return nodes

    def find(self, val):
        """Метод возвращает первый найденный по значению val узел"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """Метод возвращает список всех узлов со значением val"""
        node = self.head
        nodes_list = []
        while node is not None:
            if node.value == val:
                nodes_list.append(node)
            node = node.next
        return nodes_list

    def delete(self, val, rm_all=False):
        node = self.head
        did_rm = False
        while (node is not None) and (not all([not rm_all, did_rm])):
            if node.value == val:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                else:
                    if node is self.head:
                        node.next.prev = None
                        self.head = node.next
                    elif node is self.tail:
                        node.prev.next = None
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                        node.prev.next = node.next
                    did_rm = True
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            if (afterNode is None) or (self.tail is afterNode):
                self.add_in_tail(newNode)
            else:
                node = self.head
                while node is not None:
                    if node is afterNode:
                        node.next.prev = newNode
                        newNode.next = node.next
                        node.next = newNode
                        newNode.prev = node
                        break
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
