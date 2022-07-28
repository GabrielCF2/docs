import yaml

def int_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


read_path = '/mnt/MOOKER/cumcraft/plugins/Foodeffect/config.yml'
write_path = '/mnt/MOOKER/cumcraft/docs/food/index.md'
texture_link = 'https://devbaraus.ddns.net/download/VanillaDefault+1.19/assets/minecraft/textures/item'

f = open(write_path, 'w')
f.write(f'--- \nicon: \':apple:\' \n---\n\n')
f.write(f'# Comidas\n\n')
f.write(f'Comida | Efeito | Duração (s) | Chance (%)\n')
f.write(f'--- | --- | --- | ---\n')


with open(read_path) as file:
    food = yaml.load(file, Loader=yaml.FullLoader)
    food = food['food']
    
    for s, food_effect in food.items():
        name = s.replace('_', ' ').title()
        amplifier = int_roman(food_effect['amplifier']+1)
        effects = ", ".join([i.replace('_', ' ').title() + ' ' + amplifier  for i in food_effect["effect"]])
        chance = food_effect['chance']
        duration = food_effect['duration'] // 20
        icon_name = s.replace('raw_', '') if s != 'steak' else 'cooked_beef'
        if chance == 0:
            continue

        f.write(f'![]({texture_link}/{icon_name}.png) {name} | {effects} | {duration} | {chance} \n')

f.write(f'\n\n')