from igraph import *

g=Graph()

g.add_vertices(10)

g.vs['name'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

g.add_edges([('a','b'),('a','c'),('a','f'),('a','d'),('b','e'),('b','g'),('b','d'),('c','f'),('c','d'),('d','e'), ('e','g'), ('g','f'),('h','f'),('h','g'),('h','i'),('i','j')])

print g




