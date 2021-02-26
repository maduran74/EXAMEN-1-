# Tu nombre: Mauricio Duran 
# Tu Carnet: 20181120230


def sonPanas(a,b):
    
        s = 0
        for x in range(1,a):
            if a%x == 0:
                s= s+x
        t = 0
        for x in range(1,b):
            if b%x == 0:
                t= t+x
        #comparo
        if s==b and t==a and a!=b:
            return True
        else: 
            return False

def suma_de_numeros_panas(p):
    count=0
    for x in range(1,p):
      for w in range(x,p):
          if sonPanas(w,x) == True:
              print(w,x)
              count= count+1
              
    print(count)
              
suma_de_numeros_panas(500)