"""
Teste de Impacto do Fator de Carga - Hashtable

Este módulo analisa como o fator de carga (α) afeta o desempenho
da hashtable e valida empiricamente a relação O(1+α).

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
import time
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from hashtable import HashTable


def testar_impacto_fator_carga():
    """
    Testa o impacto do fator de carga no desempenho de inserção e busca.
    Valida empiricamente a complexidade O(1+α).
    """
    print("\n" + "="*60)
    print("IMPACTO DO FATOR DE CARGA - HASHTABLE")
    print("="*60)
    
    fatores = [0.5, 1.0, 2.0, 5.0, 10.0]
    n = 1000
    
    print(f"\nTestando com {n} elementos\n")
    print(f"{'Fator α':<10} {'Size':<10} {'Insert (μs)':<15} {'Search (μs)':<15} {'Colisões médias':<18}")
    print("-" * 68)
    
    resultados = []
    
    for alpha in fatores:
        size = int(n / alpha)
        ht = HashTable(size=size)
        
        # Medir INSERT
        start = time.perf_counter()
        for i in range(n):
            ht.insert(i, i*2)
        tempo_insert = (time.perf_counter() - start) / n * 1000000
        
        # Medir SEARCH
        start = time.perf_counter()
        for i in range(n):
            ht.search(i)
        tempo_search = (time.perf_counter() - start) / n * 1000000
        
        # Calcular média de elementos por bucket não-vazio
        distribuicao = ht.get_distribution()
        buckets_com_elementos = [x for x in distribuicao if x > 0]
        media_colisoes = sum(buckets_com_elementos) / len(buckets_com_elementos) if buckets_com_elementos else 0
        
        resultados.append({
            'alpha': alpha,
            'size': size,
            'insert': tempo_insert,
            'search': tempo_search,
            'colisoes': media_colisoes
        })
        
        print(f"{alpha:<10.1f} {size:<10} {tempo_insert:<15.4f} {tempo_search:<15.4f} {media_colisoes:<18.2f}")
    
    # ANÁLISE
    print("\n" + "="*60)
    print("ANÁLISE DETALHADA:")
    print("="*60)
    
    # Encontrar melhor desempenho
    melhor_search = min(resultados, key=lambda x: x['search'])
    pior_search = max(resultados, key=lambda x: x['search'])
    
    print(f"\nTempo de search:")
    print(f"  Melhor (α={melhor_search['alpha']:.1f}): {melhor_search['search']:.4f} μs")
    print(f"  Pior (α={pior_search['alpha']:.1f}): {pior_search['search']:.4f} μs")
    
    degradacao = (pior_search['search'] / melhor_search['search'] - 1) * 100
    print(f"  Degradação total: {degradacao:.1f}%")
    
    print(f"\nRelação α vs tempo de search:")
    for i in range(len(resultados)):
        if i > 0:
            crescimento = (resultados[i]['search'] / resultados[i-1]['search'] - 1) * 100
            crescimento_alpha = (resultados[i]['alpha'] / resultados[i-1]['alpha'] - 1) * 100
            print(f"  α={resultados[i-1]['alpha']:.1f} → α={resultados[i]['alpha']:.1f}: +{crescimento:.1f}% tempo ({crescimento_alpha:.0f}% aumento em α)")
    
    # Validar O(1+α)
    print(f"\nValidação teórica O(1+α):")
    print("  Se O(1+α) for válido, tempo deve crescer aproximadamente linear com α")
    
    # Calcular correlação entre α e tempo
    alphas = [r['alpha'] for r in resultados]
    tempos = [r['search'] for r in resultados]
    
    # Crescimento médio
    crescimentos = []
    for i in range(1, len(resultados)):
        crescimento_tempo = (tempos[i] - tempos[i-1]) / tempos[i-1]
        crescimento_alpha = (alphas[i] - alphas[i-1]) / alphas[i-1]
        if crescimento_alpha > 0:
            razao = crescimento_tempo / crescimento_alpha
            crescimentos.append(razao)
    
    razao_media = sum(crescimentos) / len(crescimentos) if crescimentos else 0
    
    print(f"  Razão média crescimento_tempo/crescimento_α: {razao_media:.2f}")
    if 0.5 <= razao_media <= 1.5:
        print("  ✓ Relação linear confirmada - O(1+α) validado")
    else:
        print("  ⚠️  Desvio da linearidade observado")
    
    print(f"\nCONCLUSÃO:")
    if degradacao < 100:
        print(f"  ✓ Degradação aceitável ({degradacao:.1f}%) mesmo com α alto")
        print(f"  ✓ α={melhor_search['alpha']:.1f} oferece melhor desempenho")
        if melhor_search['alpha'] >= 1.0:
            print(f"  ✓ Contraintuitivo: α={melhor_search['alpha']:.1f} melhor que α=0.5")
            print("    (overhead de gerenciamento supera benefício de menos colisões)")
    elif degradacao < 300:
        print(f"  ⚠️  Degradação moderada ({degradacao:.1f}%) - α>5 não recomendado")
    else:
        print(f"  ✗ Degradação severa ({degradacao:.1f}%) - α>2 inviável")
    
    print("\n" + "="*60)
    print("TABELA PARA COPIAR NO ARTIGO:")
    print("="*60)
    print("")
    print("Tabela X - Impacto do Fator de Carga no Desempenho (1.000 elementos)")
    print("")
    print("+----------+----------+---------------+---------------+------------------+")
    print("| α        | Size     | Insert (μs)   | Search (μs)   | Colisões médias  |")
    print("+----------+----------+---------------+---------------+------------------+")
    for r in resultados:
        print(f"| {r['alpha']:<8.1f} | {r['size']:<8} | {r['insert']:<13.4f} | {r['search']:<13.4f} | {r['colisoes']:<16.2f} |")
    print("+----------+----------+---------------+---------------+------------------+")
    print("")
    print("="*60)
    
    return resultados


def analisar_relacao_alpha_desempenho():
    """
    Análise detalhada da relação entre α e desempenho.
    Gera dados para gráfico α vs tempo.
    """
    print("\n" + "="*60)
    print("ANÁLISE DETALHADA: α vs DESEMPENHO")
    print("="*60)
    print("\nTestando faixa ampla de fatores de carga\n")
    
    # Testar mais valores para gráfico
    alphas = [0.1, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0]
    n = 1000
    
    print(f"{'α':<8} {'Insert (μs)':<15} {'Search (μs)':<15} {'Delete (μs)':<15}")
    print("-" * 53)
    
    resultados = []
    
    for alpha in alphas:
        size = max(10, int(n / alpha))
        ht = HashTable(size=size)
        
        # INSERT
        start = time.perf_counter()
        for i in range(n):
            ht.insert(i, i*2)
        tempo_insert = (time.perf_counter() - start) / n * 1000000
        
        # SEARCH
        start = time.perf_counter()
        for i in range(n):
            ht.search(i)
        tempo_search = (time.perf_counter() - start) / n * 1000000
        
        # DELETE
        start = time.perf_counter()
        for i in range(n):
            ht.delete(i)
        tempo_delete = (time.perf_counter() - start) / n * 1000000
        
        print(f"{alpha:<8.1f} {tempo_insert:<15.4f} {tempo_search:<15.4f} {tempo_delete:<15.4f}")
        
        resultados.append({
            'alpha': alpha,
            'insert': tempo_insert,
            'search': tempo_search,
            'delete': tempo_delete
        })
    
    print("\n" + "="*60)
    print("PONTOS-CHAVE OBSERVADOS:")
    print("="*60)
    
    # Identificar pontos de inflexão
    tempo_min = min(r['search'] for r in resultados)
    alpha_otimo = next(r['alpha'] for r in resultados if r['search'] == tempo_min)
    
    print(f"\nα ótimo: {alpha_otimo:.1f}")
    print(f"  Oferece melhor compromisso memória/desempenho")
    
    # Faixa recomendada
    threshold = tempo_min * 1.2  # 20% de overhead aceitável
    faixa_recomendada = [r['alpha'] for r in resultados if r['search'] <= threshold]
    
    print(f"\nFaixa recomendada (degradação < 20%):")
    print(f"  α entre {min(faixa_recomendada):.1f} e {max(faixa_recomendada):.1f}")
    
    # Alertas
    print(f"\nAlertas de desempenho:")
    for r in resultados:
        if r['search'] > tempo_min * 2:
            print(f"  ⚠️  α={r['alpha']:.1f}: Desempenho degradado em {((r['search']/tempo_min - 1)*100):.0f}%")
    
    print("="*60)
    
    return resultados


def executar_todas_analises_fator_carga():
    """Executa todas as análises relacionadas ao fator de carga"""
    print("="*70)
    print("ANÁLISES COMPLETAS - FATOR DE CARGA")
    print("="*70)
    
    resultados = {}
    
    # 1. Impacto básico do fator de carga
    resultados['impacto_basico'] = testar_impacto_fator_carga()
    
    # 2. Análise detalhada α vs desempenho
    resultados['analise_detalhada'] = analisar_relacao_alpha_desempenho()
    
    print("\n" + "="*70)
    print("TODAS AS ANÁLISES DE FATOR DE CARGA CONCLUÍDAS!")
    print("="*70)
    print("\nRECOMENDAÇÕES FINAIS:")
    print("  • Para aplicações gerais: α entre 1.0 e 2.0")
    print("  • Para performance crítica: α entre 0.5 e 1.0")
    print("  • Para economia de memória: α entre 2.0 e 5.0")
    print("  • Evitar: α > 10.0 (degradação significativa)")
    print("="*70)
    
    return resultados


if __name__ == "__main__":
    resultados = executar_todas_analises_fator_carga()
