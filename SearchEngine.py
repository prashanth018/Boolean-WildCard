Docs = ['austen-emma.txt','austen-persuasion.txt','austen-sense.txt','blake-poems.txt','bryant-stories.txt','burgess-busterbrown.txt','carroll-alice.txt','chesterton-ball.txt','chesterton-brown.txt','chesterton-thursday.txt','edgeworth-parents.txt','milton-paradise.txt','shakespeare-caesar.txt','shakespeare-hamlet.txt','shakespeare-macbeth.txt','whitman-leaves.txt']

import nltk
import nltk.tokenize
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
import Tkinter as tk
from Tkinter import StringVar
from Tkinter import IntVar
import re

def tok(stri):                                              #function to know if a given substring is a token or AND/NOT/OR
    if stri=="AND" or stri=="NOT" or stri=="OR":
        return False
    return True

def noting(l):                                              #function to complement of a given list documents
    ans=[]                                                  #l is a list
    for i in range(len(Docs)):
        if i not in l:
            ans.append(i)
    return ans                                              #ans is a complemented list of l

def anding(l,r):                                            #anding finds the intersection of 2 lists
    ans=[]
    for i in range(len(l)):
        if l[i] in r:
            ans.append(l[i])
    return ans                                              #ans contains common elemets of list l and r

def oring(l,r):                                             #oring finds the union of 2 lists
    ans=[]
    ans=l+r
    ans = list(set(ans))
    return ans                                              #ans returns the union list of l and r


dictionary ={}                                                     #dictionary here, is used as a map from tokenized, lematized, string to list of document in which it occurs  
i=0
j=0
gut = nltk.corpus.gutenberg
st = PorterStemmer()                                        #stemming used here is porter's stemmer

for i in range(len(Docs)):                                     
    cor = gut.words(Docs[i])
    corp = []
    for j in range(len(cor)):
        l = word_tokenize(cor[j])                           #tokenizing the words
        for k in range(len(l)):
            corp.append(l[k])
        l=[]
    for j in range(len(corp)):                              
        wd = st.stem(corp[j])                               #stemming the words
        
        if wd.lower() in dictionary and not (i in dictionary[wd.lower()]):     #if the word is in dictionary and if the document id doesn't already exist in the list then append the doc id to the list
            dictionary[wd.lower()].append(i)                 #case-lowering the word and appending it to dictionary 
        elif wd.lower() not in dictionary:                  #if word is not in the dictionary
            dictionary[wd.lower()]=[]                        #initialize the list
            dictionary[wd.lower()].append(i)                 #and append the document


hashdictionary={}                                            #This is a map to find the unique keywords used to answer wildcard queries
for i in range(len(Docs)):                                           #It is a map from tokenized but not lematized string to list of documents
    cor = gut.words(Docs[i])
    for j in range(len(cor)):
        if (cor[j].lower()) in hashdictionary and not (i in hashdictionary[cor[j].lower()]):      #if the word is in dictionary and if the document id doesn't already exist in the list then append the doc id to the list
            hashdictionary[cor[j].lower()].append(i)           #case-lowering the word and appending it to dictionary 
        elif (cor[j].lower()) not in hashdictionary:          #if word is not in the dictionary
            hashdictionary[cor[j].lower()]=[]                  #initialize the list
            hashdictionary[cor[j].lower()].append(i)           #and append the document



print "Start your search\n"                                   #Construction of GUI


