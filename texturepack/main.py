import yaml
import configparser
config = configparser.ConfigParser()
import os

import re

def read_properties(path):
    with open(path, "r") as file:
        data = file.read()
        # parsed_data = data.split('=')
        parsed_data = re.split('(?<=[^\\\\])\n', data)
        data_dict = {}
        for element in parsed_data:
            split = element.split('=')
            data_dict[split[0]] = split[1].split('\\\n')
        
        return data_dict

path_read = '/mnt/MOOKER/cumcraft/nginx/static/compcraft/assets/minecraft/optifine/cit/armorsets'
path_write = '/mnt/MOOKER/cumcraft/docs/texturepack'
texture_path = 'https://devbaraus.ddns.net/download/compcraft/assets/minecraft/optifine/cit/armorsets'

dirnames = next(os.walk(path_read))[1]  # [] if no file


f = open(f'{path_write}/index.md', 'w')
f.write("""--- 
icon: ':bricks:' 
expanded: false
---

# Texture Pack

O servidor contém um textura personalizada chamada **BetterVanillaBuild**, com ela há mudança estéticas de alguns items, principalmente de armaduras e ferramentas.

Para mudar a estética do seu item é necessário que você altere o nome dele usando uma bigorna. Os nomes estão nas seções dos respectivos grupos de items.

!!!warning Optifine
É necessário o uso de mods como optifine ou equivalentes, para as texturas personalizadas funcionarem.
!!!\n\n""")


for dname in dirnames:
    # f.write(f'---\nicon:\'\'\n---\n')
    kit_name = dname.replace('_', ' ').title()
    f.write(f'## {kit_name}\n')

    f.write('Textura | Nome | Itens \n')
    f.write('--- | --- | ---\n')

    filenames = next(os.walk(f'{path_read}/{dname}'), (None, None, []))[2]  # [] if no file

    for fname in filenames:
        fname_str, fname_ext = os.path.splitext(fname)

        if f'{fname_str}_item{fname_ext}' in filenames:
            continue 

        if fname_ext == '.properties':
            f_dict = read_properties(f'{path_read}/{dname}/{fname}')
            
            texture = f_dict['texture'][0] if 'texture' in f_dict else None
            texture_img = f'{texture_path}/{dname}/{texture}' if texture else None
            texture_tag = f'<img src="{texture_img}" width="32"/>' if texture_img else '3D'
            display_name = ', '.join([i.replace('ipattern:','').replace('iregex:','').replace('(', '').replace('|', ', ').replace(')', '').title() for i in f_dict['nbt.display.Name']])
            items = ', '.join([i.replace('_', ' ') for i in ' '.join(f_dict['items']).split(' ')])
            f.write(f'{texture_tag} | {display_name} | {items}\n') 

    f.write('\n\n')
f.close()