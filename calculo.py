import math

def calcularPotencial(Vo, m, p):
    V = []
    for k in range(0, int(m)):
        V.insert(k, [])
        for j in range(0, int(m)):
            val = 0.5*float(Vo) 
            if  j == 0 or  j == int(m)-1 or  k == int(m)-1:
                val = 0 
            if k == 0:
                val = float(Vo)
            V[k].insert(j, val)
    
    delta = 0
    i = 1

    while True:
        print("i: " + str(i))
        i += 1
        if(i == 5000):
            return V
        for k in range(1, int(m)-1):
            for j in range(1, int(m)-1):
                newVal = (V[k+1][j] + V[k-1][j] + V[k][j+1] + V[k][j-1])/4
                cambio = math.fabs((newVal - V[k][j])/V[k][j])
                if cambio > delta:
                    delta = cambio
                V[k][j] = newVal
        print("Delta: " + str(delta) )
        if delta <= float(p):
            break
        
    return V