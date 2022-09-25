# Write a function called interleave_numbers that takes as input 
# two lists of three elements and returns a list of six elements, 
# with the interleaved numbers.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def interleave_numbers(a,b):
   interleaved_list = [a[0], b[0], a[1], b[1], a[2], b[2]]
   return interleaved_list

interleaved_list = interleave_numbers(list1, list2)
print(interleaved_list)