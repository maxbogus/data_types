"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib(position):
    if position < 0:
        return None
    if position == 0 or position == 1:
        return position
    return get_fib(position - 2) + get_fib(position - 1)


# Test cases
print "first case. expect 0"
print get_fib(0)
print "second case. expect 1"
print get_fib(1)
print "third case. expect 1"
print get_fib(2)
print "fourth case. expect 2"
print get_fib(3)
print "fifth case. expect 3"
print get_fib(4)
print "sixth case. expect 5"
print get_fib(5)
print "seventh case. expect 34"
print get_fib(9)
print get_fib(11)


def get_fib_for(position):
    """cycle representation"""
    if position <= 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    next = first + second
    i = 2
    while i < position:
        first = second
        second = next
        next = first + second
        i += 1
    return next

# Test cases
print "first case. expect 0"
print get_fib_for(0)
print "second case. expect 1"
print get_fib_for(1)
print "third case. expect 1"
print get_fib_for(2)
print "fourth case. expect 2"
print get_fib_for(3)
print "fifth case. expect 3"
print get_fib_for(4)
print "sixth case. expect 5"
print get_fib_for(5)
print "seventh case. expect 34"
print get_fib_for(9)
print get_fib(11)