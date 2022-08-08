print("=========================")
print("EJERCICIO 1")
print("Si k(n) = 1000 y la penalización 6400")
print("=========================")


n = 0
cdem = 500
cmdp = 100
penalizacion = 6400

#Recoge los valores de penalización, costo marginal y costo de encender la maquina
kx = cdem / cmdp
vp = penalizacion / cmdp
min = 0
#Se calcula

print("El costo mínimo esperado es de " +str(vp)+ " en la etapa 4")
print("=========================")
print("Ahora calculamos la etapa 3, usando de penalización " +str(vp))
print("=========================")

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")
if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ "productos en la etapa 3")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 3")
print("=========================")
print("Ahora calculamos la etapa 2, usando de penalización " +str(vm))
print("=========================")

vp = vm
vm = 0
varm = 0
varm1 = 0
min == 0

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")

if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ "productos en la etapa 2")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 2")
print("=========================")
print("Ahora calculamos la etapa 1, usando de penalización " +str(vm))
print("=========================")

vp = vm
vm = 0
varm = 0
varm1 = 0
min == 0

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")

if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " productos en la etapa 1")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 1")

print("=========================")
print("Por tanto, el costo final esperado si se sigue esta política es el valor mínimo de " +str(vm)+ " unidades")

#--------------------------------------------------------------------------------------------------

print("=========================")
print("EJERCICIO 2")
print("Si k(n) = 600, la penalización 3000 y costo marginal 150")
print("=========================")


n = 0
cdem = 600
cmdp = 150
penalizacion = 3000

kx = cdem / cmdp
vp = penalizacion / cmdp
min = 0

print("El costo mínimo esperado es de " +str(vp)+ " en la etapa 4")
print("=========================")
print("Ahora calculamos la etapa 3, usando de penalización " +str(vp))
print("=========================")

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")
if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ "productos en la etapa 3")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 3")
print("=========================")
print("Ahora calculamos la etapa 2, usando de penalización " +str(vm))
print("=========================")

vp = vm
vm = 0
varm = 0
varm1 = 0
min == 0

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")

if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ "productos en la etapa 2")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 2")
print("=========================")
print("Ahora calculamos la etapa 1, usando de penalización " +str(vm))
print("=========================")

vp = vm
vm = 0
varm = 0
varm1 = 0
min == 0

for var in range (0,10):
    if var == 0:
        min = vp
        vm = min
        varm = var
    else:
        min = kx + var + (1/2**var) * (vp)
        if min < vm:
            vm = min
            varm = var
        else:
            if min == vm:
                varm1 = var
    print("Para Xn valor de " +str(var)+ " el valor es de " +str(min)+ " unidades")

if(varm1 == 0):
    print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " productos en la etapa 1")
else:
    if(varm1 != 0):
        print("El costo mínimo esperado es de " +str(vm)+ " produciendo " +str(varm)+ " o " +str(varm1)+ " productos en la etapa 1")

print("=========================")
print("Por tanto, el costo final esperado si se sigue esta política es el valor mínimo de " +str(vm)+ " unidades")