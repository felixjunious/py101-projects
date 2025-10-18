import uuid

items = [
    ['laptop', 1200],
    ['mouse', 20],
    ['keyboard', 30],
    ['tablet', 200]
]

item_data = {}

for item in items:
    item_id = uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key = item_id.hex[:6]
    item_data[key] = item

for k,v in item_data.items():
    print(f'{k}: {v}')