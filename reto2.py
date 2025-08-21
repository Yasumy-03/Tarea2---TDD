#Test primero : mostrar test que falla 
#es_par(4)  # True
#es_par(5) # False

# Codigo minimo: funcion que pasa el test
def es_par(numero):
    return numero % 2 == 0

# Casos de prueba
print(es_par(4))  # True
print(es_par(5))  # False
