import pandas as pd
import os

RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')

def carregar_dados():
    """
    Carrega os dados brutos de vendas, produtos e clientes de arquivos CSV.

    Retorna:
        Um dicionário contendo os DataFrames de vendas, produtos e clientes.
    """
    try:
        df_vendas = pd.read_csv(os.path.join(RAW_DATA_PATH, 'vendas.csv'), sep=';')
        df_produtos = pd.read_csv(os.path.join(RAW_DATA_PATH, 'produtos.csv'), sep=';')
        df_clientes = pd.read_csv(os.path.join(RAW_DATA_PATH, 'clientes.csv'), sep=';')
        
        print("Dados carregados com sucesso!")
        
        return {
            "vendas": df_vendas,
            "produtos": df_produtos,
            "clientes": df_clientes
        }
    except FileNotFoundError as e:
        print(f"Erro ao carregar os arquivos: {e}")
        print("Verifique se os arquivos .csv estão na pasta 'data/raw'.")
        return None
    
def limpar_e_transformar_dados(dfs: dict):
    """
    Limpa e transforma os DataFrames, ajustando tipos de dados.

    Args:
        dfs (dict): Dicionário de DataFrames (vendas, produtos, clientes).

    Retorna:
        Um dicionário contendo os DataFrames limpos e transformados.
    """
    if dfs is None:
        return None
        
    # --- Limpeza do DataFrame de Vendas ---
    df_vendas = dfs['vendas'].copy()
    df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'], format='%d/%m/%Y')
    df_vendas['Valor_Total_Venda'] = df_vendas['Valor_Total_Venda'].str.replace(',', '.').astype(float)

    # --- Limpeza do DataFrame de Produtos ---
    df_produtos = dfs['produtos'].copy()
    df_produtos['Preco_Unitario'] = df_produtos['Preco_Unitario'].str.replace(',', '.').astype(float)
    
    df_clientes = dfs['clientes'].copy()

    print("Limpeza e transformação dos dados concluída.")

    return {
        "vendas": df_vendas,
        "produtos": df_produtos,
        "clientes": df_clientes
    }

def mesclar_dados(dfs_limpos: dict):
    """
    Mescla os DataFrames de vendas, produtos e clientes em um único DataFrame.

    Args:
        dfs_limpos (dict): Dicionário com os DataFrames já limpos.

    Retorna:
        Um único DataFrame consolidado com todas as informações.
    """
    if dfs_limpos is None:
        return None
        
    # Mescla vendas com clientes usando 'ID_Cliente'
    df_merged = pd.merge(dfs_limpos['vendas'], dfs_limpos['clientes'], on='ID_Cliente', how='left')
    
    # Mescla o resultado anterior com produtos usando 'ID_Produto'
    df_final = pd.merge(df_merged, dfs_limpos['produtos'], on='ID_Produto', how='left')
    
    print("Dados mesclados em um único DataFrame.")
    
    return df_final

def salvar_dados_processados(df, nome_arquivo="dados_consolidados.csv"):
    """
    Salva o DataFrame processado na pasta 'data/processed'.

    Args:
        df (DataFrame): O DataFrame a ser salvo.
        nome_arquivo (str): O nome do arquivo a ser criado.
    """
    if df is None:
        print("Nenhum dado para salvar.")
        return
        
    # Cria a pasta 'processed' se ela não existir
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)
        
    caminho_saida = os.path.join(PROCESSED_DATA_PATH, nome_arquivo)
    df.to_csv(caminho_saida, index=False, sep=';', decimal=',')
    print(f"Arquivo processado salvo em: {caminho_saida}")