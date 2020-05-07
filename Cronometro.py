#Ejercicio Cronometro
"""Integrantes: Maria Fernanda Uribe Hernandez - 20172020110
                Yeimer Serrano Navarro         - 20181020060
                Juan David Rosero Torres       - 20181020071
"""

from tkinter import *
from tkinter.font import Font
import time

global continuar
continuar=True
global seg
seg=0
global mili
mili=0

class interfaz:
    def iniciarCronometro(self):
         global continuar
         continuar=True
         self.tick()
    def detenerCronometro(self):
        global continuar
        continuar=False
    def reiniciarCronometro(self):
         global continuar
         continuar= False
         self.text.set("00:00:00:00")
         global seg
         seg=0
    def tick(self):
        global continuar
        global seg
        if(continuar):  
            global mili
            if(mili==10):
                seg +=1
                mili=0
            self.text.set(self.controlador.get(seg)+":"+str(mili))
            mili +=1
            if(continuar):
                self.root.after(95,self.tick)
        
    def  __init__(self):
        self.controlador = Cronometro()
        self.root= Tk()
        self.root.title("Cronometro")     #Ponerle el nombre a la ventana
        self.root.geometry("350x100")
        self.root.resizable(False,False)
        self.text = StringVar()
        self.text.set("00:00:00:00")
        self.myFont =Font(family="Times New Roman", size=18)
        self.etiqueta = Label(self.root,textvariable=self.text)
        self.etiqueta.pack()
        self.etiqueta.configure(font=self.myFont)
        self.btnReiniciar = Button(self.root,text="Reiniciar",fg="Blue",command= self.reiniciarCronometro).place(x=10,y=70,height=20,width=80) 
        self.btnIniciar = Button(self.root,text="Iniciar",fg="Green",command= self.iniciarCronometro).place(x=130,y=70,height=20,width=80) 
        self.btnParar = Button(self.root,text="Parar",fg="red",command= self.detenerCronometro).place(x=250,y=70,height=20,width=80)  
    

class tiempo:
   def __init__(self,n):
       self.tiempo_seg=time.gmtime(n)
     

class horas(tiempo):      
   def __init__(self,n):
      tiempo.__init__(self, n)
      self.get()    
   def get(self):
       return (time.strftime("%H",self.tiempo_seg ))
   
class minutos(tiempo):  
   def __init__(self,n):
      tiempo.__init__(self, n)
      self.get()
   def get(self):
       return (time.strftime("%M",self.tiempo_seg ))
   
class segundos(tiempo):  
   def __init__(self,n):
      tiempo.__init__(self, n)
      self.get()
   def get(self):
       return (time.strftime("%S",self.tiempo_seg ))
   
   
class Cronometro():
   def get(self,j):
           t=segundos(j)
           s= t.get()
           t=minutos(j)
           m= t.get()
           t=horas(j)
           h= t.get()  
           self.aux=h+":"+m+":"+s
           return self.aux    
       

App=interfaz()
App.root.mainloop()  #Mantiene la ventana abierta
