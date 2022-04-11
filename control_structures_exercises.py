# 1.
## a.

def is_monday(day):
    if day.lower()=='monday':
        return "You entered Monday"
    else:
        return "You did not enter Monday"

user_in = input("1a. Enter a day of the week: ")
print(is_monday(user_in))

#b.
def is_weekday(day):
    if day.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
        return "That is a weekday"
    elif day.lower() in ('saturday', 'sunday'):
        return "That is in the weekend"
    else:
        return "That is not a day"

user_in = input("1b. enter a day of the week: ")
print(is_weekday(user_in))

#c.
def paycheck_calculator(hours, wage):
    if hours>40:
        return 40*wage+(hours-40)*wage*(1.5)
    else:
        return wage*hours

print(paycheck_calculator(42.5, 2))

#2.
#a.
i = 5
while i<= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i+=2

i=100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <1000000:
    print(i)
    i = i**2

i = 100
while i>0:
    print(i)
    i -= 5

#2
#b.
def multiplication_tabl(n):
    prnt_str = ""
    for x in range(11):
        prod = n*x
        prnt_str += f"{n} x {x} = {prod}\n"
    print(prnt_str)

def get_input_2b():
    while True:
        user_in = input("2b. Choose a multiplication table: ")
        if user_in.isnumeric():
            multiplication_tabl(int(user_in))
            break
        else:
            print("Invalid input. Please enter a number.")

get_input_2b()

for x in range(10):
    print(str(x)*x)


#2.
#c.
def skipper(n):
    print_msg = f"\nNumber to skip: {n}\n\n"
    for x in range(1,50,2):
        if x!=n:
            print_msg += f"Here is an odd number: {x}\n"
        else:
            print_msg += f"Yikes! Skipping number: {n}\n"
            # not sure where a continue should go?
            # this will not do anything since it's at the end of the loop
            continue
    print(print_msg)

def get_input_2c():
    while True:
        user_in = input("2c. Enter an odd number between 1 and 50: ")
        if user_in.isnumeric() and bool(int(user_in)%2) and int(user_in) <= 50 and int(user_in) >= 1:
            skipper(int(user_in))
            break
        else:
            print("Invalid input.")

get_input_2c()

#d.
def counter(n):
    for x in range(n+1):
        print(x)

def get_input_2d():
    while True:
        user_in = input("2d. Enter a positive number ")
        if user_in.isnumeric() and int(user_in) > 0:
            counter(int(user_in))
            break
        else:
            print("Invalid input.")

get_input_2d()

#e.
def countdown(n):
    for x in range(n,0,-1):
        print(x)

def get_input_2e():
    while True:
        user_in = input("2e. Enter a positive number ")
        if user_in.isnumeric() and int(user_in) > 0:
            countdown(int(user_in))
            break
        else:
            print("Invalid input.")

get_input_2e()

#3
#fizzbuzz
def fizzbuzz():
    print_msg = ""
    for x in range(1,101):
        if not(x%3 or x%5):
            print_msg += "fizzbuzz\n"
        elif not(x%3):
            print_msg += "fizz\n"
        elif not(x%5):
            print_msg += "buzz\n"
        else:
            print_msg += f"{x}\n"
    print(print_msg)

fizzbuzz()

#4
def square_and_cube(n):
    if len(str(n**3))+1 > 8:
        max_length = len(str(n**3))+1
    else:
        max_length = 9
    print_msg = "\nHere is your table!\n\n"
    print_msg += f"{'number '.ljust(max_length)}|{' squared '.ljust(max_length)}|{' cubed '.ljust(max_length)}\n"
    print_msg += ''.ljust(max_length,'-') + '|' +''.ljust(max_length,'-') + '|' +''.ljust(max_length,'-') +'\n'
    for x in range(1,n):
        print_msg += f"{str(x).ljust(max_length)}|{str(x**2).ljust(max_length)}|{str(x**3).ljust(max_length)}\n"
    print(print_msg)

