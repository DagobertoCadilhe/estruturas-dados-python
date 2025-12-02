"""
Testes Funcionais - Hashtable

Este módulo contém os testes funcionais para validar a corretude
da implementação da estrutura de dados Hashtable.

Artigo: "Implementação de Estruturas de Dados Lineares"
Autores: Silveira et al. (2025)
"""

import sys
from pathlib import Path

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from hashtable import HashTable


def test_insert_search_delete():
    """Teste 1: Verifica operações básicas de insert, search e delete"""
    print("\n[TESTE 1] Insert/Search/Delete")
    ht = HashTable()
    ht.insert("nome", "João")
    ht.insert("idade", 25)
    ht.insert("cidade", "SP")
    
    busca1 = ht.search("nome")
    busca2 = ht.search("idade")
    
    deleted = ht.delete("idade")
    
    try:
        ht.search("idade")
        delete_ok = False
    except KeyError:
        delete_ok = True
    
    assert busca1 == "João" and busca2 == 25 and deleted == 25 and delete_ok, \
        f"Valores: {busca1}, {busca2}, {deleted}, {delete_ok}"
    print("✓ PASSOU")
    print(f"  Insert: 3 pares inseridos")
    print(f"  Search: 'nome'→'{busca1}', 'idade'→{busca2}")
    print(f"  Delete: removeu 'idade'→{deleted}")
    print(f"  Search após delete: KeyError lançado corretamente")
    return True


def test_atualizacao_valor():
    """Teste 2: Verifica atualização de valor existente"""
    print("\n[TESTE 2] Atualização de valor existente")
    ht = HashTable()
    ht.insert("key", "valor1")
    count_antes = ht.count
    
    ht.insert("key", "valor2")
    count_depois = ht.count
    valor_final = ht.search("key")
    
    assert valor_final == "valor2" and count_antes == 1 and count_depois == 1, \
        f"Valor: {valor_final}, Count: {count_antes}→{count_depois}"
    print("✓ PASSOU")
    print(f"  Valor inicial: 'valor1'")
    print(f"  Após update: '{valor_final}'")
    print(f"  Count permaneceu: {count_depois} (não duplicou)")
    return True


def test_excecao_search():
    """Teste 3: Verifica exceção em search de chave inexistente"""
    print("\n[TESTE 3] Exceção em search de chave inexistente")
    ht = HashTable()
    
    try:
        ht.search("nao_existe")
        print("✗ FALHOU - Não lançou exceção")
        return False
    except KeyError as e:
        print("✓ PASSOU")
        print(f"  Exceção lançada: {e}")
        return True


def test_excecao_delete():
    """Teste 4: Verifica exceção em delete de chave inexistente"""
    print("\n[TESTE 4] Exceção em delete de chave inexistente")
    ht = HashTable()
    
    try:
        ht.delete("nao_existe")
        print("✗ FALHOU - Não lançou exceção")
        return False
    except KeyError as e:
        print("✓ PASSOU")
        print(f"  Exceção lançada: {e}")
        return True


def test_colisoes():
    """Teste 5: Verifica tratamento correto de colisões"""
    print("\n[TESTE 5] Tratamento de colisões")
    ht_pequena = HashTable(size=5)
    
    # Inserir 25 elementos (forçar colisões)
    for i in range(25):
        ht_pequena.insert(f"key{i}", i * 10)
    
    # Verificar que todos são recuperáveis
    todos_ok = True
    for i in range(25):
        try:
            valor = ht_pequena.search(f"key{i}")
            if valor != i * 10:
                todos_ok = False
                break
        except KeyError:
            todos_ok = False
            break
    
    assert todos_ok and ht_pequena.count == 25, \
        f"Recuperação: {todos_ok}, Count: {ht_pequena.count}"
    print("✓ PASSOU")
    print(f"  Inseridos: 25 elementos em tabela size=5")
    print(f"  Todos recuperáveis corretamente")
    print(f"  Count: {ht_pequena.count}")
    return True


def test_load_factor():
    """Teste 6: Verifica cálculo do fator de carga"""
    print("\n[TESTE 6] Load factor")
    ht = HashTable(size=10)
    
    for i in range(50):
        ht.insert(i, i)
    
    lf = ht.load_factor()
    
    assert lf == 5.0 and ht.count == 50, f"Load factor: {lf}, Count: {ht.count}"
    print("✓ PASSOU")
    print(f"  50 elementos em size=10")
    print(f"  Load factor: {lf} (correto: 50/10 = 5.0)")
    return True


def test_tipos_diversos():
    """Teste 7: Verifica suporte a tipos diversos como chave"""
    print("\n[TESTE 7] Tipos diversos como chave")
    ht = HashTable()
    
    ht.insert(42, "int key")
    ht.insert("string", "string key")
    ht.insert((1, 2), "tuple key")
    
    v1 = ht.search(42)
    v2 = ht.search("string")
    v3 = ht.search((1, 2))
    
    assert v1 == "int key" and v2 == "string key" and v3 == "tuple key", \
        f"Valores: {v1}, {v2}, {v3}"
    print("✓ PASSOU")
    print(f"  Int key: {v1}")
    print(f"  String key: {v2}")
    print(f"  Tuple key: {v3}")
    return True


def test_grande_escala():
    """Teste 8: Verifica operações em grande escala"""
    print("\n[TESTE 8] Operações em grande escala")
    ht = HashTable(size=100)
    
    # Inserir 1000 elementos
    for i in range(1000):
        ht.insert(f"key{i}", i)
    
    # Buscar todos
    busca_ok = True
    for i in range(1000):
        if ht.search(f"key{i}") != i:
            busca_ok = False
            break
    
    # Deletar metade
    for i in range(0, 1000, 2):
        ht.delete(f"key{i}")
    
    count_final = ht.count
    
    assert busca_ok and count_final == 500, \
        f"Busca ok: {busca_ok}, Count final: {count_final}"
    print("✓ PASSOU")
    print(f"  Inseridos: 1000 elementos")
    print(f"  Todos recuperáveis: Sim")
    print(f"  Deletados: 500 elementos")
    print(f"  Count final: {count_final}")
    return True


def executar_todos_testes():
    """Executa todos os testes e gera relatório"""
    print("="*60)
    print("TESTES FUNCIONAIS - HASHTABLE")
    print("="*60)
    
    testes = [
        ("Insert/Search/Delete", test_insert_search_delete),
        ("Atualização de valor", test_atualizacao_valor),
        ("Exceção search", test_excecao_search),
        ("Exceção delete", test_excecao_delete),
        ("Tratamento de colisões", test_colisoes),
        ("Load factor", test_load_factor),
        ("Tipos diversos", test_tipos_diversos),
        ("Grande escala (1000 elem)", test_grande_escala),
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
    print("RESUMO DOS TESTES - HASHTABLE")
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
