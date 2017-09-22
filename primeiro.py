usuarios = [
    { "id": 0, "nome": "Juliano" },
    { "id": 1, "nome": "Fulano" },
    { "id": 2, "nome": "Beltrano" },
    { "id": 3, "nome": "Micronano" },
    { "id": 4, "nome": "Juslano" },
    { "id": 5, "nome": "Tanano" },
    { "id": 6, "nome": "Tamonano" },
    { "id": 7, "nome": "Boleano" }
]

amizades =[ (0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7) ]

for usuario in usuarios:
    usuario["amigos"]=[]

for x, y in amizades:
    usuarios[x]["amigos"].append(usuarios[y])
    usuarios[y]["amigos"].append(usuarios[x])

def numero_de_amigos(usuario):
    return len(usuario["amigos"])

total_de_conexoes = sum(numero_de_amigos(usuario) for usuario in usuarios)

numero_usuarios = len(usuarios)
media_conexoes = total_de_conexoes / numero_usuarios

num_amigos_por_id = [ (usuario["id"], numero_de_amigos(usuario)) for usuario in usuarios ]

sorted( num_amigos_por_id, key=lambda usuario_id: usuario_id[0], reverse=True )

# Imprime Lista de Amigos com suas quantidades
for X, Y in num_amigos_por_id:
    print( "Usuarios = ID: " + str(X) + " AMIGOS: " + str(Y))

def amigos_de_amigos_ids(usuario):
    return [ada["id"]
            for amigo in usuario["amigos"]
            for ada in amigo["amigos"]]