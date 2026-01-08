# RAFAELIA/ZRF: Documentação Tecnológica
## Guia Técnico Completo do Framework

**RAFCODE-Φ | Pre6seal | Versão 1.0**

---

## Índice

1. [Visão Geral da Arquitetura](#1-visão-geral-da-arquitetura)
2. [Componentes Principais](#2-componentes-principais)
3. [Biblioteca Matemática](#3-biblioteca-matemática)
4. [Sistema Bitraf64](#4-sistema-bitraf64)
5. [Framework RAFAELIA](#5-framework-rafaelia)
6. [Guia de Uso](#6-guia-de-uso)
7. [API Reference](#7-api-reference)
8. [Exemplos Práticos](#8-exemplos-práticos)
9. [Performance e Otimização](#9-performance-e-otimização)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Visão Geral da Arquitetura

### 1.1 Estrutura do Projeto

```
Zrf/
├── src/
│   ├── mathematics.py          # Biblioteca de 69 operações matemáticas
│   ├── pseudo.py               # Código básico e conceitos fundamentais
│   └── copilot_rafaelia.py     # Framework completo RAFAELIA
├── docs/
│   ├── DISSERTATION.md         # Dissertação acadêmica
│   ├── TECHNOLOGY.md           # Este documento
│   ├── INDEX.md                # Índice geral
│   └── APPLICATIONS.md         # Guia de aplicações
├── scripts/
│   └── [utilitários]
└── README.md
```

### 1.2 Paradigma de Execução

O framework segue o ciclo VAZIO→VERBO→CHEIO→RETRO→NOVO VAZIO:

```
┌─────────────────────────────────────────────┐
│                  VAZIO                      │
│  (Inicialização: tokens, hashes, config)   │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│                  VERBO                      │
│  (Processamento: fractais, ética, cálculo) │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│                  CHEIO                      │
│  (Consolidação: serialização, exportação)  │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│                  RETRO                      │
│  (Retroalimentação: validação, checkpoint) │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│               NOVO VAZIO                    │
│  (Reinicialização para próximo ciclo)      │
└──────────────────┬──────────────────────────┘
                   ↓
                  (loop)
```

---

## 2. Componentes Principais

### 2.1 mathematics.py - Biblioteca Matemática

Biblioteca contendo 69 operações matemáticas organizadas em três categorias:

- **Derivadas (1-23)**: Cálculo diferencial para funções elementares e compostas
- **Antiderivadas (24-46)**: Integração analítica de funções
- **Inversas (47-69)**: Operações inversas incluindo métodos numéricos

**Características:**
- Type hints completos para melhor IDE support
- Tratamento robusto de exceções
- Documentação inline detalhada
- Validação de domínio antes do cálculo

### 2.2 pseudo.py - Conceitos Fundamentais

Implementação básica demonstrando os conceitos core:

```python
# Exemplo de estrutura básica
def inicializar_zrf():
    """VAZIO → Carrega tokens e hashes"""
    tokens = load_tokens(BITRAF_PATH)
    hashchain = gerar_hashchain(tokens)
    return tokens, hashchain

def processar_fractal(tokens):
    """VERBO → Aplicação fractal e ética"""
    fractal = {}
    for t in tokens:
        fractal[t] = (math.sqrt(3)/2) ** math.pi
    return fractal
```

### 2.3 copilot_rafaelia.py - Framework Completo

Implementação completa do sistema RAFAELIA incluindo:

- Processamento fractal avançado
- Sistema de validação ética (Φ_ethica)
- Compressão Bitraf64
- Exportação .zipraf
- Retroalimentação automática

---

## 3. Biblioteca Matemática

### 3.1 Instalação de Dependências

```bash
pip install numpy  # Opcional, para operações vetorizadas futuras
```

### 3.2 Importação

```python
from src.mathematics import *

# Ou importar funções específicas
from src.mathematics import (
    derivative_sine,
    antiderivative_power,
    inverse_exponential
)
```

### 3.3 Categorias de Operações

#### 3.3.1 Derivadas (Operações 1-23)

**Funções Polinomiais e Potências:**
```python
# Derivada de x^n
result = derivative_power(x=2.0, n=3)  # 3*2^2 = 12.0

# Derivada de √x
result = derivative_sqrt(x=4.0)  # 1/(2√4) = 0.25

# Derivada de polinômio [a₀, a₁, a₂, ...] representa a₀ + a₁x + a₂x² + ...
coeffs = [1, 2, 3]  # 1 + 2x + 3x²
result = derivative_polynomial(coeffs, x=2.0)  # 2 + 6*2 = 14.0
```

**Funções Exponenciais e Logarítmicas:**
```python
# Derivada de e^x
result = derivative_natural_exp(x=1.0)  # e^1 ≈ 2.718

# Derivada de ln(x)
result = derivative_natural_log(x=2.0)  # 1/2 = 0.5

# Derivada de a^x
result = derivative_exponential(a=2.0, x=3.0)  # 2^3 * ln(2) ≈ 5.545
```

**Funções Trigonométricas:**
```python
import math

# Derivada de sin(x)
result = derivative_sine(x=math.pi/4)  # cos(π/4) ≈ 0.707

# Derivada de tan(x)
result = derivative_tangent(x=math.pi/6)  # sec²(π/6) ≈ 1.333
```

**Funções Hiperbólicas:**
```python
# Derivada de sinh(x)
result = derivative_sinh(x=1.0)  # cosh(1) ≈ 1.543

# Derivada de tanh(x)
result = derivative_tanh(x=0.5)  # sech²(0.5) ≈ 0.786
```

#### 3.3.2 Antiderivadas (Operações 24-46)

**Integrais Básicas:**
```python
# ∫x^n dx = x^(n+1)/(n+1) + C
result = antiderivative_power(x=3.0, n=2)  # 3^3/3 = 9.0

# ∫1/x dx = ln|x| + C
result = antiderivative_reciprocal(x=5.0)  # ln(5) ≈ 1.609

# ∫e^x dx = e^x + C
result = antiderivative_exponential(x=2.0)  # e^2 ≈ 7.389
```

**Integrais Trigonométricas:**
```python
# ∫sin(x) dx = -cos(x) + C
result = antiderivative_sine(x=math.pi/3)  # -cos(π/3) = -0.5

# ∫cos(x) dx = sin(x) + C
result = antiderivative_cosine(x=math.pi/6)  # sin(π/6) = 0.5

# ∫sec²(x) dx = tan(x) + C
result = antiderivative_secant_squared(x=math.pi/4)  # tan(π/4) = 1.0
```

**Integrais de Polinômios:**
```python
# Antiderivada de polinômio
coeffs = [1, 2, 3]  # 1 + 2x + 3x²
# Resultado: x + x² + x³
result = antiderivative_polynomial(coeffs, x=2.0)  # 2 + 4 + 8 = 14.0
```

#### 3.3.3 Inversas (Operações 47-69)

**Funções Algébricas:**
```python
# Inversa de y = ax + b
x = inverse_linear(y=10, a=2, b=1)  # (10-1)/2 = 4.5

# Inversa de y = ax² (ramo positivo)
x = inverse_quadratic_positive(y=9, a=1, b=0, c=0)  # √9 = 3.0

# Inversa de y = x^n
x = inverse_power(y=8, n=3)  # ∛8 = 2.0
```

**Funções Transcendentais:**
```python
# Inversa de y = e^x (logaritmo natural)
x = inverse_exponential(y=10)  # ln(10) ≈ 2.303

# Inversa de y = ln(x) (exponencial)
x = inverse_logarithm(y=2)  # e^2 ≈ 7.389
```

**Funções Trigonométricas:**
```python
# arcsin, arccos, arctan
x = inverse_sine(y=0.5)  # arcsin(0.5) = π/6 ≈ 0.524
x = inverse_cosine(y=0.5)  # arccos(0.5) = π/3 ≈ 1.047
x = inverse_tangent(y=1.0)  # arctan(1) = π/4 ≈ 0.785
```

**Métodos Numéricos:**
```python
# Inversa de polinômio usando Newton-Raphson
coeffs = [0, 0, 1]  # y = x²
x = inverse_polynomial_newton(
    y=16.0,
    coefficients=coeffs,
    initial_guess=3.0,
    max_iterations=100,
    tolerance=1e-10
)  # x ≈ 4.0
```

### 3.4 Tratamento de Erros

Todas as funções validam seus domínios e lançam `ValueError` quando apropriado:

```python
try:
    # Tentando calcular ln(x) com x negativo
    result = derivative_natural_log(x=-1.0)
except ValueError as e:
    print(f"Erro: {e}")  # "Natural log derivative undefined for x <= 0"
```

### 3.5 Listagem de Operações

```python
from src.mathematics import list_operations, get_all_operations

# Exibir lista formatada de todas as 69 operações
list_operations()

# Obter dicionário com todas as operações
ops = get_all_operations()
operation_name, operation_func = ops[1]  # Operação #1
```

---

## 4. Sistema Bitraf64

### 4.1 Conceito

Bitraf64 é um sistema de encapsulamento e compressão simbólica que:

1. Serializa dados em JSON
2. Codifica em Base64
3. Adiciona hash de integridade
4. Marca com prefixo identificador

### 4.2 Implementação

```python
def compress_bitraf64(payload: bytes) -> str:
    """
    Encapsula payload em formato Bitraf64
    Formato: BITRAF64:<hash>:<base64_data>
    """
    enc = base64.b64encode(payload).decode("ascii")
    digest = blake3_hash(payload).lower()[:16]
    return f"BITRAF64:{digest}:{enc}"
```

### 4.3 Uso

```python
import json

data = {"key": "value", "number": 42}
payload = json.dumps(data).encode("utf-8")
compressed = compress_bitraf64(payload)

print(compressed)
# Output: BITRAF64:a1b2c3d4e5f6g7h8:eyJrZXkiOi...
```

---

## 5. Framework RAFAELIA

### 5.1 Configuração

```python
# Parâmetros principais
YEARS = 99                          # Ciclos de desenvolvimento simulados
BRANCHING_FACTOR = 3                # Fator de ramificação fractal
CYCLES_PER_YEAR = 4                 # Ciclos por ano
MAX_BRANCHES = BRANCHING_FACTOR ** 5  # Limite de ramificações

# Caminhos
BITRAF_PATH = "./bitraf64"          # Arquivo de tokens
ZIPRAF_OUT = "./zrf_output.zipraf"  # Saída
RAFAELIA_CORE = "./RAFAELIA_CORE"   # Núcleo de retroalimentação
```

### 5.2 Kernel Fractal

```python
def spiral_kernel(n: int) -> float:
    """
    Kernel espiral: (√3/2)^n
    Usado para atenuação fractal
    """
    base = math.sqrt(3) / 2.0  # ≈ 0.866
    return base ** n
```

Propriedades:
- Convergente (base < 1)
- Auto-similar em diferentes escalas
- Preserva estrutura fractal

### 5.3 Fibonacci-Rafael Modificada

```python
def F_Rafael(n: int) -> int:
    """
    Fibonacci com modificação Rafael
    F(n) = F(n-1) + F(n-2) + 1
    """
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a + b + 1
    return b
```

### 5.4 Sistema Ético (Φ_ethica)

```python
def apply_ethica(candidate: dict, context: dict) -> dict:
    """
    Aplica validação ética aos dados
    Calcula: coerência, entropia, score ético
    """
    # Cálculo de coerência
    keys = list(candidate.keys())
    predictable = sum(1 for k in keys if isinstance(k, str) and len(k) < 64)
    coherence = predictable / max(1, len(keys))
    
    # Cálculo de entropia
    numeric_vals = [v for v in candidate.values() if isinstance(v, (int, float))]
    if numeric_vals:
        mean = sum(numeric_vals) / len(numeric_vals)
        ent = sum(abs(x - mean) for x in numeric_vals) / len(numeric_vals)
    else:
        ent = 0.0
    
    # Score ético final
    insight = 1.0
    eth_score = (insight * (coherence + 1/(1+ent))) / 2.0
    
    # Aplicar correções se necessário
    if eth_score < 0.3:
        # Suavizar valores extremos
        for k, v in list(candidate.items()):
            if isinstance(v, (int, float)):
                candidate[k] = (v + mean) / 2.0 if numeric_vals else v
    
    # Anexar metadados éticos
    candidate["_RAFAELIA_ethica"] = {
        "coherence": coherence,
        "entropy_like": ent,
        "eth_score": eth_score
    }
    
    return candidate
```

### 5.5 Ciclo de Execução

```python
def main():
    # 1. VAZIO - Inicialização
    tokens = load_tokens(BITRAF_PATH)
    print("🔹 Tokens carregados:", len(tokens))
    
    # 2. VERBO - Processamento
    evolution = generate_evolution(tokens, YEARS, BRANCHING_FACTOR, CYCLES_PER_YEAR)
    print(f"🔸 Ramificações geradas: {evolution['meta']['branch_count']}")
    
    # 3. CHEIO - Exportação
    export_info = export_zipraf(evolution, ZIPRAF_OUT)
    print("✅ Exportado:", export_info["path"])
    
    # 4. RETRO - Retroalimentação
    ck = retroalimentar_core(export_meta)
    print("♾️ Retroalimentação registrada")
    
    # 5. NOVO VAZIO - Ciclo completo
    print("🌀 Ciclo completo: VAZIO→VERBO→CHEIO→RETRO→NOVO VAZIO")
```

---

## 6. Guia de Uso

### 6.1 Instalação

```bash
# Clone o repositório
git clone https://github.com/instituto-Rafael/Zrf.git
cd Zrf

# (Opcional) Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install numpy  # Opcional
```

### 6.2 Uso Básico

```python
# Importar biblioteca matemática
from src.mathematics import *

# Calcular derivadas
print(derivative_sine(math.pi/4))  # ≈ 0.707

# Calcular antiderivadas
print(antiderivative_power(2.0, 3))  # 4.0

# Calcular inversas
print(inverse_exponential(10))  # ≈ 2.303
```

### 6.3 Uso Avançado - Framework RAFAELIA

```python
# Executar framework completo
import sys
sys.path.append('src')
from copilot_rafaelia import main

# Executar ciclo completo
main()
```

---

## 7. API Reference

### 7.1 mathematics.py

**Derivadas:**
- `derivative_polynomial(coefficients, x)` - Derivada de polinômio
- `derivative_exponential(a, x)` - Derivada de a^x
- `derivative_sine(x)` - Derivada de sin(x)
- [... 20 funções adicionais ...]

**Antiderivadas:**
- `antiderivative_power(x, n)` - ∫x^n dx
- `antiderivative_exponential(x)` - ∫e^x dx
- `antiderivative_sine(x)` - ∫sin(x) dx
- [... 20 funções adicionais ...]

**Inversas:**
- `inverse_linear(y, a, b)` - Inversa de y = ax + b
- `inverse_exponential(y, base)` - Inversa de y = b^x
- `inverse_polynomial_newton(y, coeffs, ...)` - Inversa numérica
- [... 20 funções adicionais ...]

**Utilitários:**
- `get_all_operations()` - Retorna dict com todas as 69 operações
- `list_operations()` - Exibe lista formatada de operações

---

## 8. Exemplos Práticos

### 8.1 Cálculo de Tangente

```python
import math
from src.mathematics import derivative_polynomial, inverse_linear

# Encontrar equação da reta tangente a y = x² no ponto x=2
x0 = 2
coeffs = [0, 0, 1]  # y = x²

# Calcular y(2) = 4
y0 = sum(coeffs[i] * (x0 ** i) for i in range(len(coeffs)))

# Calcular derivada (inclinação) no ponto
m = derivative_polynomial(coeffs, x0)  # m = 2x = 4

# Equação da tangente: y - y0 = m(x - x0)
# y = mx - mx0 + y0 = 4x - 8 + 4 = 4x - 4

print(f"Tangente: y = {m}x + {y0 - m*x0}")  # y = 4x - 4
```

### 8.2 Cálculo de Área

```python
from src.mathematics import antiderivative_power

# Calcular área sob y = x² de x=0 a x=3
# A = ∫₀³ x² dx = [x³/3]₀³ = 27/3 - 0 = 9

a, b = 0, 3
area = antiderivative_power(b, 2) - antiderivative_power(a, 2)
print(f"Área: {area}")  # 9.0
```

### 8.3 Resolução de Equação

```python
from src.mathematics import inverse_polynomial_newton

# Resolver x³ - 2x - 5 = 0
coeffs = [-5, -2, 0, 1]  # -5 - 2x + 0x² + x³
y_target = 0

x_solution = inverse_polynomial_newton(
    y=y_target,
    coefficients=coeffs,
    initial_guess=2.0
)
print(f"Solução: x ≈ {x_solution:.6f}")  # x ≈ 2.094551
```

---

## 9. Performance e Otimização

### 9.1 Complexidade Computacional

| Operação | Complexidade | Notas |
|----------|--------------|-------|
| Derivadas elementares | O(1) | Cálculo direto |
| Derivada de polinômio | O(n) | n = grau do polinômio |
| Antiderivadas | O(1) | Fórmulas fechadas |
| Inversas analíticas | O(1) | Fórmulas fechadas |
| Newton-Raphson | O(k log ε) | k = iterações, ε = tolerância |

### 9.2 Dicas de Otimização

1. **Cache de Valores Constantes:**
```python
# Evitar recalcular constantes
PI_HALF = math.pi / 2
SQRT_3_HALF = math.sqrt(3) / 2
```

2. **Vetorização (futuro):**
```python
import numpy as np
# Aplicar operação a arrays inteiros
xs = np.linspace(0, 2*math.pi, 100)
ys = np.array([derivative_sine(x) for x in xs])
```

3. **Tolerância Apropriada:**
```python
# Para Newton-Raphson, ajustar tolerância vs. velocidade
x = inverse_polynomial_newton(y, coeffs, tolerance=1e-6)  # Mais rápido
x = inverse_polynomial_newton(y, coeffs, tolerance=1e-12)  # Mais preciso
```

---

## 10. Troubleshooting

### 10.1 Erros Comuns

**ValueError: "Domain error"**
```python
# Problema: Argumento fora do domínio da função
derivative_natural_log(-1)  # x deve ser > 0

# Solução: Validar entrada
x = -1
if x > 0:
    result = derivative_natural_log(x)
else:
    print("Erro: x deve ser positivo")
```

**ValueError: "Newton-Raphson did not converge"**
```python
# Problema: Chute inicial muito longe da raiz
inverse_polynomial_newton(y, coeffs, initial_guess=1000)

# Solução: Melhorar chute inicial
inverse_polynomial_newton(y, coeffs, initial_guess=0)
```

### 10.2 Debugging

```python
# Habilitar debug mode (exemplo)
import logging
logging.basicConfig(level=logging.DEBUG)

# Verificar valores intermediários
def debug_derivative(x):
    print(f"Input: x = {x}")
    result = derivative_sine(x)
    print(f"Output: sin'({x}) = {result}")
    return result
```

### 10.3 Reporting Issues

Para reportar problemas:
1. Descreva o comportamento esperado vs. observado
2. Forneça código mínimo reproduzível
3. Inclua versão do Python e sistema operacional
4. Abra issue no GitHub: https://github.com/instituto-Rafael/Zrf/issues

---

## Conclusão

Esta documentação técnica cobre os aspectos principais do framework RAFAELIA/ZRF. Para informações adicionais:

- **Dissertação Acadêmica**: `docs/DISSERTATION.md`
- **Índice Geral**: `docs/INDEX.md`
- **Aplicações**: `docs/APPLICATIONS.md`
- **README**: `README.md`

**Suporte:**
- GitHub Issues: https://github.com/instituto-Rafael/Zrf/issues
- Email: [configurar se disponível]

**Contribuições:**
Pull requests são bem-vindos! Consulte `CONTRIBUTING.md` para diretrizes.

---

**Última Atualização:** Janeiro 2026  
**Versão:** 1.0  
**Mantenedor:** Instituto Rafael
