"""
Testes Funcionais - Fila (Queue)

Este módulo contém os testes funcionais para validar a corretude
da implementação da estrutura de dados Fila.

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from queue import Queue


def test_enqueue_dequeue_fifo():
    """Teste 1: Verifica comportamento FIFO (First In, First Out)"""
    print("\n[TESTE 1] Enqueue/Dequeue FIFO")
    fila = Queue()
    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    
    r1 = fila.dequeue()
    r2 = fila.dequeue()
    r3 = fila.dequeue()
    
    assert r1 == "A" and r2 == "B" and r3 == "C", f"Esperado: A,B,C | Obtido: {r1},{r2},{r3}"
    print("✓ PASSOU")
    print(f"  Enfileirou: A, B, C")
    print(f"  Desenfileirou: {r1}, {r2}, {r3} (ordem FIFO correta)")
    return True


def test_excecao_fila_vazia():
    """Teste 2: Verifica se exceção é lançada em dequeue() de fila vazia"""
    print("\n[TESTE 2] Exceção em fila vazia")
    fila_vazia = Queue()
    
    try:
        fila_vazia.dequeue()
        print("✗ FALHOU - Não lançou exceção")
        return False
    except IndexError as e:
        print("✓ PASSOU")
        print(f"  Exceção lançada: {e}")
        return True


def test_front_nao_remove():
    """Teste 3: Verifica que front() não remove elementos"""
    print("\n[TESTE 3] Front não remove elemento")
    fila = Queue()
    fila.enqueue(100)
    
    f1 = fila.front()
    f2 = fila.front()
    f3 = fila.front()
    tamanho = fila.size()
    
    assert f1 == 100 and f2 == 100 and f3 == 100 and tamanho == 1, \
        f"Front: {f1},{f2},{f3} | Tamanho: {tamanho}"
    print("✓ PASSOU")
    print(f"  Front retornou: {f1}, {f2}, {f3}")
    print(f"  Tamanho permaneceu: {tamanho}")
    return True


def test_is_empty():
    """Teste 4: Verifica funcionamento do método is_empty()"""
    print("\n[TESTE 4] is_empty funciona")
    fila = Queue()
    
    vazio1 = fila.is_empty()
    fila.enqueue(5)
    vazio2 = fila.is_empty()
    fila.dequeue()
    vazio3 = fila.is_empty()
    
    assert vazio1 == True and vazio2 == False and vazio3 == True, \
        f"Valores: {vazio1}, {vazio2}, {vazio3}"
    print("✓ PASSOU")
    print(f"  Fila nova: vazia = {vazio1}")
    print(f"  Após enqueue: vazia = {vazio2}")
    print(f"  Após dequeue: vazia = {vazio3}")
    return True


def test_escalabilidade():
    """Teste 5: Verifica suporte a grandes volumes (10.000 elementos)"""
    print("\n[TESTE 5] Suporta 10.000 elementos")
    fila = Queue()
    
    for i in range(10000):
        fila.enqueue(i)
    
    tamanho_final = fila.size()
    assert tamanho_final == 10000, f"Esperado: 10000 | Obtido: {tamanho_final}"
    print("✓ PASSOU")
    print(f"  Inseridos: 10.000 elementos")
    print(f"  Tamanho: {tamanho_final}")
    return True


def test_operacoes_intercaladas():
    """Teste 6: Verifica operações intercaladas de enqueue e dequeue"""
    print("\n[TESTE 6] Operações intercaladas")
    fila = Queue()
    fila.enqueue(1)
    fila.enqueue(2)
    d1 = fila.dequeue()  # 1
    fila.enqueue(3)
    d2 = fila.dequeue()  # 2
    d3 = fila.dequeue()  # 3
    
    assert d1 == 1 and d2 == 2 and d3 == 3, f"Esperado: 1,2,3 | Obtido: {d1},{d2},{d3}"
    print("✓ PASSOU")
    print(f"  Sequência: enqueue(1,2), dequeue, enqueue(3), dequeue(2x)")
    print(f"  Resultados: {d1}, {d2}, {d3} (correto)")
    return True


def executar_todos_testes():
    """Executa todos os testes e gera relatório"""
    print("="*60)
    print("TESTES FUNCIONAIS - FILA")
    print("="*60)
    
    testes = [
        ("Enqueue/Dequeue FIFO", test_enqueue_dequeue_fifo),
        ("Exceção fila vazia", test_excecao_fila_vazia),
        ("Front não remove", test_front_nao_remove),
        ("is_empty", test_is_empty),
        ("10.000 elementos", test_escalabilidade),
        ("Operações intercaladas", test_operacoes_intercaladas),
    ]
    
    resultados = []
    
    for nome, teste_func in testes:
        try:
            resultado = teste_func()
            resultados.append(("✓", nome, resultado))
        except Exception as e:
            print(f"✗ FALHOU - Exceção não esperada: {e}")
            resultados.append(("✗", nome, False))
    
    # RESUMO
    print("\n" + "="*60)
    print("RESUMO DOS TESTES - FILA")
    print("="*60)
    
    for simbolo, nome, passou in resultados:
        print(f"{nome:30} {simbolo}")
    
    print("="*60)
    
    total_passou = sum(1 for _, _, passou in resultados if passou)
    total_testes = len(resultados)
    
    if total_passou == total_testes:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("\n📋 TABELA PARA O ARTIGO:")
        print("-"*60)
        print("| Teste                          | Resultado  |")
        print("+--------------------------------+------------+")
        for _, nome, passou in resultados:
            print(f"| {nome:30} | {'✓':^10} |")
        print("+--------------------------------+------------+")
    else:
        print(f"⚠️  {total_passou}/{total_testes} testes passaram")
    
    print("="*60)
    
    return total_passou == total_testes


if __name__ == "__main__":
    sucesso = executar_todos_testes()
    sys.exit(0 if sucesso else 1)
