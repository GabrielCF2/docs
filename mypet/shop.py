import yaml
import re

read_path = '/mnt/MOOKER/cumcraft/plugins/MyPet/pet-shops.yml'
write_path = '/mnt/MOOKER/cumcraft/docs/mypet/shop.md'

all_pets = None
baby_pets = None

with open(read_path) as file:
    shop = yaml.load(file, Loader=yaml.FullLoader)
    
    all_pets = shop['Shops']['all']['Pets']
    baby_pets = shop['Shops']['babies']['Pets']

f = open(write_path, 'w')
f.write(f'--- \nicon: \':shopping_trolley:\' \n---\n\n')
f.write(f'# Shop Pets\n\n')
f.write(f'## Pets\n')
f.write(f'Pet | Preço | XP \n')
f.write(f'--- | --- | --- \n')

for s, pet in all_pets.items():
    name = pet['Name']
    price = pet['Price']
    exp = pet['EXP']

    f.write(f'{name} | {price} | {exp}\n')

f.write(f'## Pets Bebê\n')
f.write(f'Pet | Preço | XP \n')
f.write(f'--- | --- | --- \n')

for s, pet in baby_pets.items():
    name = pet['Name']
    price = pet['Price']
    exp = pet['EXP']

    f.write(f'{name} | {price} | {exp}\n')

f.close()