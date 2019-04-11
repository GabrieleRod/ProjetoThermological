S = input("Substância: ")
m = float(input("Massa(em g): "))
a = int(input("Temperatura inicial(em °C): "))
h = int(input("Temperatura final (em °C): "))
d = int(input("Temperatura de fusão/solidificação (em °C): "))
f = int(input("Temperatura de ebulição/condensação (em °C): "))      
N = "="*77
print(N)
D = input("Potência ou Quantidade de Calor? ")

A = ["Quantidade de Calor", "quantidade de calor", "Quantidade de calor"] 
B = ["Potência", "potência"]
C = ["Quantidade de Calor", "quantidade de calor", "Quantidade de calor", "Potência", "potência"]

while D not in C:
    D = input("Potência ou Quantidade de Calor? ")
                                                                              #Fórmulas: 
if D in A:                                                                                                                                              
    if a < d:                                                           #c = (Q) /(m *(Tf - Ti))      c = (P * t) /(m *(Tf - Ti))                
        print(N)                                                        #L = (Q) / m                  L = (P * t) / m
        print("Fase: Sólida")
        if h >= f:
            cs = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(d - a))
        
            print(N)
            print("Mudança de Fase: Fusão")
            Lf = (float(input("Quantidade de calor recebida (em cal): ")))/ m

            print(N)
            print("Fase: Líquida")
            cl = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(f - d))

            print(N)
            print("Mudança de Fase: Ebulição")
            Le = (float(input("Quantidade de calor recebida (em cal): ")))/ m

            print(N)
            print("Fase: Gasosa")
            cg = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - f))

            print(N)
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            print("Calor latente de fusão: {:.1f} cal/g".format(Lf))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor eatente de ebulição: {:.1f} cal/g".format(Le))
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
        elif d <= h < f:
            cs = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(d - a))

            print(N)
            print("Mudança de Fase: Fusão")
            Lf = (float(input("Quantidade de calor recebida (em cal): ")))/ m

            print(N)
            print("Fase: Líquida")
            cl = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - d))
        
            print(N)
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            print("Calor latente de fusão: {:.1f} cal/g".format(Lf))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
        else:
            if h > a:
                cs = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - a))

                print(N)
                print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            elif h < a:
                cs = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(h - a))

                print(N)
                print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))

    elif d <= a < f:
        print(N)
        print("Fase: Líquida")
        if h >= f:
            cl = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(f - a))
            
            print(N)
            print("Mudança de Fase: Ebulição")
            Le = (float(input("Quantidade de calor recebida (em cal): ")))/ m

            print(N)
            print("Fase: Gasosa")
            cg = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - f))
        
            print(N)
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de ebulição: {:.1f} cal/g".format(Le))
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
        elif d <= h < f:
            if h > a:
                cl = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - a))

                print(N)
                print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            elif h < a:
                cl = (-(float(input("Quantidade de calor cedida (em cal): ")))/(m *(h - a)))

                print(N)
                print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
        else:
            cl = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(d - a))
                
            print(N)
            print("Mudança de Fase: Solidificação")
            Ls = (-(float(input("Quantidade de calor cedida (em cal): "))))/ m

            print(N)
            print("Fase: Sólida")
            cs = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(h - d))

            print(N)
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de solidificação: {:.1f} cal/g".format(Ls))
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))

    else:
        print(N)
        print("Fase: Gasosa")
        if h >= f:
            if h > a:
                cg = (float(input("Quantidade de calor recebida (em cal): ")))/(m *(h - a))
        
                print(N)
                print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            elif h < a:
                cg = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(h - a))
        
                print(N)
                print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
        elif d <= h < f:
            cg = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(f - a))

            print(N)
            print("Mudança de Fase: Condensação")
            Lc = (-(float(input("Quantidade de calor cedida (em cal): "))))/ m

            print(N)
            print("Fase: Líquida")
            cl = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(h - f))

            print(N)
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            print("Calor latente de condensação: {:.1f} cal/g".format(Lc))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
        else:
            cg = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(f - a))
            
            print(N)
            print("Mudança de Fase: Condensação")
            Lc = (-(float(input("Quantidade de calor cedida (em cal): "))))/ m

            print(N)
            print("Fase: Líquida")
            cl = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(d - f))     
  
            print(N)
            print("Mudança de Fase: Solidificação")                    
            Ls = (-(float(input("Quantidade de calor cedida (em cal): "))))/ m  

            print(N)                                                     
            print("Fase: Sólida")   
            cs = (-(float(input("Quantidade de calor cedida (em cal): "))))/(m *(h - d))

            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            print("Calor latente de condensação: {:.1f} cal/g".format(Lc))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de solidificação: {:.1f} cal/g".format(Ls))
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))

            
elif D in B :                              
    print(N)
    P = (float(input("Potência (em W): ")))/4
    if a < d:
        print(N)
        print("Fase: Sólida")
        b = (int(input("Tempo (em minutos): ")))*60
        if h >= f:
            cs = (P * b)/(m *(d - a))
            
            print(N)
            print("Mudança de Fase: Fusão")
            Lf = (P * (int(input("Tempo (em minutos): ")))*60)/ m

            print(N)
            print("Fase: Líquida")
            cl = (P * (int(input("Tempo (em minutos): ")))*60)/(m *(f - d))

            print(N)
            print("Mudança de Fase: Ebulição")
            Le = (P * (int(input("Tempo (em minutos): ")))*60)/ m 

            print(N)
            print("Fase: Gasosa")
            cg = (P * (int(input("Tempo (em minutos): ")))*60)/(m *(h - f))

            print(N)
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            print("Calor latente de fusão: {:.1f} cal/g".format(Lf))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor eatente de ebulição: {:.1f} cal/g".format(Le))
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))    
        elif d <= h < f:
            cs = (P * b)/(m *(d - a))
            
            print(N)
            print("Mudança de Fase: Fusão")
            Lf = (P * (int(input("Tempo (em minutos): ")))*60)/ m

            print(N)
            print("Fase: Líquida")
            cl = (P * (int(input("Tempo (em minutos): ")))*60)/(m *(h - d))
        
            print(N)
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            print("Calor latente de fusão: {:.1f} cal/g".format(Lf))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
        else:
            if h > a:
                cs = (P * b)/(m *(h - a))

                print(N)
                print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
            elif h < a:
                cs = (-(P * b))/(m *(h - a))

                print(N)
                print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
        
    elif d <= a < f:
        print(N)
        print("Fase: Líquida")
        g = (int(input("Tempo (em minutos): ")))*60
        if h >= f:
            cl = (P * g)/(m *(f - a))
            
            print(N)
            print("Mudança de Fase: Ebulição")
            Le = (P * (int(input("Tempo (em minutos): ")))*60)/ m

            print(N)
            print("Fase: Gasosa")
            cg = (P * (int(input("Tempo (em minutos): ")))*60)/(m *(h - f))            
        
            print(N)
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de ebulição: {:.1f} cal/g".format(Le))
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
        elif d <= h < f:
            if h > a:
                cl = (P * g)/(m *(h - a))

                print(N)
                print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            elif h < a:
                cl = (-(P * g))/(m *(h - a))

                print(N)
                print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))

        else:
            cl = (-(P * g))/(m *(d - a))
            
            print(N)
            print("Mudança de Fase: Solidificação")
            Ls = (-(P * (int(input("Tempo (em minutos): ")))*60))/ m

            print(N)
            print("Fase: Sólida")
            cs = (-(P * (int(input("Tempo (em minutos): ")))*60))/(m *(h - d))

            print(N)
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de solidificação: {:.1f} cal/g".format(Ls))
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
        
    else:
        print(N)
        print("Fase: Gasosa")
        k = (int(input("Tempo (em minutos): ")))*60
        if h >= f:
            if h > a:
                cg = (P * k)/(m *(h - a))
        
                print(N)
                print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            elif h < a:
                cg = (-(P * k))/(m *(h - a))
        
                print(N)
                print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
        elif d <= h < f:
            cg = (-(P * k))/(m *(f - a))
            
            print(N)
            print("Mudança de Fase: Condensação")
            Lc = (-(P * (int(input("Tempo (em minutos): ")))*60))/ m

            print(N)
            print("Fase: Líquida")
            cl = (-(P * (int(input("Tempo (em minutos): ")))*60))/(m *(h - f))

            print(N)
            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            print("Calor latente de condensação: {:.1f} cal/g".format(Lc))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
        else:
            cg = (-(P * k))/(m *(f - a))
            
            print(N)
            print("Mudança de Fase: Condensação")
            Lc = (-(P * (int(input("Tempo (em minutos): ")))*60))/ m

            print(N)                                                                  
            print("Fase: Líquida")
            cl = (-(P * (int(input("Tempo (em minutos): ")))*60))/(m *(d - f))               
                                                                                        
            print(N)                                                                  
            print("Mudança de Fase: Solidificação")                                                        
            Ls = (-(P * (int(input("Tempo (em minutos): ")))*60))/ m                    
                                                                                       
            print(N)                                                     
            print("Fase: Sólida")   
            cs = (-(P * (int(input("Tempo (em minutos): ")))*60))/(m *(h - d))

            print("Calor específico do estado gasoso: {:.1f} cal/g°C".format(cg))
            print("Calor latente de condensação: {:.1f} cal/g".format(Lc))
            print("Calor específico do estado líquido: {:.1f} cal/g°C".format(cl))
            print("Calor latente de solidificação: {:.1f} cal/g".format(Ls))
            print("Calor específico do estado sólido: {:.1f} cal/g°C".format(cs))
