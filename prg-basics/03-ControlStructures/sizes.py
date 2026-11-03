size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print("M: Medium size")
elif size == 'L':
    print("L: Large size")
elif size == 'XL':
    print("XL: Extra Large size")
else:
   raise ValueError('Invalid size symbol')
