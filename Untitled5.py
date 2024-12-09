#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))


if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
 
    print(f"The factorial of {number} is {factorial(number)}")



# In[3]:


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci(n)


# In[4]:


def sum_of_list(lst):
    return sum(lst)

lst = [1, 2, 9, 4, 5]
print(sum_of_list(lst))


# In[5]:



import math

def even(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

def numb(start, end):
    result = []
    for num in range(start, end + 1):
        if even(num) and int(math.sqrt(num)) ** 2 == num:
            result.append(num)
    return result

start = 1000
end = 9999
print(numb(start, end))


# In[6]:


N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(i * j, end=" ")
    print()


# In[7]:


string = input()

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"'{char}': {count}")


# In[8]:


string = input()

if string.endswith('ing'):
    string += 'ly'
else:
    string += 'ing'

print(string)


# In[9]:



words = input().split()

longword = max(words, key=len)

print(len(longword))


# In[10]:



number = 35

factors = [i for i in range(1, number + 1) if number % i == 0]

print(factors)


# In[11]:



area_square = lambda side: side * side

area_rectangle = lambda length, width: length * width


area_triangle = lambda base, height: 0.5 * base * height
side= int(input("enter side"))
length=int(input("enter the length"))
width=int(input("enter the width"))
base=int(input("enter the base"))
height=int(input("enter the height"))
print(area_square(side))          
print(area_rectangle(length,width))   
print(area_triangle(base,height ))     


# In[ ]:




