#!/usr/bin/env python
# coding: utf-8

# In[2]:


f_name=input("Enter Your First Name:\n")
l_name=input("Enter Your Last Name:\n")
print("Greetings!!!",f_name,l_name)


# In[6]:


a=10
b=2.3
c="heyy"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[18]:


r=int(input("Enter Radius of a circle:\n"))
pi=3.14
area=pi*r*r
print("Area of a circle:",area)


# In[26]:


bp=input("Enter Your Salary:\n")
hra=int(bp)*0.10
ta=int(bp)*0.5
print("HRA is",hra)
print("TA is",ta)


# In[23]:


num1=int(input("Enter First Number:\n"))
num2=int(input("Enter Second Number:\n"))
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print("ADDITON:",add)
print("SUBSTRACT:",sub)
print("MULTIPLICATION:",mul)
print("DIVISION:",div)


# In[1]:


num=int(input("Enter a Number:\n"))
if(num%2==0):
    print("Its Even")
else:
    print("Its Odd")


# In[16]:


year1 =int(input("Enter a Year: \n"))
year2 =int(input("Enter Second Year: \n"))
print("Leap years between",year1,"and",year2,"are:")
for year in range(year1,year2 + 1):
    if (year%400==0)and(year%100==0)or(year%4==0):
        print(year)
    


# In[18]:


a = input("Enter a first number: \n")
b = input("Enter a second number: \n")
c = input("Enter a third number: \n")
if(a>b):
    if(a>c):
        print(a,"is the greatest number")
    else:
        print(c,"is the greatest number")
else:
    if(b>c):
        print(b,"is the greatest number")
    else:
        print(c,"is the greatest number")


# In[21]:


character = input("Enter a string: \n")
vowels = ["a","e","i","o","u"]
for i in character:
    if i in vowels:
        print(i,"is vowel")
    else:
        print(i,"is character")


# In[23]:


num = int(input("Enter a number: \n"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print("The Factorial of",num,"is",factorial)


# In[15]:


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i*j, end=" ")
    print("")


# In[10]:


user_input = input("Enter numbers separated by spaces: ")
numbers_str = user_input.split()
numbers = [int(num) for num in numbers_str]
total_sum = sum(numbers)
print("The sum of all the numbers is:", total_sum)


# In[18]:


a, b = 0, 1
print("Fbinocci series")
n = int(input("Enter number of terms:"))
for _ in range(n):
    print(a,end="")
    a,b=b,a+b


# In[ ]:





# In[1]:



N = int(input("Enter a value for N: "))
for i in range(1, N + 1):
    for j in range(1, i + 1):
        multiple = i * j
        print(multiple, end=" ")  
    print()  


# In[2]:


number = int(input("Enter a number to find its factors: "))
divisor = 1
print(f"The factors of {number} are:")
while divisor <= number:
    if number % divisor == 0: 
        print(divisor)  
    divisor += 1  


# In[3]:



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
gcd = num1
print(f"The GCD of the two numbers is: {gcd}")


# In[6]:


number = int(input("Enter a number to reverse: "))
reverse = 0
while number > 0:
    remainder = number % 10  
    reverse = reverse * 10 + remainder  
    number //= 10  
print(f"The reversed number is: {reverse}")


# In[8]:


number = int(input("Enter a number to check if it's an Armstrong number: "))
original_number = number
sum_of_powers = 0
num_digits = 0
temp_number = number
while temp_number > 0:
    temp_number //= 10
    num_digits += 1 
temp_number = number
while temp_number > 0:
    digit = temp_number % 10  
    sum_of_powers += digit ** num_digits 
    temp_number //= 10  
if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")


# In[9]:


n = int(input("Enter the value of n: "))
sum_of_numbers = 0
for i in range(1, n + 1):
    sum_of_numbers += i 
average = sum_of_numbers / n
print(f"The average of the first {n} natural numbers is: {average}")


# In[10]:


n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication Table of {n}:")
for i in range(1, 11):  
    result = n * i
    print(f"{n} x {i} = {result}")


# In[11]:


n = int(input("Enter the value of n: "))
sum_of_series = 0.0 
for i in range(1, n + 1):
    sum_of_series += i / (i + 1)  
print(f"The sum of the series up to {n} terms is: {sum_of_series:.4f}")


# In[12]:


n = int(input("Enter the number of rows for the upper half of the pattern: "))
for i in range(1, n + 1): 
    for j in range(i):  
        print("*", end=" ")
    print()  
for i in range(n - 1, 0, -1):  
    for j in range(i):  
        print("*", end=" ")
    print()


# In[ ]:




