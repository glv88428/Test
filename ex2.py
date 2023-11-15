import json

with open('catalog.json') as f:
    data = json.load(f)

p=[item['price'] for item in data if item['name'] == 'jacket']

jacket_quantity=len(p)
maxp=max(p)
minp=min(p)

print(f"個数: {jacket_quantity}")
print(f"max: {maxp}")
print(f"min: {minp}")