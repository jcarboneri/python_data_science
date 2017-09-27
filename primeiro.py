# -----------------------------------------------------------------------------
# Data Science
#
# Estudos
# Juliano Carboneri Francisco
# -----------------------------------------------------------------------------
from collections import Counter
from collections import defaultdict
import json

# Definicao procedure
# nome: amigos_de_amigos_ids
# retorna array com id de amigos de amigos
#
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

# Tabela de Usuarios
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

# Relacionamento de amizades, por IDs
amizades =[ (0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (0, 7), (3, 1) ]

# Tabela de interesses
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

salario_e_experiencia = [   (10000, 8.7), (11000, 8.1),
                            (15000, 7.1), (7600, 5),
                            (18000, 8.4), (25000, 9.1),
                            (5000, 4.8) ]

# Cria campo "amigos" nos dicts de usuarios (para cada usuario)
for usuario in usuarios:
    usuario["amigos"]=[]

# Faz um novo append para cada usuario que é amigo de X
for x, y in amizades:
    #print(str(usuarios[x]))
    #print(str(usuarios[y]))
    #print(' ')
    usuarios[x]["amigos"].append(usuarios[y])
    usuarios[y]["amigos"].append(usuarios[x])

# Devolve quantos amigos o usuario tem
def numero_de_amigos(usuario):
    return len(usuario["amigos"])

# funcao que encontra usuarios com mesmo interesse
def cientistas_de_dados_que_gostam(interesse_alvo):
    return [user_id
            for user_id, user_interesse in interesses
            if user_interesse == interesse_alvo]


# chaves sao interesses, valores sao listas com user_ids com interesses
user_ids_por_interesses = defaultdict(list)
for user_id, interesse in interesses:
    user_ids_por_interesses[interesse].append(user_id)

# agora interesse por user_id
interesse_por_user_id = defaultdict(list)
for user_id, interesse in interesses:
    interesse_por_user_id[user_id].append(interesse)

# cria tupla com interesse comuns por usuarios
# com esta informacao poderia criar um metodo a mais de cientistas de dados que voce poderia conhecer e trocar mais informacoes
def interesses_mais_comuns(usuario):
    return Counter( interesse_por_user_id
                    for interesse in interesse_por_user_id[usuario["id"]]
                    for interesse_por_user_id in user_ids_por_interesses[interesse]
                    if interesse_por_user_id != usuario["id"])

for usuario in usuarios:
    print ("Interesse comuns " + str(usuario["id"]) + " ==> " + str(interesses_mais_comuns(usuario)))

# Soma todos os valores de amigos para cada usuario
total_de_conexoes = sum(numero_de_amigos(usuario) for usuario in usuarios)

# Pega o valor de numero de usuarios
numero_usuarios = len(usuarios)

# Media de total de conexoes por numero de usuarios
media_conexoes = total_de_conexoes / numero_usuarios

# Faz um array com o valor do ID do Usuario e quantos amigos ele tem
num_amigos_por_id = [ (usuario["id"], numero_de_amigos(usuario)) for usuario in usuarios ]
# mostra o array/tupla
for x, y in num_amigos_por_id:
    print("ID: " + str(x) + " tem " + str(y) + "amigo(s)")

# Ordena o num_amigos_por_id
sorted( num_amigos_por_id, key=lambda usuario_id: usuario_id[0], reverse=True )

#for user in usuarios:
    #json_get = "{" + str(user) + "}"
    #print(json.dumps(str(user), indent=3))
    #print(' ')

for usuario in usuarios:
    print("AMIGO DO AMIGO IDS = " + str(amigos_de_amigos_ids(usuario)))
print(' ')

for usuario in usuarios:
    print("ID dos amigos do amigo = " + str(usuario["id"]) + " --> " + str(ids_dos_amigos_dos_amigos(usuario)))


# -------------------------------------------
# Analise sobre os salarios
# -------------------------------------------

salario_por_experiencia = defaultdict(list)

for salario, experiencia in salario_e_experiencia:
    salario_por_experiencia[experiencia].append(salario)

media_salario_por_experiencia = {
    experiencia : sum(salarios) / len(salarios)
    for experiencia salarios in salario_por_experiencia.items()
}
