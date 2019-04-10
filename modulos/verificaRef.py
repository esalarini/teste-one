import pandas as pd 

def verificaRef(ref):

    arquivo=pd.read_csv('locacao.csv', '\t')

    teste=arquivo.query("refe=="+str(ref))
    if teste.empty==True:
        return ('Referência não cadastrada!')
    else:
        #não sei o que fazer aqui
        #quero a linha para pegar os valores do mural(mura) e do destaque(dest) para retornar eles
        
        return ('No mural')

def pegarRef():
    arquivo=pd.read_csv('locacao.csv', '\t')
    return (arquivo.refe)