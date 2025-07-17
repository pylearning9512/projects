import requests
import json
"""
this is an implementation of a text-based pokedex by consuming api data in the form of a json file. formatting it and printing the pokemon info.

will hopefully add a gui at some point. though the purpose of this code is only as proof of concept using an api and json

"""
base_url = "http://pokeapi.co/api/v2/"


def pokedex():

    def get_pokemon_info(name):
        url= f"{base_url}/pokemon/{pkmn_name}"
        response = requests.get(url)
        if response.status_code==200:
            pokemon_data=response.json()
            return pokemon_data
        else:
            print("pokemon not found")

    pkmn_name= input("enter pokemon here: ").casefold()
    pkmn_info = get_pokemon_info(pkmn_name)
        

    def description():
        desc_url= f"{base_url}/pokemon-species/{pkmn_info["id"]}/"
        flavor_text = requests.get(desc_url)
                
        if flavor_text.status_code==200:
            pkdx_entry = flavor_text.json()
            clean_description = pkdx_entry["flavor_text_entries"][0]["flavor_text"].replace('\n', ' ').replace('\f', ' ')
            print(f"\nDescription:\n{clean_description}")
        else:
            print("Description not found")
            

    

    if pkmn_info:
        print("----------------------------------------------")
        print(f"\nname: {pkmn_info["name"].capitalize()}")
        print(f"ID: {pkmn_info["id"]}")
        print(f"height:{(pkmn_info["height"])*10}cm")
        print(f"weight: {(pkmn_info["weight"])/10} kg")
    
        description()
        print("----------------------------------------------")
    
    
    



    

pokedex()
