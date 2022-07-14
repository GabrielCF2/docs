import yaml
import os
import re

read_path = '/mnt/MOOKER/survi_craft/plugins/EcoEnchants/enchants'
write_path = '/mnt/MOOKER/survi_craft/docs/ecoenchants'

tools = []
enchants = []
rarity = []

dirnames = next(os.walk(read_path))[1]  # [] if no file

for d in dirnames:
    filenames = next(os.walk(f'{read_path}/{d}'), (None, None, []))[2]

    for f in filenames:
        with open(f'{read_path}/{d}/{f}') as file:
            enchant = yaml.load(file, Loader=yaml.FullLoader)
            
            obtaining = enchant['obtaining']
            general_config = enchant['general-config']
            
            way_obtain = [key for key, value in obtaining.items() if value == True]

            description = enchant['description']
            description = re.sub('&[a-zA-Z0-9]', '', description)

            description = description.replace('%value%', '').replace('%', '').strip().capitalize()
            

            max_level = general_config['maximum-level'] if 'maximum-level' in general_config else 1

            targets = general_config['targets']

            for t in targets:
                if t not in tools:
                    tools.append(t)

            if obtaining['rarity'] not in rarity:
                rarity.append(obtaining['rarity'])

            dict_enchant = {
                'name': enchant['name'],
                'description': description,
                'obtaining': way_obtain,
                'targets': targets,
                'type': obtaining['rarity'],
                'max_level': max_level
            }

            enchants.append(dict_enchant)

tools.remove('all')

w = open(f'{write_path}/index.md', 'w')
w.write('---\nicon: ":book:"\n---\n')
w.write('# Eco Enchants\n\n')
w.write('## Sinopse\n\n')
w.write('EcoEnchants adiciona mais de 200 encantamentos personalizados ao servidor. Ele se integra totalmente ao vanilla para fornecer uma experiência perfeita e intuitiva aos jogadores. Ele suporta a Mesa Encantadora, Comércio de Aldeões, Bigornas, Pedras de Rebolo e até mesmo desova natural em todo o mundo em estruturas como End Cities.\n\n')

w.write('Name | Description | Type | Items | Max Level\n')
w.write('--- | --- | --- | --- | ---\n')

for e in enchants:
    targets = ', '.join([tar.capitalize() for tar in e['targets']])
    w.write(f"{e['name']} | {e['description']} | {e['type'].capitalize()} | {targets if targets != 'All' else 'Everything'} | {e['max_level']}\n")

w.close()

for t in tools:
    e_t = list(filter(lambda e: t in e['targets'] ,enchants))

    e_r = {}

    w = open(f'{write_path}/{t}.md', 'w')
    w.write(f'# {t.capitalize()}\n')

    for r in rarity:
        e_r[r] = list(filter(lambda e: r in e['type'], e_t))

    for r, ench in e_r.items():
        if len(ench) == 0:
            continue 

        w.write(f'## {r.capitalize()}\n')

        w.write('Name | Description | Type | Obtaining | Max Level\n')
        w.write('--- | --- | --- | --- | ---\n')

        for e in ench:
            obtaining = ', '.join([tar.capitalize() for tar in e['obtaining']])
            w.write(f"{e['name']} | {e['description']} | {e['type'].capitalize()} | {obtaining} | {e['max_level']}\n")
        
    w.close()


# pets = None

# with open(read_path) as file:
#     pets = yaml.load(file, Loader=yaml.FullLoader)
    
#     pets = pets['MyPet']['Pets']

