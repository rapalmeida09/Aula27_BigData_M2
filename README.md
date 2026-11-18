# Aula27_BigData_M2
# Análise de Correlação – Dados do ISP-RJ

Atividades de estatística em Python que calculam e visualizam a **correlação de Pearson** entre variáveis de segurança pública, usando a base de dados do Instituto de Segurança Pública do Rio de Janeiro (ISP-RJ).

## Fonte dos dados

Base **Evolução Mensal por CISP** (`BaseDPEvolucaoMensalCisp.csv`):

https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv

- Separador: `;`
- Codificação: `iso-8859-1`

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `exemplo01.py` | Exemplo: correlação entre **roubo de veículos** e **recuperação de veículos** por CISP, com gráfico de dispersão. |
| `atividade01.py` | Atividade 01: correlação entre **lesão corporal seguida de morte** e **lesão corporal dolosa** por CISP, com gráfico de dispersão. |
| `machine_learning.ipynb` | Notebook que obtém os dados direto do site do ISP, remove valores extremos (acima do percentil 95) e calcula a correlação entre roubo e recuperação de veículos. |

## Como funciona

1. Lê o CSV do ISP-RJ com `pandas`.
2. Seleciona as colunas de interesse (`cisp` e as duas variáveis analisadas).
3. Agrupa por `cisp` e soma os valores de cada variável.
4. Calcula a correlação de Pearson com `numpy.corrcoef`.
5. Plota o gráfico de dispersão com `matplotlib`, exibindo o coeficiente no título.

No notebook, há uma etapa extra: filtra os valores abaixo do **percentil 95** de cada variável para reduzir o efeito de outliers antes de calcular a correlação.

## Requisitos

- Python 3.10+ (o notebook foi executado com Python 3.13)
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `jupyter` (apenas para o notebook)

Instalação:

```bash
pip install pandas numpy matplotlib jupyter
```

## Como executar

### 1. Baixar os dados

Baixe o arquivo `BaseDPEvolucaoMensalCisp.csv` no link acima e coloque-o na mesma pasta dos scripts (os scripts `.py` leem `./BaseDPEvolucaoMensalCisp.csv`).

### 2. Rodar os scripts

```bash
python exemplo01.py
python atividade01.py
```

Cada script imprime os 10 primeiros registros agrupados, o coeficiente de correlação e abre uma janela com o gráfico de dispersão.

### 3. Rodar o notebook

```bash
jupyter notebook machine_learning.ipynb
```

O notebook baixa os dados diretamente da URL do ISP, então precisa de conexão com a internet.

## Observações

- Os scripts usam `subprocess.run('cls', shell=True)` para limpar o terminal, o que funciona apenas no **Windows**. No Linux/macOS, troque por `'clear'`.
- A correlação mede associação linear, não causalidade.
- A base é agregada por CISP (circunscrição de delegacia), então os resultados refletem totais por área, sem ajuste pela população ou pelo porte de cada CISP.

## Licença

Uso educacional. Os dados pertencem ao ISP-RJ.
