from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Unit converter')
root.iconbitmap("C:\\Users\\user\\OneDrive\\Pictures\\calculator.ico")

centimeter_lbl= Label(root, text='CM >> M')
centimeter_lbl.grid(row=0, column=0,)
cmeter_lbl= Label(root, text='M >> CM')
cmeter_lbl.grid(row=2, column=0,)

kilometer_lbl= Label(root, text='KM >> M')
kilometer_lbl.grid(row=4, column=0)
kmeter_lbl= Label(root, text='M >> KM')
kmeter_lbl.grid(row=6, column=0)

kelvin_lbl= Label(root, text='Kelv >> Cel')
kelvin_lbl.grid(row=8, column=0,)
celsius_lbl= Label(root, text='Cel >> Kelv')
celsius_lbl.grid(row=10, column=0,)

gram_lbl= Label(root, text='KG >> G')
gram_lbl.grid(row=12, column=0,)
kilogram_lbl= Label(root, text='G >> KG')
kilogram_lbl.grid(row=14, column=0,)

litre_lbl= Label(root, text='L >> ML')
litre_lbl.grid(row=16, column=0,)
mililitre_lbl= Label(root, text='ML >> L')
mililitre_lbl.grid(row=18, column=0,)



centi=Entry(root, width=35)
centi.grid(row=1, column=0)
meter=Entry(root, width=35)
meter.grid(row=3, column=0)

kilo=Entry(root, width=35)
kilo.grid(row=5, column=0)
kmeter=Entry(root, width=35)
kmeter.grid(row=7, column=0)

kelvin=Entry(root, width=35)
kelvin.grid(row=9, column=0)
kcelsius=Entry(root, width=35)
kcelsius.grid(row=11, column=0)

grams=Entry(root, width=35)
grams.grid(row=13, column=0)
kgrams=Entry(root, width=35)
kgrams.grid(row=15, column=0)

litres=Entry(root, width=35)
litres.grid(row=17, column=0)
lmili=Entry(root, width=35)
lmili.grid(row=19, column=0)

def cm_m():
    cm=int(centi.get())*100
    ans_cm=Label(root,text=cm )
    ans_cm.grid(row=1, column=2)    
def m_cm():
    m=int(meter.get())/100
    ans_m=Label(root,text=m )
    ans_m.grid(row=3, column=2)

def km_m():
    km=int(kilo.get())*1000
    ans_km=Label(root,text=km )
    ans_km.grid(row=5, column=2)
def m_km():
    klm=int(kmeter.get())/100
    ans_klm=Label(root,text=klm )
    ans_klm.grid(row=7, column=2)

def ke_cel():
    ke=int(kelvin.get())-273
    ans_ke=Label(root,text=ke )
    ans_ke.grid(row=9, column=2)
def cel_ke():
    cel=int(kcelsius.get())+273
    ans_cel=Label(root,text=cel)
    ans_cel.grid(row=11, column=2)

def kg_g():
    kg=int(grams.get())*1000
    ans_kg=Label(root,text=kg)
    ans_kg.grid(row=13, column=2)
def g_kg():
    g=int(kgrams.get())/1000
    ans_g=Label(root,text=g)
    ans_g.grid(row=15, column=2)

def l_ml():
    l=int(litres.get())*1000
    ans_l=Label(root,text=l)
    ans_l.grid(row=17, column=2)
def ml_l():
    ml=int(ml.get())/100
    ans_ml=Label(root,text=ml )
    ans_ml.grid(row=19, column=2)
















































but_cm=Button(root, text='Convert>>', command=cm_m)
but_cm.grid(row=1, column=1)
but_m=Button(root, text='Convert>>', command=m_cm)
but_m.grid(row=3, column=1)

but_klm=Button(root, text='Convert>>', command=km_m)
but_klm.grid(row=5, column=1)
but_mkl=Button(root, text='Convert>>', command=m_km)
but_mkl.grid(row=7, column=1)

but_ke=Button(root, text='Convert>>', command=ke_cel)
but_ke.grid(row=9, column=1)
but_cel=Button(root, text='Convert>>', command=cel_ke)
but_cel.grid(row=11, column=1)

but_kg=Button(root, text='Convert>>', command=kg_g)
but_kg.grid(row=13, column=1)
but_g=Button(root, text='Convert>>', command=g_kg)
but_g.grid(row=15, column=1)

but_lit=Button(root, text='Convert>>', command=l_ml)
but_lit.grid(row=17, column=1)
but_ml=Button(root, text='Convert>>', command=ml_l)
but_ml.grid(row=19, column=1)






mainloop()