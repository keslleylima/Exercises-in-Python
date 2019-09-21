# Challenge 09
n1 = int(input('type a number\n'))
print('the multiplication table of {} is:'.format(n1))
for i in range(1, 11):
    print(n1, 'x', i, '=', n1 * i)