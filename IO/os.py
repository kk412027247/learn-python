import os

print(os.name)

print(os.uname())

print(os.environ.get('PATH'))

print(os.path.abspath('.'))

print(os.path.join('/Users/tmd/Desktop/learn-python/IO', 'testdir'))

os.mkdir('/Users/tmd/Desktop/learn-python/IO/testdir')

os.rmkdir('/Users/tmd/Desktop/learn-python/IO/testdir')
