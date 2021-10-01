import unittest
import ex_13_sol

class Test_ex_13_sol(unittest.TestCase):

    def test_UFO(self):
        
        self.assertEqual(ex_13_sol.UFO(0, []), [])
        self.assertEqual(ex_13_sol.UFO(0, [], False), [])
        self.assertEqual(ex_13_sol.UFO(1, [1234], False), [4660])
        self.assertEqual(ex_13_sol.UFO(1, [1234]), [668])
        self.assertEqual(ex_13_sol.UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(ex_13_sol.UFO(2, [1234, 1777]), [668, 1023])

if __name__ == "__main__":
    unittest.main()
