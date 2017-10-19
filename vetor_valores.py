def obter_vetor_valores(num_servidores, id_servidor):
    vetor = ["-"] * num_servidores
    vetor[id_servidor-1] = 0
    return vetor
