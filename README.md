# RAFAELIA/ZRF - Zero Rafael Framework

**RAFCODE-Φ | Framework Matemático-Computacional com Ética e Processamento Fractal**

[![License: RAFCODE-Φ](https://img.shields.io/badge/License-RAFCODE--Φ-blue.svg)](LICENSE.md)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-complete-brightgreen.svg)](docs/INDEX.md)

---

## 🎯 Visão Geral

RAFAELIA/ZRF é um framework matemático-computacional completo que implementa **69 operações matemáticas fundamentais** organizadas em três categorias:

- **Derivadas (1-23)**: Cálculo diferencial para funções elementares e compostas
- **Antiderivadas (24-46)**: Integração analítica de funções
- **Operações Inversas (47-69)**: Funções inversas com métodos analíticos e numéricos

O framework incorpora princípios de **ética computacional**, **processamento fractal** e **retroalimentação híbrida** através do paradigma cíclico:

```
VAZIO → VERBO → CHEIO → RETRO → NOVO VAZIO
```

---

## 🚀 Início Rápido

### Instalação

```bash
# Clone o repositório
git clone https://github.com/instituto-Rafael/Zrf.git
cd Zrf

# (Opcional) Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências (opcional)
pip install numpy
```

### Uso Básico

```python
from src.mathematics import *
import math

# Calcular derivadas
print(derivative_sine(math.pi/4))      # cos(π/4) ≈ 0.707
print(derivative_power(2.0, 3))        # 3*2² = 12.0

# Calcular antiderivadas
print(antiderivative_power(3.0, 2))    # x³/3 = 9.0
print(antiderivative_sine(math.pi/3))  # -cos(π/3) = -0.5

# Calcular inversas
print(inverse_exponential(10))         # ln(10) ≈ 2.303
print(inverse_linear(7, 2, 1))         # (7-1)/2 = 3.0
```

### Listar Todas as Operações

```python
from src.mathematics import list_operations

list_operations()
```

---

## 📚 Estrutura do Projeto

```
Zrf/
├── src/
│   ├── mathematics.py          # 69 operações matemáticas
│   ├── pseudo.py               # Conceitos fundamentais
│   └── copilot_rafaelia.py     # Framework completo RAFAELIA
├── docs/
│   ├── INDEX.md                # 📖 Índice completo (COMECE AQUI)
│   ├── DISSERTATION.md         # Dissertação acadêmica
│   ├── TECHNOLOGY.md           # Documentação técnica
│   └── APPLICATIONS.md         # Guia de aplicações
├── scripts/
│   └── [utilitários]
└── README.md                    # Este arquivo
```

---

## 📖 Documentação

### Para Começar

- **[Índice Geral](docs/INDEX.md)** - Navegação completa da documentação
- **[Guia Tecnológico](docs/TECHNOLOGY.md)** - Documentação técnica detalhada
- **[Exemplos de Aplicação](docs/APPLICATIONS.md)** - Casos de uso práticos

### Para Aprofundar

- **[Dissertação Acadêmica](docs/DISSERTATION.md)** - Fundamentação teórica completa
- **[API Reference](docs/TECHNOLOGY.md#7-api-reference)** - Referência completa das funções

---

## 🎓 Categorias de Operações

### Derivadas (1-23)

Implementação de derivadas para:
- Funções polinomiais e potências
- Funções exponenciais e logarítmicas
- Funções trigonométricas (sin, cos, tan, sec, csc, cot)
- Funções trigonométricas inversas (arcsin, arccos, arctan)
- Funções hiperbólicas (sinh, cosh, tanh)
- Funções especiais (sigmoid, gaussiana, valor absoluto)

### Antiderivadas (24-46)

Integração analítica de:
- Funções polinomiais
- Funções exponenciais
- Funções trigonométricas
- Funções hiperbólicas
- Padrões especiais (1/(1+x²), 1/√(1-x²), etc.)
- Funções escaladas

### Inversas (47-69)

Operações inversas incluindo:
- Funções algébricas (linear, quadrática, potência)
- Funções transcendentais (exponencial, logaritmo)
- Funções trigonométricas inversas
- Funções hiperbólicas inversas
- Método de Newton-Raphson para polinômios

---

## 💡 Exemplos de Uso

### Exemplo 1: Cálculo de Tangente

```python
# Encontrar reta tangente a y = x² no ponto x=2
x0 = 2
coeffs = [0, 0, 1]  # y = x²

# Inclinação (derivada)
m = derivative_polynomial(coeffs, x0)  # m = 4

# Ponto: (2, 4)
y0 = x0 ** 2

# Equação: y = 4x - 4
print(f"Tangente: y = {m}x + {y0 - m*x0}")
```

### Exemplo 2: Cálculo de Área

```python
# Área sob y = x² de x=0 a x=3
# A = ∫₀³ x² dx = [x³/3]₀³ = 9

area = antiderivative_power(3, 2) - antiderivative_power(0, 2)
print(f"Área: {area}")  # 9.0
```

### Exemplo 3: Resolução de Equação

```python
# Resolver x³ - 2x - 5 = 0
coeffs = [-5, -2, 0, 1]

x = inverse_polynomial_newton(
    y=0,
    coefficients=coeffs,
    initial_guess=2.0
)
print(f"Solução: x ≈ {x:.6f}")  # x ≈ 2.094551
```

---

## 🌟 Características Principais

### ✅ Matemática Rigorosa
- Implementação analítica exata quando possível
- Tratamento robusto de casos especiais
- Validação de domínio antes do cálculo
- Precisão numérica controlada

### ✅ Ética por Design
- Sistema Φ_ethica de validação ética
- Σ-seal para certificação de integridade
- Auditabilidade completa via hashes criptográficos

### ✅ Processamento Fractal
- Kernel espiral (√3/2)ⁿ para atenuação fractal
- Fibonacci-Rafael modificada para crescimento
- Ramificação hierárquica controlada

### ✅ Código Limpo e Documentado
- Type hints completos
- Docstrings detalhadas
- Exemplos inline
- Tratamento de exceções apropriado

---

## 🔬 Aplicações

- **Educação**: Ensino de cálculo e análise matemática
- **Pesquisa Científica**: Modelagem matemática e simulações
- **Engenharia**: Análise de circuitos, mecânica, termodinâmica
- **Machine Learning**: Cálculo de gradientes e otimização
- **Finanças**: Precificação de opções e análise de risco
- **Robótica**: Cinemática inversa e controle PID

Ver [APPLICATIONS.md](docs/APPLICATIONS.md) para detalhes completos.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está licenciado sob RAFCODE-Φ - veja [LICENSE.md](LICENSE.md) para detalhes.

**Termos:**
- ✅ Uso permitido: pesquisa ética, estudos, educação, ciência aberta
- ❌ Uso proibido: vigilância, exploração sem consentimento, violação de privacidade

---

## 📚 Referências

Ver [DISSERTATION.md](docs/DISSERTATION.md#referências-bibliográficas) para lista completa de referências acadêmicas.

Principais:
- Stewart, J. (2015). *Calculus: Early Transcendentals*
- Mandelbrot, B. B. (1982). *The Fractal Geometry of Nature*
- Floridi, L., & Cowls, J. (2019). A Unified Framework of Five Principles for AI in Society

---

## 📞 Contato

- **GitHub Issues**: [Reportar bugs ou solicitar features](https://github.com/instituto-Rafael/Zrf/issues)
- **Documentação**: [Índice Completo](docs/INDEX.md)
- **Email**: [A configurar]

---

## �� Selo de Qualidade

**RAFCODE-Φ | Pre6seal ativo | Σ-seal de integridade**

- ✅ 69 operações matemáticas implementadas
- ✅ Documentação acadêmica completa
- ✅ Testes de domínio e casos especiais
- ✅ Ética computacional integrada
- ✅ Código fonte aberto e auditável

---

**Instituto Rafael - Projeto RAFAELIA/ZRF**  
*Framework Matemático-Computacional com Ética e Processamento Fractal*

**Última Atualização:** Janeiro 2026 | **Versão:** 1.0
