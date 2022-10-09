


from cmath import exp
import functools
import itertools
import operator
# FICHA 1


def le_ficheiro(ficheiro):
    """Imprime cada linha no ficheiro

    Args:
        ficheiro (str): ficheiro a ser lido
    """
    counter = 1
    with open(ficheiro) as f:
        for linha in f:
            print(str(counter) + " " + linha, end=" ")
            counter += 1


def escreve_ficheiro():
    """Escreve no ficheiro ex4.txt tudo o que o user escrever como input.
    """
    with open('ex4.txt', 'w') as f:
        x = input("Escreva uma frase")
        while x != "":
            x = input("Escreva uma frase")
            f.write(x + ' ')


def copia_ficheiro(ficheiro1, ficheiro2):
    """Copia conteúdo do ficheiro 1 para o ficheiro2

    Args:
        ficheiro1 (str): Ficheiro a ser copiado
        ficheiro2 (str): Ficheiro para onde vai ser copiado o conteudo
    """
    with open(ficheiro1) as f1, open(ficheiro2, 'w') as f2:
        for linha in f1:
            f2.write(linha)


def copia_ficheiro_maiusculas(ficheiro1, ficheiro2):
    """Copia o conteudo do ficheiro 1 para o ficheiro dois em letras maiusculas

    Args:
        ficheiro1 (str): ficheiro a ser copiado
        ficheiro2 (str): ficheiro para onde vai ser copiado o conteudo
    """
    with open(ficheiro1) as f1, open(ficheiro2, 'w') as f2:
        for linha in f1:
            f2.write(linha.upper())


def conta_linhas(ficheiro):
    """Conta as linhas de um ficheiro de txt

    Args:
        ficheiro (str): ficheiro a ler

    Returns:
        int: numero de linhas no ficheiro
    """
    counter = 0
    with open(ficheiro) as f:
        for linha in f:
            counter += 1
    return counter


def conta_linhas_com_string(ficheiro, texto):
    """conta as ocorrencias de "texto" no ficheiro

    Args:
        ficheiro (str): ficheiro a ler
        texto (str): string que se pretende contar

    Returns:
       int: numero de ocorrencias do texto no ficheiro
    """
    counter = 0
    with open(ficheiro) as f:
        for linha in f:
            if linha.strip() == texto:  # temos de usar o .strip() porque senão vai contas com os /n
                counter += 1
    return counter


def conta_linhas_caracteres(ficheiro):
    """Conta o numero de linhas e caracteres num ficheiro de texto

    Args:
        ficheiro (str): ficheiro a ler

    Returns:
        tuple: par de linhas e caracteres
    """
    caracteres = 0
    with open(ficheiro) as f:
        for linha in f:
            caracteres += len(linha.strip())
    return (conta_linhas(ficheiro), caracteres)


def lista_floats(lista):
    res = []
    for ele in lista:
        try:
            res.append(float(ele))
        except ValueError:
            return "linha mal formada"
    return res


def media(lista):
    try:
        return media(lista)
    except ValueError:
        return "linha vazia"


def imprime_medias(ficheiro):
    with open(ficheiro) as f:
        for linha in f:
            print(media(lista_floats(linha.split())))


def principal():
    temps = input('Insira um ficheiro de temperaturas')
    with open(temps) as f:
        try:
            return imprime_medias(f)
        except IOError:
            return 'ERRO'


def salta_comentario(ficheiro):
    with open(ficheiro, encoding="utf8") as f:
        for linha in f:
            if not linha.startswith('#'):
                return linha

# ---------------------------------------------------------------------------
# FICHA 2

# Exercicio 1


def conjunto_linhas(ficheiro, aString):
    conjunto = set()
    with open(ficheiro, encoding="utf8") as f:
        for linha in f:
            if aString in linha:
                conjunto.add(linha)
    return conjunto


# Exericio 2

def conjunto_algumas_linhas(ficheiro, coisas):
    conjunto = set()
    with open(ficheiro, encoding='utf8') as f:
        for linha in f:
            for i in coisas:
                if i in linha:
                    conjunto.add(linha)
    return conjunto


# Exercicio 3 - não sei fazer

# def conjunto_algumas_linhas(ficheiro, coisas):
#     conjunto = set()
#     with open(ficheiro, encoding='utf8') as f:
#         for linha in f:
#             for i in coisas:
#                 if (sum(i in linha) >= 2) == True:
#                     conjunto.add(linha)
#     return conjunto


# Exercicio 4

