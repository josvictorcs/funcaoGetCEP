import re
def extrair_cep(endereco):
    molde = re.compile('[0-9]{5}[-]?[0-9]{3}')
    busca = molde.search(endereco)
    if busca:
        cep = busca.group()
        return cep
    else:
        return -1

    #Teste do git

