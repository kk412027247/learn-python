import pickle
import json

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)
