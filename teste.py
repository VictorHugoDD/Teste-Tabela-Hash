from instancias_flocos.instancias.flocos import sao_gemeos, existe_par_gemeo_ingenuo, chave_canonica, existe_par_gemeo_hash, le_instancia,benchmark
import time

caminhos=['instancias_flocos/instancias/floco_2000_gemeo_fim.txt','instancias_flocos/instancias/floco_2000_gemeo_inicio.txt']

print(f"{'instância':30s} {'N':>7s} {'ingênuo (s)':>14s} {'hash (s)':>12s}")
for nome in caminhos:
    flocos = le_instancia(nome)
    n = len(flocos)

    t_ingenuo, r1 = benchmark(nome, existe_par_gemeo_ingenuo)
    t_hash, r2 = benchmark(nome, existe_par_gemeo_hash)

    assert (r1 is None) == (r2 is None), "as duas soluções discordam!"

    print(f"{nome:30s} {n:7d} {t_ingenuo:14.4f} {t_hash:12.4f}")