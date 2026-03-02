# MyFunction

Python utility functions collection.

## Features

### Fibonacci Calculator

Multiple implementations for calculating Fibonacci numbers:

- **Recursive**: Simple but exponential time complexity
- **Iterative**: Efficient O(n) time, O(1) space
- **Sequence**: Generate list of first n numbers
- **Generator**: Memory-efficient streaming

## Usage

```python
from fibonacci import fibonacci_iterative, fibonacci_sequence, fibonacci_generator

# Calculate specific Fibonacci number
result = fibonacci_iterative(10)  # Returns 55

# Generate sequence
sequence = fibonacci_sequence(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Use generator for large sequences
for num in fibonacci_generator(100):
    print(num)
```

## Run Demo

```bash
python fibonacci.py
```

## License

MIT
