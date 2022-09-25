#A four-digit integer is given. Find the sum of even digits in it.
even = 2436
counter = 0 
#Create a variable "var_int" and assign it a four-digit integer value.

x1 = even % 10 
x1 += 1
counter += x1 %  2
even//= 10 

x2 = even % 10 
x2 += 1
counter += x2 %  2
even //= 10 

x3 = even % 10 
x3 += 1
counter += x3 %  2
even //= 10 

x4 = even % 10 
x4 += 1
counter += x4 %  2
even //= 10 

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
print(counter)