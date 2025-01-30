friends=["apple","orange",23,45.67,False,"aakash","rohan"]
print(friends[0])
Name="Shubh"
print(Name[0])
# Name[0]="A"# Error because string is immutable
friends[0]="Mango"
print(friends[0]) # Output: Mango  because list is mutable
print(friends[1:4]) # Output: ['orange', 23, 45.67]