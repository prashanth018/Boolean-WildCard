'''
from Tkinter import * as tk
z = tkinter
z.Label(p,text="first Name").grid(row=1,column=1)
'''


import Tkinter as tk
from Tkinter import StringVar
from Tkinter import IntVar
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        labelText = StringVar()
        labelText.set("Query")
        #root = tk()
        self.title("Search Engine")
        self.labelDir = tk.Label(self, textvariable=labelText, height=4)
        self.labelDir.grid(row=0)
        self.labelDir.pack()
        directory=StringVar(None)
        self.entry = tk.Entry(self,textvariable=directory,width=50)
        self.entry.grid(row=0,column=1)
        self.entry.pack()
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.grid(row=1,column=0)
        self.button.pack()
        self.tex = tk.Text(self)
        self.tex.grid(row=2)
        self.tex.pack()
        self.p = IntVar()
        #labelText.set("Boolean query")
        self.rb1 = tk.Radiobutton(self, text="Boolean query", variable = self.p , value=1)
        #labelText.set("Wildcard")
        self.rb2 = tk.Radiobutton(self, text="Wildcard", variable = self.p , value=2)
        self.rb1.grid(row=1,column=1)
        self.rb2.grid(row=1,column=2)
        self.rb1.pack()
        self.rb2.pack()
    
    def on_button(self):
        #print(self.entry.get())
        self.tex.delete("1.0",tk.END)
        q = self.entry.get()
        #k = q.split()
        if self.p.get()==1:
            for i in range(5):
                self.tex.insert(tk.END, "Hey i'm in Boolean query")
                self.tex.see(tk.END)
                self.tex.insert(tk.END,"\n")
                self.tex.see(tk.END)
        elif self.p.get()==2:
            for i in range(5):
                self.tex.insert(tk.END, "Hey i'm in Wildcard")
                self.tex.see(tk.END)
                self.tex.insert(tk.END,"\n")
                self.tex.see(tk.END)                
app = SampleApp()
app.mainloop()

'''

import Tkinter as tk

def cbc(id, tex):
    return lambda : callback(id, tex)

def callback(id, tex):
    s = 'At {} f is {}\n'.format(id, id**id/0.987)
    tex.insert(tk.END, s)
    tex.see(tk.END)             # Scroll if necessary

top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
for k in range(1,10):
    tv = 'Say {}'.format(k)
    b = tk.Button(bop, text=tv, command=cbc(k, tex))
    b.pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()
'''
'''
import Tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=42, width=42)
        self.entry = tk.Entry(self)
        self.entry.focus()
        self.entry.pack()
        self.tex = tk.Text(self)
        self.tex.pack()
        self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)
        self.clear_button.pack()
        self.get_button = tk.Button(self, text="Run",command=self.run_text)
        self.get_button.pack()

    def clear_text(self):
        self.tex.delete("1.0",tk.END)
    def run_text(self):
        q = self.entry.get()
        k = q.split()
        self.tex.insert(tk.END,str(k))
        self.tex.see(tk.END)

def main():
    root = tk.Tk()
    App(root).pack(expand=True, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()

'''






















