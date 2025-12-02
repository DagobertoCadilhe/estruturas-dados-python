"""
Benchmark de Desempenho - Pilha (Stack)

Este módulo mede o tempo de execução das operações da pilha
para validar empiricamente a complexidade O(1).

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
import time
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from stack import Stack


def benchmark_tempo_pilha():
    """Mede o tempo de execução de push() e pop() para diferentes tamanhos"""
    print("\n" + "="*60)
    print("BENCHMARK DE TEMPO - PILHA")
    print("="*60)
    
    tamanhos = [100, 1000, 10000, 100000]
    resultados_push = []
    resultados_pop = []
    
    print("\nMedindo tempo de PUSH...")
    for n in tamanhos:
        pilha = Stack()
        
        start = time.perf_counter()
        for i in range(n):
            pilha.push(i)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000  # microsegundos
        resultados_push.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    print("\nMedindo tempo de POP...")
    for n in tamanhos:
        pilha = Stack()
        
        # Preencher pilha
        for i in range(n):
            pilha.push(i)
        
        # Medir pop
        start = time.perf_counter()
        for i in range(n):
            pilha.pop()
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000
        resultados_pop.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    # TABELA FORMATADA
    print("\n" + "="*60)
    print("TABELA PARA COPIAR NO ARTIGO:")
    print("="*60)
    print("")
    print("Tabela X - Tempo de Execução da Pilha (microsegundos/operação)")
    print("")
    print("+------------+----------+----------+----------+----------+")
    print("| Operação   | 100      | 1.000    | 10.000   | 100.000  |")
    print("+------------+----------+----------+----------+----------+")
    print(f"| push()     | {resultados_push[0]:>8.4f} | {resultados_push[1]:>8.4f} | {resultados_push[2]:>8.4f} | {resultados_push[3]:>8.4f} |")
    print(f"| pop()      | {resultados_pop[0]:>8.4f} | {resultados_pop[1]:>8.4f} | {resultados_pop[2]:>8.4f} | {resultados_pop[3]:>8.4f} |")
    print("+------------+----------+----------+----------+----------+")
    print("")
    
    # ANÁLISE
    print("ANÁLISE:")
    variacao_push = (resultados_push[3] / resultados_push[0] - 1) * 100
    variacao_pop = (resultados_pop[3] / resultados_pop[0] - 1) * 100
    
    print(f"  Variação push (100 → 100.000): {variacao_push:+.1f}%")
    print(f"  Variação pop (100 → 100.000): {variacao_pop:+.1f}%")
    
    if abs(variacao_push) < 50 and abs(variacao_pop) < 50:
        print("  ✓ Complexidade O(1) confirmada (variação < 50%)")
    else:
        print("  ⚠️  Variação significativa detectada")
    
    print("="*60)
    
    return {
        'push': resultados_push,
        'pop': resultados_pop,
        'tamanhos': tamanhos
    }


def benchmark_memoria_pilha():
    """Mede o uso de memória da pilha"""
    print("\n" + "="*60)
    print("BENCHMARK DE MEMÓRIA - PILHA")
    print("="*60)
    
    tamanhos = [100, 1000, 10000]
    
    print("\nMedindo uso de memória...")
    print(f"{'Elementos':<12} {'Mem Total (KB)':<18} {'Bytes/elemento':<15}")
    print("-" * 45)
    
    resultados = []
    
    for n in tamanhos:
        pilha = Stack()
        for i in range(n):
            pilha.push(i)
        
        mem_total = sys.getsizeof(pilha._items)
        mem_por_elemento = mem_total / n
        
        resultados.append(mem_por_elemento)
        
        print(f"{n:<12} {mem_total/1024:<18.2f} {mem_por_elemento:<15.2f}")
    
    # MÉDIA
    media = sum(resultados) / len(resultados)
    
    print("\n" + "="*60)
    print("VALOR PARA USAR NO ARTIGO:")
    print("="*60)
    print(f"\nPilha: {media:.2f} bytes/elemento (média)")
    print("\nOu se preferir usar o valor de 1000 elementos:")
    print(f"Pilha: {resultados[1]:.2f} bytes/elemento")
    print("="*60)
    
    return {
        'media': media,
        'resultados': resultados,
        'tamanhos': tamanhos
    }


def analisar_realocacoes():
    """Analisa o comportamento de realocações (O(1) amortizado)"""
    print("\n" + "="*60)
    print("ANÁLISE DE REALOCAÇÕES - PILHA")
    print("="*60)
    print("\nEste teste demonstra o comportamento O(1) amortizado\n")
    
    tamanhos = [100, 500, 1000, 5000, 10000, 50000, 100000]
    
    print(f"{'Elementos':<12} {'Tempo/op (μs)':<18} {'Crescimento':<15}")
    print("-" * 45)
    
    tempo_anterior = None
    resultados = []
    
    for n in tamanhos:
        pilha = Stack()
        
        start = time.perf_counter()
        for i in range(n):
            pilha.push(i)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000
        
        if tempo_anterior:
            crescimento = ((tempo_por_op / tempo_anterior) - 1) * 100
            print(f"{n:<12} {tempo_por_op:<18.4f} {crescimento:+.1f}%")
        else:
            print(f"{n:<12} {tempo_por_op:<18.4f} baseline")
        
        resultados.append({'elementos': n, 'tempo': tempo_por_op})
        tempo_anterior = tempo_por_op
    
    print("\n" + "="*60)
    print("INTERPRETAÇÃO:")
    print("  Se fosse O(n), veríamos crescimento linear (~900% de 100→100K)")
    print("  O crescimento próximo a 0% confirma O(1) amortizado")
    print("  Pequenas variações são normais devido a realocações ocasionais")
    print("="*60)
    
    return resultados


def comparar_peek_vs_pop():
    """Compara o custo de peek() vs pop()"""
    print("\n" + "="*60)
    print("COMPARAÇÃO: PEEK vs POP - PILHA")
    print("="*60)
    print("\nMedindo custo de peek (não-destrutivo) vs pop (destrutivo)\n")
    
    tamanhos = [1000, 10000, 100000]
    
    print(f"{'Elementos':<12} {'Peek (μs)':<15} {'Pop (μs)':<15} {'Diferença':<12}")
    print("-" * 54)
    
    resultados = []
    
    for n in tamanhos:
        # Testar PEEK
        pilha = Stack()
        for i in range(n):
            pilha.push(i)
        
        start = time.perf_counter()
        for i in range(n):
            pilha.peek()
        tempo_peek = (time.perf_counter() - start) / n * 1000000
        
        # Testar POP
        pilha = Stack()
        for i in range(n):
            pilha.push(i)
        
        start = time.perf_counter()
        for i in range(n):
            pilha.pop()
        tempo_pop = (time.perf_counter() - start) / n * 1000000
        
        diferenca = ((tempo_pop / tempo_peek) - 1) * 100
        
        print(f"{n:<12} {tempo_peek:<15.4f} {tempo_pop:<15.4f} {diferenca:+.1f}%")
        
        resultados.append({
            'elementos': n,
            'peek': tempo_peek,
            'pop': tempo_pop,
            'diferenca_percentual': diferenca
        })
    
    print("\n" + "="*60)
    print("CONCLUSÃO:")
    print("  Pop é ligeiramente mais lento que peek devido à remoção")
    print("  Ambas são O(1), mas pop tem overhead de ajustar tamanho")
    print("="*60)
    
    return resultados


def executar_todos_benchmarks():
    """Executa todos os benchmarks e salva resultados"""
    print("="*70)
    print("BENCHMARKS COMPLETOS - PILHA")
    print("="*70)
    
    resultados = {}
    
    # 1. Benchmark de tempo
    resultados['tempo'] = benchmark_tempo_pilha()
    
    # 2. Benchmark de memória
    resultados['memoria'] = benchmark_memoria_pilha()
    
    # 3. Análise de realocações
    resultados['realocacoes'] = analisar_realocacoes()
    
    # 4. Comparação peek vs pop
    resultados['peek_vs_pop'] = comparar_peek_vs_pop()
    
    print("\n" + "="*70)
    print("TODOS OS BENCHMARKS CONCLUÍDOS!")
    print("="*70)
    
    return resultados


if __name__ == "__main__":
    resultados = executar_todos_benchmarks()
