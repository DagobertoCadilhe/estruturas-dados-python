"""
Implementação de Pilha (Stack) - LIFO (Last In, First Out)

Este módulo faz parte do artigo:
"Implementação de Estruturas de Dados Lineares: Hashtable, Pilha e Fila em Python"

Autores: Silveira et al. (2025)
"""


class Stack:
    """
    Implementação de uma pilha usando lista Python como estrutura interna.
    
    A pilha segue o princípio LIFO (Last In, First Out), onde o último
    elemento inserido é o primeiro a ser removido.
    
    Complexidade:
        - push(): O(1) amortizado
        - pop(): O(1)
        - peek(): O(1)
        - is_empty(): O(1)
        - size(): O(1)
    
    Attributes:
        _items (list): Lista Python contendo os elementos da pilha
    
    Examples:
        >>> pilha = Stack()
        >>> pilha.push(10)
        >>> pilha.push(20)
        >>> pilha.pop()
        20
        >>> pilha.peek()
        10
    """
    
    def __init__(self):
        """Inicializa uma pilha vazia."""
        self._items = []
    
    def push(self, item):
        """
        Adiciona um elemento no topo da pilha.
        
        Args:
            item: Elemento a ser adicionado (qualquer tipo Python)
        
        Complexity:
            O(1) amortizado devido a realocações ocasionais da lista
        """
        self._items.append(item)
    
    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.
        
        Returns:
            O elemento removido do topo
        
        Raises:
            IndexError: Se a pilha estiver vazia
        
        Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Pop de pilha vazia")
        return self._items.pop()
    
    def peek(self):
        """
        Retorna o elemento do topo sem removê-lo.
        
        Returns:
            O elemento no topo da pilha
        
        Raises:
            IndexError: Se a pilha estiver vazia
        
        Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Peek de pilha vazia")
        return self._items[-1]
    
    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            bool: True se vazia, False caso contrário
        
        Complexity:
            O(1)
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Retorna o número de elementos na pilha.
        
        Returns:
            int: Quantidade de elementos armazenados
        
        Complexity:
            O(1)
        """
        return len(self._items)
    
    def __repr__(self):
        """Representação em string da pilha para debugging."""
        return f"Stack({self._items})"
    
    def __len__(self):
        """Permite usar len(pilha)."""
        return self.size()


if __name__ == "__main__":
    # Exemplo de uso básico
    print("=== Demonstração da Pilha ===\n")
    
    pilha = Stack()
    
    print("1. Empilhando elementos: 10, 20, 30")
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    print(f"   Pilha: {pilha}")
    print(f"   Tamanho: {pilha.size()}")
    
    print("\n2. Visualizando topo (peek):")
    print(f"   Topo: {pilha.peek()}")
    print(f"   Tamanho: {pilha.size()} (não mudou)")
    
    print("\n3. Desempilhando elementos:")
    print(f"   pop() = {pilha.pop()}")
    print(f"   pop() = {pilha.pop()}")
    print(f"   Tamanho: {pilha.size()}")
    
    print("\n4. Estado da pilha:")
    print(f"   Pilha: {pilha}")
    print(f"   Vazia? {pilha.is_empty()}")
    
    print("\n5. Esvaziando completamente:")
    pilha.pop()
    print(f"   Vazia? {pilha.is_empty()}")
    
    print("\n6. Tentando pop em pilha vazia:")
    try:
        pilha.pop()
    except IndexError as e:
        print(f"   Exceção capturada: {e}")
