# Fill a list with 10 integers entered by the user

list = []
for x in range(10):
   x = int(input())
   list.append(x)


#  a) print the highest number on the list:
def print_max_list(list):
    print(max(list))


# b) print the lowest number on the list:
def print_min_list(list):
    print(min(list))
    

# c) the average of the numbers contained in the list:
def print_average_list(list):
        sum_list = sum(list)
        print(sum_list/len(list))


# calling the functions
max_number = print_max_list(list)
min_number = print_min_list(list)
average = print_average_list(list)
