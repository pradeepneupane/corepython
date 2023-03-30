""""
Iterable - __iter__() or __getitem__()
Iterator - __next()__
Iteration
"""

# for i in range(50):
#     print(i)

def gen(n):
    for i in range(n):
        yield i

# g = gen(456789)
# print(g)

g = gen(3)
# print(g)
# #
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# #
# for i in g:
#     print(i)

h  = "harry"
# for c in h:
#     print(c)
#     print(h[0])

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


