from tkinter import *
import random as rn

seed=rn.randint(0,10000000)
print("seed:",seed)
rn.seed(seed)

tk=Tk()
window=Canvas(tk,bg="#FFFFFF",height=500,width=1000)
window.pack()

xOne=0
xTwo=1000
yOne=0
yTwo=500

for i in range(251):
	color="%06x"%rn.randint(0,0xFFFFFF)
	window.create_rectangle(xOne,yOne,xTwo,yTwo,outline="#"+color)
	xOne+=1
	yOne+=1
	xTwo-=1
	yTwo-=1
	
mainloop()
