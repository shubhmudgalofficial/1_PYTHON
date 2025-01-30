a=("rohan","apple",1,123,45.67,1)
print(a)
print(a[2])
print(type(a))
#tuple methods
print(a.count(1)) # Output: 2 because 1 is present 2 times in tuple
print(a.index(45.67)) # Output: 4 because 45.67 is present at index 4`
# a[3]=5 # Error because tuple is immutable
repeat=a*3
print(repeat)
print(len(a))
print("apple" in a) # Output: True because "apple" is present in tuple
print("grape" in a) # Output: False because "grape" is not present in tuple
# print(max(a)) # Output: Error because tuple contains string and integer
b=(12,3,4,56,224,)
print(max(b)) # Output: 224 because all elements in tuple are integers
print(min(b)) # Output:  3 because all elements in tuple are integers
d,e,f,g,h=b
z=len(b)
print(a)

print(d,e,f,g,h) 
print(z)
