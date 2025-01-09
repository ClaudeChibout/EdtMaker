import tkinter as tk

edt = [["" for _ in range(5)] for _ in range(5)]
hOfMat = {
    "system1": "0:0|1:2,3",#10
    "system2": "0:0|1:2,3",#10
    "system3": "0:0|2:0,1",#10
    "system4": "0:0|3:0,1",#10
    "system5": "0:0|4:2,3",#10
    "system6": "0:0|4:0,1",#10
    "system7": "0:0|2:2,3",#10
    "GenieLo1": "3:1|2:0,1",#12
    "GenieLo2": "3:1,2,3",#12
    "ProjetBio": "",#402
    "ProjetEmbarque": "",#401
    "ProjetRecherche": "",#400
    "web1": "1:1,2,3",#17
    "web2": "1:1|2:2,3",#17
    "web3": "1:1|3:3,4",#17
    "web4": "1:1|4:0,1",#17
    "Compilation": "1:2|3:0,1",#18
    "Crypto1": "2:1|0:1,2",#24
    "Crypto2": "2:1,3,4",#24
    "Crypto3": "2:1|3:0,1",#24
    "Crypto4": "2:1|4:2,3",#24
    "ia1": "3:2|0:2,3",#25
    "ia2": "3:2|4:2,3",#25
    "ia3": "3:2|1:2,3",#25
    "ia4": "3:2|4:0,1",#25
    "sdd1": "1:0|0:1,2",#26
    "sdd2": "1:0,3,4",#26
    "sdd3": "1:0|2:2,3",#26
    "eco": "2:2|3:2,3",#27
    "calcul1": "2:0|0:2,3",#30
    "calcul2": "2:0|4:0,1",#30
    "archi2": "2:2,3,4",#31
    "progComparee": "0:1,2,3"#32
}

root = tk.Tk()
#root.geometry("700x500")

canv = tk.Canvas(root, background="Gray", height=500, width= 700)
canv.grid(row=0, column=0, columnspan=7)

H = 500
W = 700

h_rect = H/5
w_rect = W/5

def addDelMat(m):
    data = hOfMat[m].split("|")
    data = [(int(x.split(":")[0]), x.split(":")[1]) for x in data]
    for d in data:
        x = d[0]
        v = [int(z) for z in d[1].split(",")]
        for y in v:
            if edt[x][y] == "":
                val = canv.create_rectangle(x*w_rect, y*h_rect, (x+1)*w_rect, (y+1)*h_rect, fill="green")
            else:
                canv.delete(edt[x][y])
                val = canv.create_rectangle(x*w_rect, y*h_rect, (x+1)*w_rect, (y+1)*h_rect, fill="red")
            edt[x][y] = val

    # ajoute le text
    t = Label.cget("text")
    Label.config(text=(Label.cget("text")+" | "+m if t != "" else m))

def undo():
    t= Label.cget("text")
    t = t.split(" | ")
    t.pop(-1)
    reset()
    for x in t:
        addDelMat(x)
    t = " | ".join(t)
    Label.config(text=t)

def reset():
    for x, day in enumerate(edt):
        for y, h in enumerate(day):
            if edt[x][y] != "":
                canv.delete(edt[x][y])
                edt[x][y] = ""
    Label.config(text="")


Label = tk.Label(root, font=("Arial", 15), fg = "red")
Label.grid(row=10, column=0, columnspan=7)

madeLabel = tk.Label(root,text="Made by Claude Chibout", font=("Arial", 15), fg = "Purple")
madeLabel.grid(row=1, column=3, columnspan=4)

# crée la grille
for x, day in enumerate(edt):
    for y, hour in enumerate(day):
        print(x*w_rect, y*h_rect, (x+1)*w_rect, (y+1)*h_rect)
        canv.create_rectangle(x*w_rect, y*h_rect, (x+1)*w_rect, (y+1)*h_rect)

buttonReset = tk.Button(text = "reset", command=reset)
buttonReset.grid(row=1, column =0)

buttonUndo = tk.Button(text = "undo", command=undo)
buttonUndo.grid(row=1, column = 2)

buttonArchi = tk.Button(text = "archi2", command=lambda:addDelMat("archi2"))
buttonArchi.grid(row=2, column =0)

buttonprogComparee = tk.Button(text = "progComparee", command=lambda:addDelMat("progComparee"))
buttonprogComparee.grid(row=2, column =2)

