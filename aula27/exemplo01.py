# import pandas e numpy
import pandas as pd
import numpy as np
import subprocess
import matplotlib.pyplot as plt


subprocess.run('cls', shell=True)

# ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
ENDERECO_DADOS = './BaseDPEvolucaoMensalCisp.csv'

# Carregando os dados do arquivo CSV
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Delimitando as variaveis 'cisp', 'roubo_veiculo', 'recuperacao_veiculos'
    df_ocorrencias = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # agrupar por 'cisp' e totalizar totalizando as colunas 'roubo_veiculo' e 'recuperacao_veiculos'
    df_total_veiculos = df_ocorrencias.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()

    print(df_total_veiculos.head(10))

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')

# Obtendo a correlação person usando numpy
try:
    correlacao = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])[0, 1]
    print(f'Correlação de Pearson: {correlacao}')


except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')

# Plotando a Dispersão entre roubo de veículos e recuperação de veículos
try:
    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.title(f'Correlação entre roubo de veículos e recuperação de veículos: {correlacao:.2f}')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperação de veículos')
    plt.show()

except Exception as e:
    print(f"Erro ao plotar os dados: {e}")
    print(f'Linha: {e.__traceback__.tb_lineno}')