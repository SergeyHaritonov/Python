# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]      # После каждого добавления в список, длина списка увеличивается
# def create_phone_number(arr):
#     num1 = '('
#     arr.insert(0, num1)
#     num2 = ')'
#     arr.insert(4, num2)
#     num3 = ' '
#     arr.insert(5, num3)
#     num4 = '-'
#     arr.insert(9, num4)

#     s = ''.join(str(x) for x in arr)
    
#     return s
# print(create_phone_number(array))



# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# print(create_phone_number(array))




def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
print(create_phone_number(array))


