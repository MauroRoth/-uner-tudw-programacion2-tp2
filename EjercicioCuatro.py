from Mozo import Mozo

print('4. Una vez codificadas en Python las Clases de los puntos anteriores, instancie los objetos tal como sucede en las siguientes instrucciones:')
print('mozo1 = Mozo("Alfredo")')
print('mozo2 = Mozo("Alfredo")')

mozo1 = Mozo('Alfredo')
mozo2 = Mozo('Alfredo')

print('Luego, responda lo siguiente: ')

print('i.')
print('¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?')
print('Respuesta: No, mozo1 y mozo2 no hacen referencia al mismo objeto. Son dos instancias distintas de la clase Mozo, aunque ambas fueron creadas con el mismo nombre "Alfredo"')
print('Lo verificamos utilizando el operador is, que comprueba si ambos identificadores apuntan al mismo objeto en memoria: ')
print('mozo1 is mozo2 --> ', mozo1 is mozo2)
print('ii.')
print('¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.')
print('Respueta: Sí, los objetos mozo1 y mozo2 son equivalentes en términos de su atributo nombre, ya que ambos tienen el nombre "Alfredo".')
print('Verificamos la equivalencia, comparando los atributos de los objetos:' )
print('mozo1.nombre == mozo2.nombre --> ', mozo1.nombre == mozo2.nombre)
print('iii.')
print('¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?')
print('Respuesta: No, los objetos ligados a mozo1 y mozo2 no comparten la misma posición de memoria. Cada vez que se crea una nueva instancia de una clase, se asigna una nueva posición de memoria para esa instancia.')
print('Verificamos la dirección de memoria de los objetos usando la función id():')
print('id(mozo1) --> ', id(mozo1))
print('id(mozo2) --> ', id(mozo2))


