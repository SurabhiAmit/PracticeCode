#Lookup function when index is a list
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
    
#Lookup function when index is a dictionary type 

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None    