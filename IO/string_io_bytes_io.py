from io import StringIO, BytesIO

f = StringIO()

print(f.write('hello'))

print(f.write(' '))

print(f.write('sucker'))

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())
