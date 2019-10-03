import re

s = 'ABC\\-001'
s = r'ABC\-001'

print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))

print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

print(re.split(r'[\s,;]+', 'a,b;; , c  d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(1), m.group(2))

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_telephone.match('010-12345').groups())


def is_valid_email(addr):
    return re.match(r'^\w[\w.]+@[^@]+$', addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
