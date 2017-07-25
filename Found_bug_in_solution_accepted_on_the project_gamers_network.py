# In a project at the end of course on Introduction to Computer Science by Udacity, 
# I submitted the following code : 

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def create_data_structure(string_input):
    name_start,prev_name_end,network,play_end,length=0,0,{},0,len(string_input)
    while name_start < length-1:
        friends,games=[],[]
        connections,games_to_play={},{}
        name_end=string_input.find('is connected to',prev_name_end+1)
        name=string_input[name_start:name_end-1]
        connections_end=string_input.find('.',name_end)
        friend_start=name_end+16
        friend_end=string_input.find(',',friend_start)
        while friend_end < connections_end:
            friend=string_input[friend_start:friend_end]
            friend_start=friend_end+2
            friend_end=string_input.find(',',friend_start)
            friends.append(friend)
            if friend_end==-1:
                break
        friend_end=string_input.find('.',friend_start)    
        friends.append(string_input[friend_start:friend_end])  
        connections['friends_of_'+name]=friends
        game_start=string_input.find('likes to play',connections_end)+14
        game_end=string_input.find(',',game_start)
        play_end=string_input.find('.',game_end)
        while game_end < play_end:
            game=string_input[game_start:game_end]
            game_start=game_end+2
            game_end=string_input.find(',',game_start)
            games.append(game)
            if game_end==-1:
                break
        game_end=string_input.find('.',game_start)    
        games.append(string_input[game_start:game_end])  
        games_to_play['games_for_'+name]=games    
        network[name]=connections,games_to_play
        name_start=play_end+1
        prev_name_end=name_end
    return network
    

######################################################################################

def get_connections(network, user):
    if user in network:
        return network[user][0]['friends_of_'+user]
	return None
net = create_data_structure(example_input)
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")

######################################################################################

def get_games_liked(network,user):
    if user in network:
        return network[user][1]['games_for_'+user]
    return None
net = create_data_structure(example_input)    
#print get_games_liked(net, "John") 

#######################################################################################

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B in network[user_A][0]['friends_of_'+user_A]:
        return network
    network[user_A][0]['friends_of_'+user_A].append(user_B)
    return network
net = create_data_structure(example_input)    
#print add_connection(net, "John", "Freda")

#######################################################################################

def add_new_user(network, user, games):
    if user in network:
        return network
    games_to_play={}
    connections={}
    connections['friends_of_'+user]=[]
    games_to_play['games_for_'+user]=games
    network[user]=(connections,games_to_play)
    return network
net = create_data_structure(example_input)    
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])

########################################################################################

def get_secondary_connections(network, user):
    result=[]
    if user not in network:
        return None
    friends=network[user][0]['friends_of_'+user]
    if not friends:
        return []
    for each in friends:
        for entry in network[each][0]['friends_of_'+each]:
            if entry not in result:
                result.append(entry)
    return result
net = create_data_structure(example_input)     
#print get_secondary_connections(net, "Mercedes")    
#>>>['John', 'Levi', 'Bryant', 'Ollie', 'Olive', 'Freda', 'Mercedes']

#########################################################################################

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    count=0
    for each in network[user_A][0]['friends_of_'+user_A]:
        if each in network[user_B][0]['friends_of_'+user_B]:
            count+=1
    return count 
net = create_data_structure(example_input)      
#print count_common_connections(net, "Mercedes", "John") 

#########################################################################################   
       
        
def find_path_to_friend(network, user_A, user_B):
    checked=[]
    result=[]
    if user_A not in network or user_B not in network:
        return None
    return get_path(network,checked, user_A, user_B,result)

def get_path(network,checked, user_A, user_B,result):
    friends=network[user_A][0]['friends_of_'+user_A]
    if user_B in friends:
        result.append(user_A)
        result.append(user_B)
        return result
    if user_A not in checked:
        checked.append(user_A)    
    for each in friends:
        if each not in checked:
            checked.append(each)
            if user_B in network[each][0]['friends_of_'+each]:
                result.append(user_A)
                result.append(each)
                result.append(user_B)
                return result
    
    for each in friends:
        for entry in network[each][0]['friends_of_'+each]:
            if entry not in checked:
                checked.append(each)
                if user_A not in result:														
                    result.append(user_A)
                if each not in result:														
                    result.append(each)
                path= get_path(network,checked, entry, user_B,result)
                if path:
                    return path
        return None 
        
 #print create_data_structure(example_input)

 #   The sub-program  "def find_path_to_friend(network, user_A, user_B):", passed all 
 #  test cases on submission but when I tried to improvise code, I used more complicated
 #   test cases and hence found some errors in this initial code. 
 
 # TEST CASE:

add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
add_connection(net, "Jennie", "Nick")
print find_path_to_friend(net,"John","Nick")

# OUTPUT:
None

# CORRECT OUTPUT (EXPECTED) :

['John', 'Bryant', 'Olive', 'Ollie', 'Freda', 'Debra', 'Jennie', 'Nick']

# CORRECTION I FIGURED OUT:

correction was not to append all entries checked into result (path) and
the correction I figured is, to add "return [user_A,each]+path", instead of appending all 
checked entries into final path (disregarding whether it actually constitutes path)

# AFTER CORRECTION:

for each in friends:
for entry in network[each][0]['friends_of_'+each]:
if entry not in checked:
checked.append(each)
path= get_path(network,checked, entry, user_B,result)
if path:
return [user_A,each]+path
return None

Hence,this was the correction in my initial code which passed all test cases on submission.
   
 # IMPROVISED CODE:
	---------------------
	
def find_path_to_friend(network, user_A, user_B):
    checked=[]
    if user_A not in network or user_B not in network:
        return None
    return get_path(network,checked, user_A, user_B)

def get_path(network,checked, user_A, user_B):
    friends=network[user_A][0]['friends_of_'+user_A]
    if user_B in friends:
        return [user_A,user_B]
    checked.append(user_A)    
    for each in friends:
        if each not in checked:
            path=get_path(network,checked, each, user_B)
            if path:
                return [user_A]+path
    return None 
    
    
       # LATEST CODE:
    ------------------
	
	def find_path_to_friend(network,user_A,user_B,checked=None):
    if user_A not in network or user_B not in network:
        return None
    if checked==None:
        checked=[user_A]
    if user_B in network[user_A][0]['friends_of_'+user_A]:
        return [user_A,user_B]
    for each in network[user_A][0]['friends_of_'+user_A]:
        if each not in checked:
            checked.append(each)
            path = find_path_to_friend(network,each,user_B,checked)
            if path:
                return [user_A]+path
    return None 