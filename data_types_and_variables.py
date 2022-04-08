# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

movies = [
    {'name':'the little mermaid', 'days':3},
    {'name':'brother bear', 'days':5},
    {'name':'hercules', 'days':1}
]

total_price = sum([m['days']*3 for m in movies])
#print(total_price)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and 
# Facebook, they pay you a different rate per hour. Google pays 400 dollars 
# per hour, Amazon 380, and Facebook 350. How much will you receive in payment 
# for this week? You worked 10 hours for Facebook, 6 hours for Google and 
# 4 hours for Amazon.

jobs = [
    {'co':'google', 'pay':400, 'hours':6},
    {'co':'amazon', 'pay':380, 'hours':4},
    {'co':'facebook', 'pay':350, 'hours':10},
]

total_pay = sum([j['hours']*j['pay'] for j in jobs])
print(total_pay)

# A student can be enrolled to a class only if the class is not full and the 
# class schedule does not conflict with her current schedule.
class_full = True #True if the class is full
sched_conflict = False #True if there is a schedule conflict

#can_enroll returns true if the student can enroll
can_enroll = not (class_full and sched_conflict)
#below might be a little easier to understand
can_enroll = not class_full or not sched_conflict
#print(can_enroll)

# A product offer can be applied only if people buy more than 2 items, and the 
# offer has not expired. Premium members do not need to buy a specific amount 
# of products.
items_bought = 3 #number of items bought by a single customer
offer_current = False #True if the offer is expired
premium_member = False

discount_applies = offer_current and (items_bought > 2 or premium_member)
#print(discount_applies)

# Create a variable that holds a boolean value for each of the following conditions:
#
#    the password must be at least 5 characters
#    the username must be no more than 20 characters
#    the password must not be the same as the username
#    bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_length_ok = len(password) >= 5
#print(password_length_ok)
username_length_ok = len(username) <= 20
#print(username_length_ok)
pass_usrname_equal = password != username
#print(pass_usrname_equal)
# easier to do a multistep with the bonus
usrname_whitespace = ' ' in (username[0], username[-1])
password_whitespace = ' ' in (username[0], username[-1])
#no_whitespace is true if there is no whitespace beginning or ending the username or password
no_whitespace = not (usrname_whitespace or password_whitespace)
#print(no_whitespace)
pass_ok = password_length_ok and username_length_ok and pass_usrname_equal and no_whitespace
print(pass_ok)