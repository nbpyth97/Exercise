address = '1.1.1.1'
output = ''
a = 0

for i in range(len(address)):
    if address[a] == '1':
        output = output + address[a]
    elif address[a] == '.':
        output = output + '[.]'
    a += 1
print(output)
