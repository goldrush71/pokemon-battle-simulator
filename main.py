import requests, json

#some one time setup code



iter = 1
tandem = {} #tandem contains the metadex and the pokedex
metadex = {} #the metadex relates pokemon names to numbers
pokedex = {} #the pokedex relates numbers to pokemon info
pokemon = {} #an individual pokemon
typeslist = []
abilitylist = []
stats = {}



try: #because if the file is empty it will error :3
    f = open("all_pokemon.json","r")
    pokedex = json.load(f) #to access keys
    for i in pokedex.keys():
        iter+=1
    test_range = 1017-iter
    f.close()
except:
    test_range = 1017

for i in range(test_range):

    pokemon = {} #POKEMON REFRESH

    try:
        f = open("all_pokemon.json","r")
        pokedex = json.load(f)
        f.close()
    except:
        print("bad")
    
    get = requests.get(f"https://pokeapi.co/api/v2/pokemon/{iter}") #GET DATA

    pkmn = None #JSON REFRESH ON REPEATED LOOPS

    pkmn = json.loads(get.content) #LOAD DATA
    
    pokemon['number'] = iter #NUMBER ASSIGNMENT

    pokemon['name'] = pkmn['name'] #NAME ASSGINMENT
    
    determining_type_range = 1
    if len(pkmn['types']) > 1:
        determining_type_range = 2
    y = 0
    for x in range(determining_type_range): #TYPES ASSIGNMENT
        newtype = pkmn['types'][y]['type']['name']
        typeslist.append(newtype)
        y+=1
    pokemon['types'] = typeslist
    typeslist = [] #TYPES REFRESH

    y=0
    for x in pkmn['abilities']: #ABILITIES ASSIGNMENT
        newability = pkmn['abilities'][y]['ability']['name']
        typeslist.append(newtype)
        y+=1
    pokemon['abilities'] = abilitylist
    abilitylist = [] #ABILITIES REFRESH

    stats['hp'] = pkmn['stats'][0]['base_stat'] 
    stats['atk'] = pkmn['stats'][1]['base_stat']
    stats['def'] = pkmn['stats'][2]['base_stat']
    stats['spa'] = pkmn['stats'][3]['base_stat']
    stats['spd'] = pkmn['stats'][4]['base_stat']
    stats['spe'] = pkmn['stats'][5]['base_stat']
    pokemon['stats'] = stats #STATS ASSIGNMENT

    #end code
    pokedex[f"{iter}"] = pokemon
    f = open("all_pokemon.json","w")
    json.dump(pokedex,f,indent=4)
    completion = 100*(iter/1017)
    completion = round(completion,4)
    f.close()
    print(f"Pokemon #{iter}, {pkmn['name'].upper()}, was recorded! The pokedex is {completion}% complete")
    iter+=1

