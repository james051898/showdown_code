from pandas import ExcelWriter as w

def totempexcel(data):
    outfile = r'C:/Users/kingj/OneDrive/Desktop/python/pokemon/temp.xlsx'

    with w(outfile) as writer:
        data.to_excel(writer, sheet_name="Sheet1", index = True, startrow= 2, startcol=2) 
