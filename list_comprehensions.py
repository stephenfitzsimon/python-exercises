# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [f.upper() for f in fruits]
#print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension 
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [f.title() for f in fruits]
#print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
#  Hint: You'll need a way to check if something is a vowel.
# get_vowels = [c for c in fruit if c in ('a', 'e', 'i', 'o', 'u')]
fruits_with_more_than_two_vowels = [f for f in fruits if len([c for c in f if c in ('a', 'e', 'i', 'o', 'u')])>2]
#print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [f for f in fruits if len([c for c in f if c in ('a', 'e', 'i', 'o', 'u')])==2]
#print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_five_chars = [f for f in fruits if len(f) > 5]
#print(more_than_five_chars)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
five_chars = [f for f in fruits if len(f) == 5]
#print(five_chars)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_than_five_chars = [f for f in fruits if len(f) < 5]
#print(less_than_five_chars)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
length_of_fruits = [len(f) for f in fruits]
#print(length_of_fruits)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [f for f in fruits if len([c for c in f if c == 'a'])>0]
#print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [n for n in numbers if  not (n%2)]
#print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [n for n in numbers if (n%2)]
#print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [n for n in numbers if n>0]
#print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n<0]
#print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
more_than_two_digits = [n for n in numbers if len(str((-1)*n))>=2]
#print(more_than_two_digits)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list 
# with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n**2 for n in numbers]
#print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n%2 and n<0]
#print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n+5 for n in numbers]
#print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime(n):
    #returns true if n is prime
    if n<=1:
        return False
    else:
        for i in range(2, int(n**(0.5))+1):
            if n%i==0:
                return False
        return True
primes_list = [n for n in numbers if is_prime(n)]
#print(primes_list)