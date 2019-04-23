import unittest
from insertion import insertion_sort

class SortingTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        values=[3,2,1,4,5]
        sorted_data=[1,2,3,4,5]
        insertion_sort(values)
        self.assertListEqual(values, sorted_data)

if __name__=='__main__':
    unittest.main()
