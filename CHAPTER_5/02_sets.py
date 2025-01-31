d={    }
print(d,type(d))
s=set()
print(s,type(s))
s={1,2,33,45,66,4,3,2}
z={1,2,233,45,636,4,3,52}
print(s,type(s))
s.add(77)
print(s)
s.add(988)
print(s)
print(len(s))
s.remove(66)
print(s)
s.pop() # This will remove first element
print(s) 
print((s.union(z)))
print(s.intersection(z))
print(s.difference(z))
