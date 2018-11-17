from unittest import TestCase
from ipynb.fs.full.index import *

class BloomFilterTest(TestCase):

    def test_add(self):
        bf = BloomFilter(10, 5, 99)
        item = b'Hello World'
        bf.add(item)
        expected = '0000000a080000000140'
        self.assertEqual(bf.filter_bytes().hex(), expected)
        item = b'Goodbye!'
        bf.add(item)
        expected = '4000600a080000010940'
        self.assertEqual(bf.filter_bytes().hex(), expected)
