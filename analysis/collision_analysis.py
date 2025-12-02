"""
Análise de Colisões - Hashtable

Este módulo analisa a qualidade da distribuição de colisões
na hashtable e valida a uniformidade da função hash.

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from hashtable import HashTable


def analisar_distribuicao_colisoes():
    """
    Analisa a distribuição de elementos por bucket em uma hashtable
    com fator de carga alto (α=10.0).
    """
    print("\n" + "="*60)
    print("ANÁLISE DE COLISÕES - HASHTABLE")
    print("="*60)
    
    ht = HashTable(size=100)
    
    # Inserir 1000 elementos (α = 10.0)
    print("\nInserindo 1000 elementos em tabela size=100...")
    for i in range(1000):
        ht.insert(f"key{i}", i)
    
    distribuicao = ht.get_distribution()
    
    print(f"\nTotal de elementos: {ht.count}")
    print(f"Tamanho da tabela: {ht.size}")
    print(f"Fator de carga: {ht.load_factor():.2f}")
    
    # Estatísticas por faixa
    vazios = distribuicao.count(0)
    leves = len([x for x in distribuicao if 1 <= x <= 5])
    medios = len([x for x in distribuicao if 6 <= x <= 10])
    pesados = len([x for x in distribuicao if 11 <= x <= 15])
    muito_pesados = len([x for x in distribuicao if 16 <= x <= 20])
    extremos = len([x for x in distribuicao if x > 20])
    
    print(f"\n{'Elementos/Bucket':<20} {'Qtd Buckets':<15} {'Porcentagem':<15}")
    print("-" * 50)
    print(f"{'0':<20} {vazios:<15} {vazios/100*100:<15.1f}%")
    print(f"{'1-5':<20} {leves:<15} {leves/100*100:<15.1f}%")
    print(f"{'6-10':<20} {medios:<15} {medios/100*100:<15.1f}%")
    print(f"{'11-15':<20} {pesados:<15} {pesados/100*100:<15.1f}%")
    print(f"{'16-20':<20} {muito_pesados:<15} {muito_pesados/100*100:<15.1f}%")
    print(f"{'>20':<20} {extremos:<15} {extremos/100*100:<15.1f}%")
    
    # Estatísticas adicionais
    maximo = max(distribuicao)
    minimo = min(distribuicao)
    media = sum(distribuicao) / len(distribuicao)
    
    # Calcular desvio padrão
    variancia = sum((x - media) ** 2 for x in distribuicao) / len(distribuicao)
    desvio_padrao = variancia ** 0.5
    
    print(f"\nEstatísticas:")
    print(f"  Bucket mais cheio: {maximo} elementos")
    print(f"  Bucket mais vazio: {minimo} elementos")
    print(f"  Média: {media:.2f} elementos/bucket")
    print(f"  Desvio padrão: {desvio_padrao:.2f}")
    print(f"  Buckets vazios: {vazios} ({vazios/100*100:.1f}%)")
    
    # Avaliar qualidade da distribuição
    print(f"\nAVALIAÇÃO DA DISTRIBUIÇÃO:")
    if desvio_padrao < media * 0.5:
        qualidade = "EXCELENTE"
        print(f"  ✓ {qualidade} - Distribuição muito uniforme")
    elif desvio_padrao < media:
        qualidade = "BOA"
        print(f"  ✓ {qualidade} - Distribuição adequada")
    else:
        qualidade = "IRREGULAR"
        print(f"  ⚠️  {qualidade} - Muitos clusters")
    
    if vazios < 5:
        print("  ✓ Aproveitamento eficiente do espaço")
    else:
        print(f"  ⚠️  {vazios}% de buckets vazios (desperdício)")
    
    # Calcular porcentagem dentro de ±50% da média
    faixa_ideal_min = media * 0.5
    faixa_ideal_max = media * 1.5
    dentro_faixa = len([x for x in distribuicao if faixa_ideal_min <= x <= faixa_ideal_max])
    pct_faixa = (dentro_faixa / len(distribuicao)) * 100
    
    print(f"\nUniformidade:")
    print(f"  {pct_faixa:.1f}% dos buckets estão dentro de ±50% da média")
    print(f"  Desvio padrão representa {(desvio_padrao/media)*100:.1f}% da média")
    
    print("\n" + "="*60)
    print("TABELA PARA COPIAR NO ARTIGO:")
    print("="*60)
    print("")
    print("Tabela X - Distribuição de Colisões (1.000 elementos, size=100, α=10.0)")
    print("")
    print("+----------------------+---------------+----------------+")
    print("| Elementos/Bucket     | Qtd Buckets   | Porcentagem    |")
    print("+----------------------+---------------+----------------+")
    print(f"| 0                    | {vazios:<13} | {vazios/100*100:<14.1f}% |")
    print(f"| 1-5                  | {leves:<13} | {leves/100*100:<14.1f}% |")
    print(f"| 6-10                 | {medios:<13} | {medios/100*100:<14.1f}% |")
    print(f"| 11-15                | {pesados:<13} | {pesados/100*100:<14.1f}% |")
    print(f"| 16-20                | {muito_pesados:<13} | {muito_pesados/100*100:<14.1f}% |")
    print(f"| >20                  | {extremos:<13} | {extremos/100*100:<14.1f}% |")
    print("+----------------------+---------------+----------------+")
    print("")
    print("Estatísticas:")
    print(f"  Bucket mais cheio: {maximo}")
    print(f"  Bucket mais vazio: {minimo}")
    print(f"  Média: {media:.2f}")
    print(f"  Desvio padrão: {desvio_padrao:.2f}")
    print(f"  Avaliação: {qualidade}")
    print("="*60)
    
    return {
        'distribuicao': distribuicao,
        'estatisticas': {
            'media': media,
            'desvio_padrao': desvio_padrao,
            'maximo': maximo,
            'minimo': minimo,
            'vazios': vazios
        },
        'faixas': {
            'vazios': vazios,
            'leves': leves,
            'medios': medios,
            'pesados': pesados,
            'muito_pesados': muito_pesados,
            'extremos': extremos
        },
        'qualidade': qualidade,
        'pct_faixa_ideal': pct_faixa
    }


def analisar_qualidade_hash_diferentes_tamanhos():
    """
    Testa a qualidade da distribuição para diferentes tamanhos de tabela.
    """
    print("\n" + "="*60)
    print("QUALIDADE DO HASH - DIFERENTES TAMANHOS")
    print("="*60)
    print("\nVerifica se a distribuição permanece uniforme em várias configurações\n")
    
    configs = [
        (100, 10),    # α = 10
        (500, 50),    # α = 10
        (1000, 100),  # α = 10
        (1000, 200),  # α = 5
        (1000, 500),  # α = 2
    ]
    
    print(f"{'Elementos':<12} {'Size':<8} {'α':<8} {'Desvio/Média':<15} {'Qualidade':<12}")
    print("-" * 55)
    
    resultados = []
    
    for n_elementos, tamanho in configs:
        ht = HashTable(size=tamanho)
        
        for i in range(n_elementos):
            ht.insert(f"key{i}", i)
        
        distribuicao = ht.get_distribution()
        media = sum(distribuicao) / len(distribuicao)
        variancia = sum((x - media) ** 2 for x in distribuicao) / len(distribuicao)
        desvio = variancia ** 0.5
        
        razao = desvio / media if media > 0 else 0
        alpha = ht.load_factor()
        
        if razao < 0.5:
            qualidade = "EXCELENTE"
        elif razao < 1.0:
            qualidade = "BOA"
        else:
            qualidade = "IRREGULAR"
        
        print(f"{n_elementos:<12} {tamanho:<8} {alpha:<8.2f} {razao:<15.2f} {qualidade:<12}")
        
        resultados.append({
            'elementos': n_elementos,
            'tamanho': tamanho,
            'alpha': alpha,
            'razao_desvio': razao,
            'qualidade': qualidade
        })
    
    print("\n" + "="*60)
    print("INTERPRETAÇÃO:")
    print("  Desvio/Média < 0.5: Distribuição EXCELENTE")
    print("  Desvio/Média < 1.0: Distribuição BOA")
    print("  Desvio/Média ≥ 1.0: Distribuição IRREGULAR")
    print("")
    
    todas_boas = all(r['razao_desvio'] < 1.0 for r in resultados)
    if todas_boas:
        print("  ✓ Função hash mantém qualidade em TODAS as configurações")
    else:
        print("  ⚠️  Algumas configurações apresentam distribuição irregular")
    
    print("="*60)
    
    return resultados


def executar_todas_analises():
    """Executa todas as análises de colisão"""
    print("="*70)
    print("ANÁLISES COMPLETAS DE COLISÃO - HASHTABLE")
    print("="*70)
    
    resultados = {}
    
    # 1. Análise principal de distribuição
    resultados['distribuicao'] = analisar_distribuicao_colisoes()
    
    # 2. Qualidade em diferentes tamanhos
    resultados['diferentes_tamanhos'] = analisar_qualidade_hash_diferentes_tamanhos()
    
    print("\n" + "="*70)
    print("TODAS AS ANÁLISES CONCLUÍDAS!")
    print("="*70)
    
    return resultados


if __name__ == "__main__":
    resultados = executar_todas_analises()
