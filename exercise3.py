# Fill in a list of 10 numbers entered by the user.
# From this list, generate a list with the even numbers 
# and one with the odd numbers. 

list = []
list_even_numbers = []
list_odd_numbers = []

for x in range(10):
   x = int(input())
   list.append(x)

for a in list:
   if a % 2 == 1:
       list_odd_numbers.append(a)
   else:
       list_even_numbers.append(a)

print("Even numbers: " , list_even_numbers)
print("Odd numbers: " , list_odd_numbers)