#A four-digit integer is given. Find the number of odd digits in it.
number = 5438
counter = 0 

x1 = number % 10 
counter += x1 % 2
number //= 10

x2 = number % 10 
counter += x2 % 2
number //= 10

x3 = number % 10 
counter += x3 % 2
number //= 10

x4 = number % 10 
counter += x4 % 2
number //= 10
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int"

print(counter)
