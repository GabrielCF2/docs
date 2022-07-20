import yaml
from os import walk

path_read = '/mnt/MOOKER/cumcraft/plugins/Jobs/jobs'

filenames = next(walk(path_read), (None, None, []))[2]  # [] if no file

mapps = {
    "brewer.yml": ['Brew'],
    "builder.yml": ['Place', 'Kill'],
    "crafter.yml": ['Craft','Smelt'],
    "digger.yml": ['Break'],
    "enchanter.yml": ['Enchant'],
    "explorer.yml": ['Explore'],
    "farmer.yml": ['Tame','Breed','Shear','Milk','Break','Place'],
    "fisherman.yml": ['Fish'],
    "hunter.yml": ['Tame', 'Kill'],
    "miner.yml": ['TNTBreak','Break','Place'],
    "woodcutter.yml": ['Break', 'Kill'],
    "weaponsmith.yml": ['Craft','Repair','Smelt'],
}

factor = 0.25

w = open('./jobs.md', 'w')

w.write('---\nicon: \':hammer_and_pick:\'\n---\n')
w.write('# Jobs\n')
w.write('Jobs são formas de ganhar dinheiro realizando alguma tarefa\n\n')

w.write('## Jobs disponíveis \n')
w.write('Abaixo são alguns dos trabalhos disponíveis e quanto é pago para cada atividade.\n\n')



for f in filenames:
    with open(f'{path_read}/{f}') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        job = yaml.load(file, Loader=yaml.FullLoader)
        
        f_item = list(job.keys())[0]

        if f_item == 'None' :
            continue 

        w.write(f'### {f_item}\n')

        desc = '\n'.join(job[f_item]['FullDescription'])

        w.write(f'{desc}\n\n')

        w.write('Atividade | Objeto | Preço\n')
        w.write('--- | --- | ---\n')

        for t in job[f_item].keys():
            if f in mapps and t in mapps[f]:
                for k in job[f_item][t].keys():
                    obj = str(k).replace('_', ' ').capitalize()
                    w.write(f'{t} | {obj} | {job[f_item][t][k]["income"]}  \n') 
        w.write(f'\n\n\n') 

w.close()
        