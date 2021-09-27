import pokemon_analysis as poke
import object_orientated as oo
import supportive as s
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import ExcelWriter as w
file = "C:/Users/kingj\Documents/My Games/Pokemon Showdown/Logs/2021-09/pm-csc2405jbm.txt"

infile = open(file, "r+")

substring = 'csc2405_jbm:'

wordlist = (infile.read()).split('\n')
for line in wordlist:
    if substring in line:
        team = line
# infile.truncate(0)
infile.close()
team = team.split(':')
team = team[2]
team = team.split('/')

df = poke.usage_dataframe()
pokedex = poke.pokedex()

for pokemon in team:
    pokemon = pokemon.strip()
    data = df.loc[pokemon]
    print(data)

