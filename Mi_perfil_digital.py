#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Ashlie valeria sánchez cárdenas"
edad = 14
estatura = 1.68
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Ashlie123", "V.aleria_ttw02")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Rojo ", "artista": "J Balvin", "duracion": "4:45"},
{"titulo": "Ella y tu", "artista": "Juan Manuel lebrón", "duracion": "5:06"},
{"titulo": "Con ella remix", "artista": "Kevin florez, Nicky Jam", "duracion": "3:46"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
