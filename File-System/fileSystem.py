# read and write

f = open('test.txt', 'r')
print f.name
print f.mode
f.close()

# or with context manager
# printing on our terminal exactly what the file hav
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print f_contents

# for larger files
with open('test.txt', 'r') as f:
    size_to_read = 100
    #f_contents = f.readlines()
    f_contents = f.read(size_to_read)
    print(f_contents, enumerate)
