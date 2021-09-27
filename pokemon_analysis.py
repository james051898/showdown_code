from numpy import empty
import pandas as pd
import re

def usage_dataframe():
    # File path for usage stats
    file = r'C:/Users/kingj/OneDrive/Desktop/python/pokemon/gen8ou-1825.txt'
    poketext = open(file, "r")
    seperator = '+----------------------------------------+' # Delimiter in text file
    string = poketext.read() # Entire text file as String

    data = string.split(sep = seperator) # converts to list

    len_txt = int(len(data)/9)+1 # length of data divided by 9 for iteration
    temp_dex = []

    for i in range(1,len_txt):
        num = 9*i
        bnum = num-9
        temp_dex.append(data[bnum:num])

    dex = pd.DataFrame(temp_dex)
    indx = p_reindex(dex)
    dex = pd.DataFrame(temp_dex, index=indx)
    dex = dex.iloc[:,2:]
    dex = rename_columns(dex)
    return dex

def p_reindex(df):
    temp_indx = df.iloc[:, 1]
    indx = []
    for name in temp_indx:
        new_string = name[4:-4]
        new_string = re.sub("  ", "", new_string).strip()
        indx.append(new_string)
    
    return indx

def rename_columns(df):
    columns = {2: "USAGE", 3: "Abilities", 4: "Items", 5: "Spreads", 6: "Moves", 7:"Teammates", 8:"Checks and Counters"}
    df.rename(columns=columns, inplace = True)
    return df

def pokedex():
    file = r'C:/Users/kingj/OneDrive/Desktop/python/pokemon/pokedex.txt'
    pokedex =pd.read_csv(file)
    return pokedex
