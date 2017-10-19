def obter_vetor_valores(num_servidores, id_servidor):
    vetor = ["-"] * num_servidores
    vetor[id_servidor - 1] = 0
    return vetor


def atualiza(vetor_local, outro_vetor):
    for i in range(len(vetor_local)):
        if outro_vetor[i] != "-":
            vetor_local[i] = outro_vetor[i]
    return vetor_local
