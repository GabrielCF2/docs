import yaml
import re


read_path = '/mnt/MOOKER/survi_craft/plugins/MyPet/pet-config.yml'
write_path = '/mnt/MOOKER/survi_craft/docs/mypet/pets.md'

pets = None

with open(read_path) as file:
    pets = yaml.load(file, Loader=yaml.FullLoader)
    
    pets = pets['MyPet']['Pets']

f = open(write_path, 'w')
f.write(f'--- \nicon: \':rabbit:\' \n---\n\n')
f.write(f'# Pets Domáveis\n\n')
f.write(f'Pet | HP | Velocidade | Comida | Requerimento\n')
f.write(f'--- | --- | --- | --- | ---\n')

for s, pet in pets.items():
    if 'Food' not in pet:
        continue

    food = pet['Food']

    if pet["LeashRequirements"][0] == 'Impossible':
        continue

    for i, t in enumerate(food):
        t = t.replace('_', ' ').capitalize()
        # t = translator.translate(t, dest='pt')
        food[i] = t

    food = ', '.join(food)

    requirement = {
        "LowHp": 'Low HP',
        "UserCreated": 'User Created',
        'Tamed':'Tamed'
    }[pet["LeashRequirements"][0]]

    name = re.sub( r"([A-Z])", r" \1", s).split()
    name = ' '.join(name)

    f.write(f'{name} | {pet["HP"]} | {pet["Speed"]} | {food} | {requirement} \n')

f.close()