buttoneco = tk.Button(text = "eco", command=lambda:addDelMat("eco"))
buttoneco.grid(row=2, column =3)

buttonSystem1 = tk.Button(text = "system1", command=lambda:addDelMat("system1"))
buttonSystem1.grid(row=3, column =0)
buttonSystem2 = tk.Button(text = "system2", command=lambda:addDelMat("system2"))
buttonSystem2.grid(row=3, column =1)
buttonSystem3 = tk.Button(text = "system3", command=lambda:addDelMat("system3"))
buttonSystem3.grid(row=3, column =2)
buttonSystem4 = tk.Button(text = "system4", command=lambda:addDelMat("system4"))
buttonSystem4.grid(row=3, column =3)
buttonSystem5 = tk.Button(text = "system5", command=lambda:addDelMat("system5"))
buttonSystem5.grid(row=3, column =4)
buttonSystem6 = tk.Button(text = "system6", command=lambda:addDelMat("system6"))
buttonSystem6.grid(row=3, column =5)
buttonSystem7 = tk.Button(text = "system7", command=lambda:addDelMat("system7"))
buttonSystem7.grid(row=3, column =6)

buttonGenieLo1 = tk.Button(text = "GenieLo1", command=lambda:addDelMat("GenieLo1"))
buttonGenieLo1.grid(row=4, column =0)
buttonGenieLo2 = tk.Button(text = "GenieLo2", command=lambda:addDelMat("GenieLo2"))
buttonGenieLo2.grid(row=4, column =1)

buttonweb1 = tk.Button(text = "web1", command=lambda:addDelMat("web1"))
buttonweb1.grid(row=5, column =0)
buttonweb2 = tk.Button(text = "web2", command=lambda:addDelMat("web2"))
buttonweb2.grid(row=5, column =1)
buttonweb3 = tk.Button(text = "web3", command=lambda:addDelMat("web3"))
buttonweb3.grid(row=5, column =2)
buttonweb4 = tk.Button(text = "web4", command=lambda:addDelMat("web4"))
buttonweb4.grid(row=5, column =3)




buttonCompilation = tk.Button(text = "Compilation", command=lambda:addDelMat("Compilation"))
buttonCompilation.grid(row=2, column =1)

buttonCrypto1 = tk.Button(text = "Crypto1", command=lambda:addDelMat("Crypto1"))
buttonCrypto1.grid(row=6, column =0)
buttonCrypto2 = tk.Button(text = "Crypto2", command=lambda:addDelMat("Crypto2"))
buttonCrypto2.grid(row=6, column =1)
buttonCrypto3 = tk.Button(text = "Crypto3", command=lambda:addDelMat("Crypto3"))
buttonCrypto3.grid(row=6, column =2)
buttonCrypto4 = tk.Button(text = "Crypto4", command=lambda:addDelMat("Crypto4"))
buttonCrypto4.grid(row=6, column =3)

buttoncalcul1 = tk.Button(text = "calcul1", command=lambda:addDelMat("calcul1"))
buttoncalcul1.grid(row=7, column =0)
buttoncalcul2 = tk.Button(text = "calcul2", command=lambda:addDelMat("calcul2"))
buttoncalcul2.grid(row=7, column =1)

buttonia1 = tk.Button(text = "ia1", command=lambda:addDelMat("ia1"))
buttonia1.grid(row=8, column =0)
buttonia2 = tk.Button(text = "ia2", command=lambda:addDelMat("ia2"))
buttonia2.grid(row=8, column =1)
buttonia3 = tk.Button(text = "ia3", command=lambda:addDelMat("ia3"))
buttonia3.grid(row=8, column =2)
buttonia4 = tk.Button(text = "ia4", command=lambda:addDelMat("ia4"))
buttonia4.grid(row=8, column =3)

buttonsdd1 = tk.Button(text = "sdd1", command=lambda:addDelMat("sdd1"))
buttonsdd1.grid(row=9, column =0)
buttonsdd2 = tk.Button(text = "sdd2", command=lambda:addDelMat("sdd2"))
buttonsdd2.grid(row=9, column =1)
buttonsdd3 = tk.Button(text = "sdd3", command=lambda:addDelMat("sdd3"))
buttonsdd3.grid(row=9, column =2)


root.mainloop()



