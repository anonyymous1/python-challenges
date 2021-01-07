# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calc():
    math_term = input('What calculation would you like to do? add, sub, mult, div ')
    print(math_term)
    num1 = int(input('What is number 1? '))
    print(num1)
    num2 = int(input('What is number 2? '))
    print(num2)
    print('So, '+ math_term+'ing ' + str(num1) + ' and ' + str(num2) + ' is:')
    if math_term == "div":
        print(num1 / num2)
    elif math_term == "add":
        print(num1 + num2)
    elif math_term == "sub":
        print(num1 - num2)
    elif math_term == "mult":
        print(num1 * num2)
    else:
        print('I cant ' + math_term + ' ' + str(num1) + ' and ' + str(num2))
    
calc()