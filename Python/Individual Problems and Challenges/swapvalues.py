a = 5
b = 9
print ('Before a is {}, b is {}'.format(a, b))

a = (a ^ b)
b = (a ^ b)
a = (a ^ b)

print ('After a is {}, b is {}'.format(a, b))

a=a+b
b=a-b
a=a-b

print ('After a is {}, b is {}'.format(a, b))
