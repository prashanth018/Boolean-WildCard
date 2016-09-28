a = ['shakespeare-macbeth.txt','shakespeare-hamlet.txt','shakespeare-caesar.txt','blake-poems.txt','burgess-busterbrown.txt']
import nltk
import nltk.tokenize
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
def tok(st):
    if st=="AND" or st=="NOT" or st=="OR":
        return False
    return True
def noting(l):
    ans=[]
    for i in range(5):
        if i not in l:
            ans.append(i)
    return ans
def oring(l,r):
    ans=[]
    ans=l+r
    ans = list(set(ans))
    return ans
def anding(l,r):
    ans=[]
    for i in range(len(l)):
        if l[i] in r:
            ans.append(l[i])
    return ans

dic ={}
i=0
j=0
gut = nltk.corpus.gutenberg
st = PorterStemmer()

for i in range(5):
    cor = gut.words(a[i])
    corp = []
    for j in range(len(cor)):
        l = word_tokenize(cor[j])
        for k in range(len(l)):
            corp.append(l[k])
        l=[]
    for j in range(len(corp)):
        wd = st.stem(corp[j])
        
        if wd in dic and not (i in dic[wd]):
            dic[wd].append(i)
        elif wd not in dic:
            dic[wd]=[]
            dic[wd].append(i)
            #print "else exec"
print "Enter Now"
#testing
#s = raw_input()
'''
z = word_tokenize(s)
for i in range(len(z)):
    z[i] = st.stem(z[i])
for i in range(len(z)):
    if z[i] in dic:
        print z[i] + " --> " + str(dic[z[i]])
    else:
        print z[i] + " --> " + "Not Present"
'''


    
q = ""
q = raw_input()
#q = q.lower()
#k = q.split()
k = word_tokenize(q)
i=0
for i in range(len(k)):
    if not(k[i]=="AND" or k[i]=="OR" or k[i]=="NOT"):
        k[i] = k[i].lower()
        k[i] = st.stem(k[i])
s = []
i=0
while i < (len(k)):
    if k[i]=='NOT' and i+1<len(k) and k[i+1]=='NOT':
        del(k[i])
        i-=1
    #print i
    i+=1
#k = " ".join(k)
#print k

for i in range(len(k)):
    if tok(k[i]) and k[i] in dic:
        print k[i] + "-->" + str(dic[k[i]])
    else:
        dic[k[i]]=[]
        print dic[k[i]]

    
res=[]
if k[0]=="NOT":
    res=noting(dic[k[1]])
    i=2
else:
    res = dic[k[0]]
    i=1
while i < len(k):
    #if tok(k[i]):
    #    res=k[i]
    #    op=""
    #elif k[i]=="NOT":
    #    f=1
    if k[i]=="AND":
        op=k[i]
        if i+1<len(k) and k[i+1]=="NOT":
           res = anding(res,noting(dic[k[i+2]]))
           i+=2
        else:
           res = anding(res,dic[k[i+1]])
           i+=1
    elif k[i]=="OR":
        op=k[i]
        if i+1<len(k) and k[i+1]=="NOT":
           res = oring(res,noting(dic[k[i+2]]))
           i+=2
        else:
           res = oring(res,dic[k[i+1]])
           i+=1
    i+=1
print res




















 
