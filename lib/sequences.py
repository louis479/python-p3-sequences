#!/usr/bin/env python3

# fibonacci_list = [0,1,1,2,3,5,8,13,21]
# month_tuple = ('January', 'February', 'March', 'April', 'May', 'June')
# even_numbers = range(0, 49, 98)
# sentence_string = "Python is awesome!"
# def print_fibonacci(length):
#     pass


def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    for _ in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence[:length])

# Example usage:
print_fibonacci(10) 
