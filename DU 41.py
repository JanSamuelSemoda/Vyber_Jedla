import tkinter
canvas=tkinter.Canvas(width=420,height=150,bg='white')
canvas.pack()#Spravy platno kde sa budu diať čary

def tlacidla():
    for i in range(4):
        canvas.create_rectangle(x+i*velkost,y,x+i*velkost+velkost-2,y+velkost-2,outline="",fill=farby[i])
#definicia na vykreslenie štvorcov
def click(sur):#definicia click
    if y<sur.y<y+velkost: #podmienka či sa klika na tacidlo
        poradie=(sur.x-x)//velkost #premena na poradie 
        if 0<=poradie<len(farby): #podmienka ktora kontroluje poradie a farby
            print(poradie) # piše poradie do shellu
            student = entry1.get() #premena student do ktorej bude niečo vstupovať
            if student !="": #podmienka či plocha kam niečo sa da pisať nieje prazdna
                subor=open("vyber_jedla.txt","a") # otvory subor
                subor.write(student+""+skratky[poradie]+"\n") # piše do suboru s tym že farbam dava skratky 
                subor.close()# zatvory subor
canvas.create_text(210,20,text="Vyber Jedla",font="Arial 20",fill="red") #uroby velky červeny text
subor=open("vyber_jedla.txt","w")#otvory subor a vyprazdni ho
subor.close()#zavrie ho 
farby=["red","green","blue","yellow"]#premena farby s farbamy
x, y, velkost= 10, 40, 100# premene na spravenie tacidliel / štvorcov
skratky="rgby"#skratky farieb
tlacidla()#spusti def tlacidla
canvas.bind("<Button-1>",click)# nastavy def click aby sa spustila ked stlačiš lave tlačidlo myši
label1=tkinter.Label(text="kod študenta:")#vysačka kde budeš davať kod študenta 
label1.pack()# to sa spravi
entry1=tkinter.Entry()#spravy entry 
entry1.pack()
            
