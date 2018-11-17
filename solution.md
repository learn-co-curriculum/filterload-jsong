
# Bloom Filter


```python
# Example Bloom Filter
from helper import hash256

bit_field_size = 10
bit_field = [0] * bit_field_size

h256 = hash256(b'hello world')
bit = int.from_bytes(h256, 'big') % bit_field_size
bit_field[bit] = 1
print(bit_field)
```


```python
# Example Bloom Filter 2

bit_field_size = 10
bit_field = [0] * bit_field_size

h = hash256(b'hello world')
bit = int.from_bytes(h, 'big') % bit_field_size
bit_field[bit] = 1
h = hash256(b'goodbye')
bit = int.from_bytes(h, 'big') % bit_field_size
bit_field[bit] = 1
print(bit_field)
```


```python
# Example Bloom Filter 3
from helper import hash160
from helper import murmur3

bit_field_size = 10
bit_field = [0] * bit_field_size

phrase1 = b'hello world'
h1 = hash256(phrase1)
bit1 = int.from_bytes(h1, 'big') % bit_field_size
bit_field[bit1] = 1
h2 = hash160(phrase1)
bit2 = int.from_bytes(h2, 'big') % bit_field_size
bit_field[bit2] = 1
phrase2 = b'goodbye'
h1 = hash256(phrase2)
bit1 = int.from_bytes(h1, 'big') % bit_field_size
bit_field[bit1] = 1
h2 = hash160(phrase2)
bit2 = int.from_bytes(h2, 'big') % bit_field_size
bit_field[bit2] = 1
print(bit_field)
```


```python
# Example BIP0037 Bloom Filter
from bloomfilter import BIP37_CONSTANT## Test Driven Exercise

field_size = 2
num_functions = 2
tweak = 42

bit_field_size = field_size * 8
bit_field = [0] * bit_field_size

for phrase in (b'hello world', b'goodbye'):
    for i in range(num_functions):
        seed = i * BIP37_CONSTANT + tweak
        h = murmur3(phrase, seed=seed)
        bit = h % bit_field_size
        bit_field[bit] = 1
print(bit_field)
```

## Try it


```python
# Exercise 1.1
from bloomfilter import BIP37_CONSTANT
from helper import (
    murmur3,
    bit_field_to_bytes
)

field_size = 10
function_count = 5
tweak = 99
items = (b'Hello World',  b'Goodbye!')

# bit_field_size is 8 * field_size
bit_field_size = field_size * 8
# create a bit field with the appropriate size
bit_field = [0] * bit_field_size

# for each item you want to add to the filter
for item in items:
    # iterate function_count number of times
    for i in range(function_count):
        # BIP0037 spec seed is i*BIP37_CONSTANT + tweak
        seed = i * BIP37_CONSTANT + tweak
        # get the murmur3 hash given that seed
        h = murmur3(item, seed=seed)
        # set the bit to be h mod the bit_field_size
        bit = h % bit_field_size
        # set the bit_field at the index bit to be 1
        bit_field[bit] = 1
# print the bit field converted to bytes using bit_field_to_bytes in hex
print(bit_field_to_bytes(bit_field).hex())
```

## Test Driven Exercise


```python
# Exercise 1.2

from bloomfilter import (
    BloomFilter,
    BIP37_CONSTANT
)

from helper import (
    murmur3
)

class BloomFilter(BloomFilter):

    def add(self, item):
        '''Add an item to the filter'''
        # iterate self.function_count number of times
        for i in range(self.function_count):
            # BIP0037 spec seed is i*BIP37_CONSTANT + self.tweak
            seed = i * BIP37_CONSTANT + self.tweak
            # get the murmur3 hash given that seed
            h = murmur3(item, seed=seed)
            # set the bit at the hash mod the bitfield size (self.size*8)
            bit = h % (self.size * 8)
            # set the bit field at bit to be 1
            self.bit_field[bit] = 1
```
