
flavor = input('Pass flavor here: ')
if flavor == 'Standard':
    str2 = None
else:
    str2 = flavor

str1 = 'Alice'

str3 = 'Carl'

result = '_'.join(filter(None, [str1,str2,str3]))
print(result)