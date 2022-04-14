#1.

#a.
#output from repl
#>>> function_exercises.is_vowel('e')
#True
#>>> function_exercises.is_vowel('d')
#False

#b.
from function_exercises import calculate_tip 

print(f"1b. Calculated tip: {calculate_tip(0.15,45.35)}")

#2.
import itertools as i_t

#a.
product_letters = [p for p in i_t.product(['a', 'b', 'c'], [1,2,3])]
print(product_letters)
print(f"2a. {len(product_letters)} members of [a,b,c] x [1,2,4]") #9; what we would expect from the multiplication rule

#b.
combination_letters = [c for c in i_t.combinations(['a', 'b', 'c', 'd'], 2)]
combination_list = list(i_t.combinations(['a', 'b', 'c', 'd'], 2))
#print(combination_list)
print(combination_letters)
print(f"2b. {len(combination_letters)} total combinations on the set abcd") #6 because (4!)/(2!*(4-2)!)

#c.
permutation_letters = [p for p in i_t.permutations(['a', 'b', 'c', 'd'], 2)]
print(permutation_letters)
print(f"2c. {len(permutation_letters)} total permutations on the set abcd") #12 because 4*3

#3.
import json

#store new dictionary in a variable
# This seems better than just having a file open?
with open('profiles.json') as f:
    profiles = json.load(f)

#num of users
print(f"3a. {len(profiles)} total profiles")

#num of active users
active_users = [p for p in profiles if p['isActive']==True]
print(f"3b. {len(active_users)} total active users")

#num of inactive users
inactive_users = [p for p in profiles if p['isActive']==False]
print(f"3c. {len(inactive_users)} total inactive users")

#total balance of all users
#the balances are a string like $2,000.56 so need to edit them to get a float
#can use the functions from function_exercises
from function_exercises import handle_commas, normalize_name
#normalize name to get rid of $ and handle commas to get rid of the comma
#then cast to float
#balances = [float(handle_commas(normalize_name(p['balance']))) for p in profiles]
#another way to get the balance as a float without calling the functions
#get the balances and remove dollar sign
balances = [p['balance'].replace('$', '') for p in profiles]
#remove the commas and cast to float
balances = [float(b.replace(',', '')) for b in balances]
print(f"3d. ${sum(balances)} total balance for all users")

#average balance for users
avg_balance = sum(balances)/len(balances)
print(f"3e. ${avg_balance} is the average balance of all users")

#lowest balance user
min_balance = min(balances)
min_balance_index = balances.index(min_balance)
get_profile = [p['name'] for p in profiles if p['index']==min_balance_index]
print(f"3f. {''.join(get_profile)} has the lowest balance at {min_balance}.")

#max balance
max_balance = max(balances)
max_balance_index = balances.index(max_balance)
get_profile = [p['name'] for p in profiles if p['index']==max_balance_index]
print(f"3g. {''.join(get_profile)} has the lowest balance at {max_balance}.")

#most common favorite fruit
fruit_selections = [p['favoriteFruit'] for p in profiles]
fruit_types = set([p['favoriteFruit'] for p in profiles])
fruit_totals = [fruit_selections.count(t) for t in fruit_types]
max_fruit = max(fruit_totals)
max_fruit_index = fruit_totals.index(max_fruit)
print(f"3h. {list(fruit_types)[max_fruit_index].title()} is the most popular fruit")

#least common fruit preference
min_fruit = min(fruit_totals)
min_fruit_index = fruit_totals.index(min_fruit)
print(f"3i. {list(fruit_types)[min_fruit_index].title()} is the most popular fruit")

#total unread messages
#extract all the unread messages info
greetings = [p['greeting'] for p in profiles]
#the strings have only the digits of the unread messages, everything else is chars
#can use isnumeric()
extract_num = []
for g in greetings:
    num = ""
    for c in g:
        #add the char if it is numeric
        if c.isnumeric():
            num += c
    extract_num.append(num)
#make all the strings extract into ints and cast map obj to a list obj
extract_num = list(map(int,extract_num))
#sum the numbers
message_sum = sum(extract_num)
print(f"3j. There are {message_sum} unread messages")