def le_palavras(ficheiro):
    conjunto = set()

    with open(ficheiro, encoding='utf8') as f:
        for linha in f:
            for palavra in linha.rstrip().split(" "):
                conjunto.add(palavra)
    return conjunto


# Exercicio 5

def conta_ocorrencias(ficheiro1, ficheiro2):
    palavras = le_palavras(ficheiro2)
    res = dict()
    with open(ficheiro1, encoding='utf8') as f:
        for linha in f:
            for palavra in linha.rstrip().split(" "):
                if palavra in palavras and palavra in res:
                    # se a palavra já estiver no dicionario, conta +1 ocorrencia
                    res[palavra] = res[palavra] + 1
                elif palavra in palavras and palavra not in res:
                    # se a palavra estiver na lista de palavras mas não estiver no dicionario, adicionamos a palavra ao dicionario com contagem 1
                    res[palavra] = 1
    return res  # não consigo ordernar isto alfabeticamente mas o que interessa é que funciona


# Exercicio 9
def linha_para_elemento(ficheiro, linha):

    with open(ficheiro, encoding='utf8') as f:
        linhas = f.readlines()
        # aqui criamos uma lista com os diferentes valores que queremos por no dicionario
        separar = linhas[linha].strip().split(" ")

        dicionario = {
            'nome': separar[0],
            'atomico': int(separar[1]),
            'densidade': float(separar[2])
        }

    return dicionario


# Exercicio 10

def elemento_para_string(dicionario):
    return 'nome: ' + dicionario['nome'] + " " + 'atomico:' + str(dicionario['atomico']) + " " + 'densidade: ' + str(dicionario['densidade'])


# Exercicio 11

def escrever_elementos(dicionarios, ficheiro):
    with open(ficheiro, 'w', encoding='utf8') as f:
        for i in dicionarios:
            f.write(elemento_para_string(i) + '\n')


# ---------------------------------------------------------------------------
# FICHA 6 - Funções de ordem superior

# exercicio 1 e 2
def testeLambdas():

    a = lambda x: 2*x
    b = lambda i: i[0]
    c = lambda x,y: 3*(x + y)
    d = lambda x,y,z: x*y*z
    e = lambda l1,l2: l1 + l2
    f = lambda l: l[:len(l) // 2]
    h = lambda lista: lista not in [' ', '\t', '\n']



# exercicio 3
# 3. Qual o valor de cada expressão?
# (a) map(lambda x: x + 1, range(1, 4)) --> [2, 3, 4]
# (b) map(lambda x: x > 0, [3, -5, -2, 0]) --> [True, False, False, False]
# (c) filter(lambda x: x > 5, range(1, 7)) --> [6]
# (d) filter(lambda x: x % 2 == 0, range(1, 11)) --> [2, 4, 6, 8, 10]
# (e) filter(lambda x: x > 0, map(lambda y: y ** 2, range(-3, 4))) --> [9, 4, 1, 1, 4, 9]
# (f) map(lambda x: x ** 2, filter(lambda x: x > 0, range(-3, 4)))--> [1, 4, 9]
# (g) map(lambda x: x + 's', ['As', 'armas', 'e', 'os', 'barões']) --> ['Ass', 'armass', 'es', 'oss', 'barõess']
# (h) map(lambda x: 's' + x, ['As', 'armas', 'e', 'os','barões']) --> ['sAs', 'sarmas', 'se', 'sos', 'sbarões']
# (i) map(lambda x: map(lambda y: y * y, x), [[1, 2], [3, 4, 5]])


# exercicio 4

def mapa_seletivo_a(funcao, predicado, iteravel):
    return [funcao(x) for x in iteravel if predicado(x)]


def prob4b(predicado, funcao, iter):
    return map(predicado, filter(funcao, iter))


#exercicio 9

def zip_rewritten(listA, listB):
    return list(map(lambda x, y: (x,y), listA, listB))

    
#exercicio 10
 
# (a) reduce(operator.mul, range(-3, 0, 1), 1) --> -6 
# (b) reduce(operator.mul, range(-3, 0, -1), 1) --> 1
# (c) reduce(operator.sub, [1, 2, 3]) --> -4 






#EXAME TIPO 

#grupo 2 


  
def crescente(lista):
    """_summary_

    Args:
        lista (_type_): _description_

    Returns:
        _type_: _description_
    """
    return sorted(lista, key=lambda x: x[1])


def crescente2(lista):
    """_summary_

    Args:
        lista (_type_): _description_
    """
    return sorted(lista, key=lambda x: (x[1],x[0]))


def max_em_intervalo(funcao,intervalo):
    return max(list(map(funcao, [i for i in range(intervalo[0],intervalo[1] + 1)])))


import matplotlib.pyplot as plt  # http://matplotlib.org/api/pyplot_api.html
import numpy as np  # http://www.numpy.org/
import math
import csv


def grafico():
    x = (1,2,3,4,5,6)
    y = (2,3,10,4,3,6)
    plt.plot(x,y)
    plt.xlabel("abcissas")
    plt.ylabel("ordenadas")
    plt.title("O meu gráfico preferido")
    plt.show()


def menor_stock(ficheiro, limite = ','):
    
    with open(ficheiro, 'r') as csv_file:
        linhas = csv.reader(csv_file, delimiter=limite)
        lista = list(linhas)
        return sorted(lista, key = lambda x: x[1])[0]
    

# --------------------------------------------------------------------------- #
# FICHA 7 - Ficheiros CSV (separados por virgulas)

#Funções auxiliares

def ler_csv(nome_ficheiro):
    """Ler um ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[list][str]: O conteúdo do ficheiro. 
            Cada elemento da lista contém uma linha do ficheiro CSV.
            Cada string corresponde a um valor no ficheiro CSV.
    """
    with open(nome_ficheiro, 'r') as ficheiro_csv:
        return list(csv.reader(ficheiro_csv))


def escrever_em_ficheiro(ficheiro, algo):
    """Escrever algo num ficheiro

    Args:
        ficheiro (str): O nome do ficheiro onde escrever
        algo (any): O que escrever no ficheiro
    """
    with open(ficheiro, 'w') as f:
        f.write(str(algo))


def escrever_csv(nome_ficheiro, iterador_de_iteradores, separador=','):
    """Escrever um iterador de iteradores num ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro
        iterador_de_iteradores (iter[iter]): O iterador
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = csv.writer(ficheiro_csv, delimiter=separador)
        for linha in iterador_de_iteradores:
            escritor.writerow(linha)


def imprimir_csv_dicionario(nome_ficheiro):
    """Imprimir no ecrã o conteudo de um ficheiro CSV.
    Cada linha do ficheiro aparece em forma de dicionário.
    As chaves do dicionário são lidas da 1a linha do ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv)
        for linha in leitor:
            print(linha)


