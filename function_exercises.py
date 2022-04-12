#1
def is_two(n):
    #check via the equality operator
    return n == 2 or n == '2'
#be able to handle non numeric strings
#print(is_two('2'))
#print(is_two(2))
#print(is_two('5'))
#print(is_two(5))

#2
def is_vowel(char):
    #check via list inclusion
    return char.lower() in ('a', 'e', 'i', 'o', 'u')

#print(is_vowel('B'))

#3.
def is_consonant(char):
    #should not be a vowel, and also it should be alphabetic
    return char not in ('a', 'e', 'i', 'o', 'u') and char.isalpha()

#print(is_consonant('5'))

#4.
def title_if_cons(chars):
    #check if the first letter is a consonant
    if chars[0] not in ('a', 'e', 'i', 'o', 'u') and chars.isalpha():
        #return the string in title case
        return chars.title()
    else:
        return chars

#print(title_if_cons("robert"))

#if I can use above functions.
def title_if_cons_alt(chars):
    if is_consonant(chars[0]):
        return chars.title()
    else:
        return chars

#if the string has multiple words seperated by spaces
def title_if_cons_alt_2(chars):
    words = chars.split()
    return_list = []
    for w in words:
        if is_consonant(w[0]):
            return_list.append(w.title())
        else:
            return_list.append(w)
    return ' '.join(return_list)

#print(title_if_cons_alt_2('robert obert'))

#5.
def calculate_tip(tip, bill):
    #make sure that the tip is in correct range
    if tip >= 0 and tip <= 1:
        return bill*tip
    else:
        return "invalid tip"

#6.
def apply_discount(price, discount):
    #subtract the discount from the price
    return price - price*discount

#7.
def handle_commas(num_string):
    #make a list of all chars that are not commas
    #join this list into a string and cast to float type
    return float(''.join([c for c in num_string if c != ',']))

#this is a better way
def handle_commas_alt(num_string):
    return float(num_string.replace(',', ''))

#print(handle_commas_alt('1,00,,,,,,,,,0'))

#8.
def get_letter_grade(grade):
    #make a switch to return the proper grade
    if grade > 89 and grade <=100:
        return 'A'
    elif grade > 79 and grade <= 89:
        return 'B'
    elif grade > 69 and grade <= 79:
        return 'C'
    elif grade > 59 and grade <= 69:
        return 'D'
    else:
        return 'F'

#9.
def remove_vowels(word):
    #make a list of all chars that are not vowels
    #join the list into a string
    return ''.join([c for c in word if c.lower() not in ('a', 'e', 'i', 'o', 'u')])

#print(remove_vowels('SPONGEBOB'))

#10
def normalize_name(word):
    #make a list of all chars that are permitted and join into a string
    word = ''.join([c for c in word if c not in ('@', '$', '%')])
    #strip whitespace, lower case all remaining chars, and then repleace spaces with underscores
    word = word.strip().lower().replace(' ', '_')
    return word

#print(normalize_name('    @franky  $rios   '))

#11
def cumulative_sum(num_list):
    #make a list
    #each item in the list is a partial sum of the list
    return [sum(num_list[:n]) for n in range(1,len(num_list)+1)]

#Bonus 1
def twelveto24(time_string):
    #take a time string in 12 hour time and return military time
    #split up the time string into three
    colon_index = time_string.index(":")
    time_list_split = [int(time_string[:colon_index]), time_string[colon_index+1:colon_index+3], time_string[colon_index+3:]]
    #check if the time is pm
    if time_list_split[2]=='pm':
        #since the time is pm add 12 hours
        time_list_split[0] = (time_list_split[0]+12)
    else:
        time_list_split[0] = time_list_split[0]%12
    #use join to seperate the hours and minute
    #use map to cast the ints to str
    return ':'.join(map(str, time_list_split[:2]))

#print(twelveto24("10:25pm"))
#print(twelveto24("12:50am"))

#Bonus 1 part ii
def twentyfourto12(time_string):
    #return 12hr time from 24hr time
    #split the string into a list
    colon_index = time_string.index(":")
    time_list_split = [int(time_string[:colon_index]), time_string[colon_index+1:]]
    #check for am/pm
    if time_list_split[0] <= 12:
        #time is in the morning, append am
        time_list_split.append("am")
        if time_list_split[0]==0:
            #0:mm is 12:mm
            time_list_split[0] = 12
    else:
        #time is pm, subtract 12 and append pm
        time_list_split[0] -= 12
        time_list_split.append("pm")
    #return as a string
    return f"{time_list_split[0]}:{time_list_split[1]}{time_list_split[2]}"

#print(twentyfourto12("23:55"))
#print(twentyfourto12("0:50"))

#Bonus 2 this does not work
def col_index(cols_string):
    #returns the index of the columns from a excel spreadsheet
    #use ASCII values of the letters
    cols_string = list(cols_string)
    #cols_string.reverse()
    sum = 0
    for i, letter in enumerate(cols_string):
        #print(f"{i}, {letter}, {ord(letter)-64}")
        if i==0:
            sum += ord(letter)-64
        else:
            sum += 26**(i) + ord(letter[0])-64
    return sum

    

alphabet_list = [chr(c+65) for c in range(26)]
#list to check
combos_2 = alphabet_list + [c+d for c in alphabet_list for d in alphabet_list]
combos_3 = combos_2 + [c+d+e for c in alphabet_list for d in alphabet_list for e in alphabet_list]
list_checking = combos_2
correct = [x for x in range(1,len(list_checking)+1)]
output = [col_index(c) for c in list_checking]
for o in output:
    print(o)