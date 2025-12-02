"""
Benchmark de Desempenho - Hashtable

Este módulo mede o tempo de execução das operações da hashtable
para validar empiricamente a complexidade O(1+α).

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
import time
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from hashtable import HashTable


def benchmark_tempo_hashtable():
    """Mede o tempo de execução de insert(), search() e delete()"""
    print("\n" + "="*60)
    print("BENCHMARK DE TEMPO - HASHTABLE")
    print("="*60)
    
    tamanhos = [100, 1000, 10000, 100000]
    resultados_insert = []
    resultados_search = []
    resultados_delete = []
    
    print("\nMedindo tempo de INSERT...")
    for n in tamanhos:
        ht = HashTable(size=max(10, n//10))  # Manter α ≈ 1.0
        
        start = time.perf_counter()
        for i in range(n):
            ht.insert(i, i*2)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000  # microsegundos
        resultados_insert.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    print("\nMedindo tempo de SEARCH...")
    for n in tamanhos:
        ht = HashTable(size=max(10, n//10))
        
        # Preencher hashtable
        for i in range(n):
            ht.insert(i, i*2)
        
        # Medir search
        start = time.perf_counter()
        for i in range(n):
            ht.search(i)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000
        resultados_search.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    print("\nMedindo tempo de DELETE...")
    for n in tamanhos:
        ht = HashTable(size=max(10, n//10))
        
        # Preencher hashtable
        for i in range(n):
            ht.insert(i, i*2)
        
        # Medir delete
        start = time.perf_counter()
        for i in range(n):
            ht.delete(i)
        tempo_total = time.perf_counter() - start
        
        tempo_por_op = (tempo_total / n) * 1000000
        resultados_delete.append(tempo_por_op)
        print(f"  {n:>7} elementos: {tempo_por_op:.4f} μs/operação")
    
    # TABELA FORMATADA
    print("\n" + "="*60)
    print("TABELA PARA COPIAR NO ARTIGO:")
    print("="*60)
    print("")
    print("Tabela X - Tempo de Execução da Hashtable (microsegundos/operação)")
    print("")
    print("+------------+----------+----------+----------+----------+")
    print("| Operação   | 100      | 1.000    | 10.000   | 100.000  |")
    print("+------------+----------+----------+----------+----------+")
    print(f"| insert()   | {resultados_insert[0]:>8.4f} | {resultados_insert[1]:>8.4f} | {resultados_insert[2]:>8.4f} | {resultados_insert[3]:>8.4f} |")
    print(f"| search()   | {resultados_search[0]:>8.4f} | {resultados_search[1]:>8.4f} | {resultados_search[2]:>8.4f} | {resultados_search[3]:>8.4f} |")
    print(f"| delete()   | {resultados_delete[0]:>8.4f} | {resultados_delete[1]:>8.4f} | {resultados_delete[2]:>8.4f} | {resultados_delete[3]:>8.4f} |")
    print("+------------+----------+----------+----------+----------+")
    print("")
    
    # ANÁLISE
    print("ANÁLISE:")
    variacao_insert = (resultados_insert[3] / resultados_insert[0] - 1) * 100
    variacao_search = (resultados_search[3] / resultados_search[0] - 1) * 100
    variacao_delete = (resultados_delete[3] / resultados_delete[0] - 1) * 100
    
    print(f"  Variação insert (100 → 100.000): {variacao_insert:+.1f}%")
    print(f"  Variação search (100 → 100.000): {variacao_search:+.1f}%")
    print(f"  Variação delete (100 → 100.000): {variacao_delete:+.1f}%")
    
    if abs(variacao_insert) < 100 and abs(variacao_search) < 100:
        print("  ✓ Complexidade O(1) mantida (variação < 100%)")
    else:
        print("  ⚠️  Variação significativa - pode indicar degradação")
    
    print("="*60)
    
    return {
        'insert': resultados_insert,
        'search': resultados_search,
        'delete': resultados_delete,
        'tamanhos': tamanhos
    }


def benchmark_memoria_hashtable():
    """Mede o uso de memória da hashtable"""
    print("\n" + "="*60)
    print("BENCHMARK DE MEMÓRIA - HASHTABLE")
    print("="*60)
    
    tamanhos = [100, 1000, 10000]
    
    print("\nMedindo uso de memória...")
    print(f"{'Elementos':<12} {'Mem Total (KB)':<18} {'Bytes/elemento':<15}")
    print("-" * 45)
    
    resultados = []
    
    for n in tamanhos:
        ht = HashTable(size=max(10, n//10))
        for i in range(n):
            ht.insert(i, i*2)
        
        # Memória da tabela (lista de listas)
        mem_total = sum(sys.getsizeof(bucket) for bucket in ht.table)
        # Adicionar overhead da estrutura principal
        mem_total += sys.getsizeof(ht.table)
        
        mem_por_elemento = mem_total / n
        
        resultados.append(mem_por_elemento)
        
        print(f"{n:<12} {mem_total/1024:<18.2f} {mem_por_elemento:<15.2f}")
    
    # MÉDIA
    media = sum(resultados) / len(resultados)
    
    print("\n" + "="*60)
    print("VALOR PARA USAR NO ARTIGO:")
    print("="*60)
    print(f"\nHashtable: {media:.2f} bytes/elemento (média)")
    print("\nOu se preferir usar o valor de 1000 elementos:")
    print(f"Hashtable: {resultados[1]:.2f} bytes/elemento")
    print("="*60)
    
    return {
        'media': media,
        'resultados': resultados,
        'tamanhos': tamanhos
    }


def comparar_hashtable_vs_busca_linear():
    """
    Compara hashtable vs busca linear em lista.
    Demonstra a vantagem de O(1) vs O(n).
    """
    print("\n" + "="*60)
    print("COMPARAÇÃO: HASHTABLE vs BUSCA LINEAR")
    print("="*60)
    print("\nCompara acesso por chave O(1) vs busca sequencial O(n)\n")
    
    tamanhos = [100, 1000, 5000, 10000]
    
    print(f"{'Elementos':<12} {'Hashtable (μs)':<18} {'Lista (μs)':<18} {'Speedup':<12}")
    print("-" * 60)
    
    resultados = []
    
    for n in tamanhos:
        # Preparar dados
        dados = [(f"key{i}", i*10) for i in range(n)]
        
        # Testar HASHTABLE
        ht = HashTable(size=max(10, n//10))
        for chave, valor in dados:
            ht.insert(chave, valor)
        
        start = time.perf_counter()
        for i in range(n):
            ht.search(f"key{i}")
        tempo_ht = (time.perf_counter() - start) / n * 1000000  # μs
        
        # Testar LISTA (busca linear)
        lista = dados.copy()
        
        start = time.perf_counter()
        for i in range(n):
            target = f"key{i}"
            # Busca linear
            for chave, valor in lista:
                if chave == target:
                    break
        tempo_lista = (time.perf_counter() - start) / n * 1000000  # μs
        
        speedup = tempo_lista / tempo_ht
        
        print(f"{n:<12} {tempo_ht:<18.4f} {tempo_lista:<18.4f} {speedup:<12.1f}x")
        
        resultados.append({
            'elementos': n,
            'tempo_hashtable': tempo_ht,
            'tempo_lista': tempo_lista,
            'speedup': speedup
        })
    
    print("\n" + "="*60)
    print("CONCLUSÃO:")
    print("  Hashtable mantém velocidade constante O(1)")
    print("  Lista degrada linearmente O(n) - cada busca percorre metade dos elementos")
    print(f"  Para {tamanhos[-1]} elementos, hashtable é {resultados[-1]['speedup']:.1f}x mais rápida")
    print("="*60)
    
    return resultados


def executar_todos_benchmarks():
    """Executa todos os benchmarks e salva resultados"""
    print("="*70)
    print("BENCHMARKS COMPLETOS - HASHTABLE")
    print("="*70)
    
    resultados = {}
    
    # 1. Benchmark de tempo
    resultados['tempo'] = benchmark_tempo_hashtable()
    
    # 2. Benchmark de memória
    resultados['memoria'] = benchmark_memoria_hashtable()
    
    # 3. Comparação com busca linear
    resultados['vs_busca_linear'] = comparar_hashtable_vs_busca_linear()
    
    print("\n" + "="*70)
    print("TODOS OS BENCHMARKS CONCLUÍDOS!")
    print("="*70)
    
    return resultados


if __name__ == "__main__":
    resultados = executar_todos_benchmarks()
