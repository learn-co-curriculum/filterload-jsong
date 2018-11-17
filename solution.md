
# Loading a Bloom Filter

## Test Driven Exercise


```python
# Exercise 2.1

from bloomfilter import BloomFilter
from helper import (
    encode_varint,
    int_to_little_endian
)

class BloomFilter(BloomFilter):

    def filterload(self, flag=1):
        '''Return the payload that goes in a filterload message'''
        # encode_varint self.size
        payload = encode_varint(self.size)
        # next is the self.filter_bytes()
        payload += self.filter_bytes()
        # function count is 4 bytes little endian
        payload += int_to_little_endian(self.function_count, 4)
        # tweak is 4 bytes little endian
        payload += int_to_little_endian(self.tweak, 4)
        # flag is 1 byte little endian
        payload += int_to_little_endian(flag, 1)
        return payload
```
