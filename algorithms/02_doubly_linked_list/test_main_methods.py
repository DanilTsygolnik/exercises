# pylint: disable=c0114,c0115,c0116,c0103
import unittest
import ctypes
from doubly_linked_list import LinkedList2
from doubly_linked_list import Node

def get_linked(nodes):
    s_list = LinkedList2()
    for i in nodes:
        s_list.add_in_tail(i)
    return s_list

class TestFind(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

class TestFindall(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), nodes)

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3]])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3], nodes[5]])

class TestDelete(unittest.TestCase):

    def test_single_node(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        s_list.delete(5)
        self.assertEqual(s_list.get_all_nodes(), nodes)
        s_list.delete(1)
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

    def test_long_multiple_nodes(self):
        nodes = [Node(1), Node(1), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        s_list.delete(1) # delete a single node from head ( [1->1->1->0->0->] >>> [1->1->0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[1:])
        self.assertIs(s_list.head, nodes[1])

        nodes = [Node(1), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        s_list.delete(1, True) # delete multiple nodes from head ( [1->1->0->0->] >>> [0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[2:])
        self.assertIs(s_list.head, nodes[2])

        nodes = [Node(0), Node(0), Node(1), Node(1)]
        s_list = get_linked(nodes)
        s_list.delete(1, True) # delete nodes from tail ( [0->0->1->1->] >>> [0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[:2])
        self.assertIs(s_list.tail, nodes[1])

        s_list.delete(0, True) # delete all nodes from the list ( [0->0->] >>> [] )
        self.assertEqual(s_list.get_all_nodes(), [])
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

class TestLenClean(unittest.TestCase):
    def setUp(self):
        nodes = [Node(1), Node(1), Node(1), Node(0), Node(0)]
        self.s_list = get_linked(nodes)

    def tearDown(self):
        self.s_list = None

    def test_len(self):
        self.assertEqual(self.s_list.len(), 5)

    def test_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIs(self.s_list.head, self.s_list.tail)

class TestInsert(unittest.TestCase):

    def test_case_1(self):
        """
        Case 1.1: Linked list is empty; afterNode is in list.
        Case 1.2: Linked list is empty; afterNode is not in list.

        Checked result:
            self.head=self.tail=newNode
        """
        nodes = [Node(0)]
        s_list = LinkedList2()
        # case 1.1
        s_list.insert(None, nodes[0])
        self.assertTrue(all([s_list.head is nodes[0], s_list.tail is nodes[0]]))
        s_list.clean()
        # case 1.2
        s_list.insert(Node(1), nodes[0])
        self.assertTrue(all([s_list.head is nodes[0], s_list.tail is nodes[0]]))

    def test_case_2(self):
        """
        Linked list contains a single node: [0->]
        Case 2.1: afterNode is not in list -- no changes.
        Case 2.2: afterNode=None -- add newNode in tail.
        Case 2.3: afterNode is in list (the last node) -- add newNode in tail.
        Case 2.4: as prev case; afterNode=None -- add newNode in tail.
        Case 2.5: afterNode is inside long list.
        """
        # case 2.1
        nodes = [Node(0), Node(1), Node(2)]
        s_list = LinkedList2()
        s_list.add_in_tail(nodes[0])
        s_list.insert(Node(5), nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes[:1])

        # case 2.2
        s_list.insert(None, nodes[1])
        self.assertEqual(s_list.get_all_nodes(), nodes[:2])
        self.assertIs(s_list.tail, nodes[1])

        # case 2.3
        s_list.insert(nodes[1], nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes)
        self.assertIs(s_list.tail, nodes[2])

        # case 2.4
        nodes.append(Node(3)) # nodes = [Node(0), Node(1), Node(2), Node(3)]
        s_list.insert(None, nodes[3])
        self.assertEqual(s_list.get_all_nodes(), nodes)
        self.assertIs(s_list.tail, nodes[3])

        # case 2.5
        inp_node = Node(5)
        nodes.insert(2, inp_node) # nodes = [Node(0), Node(1), Node(5), Node(2), Node(3)]
        self.assertNotEqual(s_list.get_all_nodes(), nodes)
        s_list.insert(nodes[1], nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes)


if __name__=="__main__":
    unittest.main()
