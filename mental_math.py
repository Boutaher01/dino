from tkinter import *
from time import time
from random import randint
from tkinter import messagebox

#configuration de la fenêtre principale:
sc = Tk()
sc.title('le calcul mental')
sc.geometry('500x500+50+150')
sc.config(bg='orange')
l0 = Label(sc, text='Le calcul mental', font=('arial',45))
l0.place(x=30,y=150)
l01 = Label(sc, text="Réaliser par l'ispecteur stagiaire: ", font=('arial',10))
l01.place(x=30,y=265)
l02 = Label(sc, text='Mohamed BOUTAHER', font=('arial',10))
l02.place(x=30,y=286)

#création de la menu:
mainmenu = Menu(sc)

#création des fonctions des sous-fenêtresde la 1e fenêtre:
def next_w():
    w = Toplevel(sc)
    w.title('multiplication')
    w.geometry('500x500+600+150')
    w.config(bg='yellow')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}x{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    def ok():
        v = int(e.get())
        if v == x*y:
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        x,y=[randint(0,9) for i in range(2)]
        var.set(f'{x}x{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w1():
    w = Toplevel(sc)
    w.title('multiplication')
    w.geometry('500x500+600+150')
    w.config(bg='yellow')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}x{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time() 
    def ok():
        v = int(e.get())
        if v == x*y and ((time()-t0)<=10):
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse ou temps dépassé !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        t0 = time()
        x,y=[randint(0,9) for i in range(2)]
        var.set(f'{x}x{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w2():
    w = Toplevel(sc)
    w.title('multiplication')
    w.geometry('500x500+600+150')
    w.config(bg='yellow')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}x{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time()
    score = 0
    essay = 0
    def cnt():
        nonlocal essay
        nonlocal score
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        essay += 1
        if essay <= 10:
            v = int(e.get())
            if v == x*y and ((time()-t0)<=10):
                score += 1
            t0 = time()
            x,y=[randint(0,9) for i in range(2)]
            var.set(f'{x}x{y}')
            l = Label(w, textvariable=var, font=('arial',50))
            l.place(x=200,y=0)
            e = Entry(w)
            e.place(x=200,y=100)
        else:
            messagebox.showinfo('Feedback', f'Votre score est: {score}/10')
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

#création des fonctions des sous-fenêtres de la 2e fenêtre:
def next_w20():
    w = Toplevel(sc)
    w.title('addition')
    w.geometry('500x500+600+150')
    w.config(bg='pink')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}+{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    def ok():
        v = int(e.get())
        if v == x+y:
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        x,y=[randint(0,9) for i in range(2)]
        var.set(f'{x}+{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w21():
    w = Toplevel(sc)
    w.title('addition')
    w.geometry('500x500+600+150')
    w.config(bg='pink')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}+{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time() 
    def ok():
        v = int(e.get())
        if v == x+y and ((time()-t0)<=10):
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse ou temps dépassé !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        t0 = time()
        x,y=[randint(0,9) for i in range(2)]
        var.set(f'{x}+{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w22():
    w = Toplevel(sc)
    w.title('addition')
    w.geometry('500x500+600+150')
    w.config(bg='pink')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,9) for i in range(2)]
    var.set(f'{x}+{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time()
    score = 0
    essay = 0
    def cnt():
        nonlocal essay
        nonlocal score
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        essay += 1
        if essay <= 10:
            v = int(e.get())
            if v == x+y and ((time()-t0)<=10):
                score += 1
            t0 = time()
            x,y=[randint(0,9) for i in range(2)]
            var.set(f'{x}+{y}')
            l = Label(w, textvariable=var, font=('arial',50))
            l.place(x=200,y=0)
            e = Entry(w)
            e.place(x=200,y=100)
        else:
            messagebox.showinfo('Feedback', f'Votre score est: {score}/10')
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

#création des fonctions des sous-fenêtres de la 3e fenêtre:
def next_w30():
    w = Toplevel(sc)
    w.title('soustraction')
    w.geometry('500x500+600+150')
    w.config(bg='purple')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,20) for i in range(2)]
    if x<y:
        x,y=y,x
    var.set(f'{x}-{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    def ok():
        v = int(e.get())
        if v == x-y:
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        x,y=[randint(0,20) for i in range(2)]
        if x<y:
            x,y=y,x
        var.set(f'{x}-{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w31():
    w = Toplevel(sc)
    w.title('soustraction')
    w.geometry('500x500+600+150')
    w.config(bg='purple')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,20) for i in range(2)]
    if x<y:
        x,y=y,x
    var.set(f'{x}-{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time() 
    def ok():
        v = int(e.get())
        if v == x-y and ((time()-t0)<=10):
            messagebox.showinfo('Feedback','Bravo, continue !')
            
        else:
            messagebox.showerror('Feedback','Réponse fausse ou temps dépassé !')
    b = Button(w, text='OK', command=ok)
    b.place(x=70, y=400)
    def cnt():
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        t0 = time()
        x,y=[randint(0,20) for i in range(2)]
        if x<y:
            x,y=y,x
        var.set(f'{x}-{y}')
        l = Label(w, textvariable=var, font=('arial',50))
        l.place(x=200,y=0)
        e = Entry(w)
        e.place(x=200,y=100)
        
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

def next_w32():
    w = Toplevel(sc)
    w.title('soustraction')
    w.geometry('500x500+600+150')
    w.config(bg='purple')
    var=StringVar()
    var1=IntVar()
    x,y=[randint(0,20) for i in range(2)]
    if x<y:
        x,y=y,x
    var.set(f'{x}-{y}')
    l = Label(w, textvariable=var, font=('arial',50))
    l.place(x=200,y=0)
    e = Entry(w)
    e.place(x=200,y=100)
    t0 = time()
    score = 0
    essay = 0
    def cnt():
        nonlocal essay
        nonlocal score
        nonlocal e
        nonlocal l
        nonlocal x,y
        nonlocal t0
        essay += 1
        if essay <= 10:
            v = int(e.get())
            if v == x-y and ((time()-t0)<=10):
                score += 1
            t0 = time()
            x,y=[randint(0,20) for i in range(2)]
            if x<y:
                x,y=y,x
            var.set(f'{x}-{y}')
            l = Label(w, textvariable=var, font=('arial',50))
            l.place(x=200,y=0)
            e = Entry(w)
            e.place(x=200,y=100)
        else:
            messagebox.showinfo('Feedback', f'Votre score est: {score}/10')
    b1 = Button(w, text='CONTINU', command=cnt)
    b1.place(x=350, y=400)

#création de la 1e fenêtre et ses sous-fenêtres:    
menu1 = Menu(mainmenu, tearoff=0)
menu1.add_command(label='Entrainement', command=next_w)
menu1.add_command(label='Vitesse', command=next_w1)
menu1.add_command(label='Test', command=next_w2)

#création de la 2e fenêtre et ses sous-fenêtres:    
menu2 = Menu(mainmenu, tearoff=0)
menu2.add_command(label='Entrainement', command=next_w20)
menu2.add_command(label='Vitesse', command=next_w21)
menu2.add_command(label='Test', command=next_w22)

#création de la 3e fenêtre et ses sous-fenêtres:    
menu3 = Menu(mainmenu, tearoff=0)
menu3.add_command(label='Entrainement', command=next_w30)
menu3.add_command(label='Vitesse', command=next_w31)
menu3.add_command(label='Test', command=next_w32)

#la forme de la première fenêtre:
mainmenu.add_cascade(label='Multiplication', menu=menu1)

#la forme de la 2e fenêtre:
mainmenu.add_cascade(label='Addition', menu=menu2)

#la forme de la 3e fenêtre:
mainmenu.add_cascade(label='Soustraction', menu=menu3)

sc.config(menu=mainmenu)

#boucle infinie:
mainloop()
