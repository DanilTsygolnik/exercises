import unittest
from bird_class import Bird

class TestBird(unittest.TestCase):

    def test_basic_class_features(self):
        # create two birds
        bird_1 = Bird("Jack", 1, 2)
        bird_2 = Bird("Stevie", 2, 5)

        self.assertEqual(Bird.__doc__, "An abstract class representing birds")
        self.assertEqual(Bird.objInstancesCnt, 2)

        bird_1.get_info()
        bird_2.get_info()

if __name__=="__main__":
    unittest.main()
