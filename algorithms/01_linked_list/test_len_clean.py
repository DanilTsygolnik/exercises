import ctypes
import unittest
import linked_list

class TestLinkedList(unittest.TestCase):
    
    def test_linked_list_len(self):
        memory_slots = (13*ctypes.py_object)()
        
        memory_slots[0] = linked_list.Node(0) # node 1
        memory_slots[1] = linked_list.Node(0) # node 2
        memory_slots[2] = linked_list.Node(0) # node 3
        memory_slots[3] = linked_list.Node(1) # node 4
        memory_slots[4] = linked_list.Node(0) # node 5
        memory_slots[5] = linked_list.Node(0) # node 6
        memory_slots[6] = linked_list.Node(0) # node 7
        memory_slots[7] = linked_list.Node(1) # node 8
        memory_slots[8] = linked_list.Node(1) # node 9
        memory_slots[9] = linked_list.Node(1) # node 10
        memory_slots[10] = linked_list.Node(0) # node 11
        memory_slots[11] = linked_list.Node(0) # node 12
        memory_slots[12] = linked_list.Node(0) # node 13

        s_list = linked_list.LinkedList()
        for i in range(13):
            s_list.add_in_tail(memory_slots[i])
        
        self.assertEqual(s_list.len(), 13)
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

if __name__ == "__main__":
    unittest.main()