def get_input_4():
    while True:
        user_in = input("4. What number would you like to go up to? ")
        if user_in.isnumeric() and int(user_in) > 0:
            square_and_cube(int(user_in)+1)
            user_in = input("Type n to stop, any key to continue: ")
            if user_in.lower()=='n':
                break
        else:
            print("Invalid input.")

get_input_4()

#5.
def grader(n):
    if n in range(0, 60):
        print('Your grade is a F')
    elif n in range(60, 67):
        print('Your grade is a D')
    elif n in range(67, 80):
        print('Your grade is a C')
    elif n in range(80, 87):
        print('Your grade is a B')
    elif n in range(87, 101):
        print('Your grade is a A')

def get_input_5():
    while True:
        user_in = input("5. Enter a valid grade (1-100): ")
        if user_in.isnumeric() and int(user_in) <=100:
            grader(int(user_in))
            user_in = input("Type n to stop, any key to continue: ")
            if user_in.lower()=='n':
                break
        else:
            print("Invalid input.")

get_input_5()

#6
#make the dictionary
books = [
    {'title':'aurora',
    'author':'kim stanley robinson',
    'genre': 'science fiction'},
    {'title':'the book of three',
    'author':'lloyd alexander',
    'genre': 'fantasy'},
    {'title':'complete poems',
    'author':'emily dickinson',
    'genre': 'poetry'},
    {'title':'2001: a space odyssey',
    'author':'arthur c. clark',
    'genre': 'science fiction'},
    {'title':'watership down',
    'author':'richard adams',
    'genre': 'fantasy'},
    {'title':'orlando',
    'author':'virginia woolf',
    'genre': 'fiction'},
    {'title':'paradise lost',
    'author':'john miltion',
    'genre': 'poetry'},
    {'title':'the killing moon',
    'author':'nora keita jemison',
    'genre': 'fantasy'},
    {'title':'under the glacier',
    'author':'halldor laxness',
    'genre': 'fiction'},
    {'title':'terra nostra',
    'author':'carlos fuentes',
    'genre':'fiction'}
]

def book_loop(b_dictionary):
    max_length = 24 #arbitrarily chosen max length
    print_msg = ""
    print_msg += f"{'Title '.ljust(max_length)}|{' Author '.ljust(max_length+1)}|{' Genre '.ljust(max_length)}\n"
    print_msg += ''.ljust(max_length,'-') + '|' +''.ljust(max_length+1,'-') + '|' +''.ljust(max_length,'-') +'\n'
    for b in b_dictionary:
        print_msg += f"{b['title'].title().ljust(max_length)}| {b['author'].title().ljust(max_length)}| {b['genre'].ljust(max_length)}\n"
    print(print_msg)

book_loop(books)

def print_by_genre(b_dictionary, genre):
    books_in_genre = [b for b in b_dictionary if b['genre']==genre]
    max_length = 24 #arbitrarily chosen max length
    print_msg = "\n"
    print_msg += f"{'Title '.ljust(max_length)}|{' Author '.ljust(max_length)}|{' Genre '.ljust(max_length)}\n"
    print_msg += ''.ljust(max_length,'-') + '|' +''.ljust(max_length,'-') + '|' +''.ljust(max_length,'-') +'\n'
    for b in books_in_genre:
        print_msg += f"{b['title'].title().ljust(max_length)}| {b['author'].title().ljust(max_length)}| {b['genre'].ljust(max_length)}\n"
    print(print_msg)


def get_input_6(b_dictionary):
    valid_genre = set([b['genre'] for b in b_dictionary])
    while True:
        print(f"6. Valid genres are: {valid_genre}")
        user_in = input("Enter a valid genre: ")
        if user_in in valid_genre:
            print_by_genre(b_dictionary, user_in)
            user_in = input("Type n to stop, any key to continue: ")
            if user_in.lower()=='n':
                break
        else:
            print("Invalid input.")

get_input_6(books)