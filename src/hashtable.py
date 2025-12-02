"""
Implementação de Hashtable com Encadeamento para Colisões

Este módulo faz parte do artigo:
"Implementação de Estruturas de Dados Lineares: Hashtable, Pilha e Fila em Python"

Autores: Silveira et al. (2025)
"""


class HashTable:
    """
    Implementação de hashtable usando encadeamento (chaining) para colisões.
    
    A hashtable permite associação direta de chaves a valores, oferecendo
    operações de inserção, busca e remoção em tempo O(1) médio.
    
    Método de resolução de colisões:
        - Encadeamento: cada bucket armazena uma lista de pares (chave, valor)
    
    Função hash:
        - hash(chave) % tamanho
        - Usa função hash() nativa do Python
    
    Complexidade:
        - insert(): O(1) médio, O(1+α) considerando colisões
        - search(): O(1) médio, O(1+α) considerando colisões
        - delete(): O(1) médio, O(1+α) considerando colisões
        onde α é o fator de carga (elementos/tamanho)
    
    Attributes:
        size (int): Número de buckets na tabela
        table (list): Lista de listas (buckets) contendo pares (chave, valor)
        count (int): Número total de elementos armazenados
    
    Examples:
        >>> ht = HashTable(size=10)
        >>> ht.insert("nome", "João")
        >>> ht.search("nome")
        'João'
        >>> ht.load_factor()
        0.1
    """
    
    def __init__(self, size=10):
        """
        Inicializa a hashtable com tamanho especificado.
        
        Args:
            size (int): Tamanho inicial da tabela (número de buckets).
                       Default: 10
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def _hash_function(self, key):
        """
        Calcula o índice do bucket para uma chave.
        
        Utiliza a função hash() nativa do Python combinada com operador
        módulo para mapear a chave para um índice válido.
        
        Args:
            key: Chave a ser hasheada (deve ser hashable)
        
        Returns:
            int: Índice do bucket (0 a size-1)
        
        Complexity:
            O(1)
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """
        Insere um novo par chave-valor ou atualiza valor existente.
        
        Se a chave já existe, seu valor é atualizado sem incrementar count.
        Caso contrário, um novo par é adicionado.
        
        Args:
            key: Chave do par (deve ser hashable: int, str, tuple, etc.)
            value: Valor associado à chave (qualquer tipo Python)
        
        Complexity:
            O(1) médio, O(1+α) no pior caso
            onde α = count/size (elementos por bucket em média)
        """
        index = self._hash_function(key)
        
        # Verifica se chave já existe (atualizar)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        # Adiciona novo par
        self.table[index].append((key, value))
        self.count += 1
    
    def search(self, key):
        """
        Busca um valor pela chave.
        
        Args:
            key: Chave a ser buscada
        
        Returns:
            Valor associado à chave
        
        Raises:
            KeyError: Se a chave não for encontrada
        
        Complexity:
            O(1) médio, O(1+α) no pior caso
        """
        index = self._hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        raise KeyError(f"Chave '{key}' não encontrada")
    
    def delete(self, key):
        """
        Remove um par chave-valor da hashtable.
        
        Args:
            key: Chave a ser removida
        
        Returns:
            Valor que foi removido
        
        Raises:
            KeyError: Se a chave não for encontrada
        
        Complexity:
            O(1) médio, O(1+α) no pior caso
        """
        index = self._hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return v
        
        raise KeyError(f"Chave '{key}' não encontrada")
    
    def load_factor(self):
        """
        Calcula o fator de carga da hashtable.
        
        O fator de carga (α) representa a média de elementos por bucket.
        Valores típicos recomendados: 0.5 a 2.0
        
        Returns:
            float: Razão entre número de elementos e tamanho da tabela
        
        Complexity:
            O(1)
        """
        return self.count / self.size
    
    def get_distribution(self):
        """
        Retorna a distribuição de elementos por bucket.
        
        Útil para análise de qualidade da função hash e uniformidade
        da distribuição de colisões.
        
        Returns:
            list: Lista com o número de elementos em cada bucket
        
        Complexity:
            O(size)
        
        Example:
            >>> ht.get_distribution()
            [3, 2, 0, 1, 2, ...]  # bucket 0 tem 3 elem, bucket 1 tem 2, etc
        """
        return [len(bucket) for bucket in self.table]
    
    def __repr__(self):
        """Representação em string da hashtable para debugging."""
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return f"HashTable(size={self.size}, count={self.count}, items={dict(items)})"
    
    def __len__(self):
        """Permite usar len(hashtable)."""
        return self.count
    
    def __contains__(self, key):
        """Permite usar 'key in hashtable'."""
        try:
            self.search(key)
            return True
        except KeyError:
            return False


if __name__ == "__main__":
    # Exemplo de uso básico
    print("=== Demonstração da Hashtable ===\n")
    
    ht = HashTable(size=5)
    
    print("1. Inserindo pares chave-valor:")
    ht.insert("nome", "João")
    ht.insert("idade", 25)
    ht.insert("cidade", "São Paulo")
    print(f"   {ht}")
    
    print("\n2. Buscando valores:")
    print(f"   nome: {ht.search('nome')}")
    print(f"   idade: {ht.search('idade')}")
    
    print("\n3. Fator de carga:")
    print(f"   α = {ht.load_factor():.2f}")
    print(f"   (3 elementos / 5 buckets)")
    
    print("\n4. Atualizando valor existente:")
    print(f"   Antes: idade = {ht.search('idade')}")
    ht.insert("idade", 26)
    print(f"   Depois: idade = {ht.search('idade')}")
    print(f"   Count: {ht.count} (não aumentou)")
    
    print("\n5. Removendo elemento:")
    valor = ht.delete("cidade")
    print(f"   Removido: 'cidade' = {valor}")
    print(f"   Count: {ht.count}")
    
    print("\n6. Testando colisões (forçando com size pequeno):")
    ht_pequena = HashTable(size=3)
    for i in range(9):
        ht_pequena.insert(f"key{i}", i * 10)
    
    print(f"   Inseridos: 9 elementos em {ht_pequena.size} buckets")
    print(f"   Fator de carga: α = {ht_pequena.load_factor():.2f}")
    print(f"   Distribuição: {ht_pequena.get_distribution()}")
    
    print("\n7. Operador 'in':")
    print(f"   'nome' in ht: {'nome' in ht}")
    print(f"   'telefone' in ht: {'telefone' in ht}")
    
    print("\n8. Tratamento de erro:")
    try:
        ht.search("inexistente")
    except KeyError as e:
        print(f"   Exceção capturada: {e}")
