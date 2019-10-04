import requests

r = requests.get('https://www.douban.com/')

print(r.status_code)

print(r.text)

# https://www.douban.com/search?q=python&cat=1001

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
