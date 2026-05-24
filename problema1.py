# programa-python
Solución del Problema 1 - Fase 5 Evaluación Final POA
# Matriz con datos de sesiones
sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 300, 15],
    [105, 80, 1]
]

# Función para clasificar compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"

# Informe final
print("INFORME DE COMPROMISO")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente,
          "| Clasificación:", clasificacion)
