# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.


def hello_name(user_name):
    print("hello_" + user_name.upper() + "!" )

hello_name("username")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds(num):
    for i in range(1,101,2):
        print(i, end=",")
    else:
        pass

num = 0
first_odds(num)



# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined
# as below.

list_1 = [23, 7, 345, 906, 45]

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list(list_1))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    return a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 == 0

year = 1999
print(is_leap_year(year))





# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

List = [3,4,5,6]
print(is_consecutive(List))
