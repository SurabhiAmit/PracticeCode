# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(s):
    result,word,atsplit,i=[],'',False,0
    while i<len(s):
        if s[i]=='<'or s[i]==' ':
            atsplit=True
        if s[i]!='<'and s[i]!=' ':
            word+=s[i]
        if atsplit:
            if word:
                result.append(word)
                word=''
            if s[i]==' ':
                atsplit=False
            if s[i]=='<':
                k=s.find('>',i)
                i,atsplit=k,False
        if i==len(s)-1: 
            if word:
                result.append(word)
        i+=1        
    return result            
                

#print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

#print remove_tags('This sentence has no tags.')