class SampleApp(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        
        labelText = StringVar()
        labelText.set("Enter your Query")
        
        self.title("Search Engine")
        
        self.labelDir = tk.Label(self, textvariable=labelText, height=4)            #Label
        self.labelDir.grid(row=0)
        self.labelDir.pack()
        
        directory=StringVar(None)
        self.entry = tk.Entry(self,textvariable=directory,width=50)                 #Entry
        self.entry.grid(row=0,column=1)
        self.entry.pack()
        
        self.button = tk.Button(self, text="Search", command=self.on_button)           #Button
        self.button.grid(row=1,column=0)
        self.button.pack()
        
        self.tex = tk.Text(self) #TexBox
        self.tex.grid(row=2)
        self.tex.pack()
        
        self.p = IntVar()   #Initializing Variable self.p for grouping RadioButtons 
        
        self.rb1 = tk.Radiobutton(self, text="Boolean Query", variable = self.p , value=1 )  #RadioButton1
        self.rb2 = tk.Radiobutton(self, text="Wild Card Query", variable = self.p , value=2 )       #RadioButton2
        self.rb1.grid(row=1,column=1)
        self.rb2.grid(row=1,column=2)
        self.rb1.pack()
        self.rb2.pack()
    
    def on_button(self):                                                            #eventHandler, triggered when Run is clicked    
        self.tex.delete("1.0",tk.END)                                               #clearing the text written by previous query
        q = self.entry.get()                                                        #retrieving the text entered in the entry box
        
        try:
            if self.p.get()==1:                                                     #if value returned is 1
                k = word_tokenize(q)
                i=0
                for i in range(len(k)):                                             #Code to Answer Boolean query
                    if not(k[i]=="AND" or k[i]=="OR" or k[i]=="NOT"):
                        k[i] = k[i].lower()
                        k[i] = st.stem(k[i])
                s = []
                i=0
                while i < (len(k)):
                    if k[i]=='NOT' and i+1<len(k) and k[i+1]=='NOT':
                        del(k[i])
                        i-=1
                    i+=1
                for i in range(len(k)):
                    if tok(k[i]) and k[i] in dictionary:
                        pass
                    else:
                        dictionary[k[i]]=[]      
                res=[]
                if k[0]=="NOT":
                    res=noting(dictionary[k[1]])
                    i=2
                else:
                    res = dictionary[k[0]]
                    i=1
                while i < len(k):
                    if k[i]=="AND":
                        op=k[i]
                        if i+1<len(k) and k[i+1]=="NOT":
                           res = anding(res,noting(dictionary[k[i+2]]))
                           i+=2
                        else:
                           res = anding(res,dictionary[k[i+1]])
                           i+=1
                    elif k[i]=="OR":
                        op=k[i]
                        if i+1<len(k) and k[i+1]=="NOT":
                           res = oring(res,noting(dictionary[k[i+2]]))
                           i+=2
                        else:
                           res = oring(res,dictionary[k[i+1]])
                           i+=1
                    i+=1
                for i in range(len(res)):
                    k = Docs[res[i]].split('.')
                    self.tex.insert(tk.END,k[0])                #printing the output to the text field
                    self.tex.see(tk.END)
                    self.tex.insert(tk.END,"\n")
                    self.tex.see(tk.END)
            
            elif self.p.get()==2:                               #Code to execute WildCard queries
                q = q.lower()                   
                lis = q.split()
                n = len(lis)
                for i in range(n):
                    if '*' not in lis[i]:
                        lis[i]+='$'
                    elif lis[i][-1]=='*':
                        lis[i] = lis[i].replace('*','([a-zA-Z]*)')          #regular expression to answer query of format X*
                    else:
                        lis[i] = lis[i].replace('*','([a-zA-Z]*)')          #regular expression to answer query of format X*Y or *X
                        lis[i]+='$'
                res=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                for i in range(n):
                    reg = re.compile(lis[i])                                #compiling the regex
                    stri = [w for w in hashdictionary if re.match(reg,w)]          #stri stores the list of all strings matching the regular expression 
                    r=[]
                    for j in range(len(stri)):
                        r = oring(r,hashdictionary[stri[j]])
                    res = anding(res,r)                                     #computing the result
                for i in range(len(res)):
                    k = Docs[res[i]].split('.')                                
                    self.tex.insert(tk.END,k[0])                            #print the output to the text field
                    self.tex.see(tk.END)
                    self.tex.insert(tk.END,"\n")
                    self.tex.see(tk.END)
        
        except Exception:
            self.tex.insert(tk.END,"Invalid entry")                         #Catches any kind of exceptions
            self.tex.see(tk.END)

app = SampleApp()
app.mainloop()