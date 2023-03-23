COLORES = {
    'NEGRO' : {
        'valor' : 0,
        'nombre' : 'NEGRO',
        'multiplicador' : 1
        },
    'CAFE' : {
        'valor' : 1,
        'nombre' : 'CAFE',
        'multiplicador' : 10
        },
    'ROJO' : {
        'valor' : 2,
        'nombre' : 'ROJO',
        'multiplicador' : 100
        },
    'NARANJA' : {
        'valor' : 3,
        'nombre' : 'NARANJA',
        'multiplicador' : 1000
        },
    'AMARILLO' : {
        'valor' : 4,
        'nombre' : 'AMARILLO',
        'multiplicador' : 10000
        },
    'VERDE' : {
        'valor' : 5,
        'nombre' : 'VERDE',
        'multiplicador' : 100000
        },
    'AZUL' : {
        'valor' : 6,
        'nombre' : 'AZUL',
        'multiplicador' : 1000000
        },
    'VIOLETA' : {
        'valor' : 7,
        'nombre' : 'VIOLETA',
        'multiplicador' : 10000000
        },
    'GRIS' : {
        'valor' : 8,
        'nombre' : 'GRIS',
        'multiplicador' : 100000000
        },
    'BLANCO' : {
        'valor' : 9,
        'nombre' : 'BLANCO',
        'multiplicador' : 1000000000
        }
}

TOLERANCIA = {
    'DORADO' : {
        'nombre' : 'Dorado',
        'valor' :  0.5,
    },
    'PLATA' : {
        'nombre' : 'Plateado',
        'valor' :  0.10,
    },
}

def CalcularResistencias(Banda1, Banda2, Multiplicador, Tolerancia):
    OhmPromedio = ((Banda1 * 10) + Banda2) * Multiplicador
    OhmMas = OhmPromedio + (OhmPromedio * Tolerancia)
    OhmMenos = OhmPromedio - (OhmPromedio * Tolerancia)
    return 'La resistencia se calcula entre {menos} y {mas} Ohms.'.format({'menos' : OhmMenos, 'mas' : OhmMas})