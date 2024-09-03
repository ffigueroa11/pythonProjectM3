# Lista inicial de nombres
listNombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']


grupoMagos       = ['Harry Houdini', 'David Blaine', 'Teller']
grupoCientificos = ['Newton', 'Hawking', 'Einstein']

listMagos       = [nombre for nombre in listNombres if nombre in grupoMagos]
listCientificos = [nombre for nombre in listNombres if nombre in grupoCientificos]
listOtros       = [nombre for nombre in listNombres if nombre not in grupoMagos and nombre not in grupoCientificos]

print(listMagos)
print(listCientificos)
print(listOtros)



def hacer_grandioso(lista):
    largo = len(lista)
    for i in range(largo):
        lista[i] = 'El gran ' + lista[i]
    return lista

listMagosMod = hacer_grandioso(listMagos)

print(listMagosMod)


