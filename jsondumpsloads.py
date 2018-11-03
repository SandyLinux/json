import json

data = {
            'name' : 'ACME',
                'shares' : 100,
                    'price' : 542.23
                    }

json_str = json.dumps(data)
print(json_str, 'type is :', type(json_str))

data1= json.loads(json_str)

print(data1, 'type is :', type(data1))
print(data, 'type is :', type(data))
