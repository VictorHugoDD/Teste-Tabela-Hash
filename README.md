# Teste-Tabela-Hash

# ❄️ Flocos de Neve: Busca Ingênua vs. Tabela de Dispersão
 
Trabalho da disciplina de Algoritmos e Estruturas de Dados: duas soluções para o mesmo problema — uma O(N²), outra O(N) — comparadas na prática pra ver o quanto essa diferença realmente importa.


## 🧩 O problema
 
Um floco de neve é descrito por 6 inteiros (o comprimento de cada uma das suas pontas), listados ao redor do centro a partir de um ponto de partida arbitrário. Dois flocos são **gêmeos** se um é uma rotação cíclica do outro:
 
```
[2, 3, 1, 4, 5, 6]  e  [1, 4, 5, 6, 2, 3]   →  são gêmeos
```
 
Dada uma coleção de N flocos, o objetivo é responder: **existe algum par de flocos gêmeos?**


## 🧠 As duas soluções
 
| | Busca ingênua | Tabela de dispersão |
|---|---|---|
| Ideia | Compara cada par de flocos, um a um | Calcula uma chave canônica por floco e usa um `dict` |
| Complexidade | O(N²) | O(N) |
| Função | `existe_par_gemeo_ingenuo` | `existe_par_gemeo_hash` |
 
A chave canônica de um floco é, dentre suas 6 rotações possíveis, a menor em ordem lexicográfica — assim, dois flocos gêmeos sempre produzem a mesma chave, e achar um par vira uma simples consulta em tabela hash em vez de uma comparação par a par.
 
## ▶️ Como rodar
 
```bash
python3 flocos.py
```
 
Requer Python 3 e todos os arquivos `floco_*.txt` na mesma pasta do `flocos.py`. O script já roda o benchmark nas instâncias de N=500 até N=16.000 e imprime a tabela de tempos.
 
## 📊 Resultados
 
| N | Ingênua (s) | Hash (s) |
|---:|---:|---:|
| 500 | 0.7058 | 0.0055 |
| 1.000 | 2.5279 | 0.0122 |
| 2.000 | 9.7947 | 0.0222 |
| 4.000 | 40.0981 | 0.0515 |
| 8.000 | 163.8231 | 0.0922 |
| 16.000 | 635.2844 | 0.1845 |
 
![Gráfico comparando os tempos de execução](grafico_tempos.png)
 
## 🔍 Principais conclusões
 
- **Dobrar N** multiplica o tempo da ingênua por ~4× e o da hash por ~2× — exatamente o esperado para O(N²) e O(N).
- **A posição do par gêmeo afeta muito mais a ingênua**: com o par logo no início, as duas soluções são praticamente instantâneas; com o par só no fim, a ingênua se aproxima do seu pior caso O(N²), enquanto a hash cresce apenas linearmente.
- **Em N = 100.000**, a ingênua levaria quase 7 horas (extrapolando o crescimento observado) — inviável na prática — enquanto a tabela hash resolve a mesma instância em frações de segundo.
Análise completa das perguntas do trabalho em [`Relatorio_AV4_AED_VictorHugoDD.pdf`](./Relatorio_AV4_AED_VictorHugoDD.pdf).

## 📜 Scripts
 
- **`flocos.py`** — as duas soluções (ingênua e hash) e o benchmark. É só rodar `python flocos.py` que ele já testa e mede tudo.
- **`teste.py`** — roda os casos `floco_2000_gemeo_inicio.txt` e `floco_2000_gemeo_fim.txt`, usados na análise da Tarefa 5(b).
- **`grafico.py`** — gera o gráfico a partir dos tempos medidos (Tarefa 4).

 
## ✍️ Autoria
 
Victor Hugo Dédes Dantas — Estruturas de Dados 2026.1, Turma 01 (Prof. Luis Henrique)