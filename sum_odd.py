#A four-digit integer is given. Find the sum of odd digits in it.
even = 4567
counter = 0 
#Create a variable "var_int" and assign it a four-digit integer value.

x1 = even % 10 
counter += x1 %  2
even//= 10 

x1 = even % 10 
counter += x1 %  2
even//= 10 


x1 = even % 10 
counter += x1 %  2
even//= 10 

x1 = even % 10 
counter += x1 %  2
even//= 10 
#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
print(counter)
