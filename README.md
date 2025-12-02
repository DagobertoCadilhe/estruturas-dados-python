# Implementação de Estruturas de Dados Lineares em Python

## 📄 Sobre o Projeto

Este repositório contém as implementações e experimentos realizados para o trabalho acadêmico **"Implementação de Estruturas de Dados Lineares: Hashtable, Pilha e Fila em Python"**.

O objetivo é validar empiricamente as complexidades teóricas O(1) de três estruturas de dados fundamentais através de implementações didáticas e análises de desempenho sistemáticas.

### 👥 Autores
- Samuel Barbosa Silveira
- Felipe Paravidino Silveira
- Thiago Costa Bianchini de Sá
- Roberto Tinoco Caparica
- Dagoberto do Nascimento Cadilhe

---

## 🎯 Estruturas Implementadas

### 📚 Pilha (Stack) - LIFO
Implementação usando lista Python com operações O(1) amortizado.

**Características:**
- Push/Pop em O(1)
- Uso de memória: 8.86 bytes/elemento
- Suporta milhares de elementos

### 🚶 Fila (Queue) - FIFO
Implementação usando `collections.deque` para garantir O(1) verdadeiro.

**Características:**
- Enqueue/Dequeue em O(1)
- Uso de memória: 9.21 bytes/elemento
- Evita degradação O(n) de listas comuns

### 🗃️ Hashtable - Acesso Direto
Implementação com encadeamento (chaining) para resolução de colisões.

**Características:**
- Insert/Search/Delete em O(1+α)
- Distribuição uniforme (desvio padrão 3.3 elementos)
- Fator de carga ideal: α = 1.0 - 2.0

---

## 📁 Estrutura do Repositório

```
.
├── README.md                    # Este arquivo
├── LICENSE                      # Licença MIT
├── requirements.txt             # Dependências (vazio - só stdlib)
├── .gitignore                   # Arquivos ignorados pelo Git
│
├── src/                         # 📦 Código fonte
│   ├── __init__.py
│   ├── stack.py                 # Implementação da Pilha
│   ├── queue.py                 # Implementação da Fila
│   └── hashtable.py             # Implementação da Hashtable
│
├── tests/                       # 🧪 Testes funcionais
│   ├── __init__.py
│   ├── test_stack.py            # 6 testes para Pilha
│   ├── test_queue.py            # 6 testes para Fila
│   └── test_hashtable.py        # 8 testes para Hashtable
│
├── benchmarks/                  # ⚡ Benchmarks de desempenho
│   ├── __init__.py
│   ├── benchmark_stack.py       # Tempo e memória da Pilha
│   ├── benchmark_queue.py       # Tempo e memória da Fila
│   └── benchmark_hashtable.py   # Tempo e memória da Hashtable
│
└── analysis/                    # 🔬 Análises avançadas
    ├── __init__.py
    ├── collision_analysis.py    # Distribuição de colisões
    ├── load_factor_test.py      # Impacto do fator de carga
    └── comparative_tests.py     # Comparações entre estruturas
```

---

## 🚀 Como Usar

### Pré-requisitos

```bash
Python 3.13 ou superior
```

**Nota:** Este projeto usa **apenas a biblioteca padrão do Python**. Não há dependências externas!

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/DagobertoCadilhe/estruturas-dados-python.git
cd estruturas-dados-python
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### Uso Básico

```python
# Pilha (Stack)
from src.stack import Stack

pilha = Stack()
pilha.push(10)
pilha.push(20)
print(pilha.pop())  # 20 (LIFO)

# Fila (Queue)
from src.queue import Queue

fila = Queue()
fila.enqueue(10)
fila.enqueue(20)
print(fila.dequeue())  # 10 (FIFO)

# Hashtable
from src.hashtable import HashTable

ht = HashTable()
ht.insert("nome", "João")
print(ht.search("nome"))  # João
```

### Executando Testes

```bash
# Testes funcionais (20 testes no total)
python tests/test_stack.py        # 6 testes
python tests/test_queue.py        # 6 testes
python tests/test_hashtable.py    # 8 testes
```

### Executando Benchmarks

```bash
# Benchmarks de desempenho
python benchmarks/benchmark_stack.py
python benchmarks/benchmark_queue.py
python benchmarks/benchmark_hashtable.py
```

### Executando Análises

```bash
# Análises avançadas
python analysis/collision_analysis.py    # Análise de colisões
python analysis/load_factor_test.py      # Teste de fator de carga
python analysis/comparative_tests.py     # Testes comparativos
```

---

## 📊 Resultados Principais

### Complexidade Temporal Validada ✓

Todas as estruturas confirmaram complexidade **O(1)** com variação < 50%:

| Estrutura | Operação  | Tempo (100K elem) | Variação |
|-----------|-----------|-------------------|----------|
| Pilha     | push()    | 0.12 µs          | -5.2%    |
| Pilha     | pop()     | 0.20 µs          | -4.4%    |
| Fila      | enqueue() | 0.11 µs          | -21.8%   |
| Fila      | dequeue() | 0.19 µs          | -4.3%    |
| Hashtable | insert()  | 0.89 µs          | -8.1%    |
| Hashtable | search()  | 0.50 µs          | +5.1%    |

### Uso de Memória

- **Pilha**: 8.86 bytes/elemento
- **Fila**: 9.21 bytes/elemento (4% maior que pilha)
- **Hashtable**: 19.32 bytes/elemento (2.2x maior, mas acesso O(1) por chave)

### Distribuição de Colisões (Hashtable)

Com 1.000 elementos e α=10.0:
- **Desvio padrão**: 3.28 elementos (33% da média)
- **86.5%** dos buckets contêm 6-15 elementos
- **100%** de aproveitamento (nenhum bucket vazio)
- **Qualidade**: EXCELENTE

### Fator de Carga Ideal

- **α = 1.0**: Melhor desempenho observado
- **α = 0.5 - 2.0**: Faixa recomendada
- **α > 10.0**: Degradação de 64% (ainda aceitável)

---

## 🔬 Metodologia

### Ambientes de Teste

1. **Windows 10** (nativo)
   - Python 3.13.5
   - 32GB RAM
   - AMD Ryzen 7 5700X3D

2. **Kali Linux** (virtualizado)
   - Python 3.13.3
   - 6GB RAM (VM)
   - AMD Ryzen 7 5700X3D (host)

### Métricas Avaliadas

- ⏱️ Tempo de execução (microsegundos/operação)
- 💾 Uso de memória (bytes/elemento)
- 📊 Distribuição de colisões (hashtable)
- ⚖️ Impacto do fator de carga (hashtable)
- 🖥️ Comparação entre ambientes

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Referências

Este trabalho foi fundamentado nas seguintes obras:

- **Wengrow, J.** (2020). *A Common-Sense Guide to Data Structures and Algorithms*. 2nd ed.
- **Kubica, J.** (2022). *Data Structures the Fun Way*.
- **Bhargava, A.** (2016). *Grokking Algorithms*.
- **Lafore, R.** (2022). *Data Structures & Algorithms in Python*.

---

## 🌟 Destaques

✨ **Implementações didáticas** com documentação completa  
✨ **20 testes funcionais** validando corretude  
✨ **Benchmarks sistemáticos** para validação empírica  
✨ **Análises avançadas** de colisões e fator de carga  
✨ **Código limpo** seguindo PEP 8  
✨ **Zero dependências** externas  

---

**⭐ Se este projeto foi útil para seus estudos, considere dar uma estrela! ⭐**
