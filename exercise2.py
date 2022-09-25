# Populate a list of 10 integers entered by the user and display:
#   a) the number of even numbers contained in the list;
#   b) the sum of all odd numbers in the list;

class Lists:
    def __init__(self, list):
        self.list = list
        self.list_even_numbers = []
        self.list_odd_numbers = []

    def find_even_numbers(self):
        for a in self.list:
            if a % 2 == 0:
                self.list_even_numbers.append(a) 
            else:
                pass
        qty_even_numbers = len(self.list_even_numbers)
        return qty_even_numbers

    def find_odd_numbers(self):
        for a in self.list:
            if a % 2 == 0:
                pass
            else:
                self.list_odd_numbers.append(a) 
        sum_odd_numbers = sum(self.list_odd_numbers)
        return sum_odd_numbers       

list = []
for x in range(10):
    x = int(input())
    list.append(x)

myList = Lists(list)
print(myList.find_even_numbers())
print(myList.find_odd_numbers())