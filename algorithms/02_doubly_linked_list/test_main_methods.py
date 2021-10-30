# pylint: disable=c0114,c0115,c0116,c0103
import unittest
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

class TestDeleteFromPrevTask(unittest.TestCase):
    def setUp(self):

        self.s_list_1 = LinkedList2()
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(0))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(0))

        self.s_list_2 = LinkedList2()
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(1))
        self.s_list_2.add_in_tail(Node(1))
        self.s_list_2.add_in_tail(Node(1))

        self.s_list_3 = LinkedList2()
        self.s_list_3.add_in_tail(Node(1))
        self.s_list_3.add_in_tail(Node(1))
        self.s_list_3.add_in_tail(Node(1))

    def tearDown(self):
        self.s_list_1 = None
        self.s_list_2 = None
        self.s_list_3 = None

    def test_case_1(self):
        """
        s_list_1 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        rm_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [ 1, 1, 1, 0, 1, 0]
        ожидаемый список значений [1, 1, 0, 1, 0]
        """
        nodes_val_ref = [1, 1, 0, 1, 0]
        self.s_list_1.delete(1, rm_all=False)
        nodes_val_after_del = self.s_list_1.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_2(self):
        """
        s_list_1 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        rm_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [1, 1, 1, 0, 1, 0]
        ожидаемый список значений [0, 0]
        """
        nodes_val_ref = [0, 0]
        self.s_list_1.delete(1, rm_all=True)
        nodes_val_after_del = self.s_list_1.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_3(self):
        """
        s_list_2 .....| 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> |.....

        rm_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [0, 0, 0, 1, 1, 1]
        ожидаемый список значений [0, 0, 0, 1, 1]
        """
        nodes_val_ref = [0, 0, 0, 1, 1]
        self.s_list_2.delete(1, rm_all=False)
        nodes_val_after_del = self.s_list_2.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_4(self):
        """
        s_list_2 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        rm_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [0, 0, 0, 1, 1, 1]
        ожидаемый список значений [0, 0, 0]
        """
        nodes_val_ref = [0, 0, 0]
        self.s_list_2.delete(1, rm_all=True)
        nodes_val_after_del = self.s_list_2.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_5(self):
        """
        s_list_3 .....| 1 -> 1 -> 1 -> |.....

        rm_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [1, 1, 1]
        ожидаемый список значений [1, 1]
        """
        nodes_val_ref = [1, 1]
        self.s_list_3.delete(1, rm_all=False)
        nodes_val_after_del = self.s_list_3.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)
        self.assertIsNot(self.s_list_3.head, self.s_list_3.tail)

    def test_case_6(self):
        """
        s_list_3 .....| 1 -> 1 -> 1 -> |.....

        rm_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [1, 1, 1]
        ожидаемый список значений []
        """
        nodes_val_ref = []
        self.s_list_3.delete(1, rm_all=True)
        nodes_val_after_del = self.s_list_3.get_all_nodes(as_val=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)
        self.assertIs(self.s_list_3.head, None)
        self.assertIs(self.s_list_3.tail, None)
        self.assertIs(self.s_list_3.head, self.s_list_3.tail)

if __name__=="__main__":
    unittest.main()
