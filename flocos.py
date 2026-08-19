"""
Problema dos Flocos de Neve — comparação de tempo de execução
================================================================

Um floco de neve é descrito por 6 inteiros, representando o comprimento
de cada uma das seus 6 pontas, na ordem em que aparecem ao redor do centro
(sentido horário ou anti-horário, mas o ponto de partida é arbitrário).

Dois flocos são "gêmeos" se um é uma rotação do outro. Por exemplo,
    [2, 3, 1, 4, 5, 6]  e  [1, 4, 5, 6, 2, 3]
são gêmeos (a segunda lista é a primeira "girada").

Dado um conjunto de N flocos, o objetivo é responder:
    existe algum par de flocos gêmeos?

Complete as funções abaixo. Depois use a função `benchmark` no final
do arquivo para comparar os tempos de execução das duas abordagens.
"""

import time
import itertools


def le_instancia(caminho):
    """Lê um arquivo no formato do problema e retorna uma lista de flocos.
    Cada floco é uma lista de 6 inteiros."""
    with open(caminho) as f:
        n = int(f.readline())
        flocos = []
        for _ in range(n):
            flocos.append(list(map(int, f.readline().split())))
    return flocos


def sao_gemeos(a, b):
    """Retorna True se o floco b é alguma rotação do floco a.

    Dica: gere as 6 rotações possíveis de `a` e verifique se alguma
    delas é igual a `b`.
    """
    if len(a) != len(b):
            return False
        
    for i in range(6): #verificar as 6 pontas de cada floco
    
            
        eh_gemeo=True
        for j in range(6):
            if a[j] != b[(i+j) % 6]:
                eh_gemeo=False
                break
    
        if eh_gemeo:
            return True
    
    return False
    

    # TODO: implementar
    raise NotImplementedError


def existe_par_gemeo_ingenuo(flocos):
    """Solução ingênua: compara todos os pares de flocos, um a um.

    Retorna (i, j) com os índices do primeiro par gêmeo encontrado,
    ou None se não existir nenhum par.
    """
    # TODO: implementar (dois laços aninhados + sao_gemeos)
    #raise NotImplementedError

    n=len(flocos)
    for i in range(n):
        for j in range(i+1,n):
            if sao_gemeos(flocos[i],flocos[j]):
                return (i,j)

    return None



def chave_canonica(floco):
    """Retorna uma representação do floco que é a MESMA para todas as
    suas rotações, ou seja, dois flocos gêmeos devem produzir a mesma
    chave_canonica.

    Dica: dentre as 6 rotações possíveis do floco, escolha sempre a
    mesma (por exemplo, a menor delas em ordem lexicográfica) e use
    essa rotação (convertida para tupla) como chave.
    """
    # TODO: implementar
    raise NotImplementedError


def existe_par_gemeo_hash(flocos):
    """Solução com tabela hash (dict/set nativos do Python).

    Percorre os flocos uma única vez, mantendo uma tabela hash das
    chaves canônicas já vistas. Retorna (i, j) do primeiro par gêmeo
    encontrado, ou None se não existir nenhum.
    """
    # TODO: implementar
    raise NotImplementedError


# ---------------------------------------------------------------------
# Ferramentas de benchmark
# NÃO PRECISA MEXER AQUI
# ---------------------------------------------------------------------

def benchmark(caminho, algoritmo, repeticoes=3):
    flocos = le_instancia(caminho)
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        resultado = algoritmo(flocos)
        fim = time.perf_counter()
        tempos.append(fim - inicio)
    return min(tempos), resultado


if __name__ == "__main__":
    instancias = [
        "floco_debug_12.txt",
        "floco_semgemeos_500.txt",
        "floco_semgemeos_1000.txt",
        "floco_semgemeos_2000.txt",
        "floco_semgemeos_4000.txt",
        # descomente conforme for testando N maiores
        # "floco_semgemeos_8000.txt",
        # "floco_semgemeos_16000.txt",
    ]

    print(f"{'instância':30s} {'N':>7s} {'ingênuo (s)':>14s} {'hash (s)':>12s}")
    for nome in instancias:
        flocos = le_instancia(nome)
        n = len(flocos)

        t_ingenuo, r1 = benchmark(nome, existe_par_gemeo_ingenuo)
        t_hash, r2 = benchmark(nome, existe_par_gemeo_hash)

        assert (r1 is None) == (r2 is None), "as duas soluções discordam!"

        print(f"{nome:30s} {n:7d} {t_ingenuo:14.4f} {t_hash:12.4f}")