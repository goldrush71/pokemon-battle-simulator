import requests, json

#some one time setup code

assumed_error = True
while assumed_error == True:
    try:
        test_range = int(input('Enter Range (1017 for all pokemon)\n\t>'))
        assumed_error = False
    except:
        assumed_error = True


iter = 1
pokedex = {}
meta_pokemon = {}
pokemon = {}
typeslist = []
abilitylist = []
stats = {}
with open("all_pokemon.json",'a') as f:
    for i in range(test_range):
        get = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{iter}")
        pkmn = json.loads(get.content)
        nname = pkmn['name']
        pokemon['name':nname] #the only simple one
        
        for x in pkmn['types']:
            newtype = x['type']['name']
            typeslist.append(newtype)
        pokemon['types':typeslist]
        typeslist = []

        for x in pkmn['abilities']:
            newability = x['ability']['name']
            typeslist.append(newtype)

        pokemon['ability':abilitylist]
        abilitylist = []
        stats['hp'] = pkmn['stats'][0]['base_stat']
        stats['atk'] = pkmn['stats'][1]['base_stat']
        stats['def'] = pkmn['stats'][2]['base_stat']
        stats['spa'] = pkmn['stats'][3]['base_stat']
        stats['spd'] = pkmn['stats'][4]['base_stat']
        stats['spe'] = pkmn['stats'][5]['base_stat']
        pokemon['stats':stats]
        json.dump(pokedex,f,indent=4)
        print(f"{iter}:{['name']}")
        iter += 1
