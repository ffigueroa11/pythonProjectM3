# Lista inicial de nombres
listNombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']


grupoMagos       = ['Harry Houdini', 'David Blaine', 'Teller']
grupoCientificos = ['Newton', 'Hawking', 'Einstein']

listMagos       = [nombre for nombre in listNombres if nombre in grupoMagos]
listCientificos = [nombre for nombre in listNombres if nombre in grupoCientificos]
listOtros       = [nombre for nombre in listNombres if nombre not in grupoMagos and nombre not in grupoCientificos]
"""
print(listMagos)
print(listCientificos)
print(listOtros)
"""
def hacer_grandioso(listMagos):
    largo = len(listMagos)
    for i in range(largo):
        listMagos[i] = 'El gran ' + listMagos[i]


def imprimir_nombres(listNombres):
    for nombre in listNombres:
        print(nombre)

print('*** Lista de Nombres ***')
imprimir_nombres(listNombres)

print('\n*** Lista de Magos ***')
imprimir_nombres(listMagos)
hacer_grandioso(listMagos)
print('\n*** Lista de Magos Modificada ***')
imprimir_nombres(listMagos)
print('\n*** Lista de Cientificos ***')
imprimir_nombres(listCientificos)
print('\n*** Lista de Otros ***')
imprimir_nombres(listOtros)





