import re
import pokemon_analysis as poke
import numpy as np
def get_ability(string):
    new_string = string.split('|')
    abilities = []
    substring = "%"

    for i in range(0,len(new_string)):
        temp = new_string.pop()
        if substring in temp:
            abilities.append(temp)
    keys = []
    tempkeys = []
    values = []
    for string in abilities:
        percent = re.findall(r'\d+%|([0-9]\d?)\.\d+%', string)[0]
        key  = re.split('\W+', string)
        count = 0
        for i in key: 
            temp = key[count]
            if temp == percent:
                pos = count
                break
            count = count + 1
        key = key[1:pos]
        values.append(percent)
        last = key[0]
        for i in key:
            new = i
            new_key = last + " " + new 
            last = i 
            keys.append(new_key)
    for i in keys:
        temp = i.split(" ")
        if (temp[0] != temp[1]):
            tempkeys.append(i)
    keys = {tempkeys[i]: values[i] for i in range(len(tempkeys))}
    return keys

def get_type(string):
    pokedex = poke.pokedex()
    i,c  = np.where(pokedex == string)
    index = i[0]
    type = pokedex.iloc[index,4:6]
    return type

def get_bst(string):
    pokedex = poke.pokedex()
    i,c  = np.where(pokedex == string)
    index = i[0]
    bst = pokedex.iloc[index,15:]
    return bst

def get_spread(string):
    return string

def pokemon(pokemon):
    def type():
        type1 = 'type1'
        type = [type1]
        type2 = 'type2'
        if type2 != '':
            type.append(type2) # there are pokemon with composite types
        return type
    def ability(pokemon):
        ability(string)
    def spread():
        spread = {'atk': 252, 'def' : 252, 'spatk' : 252, 'spdef' : 252, 'spd' : 252} # dictionary of always five elements; each element is a string with a number between 0 & 252
        return spread
    def nature():
        nature = [] # this needs to be key value pairs where the key is a string and the value is a probability
        return nature
    def checks():
        checks = [] # list of strings
        return checks
    def counters():
        counters = [] # list of strings
        return checks
