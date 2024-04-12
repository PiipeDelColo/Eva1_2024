str1 = "vlan es de rango normal"
str2 = "vlan es de rango extendido"
str3 = "Vlan es de rango desconocido"
idvlan = int(input("Ingrese la id de la vlan: "))

if 1 <= idvlan <= 1005:
    print(str1)
    
elif 1006 <= idvlan <= 4095:
    print(str2)
    
else:
    print(str3)
