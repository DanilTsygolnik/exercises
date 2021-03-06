import unittest
from queues import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.qu = Queue()

    def test_main_methods(self):

        # check the template
        self.assertEqual(self.qu.size(), 0)
        self.assertEqual(self.qu.queue, [])

        # enqueue(item) test
        ref = [1,2,3]
        for i in ref:
            self.qu.enqueue(i)
        self.assertEqual(self.qu.size(), 3)
        self.assertEqual(self.qu.queue, ref)

        # dequeue(item) test
        cnt = 1
        while self.qu.size() > 0:
            curr_head = self.qu.dequeue()
            self.assertEqual(curr_head, ref[cnt-1])
            self.assertEqual(self.qu.queue, ref[cnt:])
            self.assertEqual(self.qu.size(), len(ref[cnt:]))
            cnt += 1
        self.assertIs(self.qu.dequeue(), None)

    def test_rotate(self):
        self.qu.queue = [1,2,3,4]
        self.qu.count = 4
        self.qu.rotate_queue(0)
        self.assertEqual(self.qu.queue, [1,2,3,4])
        self.assertEqual(self.qu.size(), 4)
        self.qu.rotate_queue(1)
        self.assertEqual(self.qu.queue, [2,3,4,1])
        self.qu.rotate_queue(2)
        self.assertEqual(self.qu.queue, [4,1,2,3])
        self.qu.rotate_queue(5)
        self.assertEqual(self.qu.queue, [1,2,3,4])




if __name__=="__main__":
    unittest.main()
