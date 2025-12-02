"""
Estruturas de Dados Lineares em Python

Este pacote contém implementações educacionais de três estruturas
de dados fundamentais: Pilha, Fila e Hashtable.

Artigo: "Implementação de Estruturas de Dados Lineares: 
         Hashtable, Pilha e Fila em Python"

Autores:
    - Samuel Barbosa Silveira
    - Felipe Paravidino Silveira
    - Thiago Costa Bianchini de Sá
    - Roberto Tinoco Caparica
    - Dagoberto do Nascimento Cadilhe

Ano: 2025

Uso:
    from src.stack import Stack
    from src.queue import Queue
    from src.hashtable import HashTable
    
    pilha = Stack()
    fila = Queue()
    ht = HashTable()
"""

__version__ = "1.0.0"
__author__ = "Silveira et al."
__all__ = ['Stack', 'Queue', 'HashTable']

from .stack import Stack
from .queue import Queue
from .hashtable import HashTable
