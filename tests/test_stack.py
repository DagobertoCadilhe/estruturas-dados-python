"""
Testes Funcionais - Pilha (Stack)

Este módulo contém os testes funcionais para validar a corretude
da implementação da estrutura de dados Pilha.

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from stack import Stack


def test_push_pop_lifo():
    """Teste 1: Verifica comportamento LIFO (Last In, First Out)"""
    print("\n[TESTE 1] Push/Pop LIFO")
    pilha = Stack()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    
    r1 = pilha.pop()
    r2 = pilha.pop()
    r3 = pilha.pop()
    
    assert r1 == 3 and r2 == 2 and r3 == 1, f"Esperado: 3,2,1 | Obtido: {r1},{r2},{r3}"
    print("✓ PASSOU")
    print(f"  Empilhou: 1, 2, 3")
    print(f"  Desempilhou: {r1}, {r2}, {r3} (ordem LIFO correta)")
    return True


def test_excecao_pilha_vazia():
    """Teste 2: Verifica se exceção é lançada em pop() de pilha vazia"""
    print("\n[TESTE 2] Exceção em pilha vazia")
    pilha_vazia = Stack()
    
    try:
        pilha_vazia.pop()
        print("✗ FALHOU - Não lançou exceção")
        return False
    except IndexError as e:
        print("✓ PASSOU")
        print(f"  Exceção lançada: {e}")
        return True


def test_peek_nao_remove():
    """Teste 3: Verifica que peek() não remove elementos"""
    print("\n[TESTE 3] Peek não remove elemento")
    pilha = Stack()
    pilha.push(100)
    
    p1 = pilha.peek()
    p2 = pilha.peek()
    p3 = pilha.peek()
    tamanho = pilha.size()
    
    assert p1 == 100 and p2 == 100 and p3 == 100 and tamanho == 1, \
        f"Peek: {p1},{p2},{p3} | Tamanho: {tamanho}"
    print("✓ PASSOU")
    print(f"  Peek retornou: {p1}, {p2}, {p3}")
    print(f"  Tamanho permaneceu: {tamanho}")
    return True


def test_is_empty():
    """Teste 4: Verifica funcionamento do método is_empty()"""
    print("\n[TESTE 4] is_empty funciona")
    pilha = Stack()
    
    vazio1 = pilha.is_empty()
    pilha.push(5)
    vazio2 = pilha.is_empty()
    pilha.pop()
    vazio3 = pilha.is_empty()
    
    assert vazio1 == True and vazio2 == False and vazio3 == True, \
        f"Valores: {vazio1}, {vazio2}, {vazio3}"
    print("✓ PASSOU")
    print(f"  Pilha nova: vazia = {vazio1}")
    print(f"  Após push: vazia = {vazio2}")
    print(f"  Após pop: vazia = {vazio3}")
    return True


def test_escalabilidade():
    """Teste 5: Verifica suporte a grandes volumes (10.000 elementos)"""
    print("\n[TESTE 5] Suporta 10.000 elementos")
    pilha = Stack()
    
    for i in range(10000):
        pilha.push(i)
    
    tamanho_final = pilha.size()
    assert tamanho_final == 10000, f"Esperado: 10000 | Obtido: {tamanho_final}"
    print("✓ PASSOU")
    print(f"  Inseridos: 10.000 elementos")
    print(f"  Tamanho: {tamanho_final}")
    return True


def test_peek_excecao_vazio():
    """Teste 6: Verifica se peek() lança exceção em pilha vazia"""
    print("\n[TESTE 6] Peek em pilha vazia lança exceção")
    pilha_vazia = Stack()
    
    try:
        pilha_vazia.peek()
        print("✗ FALHOU - Não lançou exceção")
        return False
    except IndexError as e:
        print("✓ PASSOU")
        print(f"  Exceção lançada: {e}")
        return True


def executar_todos_testes():
    """Executa todos os testes e gera relatório"""
    print("="*60)
    print("TESTES FUNCIONAIS - PILHA")
    print("="*60)
    
    testes = [
        ("Push/Pop LIFO", test_push_pop_lifo),
        ("Exceção pop vazio", test_excecao_pilha_vazia),
        ("Peek não remove", test_peek_nao_remove),
        ("is_empty", test_is_empty),
        ("10.000 elementos", test_escalabilidade),
        ("Exceção peek vazio", test_peek_excecao_vazio),
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
    print("RESUMO DOS TESTES - PILHA")
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
