import yaml

car_dict = {'Car name': ('ЛАДА', 'Volkswagen', 'AUDI', 'Toyota'),
            'quantity car': 4,
            'Car price': {
                          'ЛАДА': '1.200.000₽-1.800.000₽',
                          'Volkswagen': '50.000€-120.000€',
                          'AUDI': '80.000€-160.000€',
                          'Toyota': '480.000¥-1.900.000¥'
                          }
            }
with open('file.yaml', 'w', encoding='utf8') as f:
    f.write(yaml.safe_dump(car_dict, sort_keys=False, allow_unicode=True))
with open('file.yaml', encoding='utf8') as g:
    print(yaml.safe_load(g))

