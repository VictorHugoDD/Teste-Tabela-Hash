from instancias_flocos.instancias.flocos import sao_gemeos, existe_par_gemeo_ingenuo, chave_canonica, existe_par_gemeo_hash, le_instancia
import matplotlib.pyplot as plt
import numpy as np

#grafico 
n=[12,500,1000,2000,4000,8000,16000]
tempo_ing=[0.0001,0.7058,2.5279,9.7947,40.0981,163.8231,635.2844]
tempo_hash=[0.0001,0.0055,0.0122,0.0222,0.0515,0.0922,0.1845]
plt.figure(figsize=(12,7))


# Plotar as duas curvas
plt.plot(n, tempo_ing, 'o-', label='Ingênua (O(N²))', color='red', linewidth=2, markersize=8)
plt.plot(n, tempo_hash, 's-', label='Tabela Hash (O(N))', color='blue', linewidth=2, markersize=8)

# Configurar o gráfico
plt.xlabel('N (número de flocos)', fontsize=14)
plt.ylabel('Tempo de execução (segundos)', fontsize=14)
plt.title('Comparação: Solução Ingênua vs Tabela Hash', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')


# Salvar o gráfico
plt.savefig('grafico_comparacao.png', dpi=300, bbox_inches='tight')
print("Gráfico salvo como 'grafico_comparacao.png'")

plt.show()