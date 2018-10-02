# python 3
'''
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    f.seek(0)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents)
    '''
# with open('test2.txt', 'w') as f:
# pass
# f.write('Test')
# f.write('Test2')
with open('test.txt', 'r') as rf:
    with open('testCopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# copy an image inside our project folder
with open('poster_one.jpg', 'rb') as rf:
    with open('../File-System/posterone_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


# outside of our folder

with open('poster_one.jpg', 'rb') as rf:
    with open('../posterone_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