def ler_csv_dicionario(nome_ficheiro, cabecalho=None):
    """Ler um ficheiro CSV. O ficheiro pode ou não ter cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro
        fieldnames (list[str], optional):  A lista com o nomes das colunas.
            Utilizar quando o ficheiro não tiver cabeçalho. Defaults to None.

    Returns:
        list[dict]: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro
            ou tiradas da lista cabeçalho.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv, fieldnames=cabecalho)
        return list(leitor)


def escrever_csv_dicionario(nome_ficheiro, iterador_de_dicionarios, cabecalho, separador= ','):
    """Escrever num ficheiro CSV um dicionário de iteradores

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV
        iterador_de_dicionarios (iter[dict]): O iterador
        cabecalho (list): A sequência de chaves do dicionário que indica a *ordem* das
        colunas a escrever no CSV.
        separador (str, optional): O separador a utilizar. Defaults to ','.
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = csv.DictWriter(ficheiro_csv, cabecalho, delimiter=separador)
        escritor.writeheader()
        for linha in iterador_de_dicionarios:
            escritor.writerow(linha)


# --------------------------------------------------------------------------- #


#Exercicio 1

def ler_primeiras_csv(nome_de_ficheiro, n):

    with open(nome_de_ficheiro) as ficheiro_csv:
        ficheiro = list(csv.reader(ficheiro_csv))

        if len(ficheiro) >= n:
           return list(map(lambda el: el[0], zip(ficheiro, range(n))))
        else: 
            return ficheiro


#Exercicio 4

def escrever_primeiros_csv(nome_ficheiro, iter_de_iters, n):
    with open(nome_ficheiro, 'w') as csv_file:
        escritor = list(csv.writer(csv_file, delimiter=','))

        if len(escritor) >= n:
           return list(map(lambda el: el[0], zip(escritor, range(n))))
        else:
           return escritor
    
def conversor(iteravel, iteravel_de_funcoes):
    return (func(el) for el, func in zip(iteravel, iteravel_de_funcoes))


#exercicio 5

