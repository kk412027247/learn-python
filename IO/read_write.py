with open('./test.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())

f = open('./test.txt', 'rb')
print(f.read())

# f = open('./test.txt', 'w')
# f.write('Hello, sucker')
# f.close()

with open('./test.txt', 'w') as f:
    f.write('Hello, sucker')
