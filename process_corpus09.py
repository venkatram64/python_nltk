
mystr = 'NLTK Dolly Python'
print('Substring ends at: ', mystr[:4])

print('Substring starts from: ', mystr[11:])

print('Substring: ', mystr[5:10])

print('Substring fancy: ', mystr[-12:-7])

if 'NLTK' in mystr:
    print('found NLTK')

replaced = mystr.replace('Dolly', 'Dorothy')
print('Replaced String: ', replaced)

print('Accessing each character: ')
for s in replaced:
    print(s)