def media_alunos(ficheiro):

    leitor = ler_csv(ficheiro)

    with open('medias_alunos.csv', 'w') as ficheiro_csv:
        writer = csv.writer(ficheiro_csv)
        for lista in leitor:
            inteiros = list(map(lambda x: int(x), lista[2:])) #transformamos as strings em ints para calcular a media
            media = sum(inteiros)/len(inteiros) #calculamos a media
            lista.append(round(media, 1)) # juntamos a media à lista original
            writer.writerow(lista) #escrevemos os resultados num ficheiro
   

# --------------------------------------------------------------------------- #
# FICHA 8 - Matplotlib & gráficos

from ficha8_grafico import *
import math


#Exercicio 2

def tracar_grafico(graf, etiquetax='x', etiquetay='f(x)', titulo='grafico da funcao f'):
    plt.plot(graf[0], graf[1])
    plt.xlabel(etiquetax)
    plt.ylabel(etiquetay)
    plt.title(titulo)
    plt.show()


#Exercicio 3

baixo = 0.1
alto = 100.0
linear = grafico (lambda n: n, baixo = baixo, alto = alto)
loglinear = grafico(lambda n: n*math.log(n), baixo=baixo, alto=alto)
quadratico = grafico(lambda n: n**2, baixo=baixo, alto=alto)


def tracar_graficos(graficos):
    list(map(lambda x: plt.plot(x[0],x[1]), graficos))
    plt.show()

#Exercicio 6
#a)

baixo = 0.1
alto = 20.0
constante = grafico(lambda x: 10.0, baixo=baixo, alto=alto)
logaritmico = grafico(lambda x: math.log(x),baixo=baixo, alto=alto)
linear = grafico(lambda x: x, baixo=baixo, alto=alto)
loglinear = grafico(lambda x: x*math.log(x),baixo=baixo, alto=alto)
quadratico = grafico(lambda x: x*x, baixo=baixo, alto=alto)
exponencial = grafico(lambda x: 2**x, baixo=baixo, alto=alto)


def tracar_subgrafico(grafico, n_linhas, n_colunas, n_grafico):
    plt.subplot(n_linhas, n_colunas, n_grafico)
    plt.plot(grafico[0], grafico[1])
    plt.show()


#Exercicio 7

baixo = 0.1
alto = 10
linear = grafico(lambda n: n, baixo=baixo, alto=alto)
loglinear = grafico(lambda n: n * math.log(n), baixo=baixo, alto=alto)
quadratico = grafico(lambda n: n**2, baixo=baixo, alto=alto)


formatacoes = ['r^-', 'go--', 'bs:']


def tracar_graficos_personalizados(graficos, forms):
    list(map(lambda x,y: plt.plot(x[0], x[1],y), graficos,forms))
    plt.title('Gráficos de várias funções')
    plt.show()


def grafico_barras(dicionario):
    etiquetas = []
    ordenadas = []
    items = dicionario.items()
    for item in items:
        etiquetas.append(item[0]), ordenadas.append(item[1])

    largura = 0.8
    plt.bar(etiquetas, ordenadas, largura, color='blue')
    # plt.xticks(abcissas, etiquetas)
    # plt.show()
   

# --------------------------------------------------------------------------- #
# FICHA 9 - Programação de Sistema

#Exericio 1

# def para_minusculas(ficheiro):
#     with open(ficheiro, 'w') as f:
#         txt = f.read()
#         txt.lower()


# if __name__ == '__main__':
#     import sys

#     nome_ficheiro = sys.argv[1]
#     para_minusculas(nome_ficheiro)


def proximidade(elem, grafo):

    lista = filter(lambda x: x[0] == elem, grafo)

    print(list(lista))


def espalma(lista_de_listas):
    return functools.reduce(operator.concat, lista_de_listas, [])

def proximos2(elem, grafo):

    listaEl = filter(lambda x: x[0] == elem, grafo)
    listaEsp = espalma(map(list, listaEl))
    return [listaEsp[i] for i in range(1, len(listaEsp), 2)]


"""

C)
"""


def colecionar(grafo):
    """
    Usei a função espalma, da alínea anterior
    
    """

    listaInicial = espalma(map(list, grafo))
    return list(set(listaInicial))


def le_temperaturas(nome_de_ficheiro):

    with open(nome_de_ficheiro, 'rU') as ficheiro_csv:
        leitor = csv.DictReader(
            ficheiro_csv, fieldnames=range(0, 24), delimiter=';')
        resultado = []
        for linha in leitor:
            resultado.append(linha)
        return resultado

def ler(ficheiro):
    with open(ficheiro, encoding='utf8') as f:
        x = input("Escreva uma frase")
        while x != "":
            x = input("Escreva uma frase")
            f.write(x + ' ')
