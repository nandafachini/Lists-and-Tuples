# Fill in two tuples with 5 numbers each, informed by the user. 
# Concatenate the two tuples and display the resulting tuple.

list1 = []
list2 = []

for x in range(5):
   x = int(input())
   list1.append(x)

for a in range(5):
   a = int(input())
   list2.append(a)

tuple1 = tuple(list1)
tuple2 = tuple(list2)
final_tuple = tuple1 + tuple2
print(final_tuple)