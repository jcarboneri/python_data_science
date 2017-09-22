from collections import Counter
import json

def amigos_de_amigos_ids(usuario):
    # ada eh uma abreviacao de amigo do amigo
    return [ada["id"]
            for amigo in usuario["amigos"]
            for ada in amigo["amigos"]]
#nao sao a mesma pessoa
def nao_eh_o_mesmo(user, outro_user):
    return user["id"] != outro_user["id"]

def nao_sao_amigos(user, outro_user):
    return all(nao_eh_o_mesmo(amigo, outro_user) for amigo in user["amigos"])

def ids_dos_amigos_dos_amigos(user):
    return Counter( ada["id"]
                    for amigo in user["amigos"]
                    for ada in amigo["amigos"]
                    if nao_eh_o_mesmo(user, ada) and
                    nao_sao_amigos(user, ada) )

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

interesses = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (1, "Spark"), (1, "MongoDB"), (1, "NodeJs"), (1, "Python"),
    (2, "Hadoop"), (2, "MongoDB"), (2, "Coding"), (2, "Debugging"),
    (3, "Python"), (3, "Java"), (3, "NodeJs"), (3, "statistics"),
    (4, "Hadoop"), (4, "NodeJs"), (4, "HBase"), (4, "Java"),
    (5, "Python"), (5, "AI"), (5, "R"), (5, "Java"),
    (6, "Java"), (6, "neural networks"), (6, "Python"), (6, "matematica"),
    (7, "SQL"), (7, "regression"), (7, "probability"), (7, "Cassandra")
]

for usuario in usuarios:
    usuario["amigos"]=[]

for x, y in amizades:
    print(str(usuarios[x]))
    print(str(usuarios[y]))
    print(' ')
    usuarios[x]["amigos"].append(usuarios[y])
    usuarios[y]["amigos"].append(usuarios[x])

def numero_de_amigos(usuario):
    return len(usuario["amigos"])

total_de_conexoes = sum(numero_de_amigos(usuario) for usuario in usuarios)

numero_usuarios = len(usuarios)
media_conexoes = total_de_conexoes / numero_usuarios

num_amigos_por_id = [ (usuario["id"], numero_de_amigos(usuario)) for usuario in usuarios ]

sorted( num_amigos_por_id, key=lambda usuario_id: usuario_id[0], reverse=True )

for user in usuarios:
    #json_get = "{" + str(user) + "}"
    print(json.dumps(str(user), indent=3))
    print(' ')

# Imprime Lista de Amigos com suas quantidades
for X, Y in num_amigos_por_id:
    print( "Usuarios = ID: " + str(X) + " AMIGOS: " + str(Y))

print(str(amigos_de_amigos_ids(usuarios[0])))
print(' ')
print(str(ids_dos_amigos_dos_amigos(usuarios[3])))
