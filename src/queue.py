"""
Implementação de Fila (Queue) - FIFO (First In, First Out)

Este módulo faz parte do artigo:
"Implementação de Estruturas de Dados Lineares: Hashtable, Pilha e Fila em Python"

Autores: Silveira et al. (2025)
"""

from collections import deque


class Queue:
    """
    Implementação de uma fila usando collections.deque como estrutura interna.
    
    A fila segue o princípio FIFO (First In, First Out), onde o primeiro
    elemento inserido é o primeiro a ser removido.
    
    Utilizamos deque ao invés de lista comum porque:
    - deque oferece O(1) para operações em ambas as extremidades
    - Lista comum tem O(n) para pop(0), degradando performance
    
    Complexidade:
        - enqueue(): O(1)
        - dequeue(): O(1)
        - front(): O(1)
        - is_empty(): O(1)
        - size(): O(1)
    
    Attributes:
        _items (deque): Collections.deque contendo os elementos da fila
    
    Examples:
        >>> fila = Queue()
        >>> fila.enqueue(10)
        >>> fila.enqueue(20)
        >>> fila.dequeue()
        10
        >>> fila.front()
        20
    """
    
    def __init__(self):
        """Inicializa uma fila vazia."""
        self._items = deque()
    
    def enqueue(self, item):
        """
        Adiciona um elemento ao final da fila.
        
        Args:
            item: Elemento a ser adicionado (qualquer tipo Python)
        
        Complexity:
            O(1)
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove e retorna o elemento da frente da fila.
        
        Returns:
            O elemento removido da frente
        
        Raises:
            IndexError: Se a fila estiver vazia
        
        Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Dequeue de fila vazia")
        return self._items.popleft()
    
    def front(self):
        """
        Retorna o elemento da frente sem removê-lo.
        
        Returns:
            O elemento na frente da fila
        
        Raises:
            IndexError: Se a fila estiver vazia
        
        Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Front de fila vazia")
        return self._items[0]
    
    def is_empty(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se vazia, False caso contrário
        
        Complexity:
            O(1)
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Retorna o número de elementos na fila.
        
        Returns:
            int: Quantidade de elementos armazenados
        
        Complexity:
            O(1)
        """
        return len(self._items)
    
    def __repr__(self):
        """Representação em string da fila para debugging."""
        return f"Queue({list(self._items)})"
    
    def __len__(self):
        """Permite usar len(fila)."""
        return self.size()


if __name__ == "__main__":
    # Exemplo de uso básico
    print("=== Demonstração da Fila ===\n")
    
    fila = Queue()
    
    print("1. Enfileirando elementos: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    print(f"   Fila: {fila}")
    print(f"   Tamanho: {fila.size()}")
    
    print("\n2. Visualizando frente (front):")
    print(f"   Frente: {fila.front()}")
    print(f"   Tamanho: {fila.size()} (não mudou)")
    
    print("\n3. Desenfileirando elementos (FIFO):")
    print(f"   dequeue() = {fila.dequeue()}")
    print(f"   dequeue() = {fila.dequeue()}")
    print(f"   Tamanho: {fila.size()}")
    
    print("\n4. Estado da fila:")
    print(f"   Fila: {fila}")
    print(f"   Vazia? {fila.is_empty()}")
    
    print("\n5. Esvaziando completamente:")
    fila.dequeue()
    print(f"   Vazia? {fila.is_empty()}")
    
    print("\n6. Tentando dequeue em fila vazia:")
    try:
        fila.dequeue()
    except IndexError as e:
        print(f"   Exceção capturada: {e}")
    
    print("\n7. Demonstração FIFO vs LIFO:")
    print("   Enfileirando: A, B, C")
    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    print(f"   Primeira saída: {fila.dequeue()} (correto: A)")
    print(f"   Segunda saída: {fila.dequeue()} (correto: B)")
