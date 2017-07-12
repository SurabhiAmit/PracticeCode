 Define a procedure, hashtable_add(htable,key,value)
#that adds the key to the hashtable (in the correct bucket), with the correct 
# value and returns the new hashtable.

#def hashtable_add(htable,key,value):
#    index=hash_string(key,len(htable))
#    htable[index].append([key,value])
#    return htable 

# More efficient code using hashtable_get_bucket(htable,keyword):
def hashtable_add(htable,key,value):
	hashtable_get_bucket(htable,key).append([key,value])
  return htable
    
     
# Define a procedure, hashtable_get_bucket, that takes two inputs - a hashtable, and a keyword, and 
# returns the bucket where the keyword could occur.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]



def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

#to test hashtable_get_bucket(htable,keyword)

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

# to test hashtable_add(htable,key,value)

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]



