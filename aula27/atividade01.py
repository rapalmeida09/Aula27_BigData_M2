# import pandas e numpy
import pandas as pd
import numpy as np
import subprocess


subprocess.run('cls', shell=True)

# ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
ENDERECO_DADOS = './BaseDPEvolucaoMensalCisp.csv'

# Carregando os dados do arquivo CSV
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # Delimitando as variaveis 'cisp', 'lesao_corp_morte', 'lesao_corp_dolosa'
    df_ocorrencias = df_ocorrencias[['cisp', 'lesao_corp_morte', 'lesao_corp_dolosa']]

    # agrupar por 'cisp' e totalizar totalizando as colunas 'lesao_corp_morte' e 'lesao_corp_dolosa'
    df_total_lesoes = df_ocorrencias.groupby('cisp', as_index=False)[['lesao_corp_morte', 'lesao_corp_dolosa']].sum()

    print(df_total_lesoes.head(10))

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')


# Obtendo a correlação person usando numpy
try:
    correlacao = np.corrcoef(df_total_lesoes['lesao_corp_morte'], df_total_lesoes['lesao_corp_dolosa'])[0, 1]
    print(f'Correlação de Pearson: {correlacao:.1f}')

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')


# Plotando a Dispersão entre 'lesao_corp_morte' e 'lesao_corp_dolosa'
try:
    import matplotlib.pyplot as plt

    plt.scatter(df_total_lesoes['lesao_corp_morte'], df_total_lesoes['lesao_corp_dolosa'])
    plt.title(f'Correlação entre lesão corporal seguida de morte e lesão corporal dolosa: {correlacao:.2f}')
    plt.xlabel('Lesão corporal seguida de morte')
    plt.ylabel('Lesão corporal dolosa')
    plt.show()

except Exception as e:
    print(f"Erro ao plotar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')