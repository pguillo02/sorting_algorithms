import unittest 
import sorting
class test_sorting(unittest.TestCase):

    def test_insertion(self):
        self.assertEqual(sorting.insertion([8,4,3,2,6,7,5,1]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.insertion([1,2,3,4,5,6,8,7]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.insertion([2,1]), [1,2])
        self.assertEqual(sorting.insertion([]),[])

    def test_bubble(self):
        self.assertEqual(sorting.bubble([8,4,3,2,6,7,5,1]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.bubble([1,2,3,4,5,6,8,7]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.bubble([2,1]), [1,2])
        self.assertEqual(sorting.bubble([]),[])

    def test_selection(self):
        self.assertEqual(sorting.selection([8,4,3,2,6,7,5,1]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.selection([1,2,3,4,5,6,8,7]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.selection([2,1]), [1,2])
        self.assertEqual(sorting.selection([]),[])

    def test_merge(self):
        self.assertEqual(sorting.merge([8,4,3,2,6,7,5,1]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.merge([1,2,3,4,5,6,8,7]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.merge([2,1]), [1,2])
        self.assertEqual(sorting.merge([]),[])

    def test_heap(self):
        self.assertEqual(sorting.heap([8,4,3,2,6,7,5,1]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.heap([1,2,3,4,5,6,8,7]), [1,2,3,4,5,6,7,8])
        self.assertEqual(sorting.heap([2,1]), [1,2])
        self.assertEqual(sorting.heap([]),[])
        
if __name__ == "__main__":

    unittest.main()