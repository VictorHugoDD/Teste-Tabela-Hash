import random
import os

OUT = "/home/claude/flocos"

def floco_aleatorio(rng):
    return [rng.randint(0, 10_000_000) for _ in range(6)]

def rotaciona(s, k):
    return s[k:] + s[:k]

def reflete(s):
    return list(reversed(s))

def escreve(path, flocos):
    with open(path, "w") as f:
        f.write(f"{len(flocos)}\n")
        for s in flocos:
            f.write(" ".join(map(str, s)) + "\n")

def instancia_sem_gemeos(n, seed):
    rng = random.Random(seed)
    return [floco_aleatorio(rng) for _ in range(n)]

def instancia_com_gemeo(n, seed, pos_a, pos_b, usa_reflexao=False):
    rng = random.Random(seed)
    flocos = [floco_aleatorio(rng) for _ in range(n)]
    base = flocos[pos_a]
    k = rng.randint(1, 5)
    gemeo = rotaciona(base, k)
    if usa_reflexao:
        gemeo = reflete(gemeo)
    flocos[pos_b] = gemeo
    return flocos

random.seed(0)

# ---------------------------------------------------------------
# 1) Instância pequena para depuração / conferência manual
#    N = 12, com 1 par gêmeo (rotacionado) em posições conhecidas
# ---------------------------------------------------------------
flocos = instancia_com_gemeo(12, seed=1, pos_a=2, pos_b=9)
escreve(f"{OUT}/floco_debug_12.txt", flocos)

# ---------------------------------------------------------------
# 2) Série "sem gêmeos" (pior caso do naive: percorre tudo)
#    N crescendo em dobro, para montar tabela/gráfico N x tempo
# ---------------------------------------------------------------
for n in [500, 1000, 2000, 4000, 8000, 16000]:
    flocos = instancia_sem_gemeos(n, seed=100 + n)
    escreve(f"{OUT}/floco_semgemeos_{n}.txt", flocos)

# ---------------------------------------------------------------
# 3) Mesmo N (2000), variando ONDE está o par gêmeo
#    -> ilustra melhor/pior caso do naive (early-exit vs percorrer quase tudo)
# ---------------------------------------------------------------
flocos_inicio = instancia_com_gemeo(2000, seed=7, pos_a=0, pos_b=3)
escreve(f"{OUT}/floco_2000_gemeo_inicio.txt", flocos_inicio)

flocos_fim = instancia_com_gemeo(2000, seed=7, pos_a=1990, pos_b=1999)
escreve(f"{OUT}/floco_2000_gemeo_fim.txt", flocos_fim)

# ---------------------------------------------------------------
# 4) Instância grande, só para tabela hash (o naive não deve nem tentar)
# ---------------------------------------------------------------
flocos_grande = instancia_sem_gemeos(100_000, seed=999)
escreve(f"{OUT}/floco_grande_100000.txt", flocos_grande)

print("Arquivos gerados:")
for f in sorted(os.listdir(OUT)):
    if f.endswith(".txt"):
        path = os.path.join(OUT, f)
        print(f"  {f:35s} {os.path.getsize(path):>10} bytes")
