import json
with open('./data/data.json') as json_file:
    data = json.load(json_file)

user = 10021
i = 0
lim = len(data['conta'])
for i in range(0,lim):
    if user == data['conta'][i]['id']:
        print('hello')
    else:
        print('f*ck')
