"""
Benchmark de Desempenho - Fila (Queue)

Este módulo mede o tempo de execução das operações da fila
para validar empiricamente a complexidade O(1).

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
import time
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from queue import Queue


def benchmark_tempo_fila():
    """Mede o tempo de execução de enqueue() e dequeue() para diferentes tamanhos"""
    print("\n" + "="*60)
    print("BENCHMARK DE TEMPO - FILA")
    print("="*60)
    
    tamanhos = [100, 1000, 10000, 100000]
    resultados_enqueue = []
    resultados_dequeue = []
    
    print("\nMedindo tempo de ENQUEUE...")
    for n in tamanhos:
        fila = Queue()
        
        start = time.perf_counter()
        for i in range(n):
            fila.enqueue(i)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000  # microsegundos
        resultados_enqueue.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    print("\nMedindo tempo de DEQUEUE...")
    for n in tamanhos:
        fila = Queue()
        
        # Preencher fila
        for i in range(n):
            fila.enqueue(i)
        
        # Medir dequeue
        start = time.perf_counter()
        for i in range(n):
            fila.dequeue()
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000
        resultados_dequeue.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    # TABELA FORMATADA
    print("\n" + "="*60)
    print("TABELA PARA COPIAR NO ARTIGO:")
    print("="*60)
    print("")
    print("Tabela X - Tempo de Execução da Fila (microsegundos/operação)")
    print("")
    print("+------------+----------+----------+----------+----------+")
    print("| Operação   | 100      | 1.000    | 10.000   | 100.000  |")
    print("+------------+----------+----------+----------+----------+")
    print(f"| enqueue()  | {resultados_enqueue[0]:>8.4f} | {resultados_enqueue[1]:>8.4f} | {resultados_enqueue[2]:>8.4f} | {resultados_enqueue[3]:>8.4f} |")
    print(f"| dequeue()  | {resultados_dequeue[0]:>8.4f} | {resultados_dequeue[1]:>8.4f} | {resultados_dequeue[2]:>8.4f} | {resultados_dequeue[3]:>8.4f} |")
    print("+------------+----------+----------+----------+----------+")
    print("")
    
    # ANÁLISE
    print("ANÁLISE:")
    variacao_enqueue = (resultados_enqueue[3] / resultados_enqueue[0] - 1) * 100
    variacao_dequeue = (resultados_dequeue[3] / resultados_dequeue[0] - 1) * 100
    
    print(f"  Variação enqueue (100 → 100.000): {variacao_enqueue:+.1f}%")
    print(f"  Variação dequeue (100 → 100.000): {variacao_dequeue:+.1f}%")
    
    if abs(variacao_enqueue) < 50 and abs(variacao_dequeue) < 50:
        print("  ✓ Complexidade O(1) confirmada (variação < 50%)")
    else:
        print("  ⚠️  Variação significativa detectada")
    
    print("="*60)
    
    return {
        'enqueue': resultados_enqueue,
        'dequeue': resultados_dequeue,
        'tamanhos': tamanhos
    }


def benchmark_memoria_fila():
    """Mede o uso de memória da fila"""
    print("\n" + "="*60)
    print("BENCHMARK DE MEMÓRIA - FILA")
    print("="*60)
    
    tamanhos = [100, 1000, 10000]
    
    print("\nMedindo uso de memória...")
    print(f"{'Elementos':<12} {'Mem Total (KB)':<18} {'Bytes/elemento':<15}")
    print("-" * 45)
    
    resultados = []
    
    for n in tamanhos:
        fila = Queue()
        for i in range(n):
            fila.enqueue(i)
        
        mem_total = sys.getsizeof(fila._items)
        mem_por_elemento = mem_total / n
        
        resultados.append(mem_por_elemento)
        
        print(f"{n:<12} {mem_total/1024:<18.2f} {mem_por_elemento:<15.2f}")
    
    # MÉDIA
    media = sum(resultados) / len(resultados)
    
    print("\n" + "="*60)
    print("VALOR PARA USAR NO ARTIGO:")
    print("="*60)
    print(f"\nFila: {media:.2f} bytes/elemento (média)")
    print("\nOu se preferir usar o valor de 1000 elementos:")
    print(f"Fila: {resultados[1]:.2f} bytes/elemento")
    print("="*60)
    
    return {
        'media': media,
        'resultados': resultados,
        'tamanhos': tamanhos
    }


def comparar_fila_deque_vs_lista():
    """
    Compara fila com deque vs lista comum.
    Demonstra por que deque é necessário para operações FIFO eficientes.
    """
    print("\n" + "="*60)
    print("COMPARAÇÃO: FILA (deque) vs LISTA COMUM")
    print("="*60)
    print("\nEste teste mostra por que usamos deque ao invés de lista\n")
    
    # Implementação com lista comum (RUIM - O(n) para remoção)
    class FilaLista:
        def __init__(self):
            self._items = []
        
        def enqueue(self, item):
            self._items.append(item)
        
        def dequeue(self):
            if len(self._items) == 0:
                raise IndexError("Dequeue de fila vazia")
            return self._items.pop(0)  # O(n) - PROBLEMA!
    
    tamanhos = [100, 1000, 5000, 10000]
    
    print(f"{'Elementos':<12} {'Fila (deque)':<18} {'Lista comum':<18} {'Diferença':<12}")
    print("-" * 60)
    
    resultados = []
    
    for n in tamanhos:
        # Testar nossa fila (deque)
        fila_deque = Queue()
        for i in range(n):
            fila_deque.enqueue(i)
        
        start = time.perf_counter()
        for i in range(n):
            fila_deque.dequeue()
        tempo_deque = (time.perf_counter() - start) * 1000  # ms
        
        # Testar fila com lista
        fila_lista = FilaLista()
        for i in range(n):
            fila_lista.enqueue(i)
        
        start = time.perf_counter()
        for i in range(n):
            fila_lista.dequeue()
        tempo_lista = (time.perf_counter() - start) * 1000  # ms
        
        razao = tempo_lista / tempo_deque
        
        print(f"{n:<12} {tempo_deque:<18.4f} {tempo_lista:<18.4f} {razao:<12.1f}x")
        
        resultados.append({
            'elementos': n,
            'tempo_deque': tempo_deque,
            'tempo_lista': tempo_lista,
            'razao': razao
        })
    
    print("\n" + "="*60)
    print("CONCLUSÃO:")
    print("  A lista comum fica cada vez MAIS LENTA conforme cresce")
    print("  porque pop(0) precisa mover TODOS os elementos (O(n))")
    print("")
    print("  Nossa fila com deque mantém velocidade constante O(1)")
    print("="*60)
    
    return resultados


def executar_todos_benchmarks():
    """Executa todos os benchmarks e salva resultados"""
    print("="*70)
    print("BENCHMARKS COMPLETOS - FILA")
    print("="*70)
    
    resultados = {}
    
    # 1. Benchmark de tempo
    resultados['tempo'] = benchmark_tempo_fila()
    
    # 2. Benchmark de memória
    resultados['memoria'] = benchmark_memoria_fila()
    
    # 3. Comparação deque vs lista
    resultados['deque_vs_lista'] = comparar_fila_deque_vs_lista()
    
    print("\n" + "="*70)
    print("TODOS OS BENCHMARKS CONCLUÍDOS!")
    print("="*70)
    
    return resultados


if __name__ == "__main__":
    resultados = executar_todos_benchmarks()
