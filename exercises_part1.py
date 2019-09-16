# Order of Operations is (), **, then * or / or // and + i
nome = 'keslley lima da silva'
# input 50 spaces in the right before the name
print('Nice to meet  {:>50}'.format(nome))
# center the name in 50 spaces
print('Nice to meet {:^50} you are awesome!'.format(nome))
# input the name betwen 50 =
print('Nice to meet  {:=^50}'.format(nome))

# Challenge 05
n1 = int(input('type a number\n'))
print('the predecessor ', n1 - 1)
print('the successor: ', n1 + 1)

# Challenge 06
n1 = int(input('type a number\n'))
print('{} * 2 is: {} '.format(n1, n1 * 2))
print('{} * 3 is: {} '.format(n1, n1 * 3))
print('square root of {} is {}'.format(n1, n1 ** (1 / 2)))

# Challenge 07
n1 = int(input('type a number\n'))
n2 = int(input('type other\n'))
print('the average is', (n1 + n2) / 2)

# Challenge 08
n1 = int(input('type a number in meters\n'))
print('{} m is {} cm'.format(n1, n1 / 100))
print('{} m is {} mm'.format(n1, n1 / 1000))

# Challenge 09
n1 = int(input('type a number\n'))
print('the multiplication table of {} is:'.format(n1))
for i in range(1, 11):
    print(n1, 'x', i, '=', n1 * i)

# Challenge 10
n1 = float(input('how much money you got?\n'))
dolar = float(3.27)
print('you got {} dollars'.format(n1 / dolar))

# Challenge 11
length = float(input('type a length?\n'))
width = float(input('type a width\n'))
print('the calculated area is ', length * width)
print('it is necessary {} l to paint the wall'.format(length * width / 2))

# Challenge 12
n1 = float(input('what the product price?\n'))
print('the price with discount of 5% is', n1*0.95)

# Challenge 13
n1 = float(input('what is your salary?\n'))
print('your new salary with an increase of 15% is', n1*1.15)