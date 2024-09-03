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



