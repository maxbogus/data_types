import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


def question1(s, t):
    """ Question 1:
    Given two strings s and t, determine whether some anagram of t is a substring of s.
    For example: if s = "udacity" and t = "ad", then the function returns True.
    Your function definition should look like: question1(s, t) and return a boolean True or False."""
    if s == t or len(s) < len(t):
        return False
    result = ''
    for letter in t:
        if letter in s:
            result += letter
    return result == t


# Should be False
print question1('a', 'a')
# Should be False
print question1(None, None)
# Should be False
print question1('a', 'b')
# Should be False
print question1('aaaaa', 'a')
# Should be True
print question1('ab', 'b')
# Should be True
print question1('udacity', 'ad')


def question2(a):
    """ # Question 2
    Given a string a, find the longest palindromic substring contained in a.
    Your function definition should look like question2(a), and return a string."""
    if is_palindrome(a):
        return a
    result = ''
    limit = len(a)
    index = 0
    while index < limit:
        pindex = 0
        if len(result) >= (limit - index):
            break
        while pindex < limit:
            sub = a[index:limit - pindex]
            # TODO: optimize break condition
            if len(result) >= len(sub):
                break
            if is_palindrome(sub):
                if len(sub) > len(result):
                    result = sub
            pindex += 1
        index += 1
    return result


def is_palindrome(s):
    return s == s[::-1]


# should be s
print question2('sex')
# should be sexes
print question2('sexes')
# should be sexes
print question2('presexesx')


def question3(G):
    """ # Question 3
    Given an undirected graph G, find the minimum spanning tree within G.
    A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
    Your function should take in and return an adjacency list structured like this:

    {'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]}
    Vertices are represented as unique strings. The function definition should be question3(G)"""
    return []


def question4(T, r, n1, n2):
    """ # Question 4
    # Find the least common ancestor between two nodes on a binary search tree.
    # The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
    # For example, the root is a common ancestor of all nodes on the tree,
    # but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor.
    # You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
    # The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
    # where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
    # r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two
    # nodes in no particular order. For example, one test case might be

    # question4([[0, 1, 0, 0, 0],
    #           [0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0],
    #           [1, 0, 0, 0, 1],
    #           [0, 0, 0, 0, 0]],
    #          3,
    #          1,
    #          4)
    # and the answer would be 3."""
    return []


def question5(ll, m):
    """ # Question 5
    # Find the element in a singly linked list that's m elements from the end.
    # For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
    # The function definition should look like question5(ll, m), where ll is the first node of a
    # linked list and m is the "mth number from the end".
    # You should copy/paste the Node class below to use as a representation of a node in the linked list.
    # Return the value of the node at that position."""
    current = ll.head
    result = [current.data]
    while current.next:
        current = current.next
        result.append(current.data)
    return result[m - 1] if m - 1 < len(result) else -1


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

# should be 3
print question5(ll, 3)
# should be 4
print question5(ll, 4)
# should be -1
print question5(ll, 6)


class TestStringMethods(unittest.TestCase):
    def test_firstQuestion(self):
        self.assertFalse(question1('a', 'a'))
        self.assertFalse(question1(None, None))
        self.assertFalse(question1('a', 'b'))
        self.assertTrue(question1('ab', 'b'))
        self.assertTrue(('udacity', 'ad'))

    def test_secondQuestion(self):
        self.assertEquals('sexes', question2('sexes'))
        self.assertEquals('sexes', question2('presexesx'))
        self.assertEquals('s', question2('sex'))

    def test_thirdQuestion(self):
        self.assertTrue(question3(''))

    def test_fourthQuestion(self):
        self.assertTrue(question4('', '', '', ''))

    def test_fifthQuestion(self):
        self.assertEquals(question5(ll, 3), 3)
        self.assertEquals(question5(ll, 4), 4)
        self.assertEquals(question5(ll, 6), -1)


if __name__ == '__main__':
    unittest.main()
