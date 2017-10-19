def obter_relogio_vetorial(num_servidores):
    return [0] * num_servidores


def incrementar(relogio_vetorial, indice):
    relogio_vetorial[indice - 1] += 1
    return relogio_vetorial


def atualizar(relogio_local, outro_relogio):
    for i in range(len(relogio_local)):
        relogio_local[i] = max(relogio_local[i], outro_relogio[i])
    return relogio_local


def eh_anterior(relogio_local, outro_relogio):
    retorno = False
    for i in range(len(relogio_local)):
        if relogio_local[i] < outro_relogio[i]:
            retorno = True
            break
    return retorno

# def eh_concorrente(relogio_local, outro_relogio):
#     return not eh_anterior(relogio_local, outro_relogio) and not eh_anterior(outro_relogio, relogio_local)
