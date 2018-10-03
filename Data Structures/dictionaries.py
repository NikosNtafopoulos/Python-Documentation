'''Examples 2.x '''
# dictionary with  string  number  list as values
clientInfo = {'name': 'George', 'age': 30,
              'orders': ['laptop', 'tablet', 'smartphone']}

# accessing values
print clientInfo['orders']

# a better way
print clientInfo.get('orders')

# adding a new entry
clientInfo['phone'] = '32832822'
print clientInfo

# multiple entries
clientInfo.update({'job': 'technician', 'status': 'married', 'id': 1})
print clientInfo

# delete
delete = clientInfo.pop('status')
print clientInfo

# proper looping a dictionary
for key, value in clientInfo.items():
    print key, value
