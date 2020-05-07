import time
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
    
    
class cronometro():
    def get(self,j):
            t=segundos(j)
            s= t.get()
            t=minutos(j)
            m= t.get()
            t=horas(j)
            h= t.get()  
            self.aux=h+":"+m+":"+s
            return self.aux    

class controlador():
    def __init__(self,n):
        self.n=n
        self.crono=cronometro()
    
    def get(self):
        return self.crono.get(n)
   
    
        

    