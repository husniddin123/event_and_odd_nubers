#A four-digit integer is given. Find the number of even digits in it.
number =  2465
counter = 0 
#Create a variable "var_int" and assign it a four-digit integer value.
x1 = number % 10 
x1 += 1
counter += x1 %  2
number //= 10 

x2 = number % 10 
x2 += 1
counter += x2 %  2
number //= 10 

x3 = number % 10 
x3 += 1
counter += x3 %  2
number //= 10 

x4 = number % 10 
x4 += 1
counter += x4 %  2
number //= 10 

#Print the number of even digits in the variable "var_int".

print(counter)