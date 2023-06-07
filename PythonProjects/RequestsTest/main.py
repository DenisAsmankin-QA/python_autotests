import requests

token = '5b66ea0bd51f643aaa2d1f955821a84a'
host = 'https://pokemonbattle.me:9104'
new_pokemon = requests.post(f'{host}/pokemons', json = 
                {
    "name": "Python Max",
    "photo": "https://dolnikov.ru/pokemons/albums/900.png"
                }, 
    headers={"Content-Type" : "application/json", "trainer_token" : token } )
print(new_pokemon.text)  #  создал нового бойца



new_name_pokemon = requests.put(f'{host}/pokemons', json = 
                {
    "pokemon_id": "13126",
    "name": "New Python",
    "photo": "https://dolnikov.ru/pokemons/albums/807.png"
                }, 
    headers={"Content-Type" : "application/json", "trainer_token" : token } )
print(new_name_pokemon.text)   #  меняю имя и фото



in_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = 
                {
    "pokemon_id": "13126"
                }, 
    headers={"Content-Type" : "application/json", "trainer_token" : token } )
print(in_pokeball.text)    #  поместил в ball


info = requests.get(f'{host}/trainers', params = {'trainer_id': 4673 } )
print(info.text)      #  информация по трениру с использованием квери параметра "trainer_id"