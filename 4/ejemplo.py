class RedSemantica:
    def __init__(self):
        self.relaciones = []

    def agregar_relacion(self, sujeto, relacion, objeto):
        self.relaciones.append((sujeto, relacion, objeto))

    def mostrar_relaciones(self, nodo):
        print(f"Relaciones de '{nodo}':")
        for sujeto, relacion, objeto in self.relaciones:
            if sujeto == nodo:
                print(f"  ({sujeto}) --{relacion}--> ({objeto})")

# Crear red y agregar relaciones
red = RedSemantica()

relaciones = [
    ("FAERUN", "ES UN", "PLANETA"),
    ("FAERUN", "ES HABITADO POR", "SERES VIVOS"),
    ("BALDURS GATE", "ESTA", "FAERUN"),
    ("BALDURS GATE", "ES UNA", "CIUDAD"),
    ("CIUDAD", "TIENE", "tiendas"),
    ("PERSONAJES", "VIVEN", "CIUDAD"),
    ("PERSONAJES", "TIENEN", "CLASE"),
    ("PERSONAJES", "TIENEN", "RAZA"),
    ("PERSONAJES", "TIENEN", "ATRIBUTO"),
    ("PERSONAJES", "USAN", "EQUIPAMIENTO"),
    ("PERSONAJES", "es un", "gale"),
    ("gale", "FORMAN", "FACCIONES"),
    ("FACCIONES", "venden", "tiendas"),
    ("RAZA", "puede ser", "HUMANO"),
    ("RAZA", "puede ser", "elfo"),
    ("CLASE", "tipo", "SPELLCASTER"),
    ("SPELLCASTER", "ES UN", "MAGO"),
    ("MAGO", "USAN", "INTELIGENCIA"),
    ("SPELLCASTER", "USAN", "MAGIA"),
    ("MAGIA", "REPRESENTA", "MISTRA"),
    ("MISTRA", "ES UNA", "DIOS"),
    ("DIOS", "REPRESENTAN", "CONCEPTOS"),
    ("ATRIBUTO", "ES UN", "INTELIGENCIA"),
]

for r in relaciones:
    red.agregar_relacion(*r)

# Ejemplo de uso
red.mostrar_relaciones("PERSONAJES")
