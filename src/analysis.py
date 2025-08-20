import pandas as pd

def get_receita_do_dia(df, dia):
    """
    Filtra o DataFrame para um dia específico e calcula a receita total.
    
    Args:
        df (pd.DataFrame): DataFrame consolidado de vendas.
        dia (str): A data no formato 'YYYY-MM-DD' (padrão).
        
    Returns:
        float: A receita total para o dia especificado.
    """
    # Converte a string 'dia' para o formato de data
    data_filtro = pd.to_datetime(dia).date()
    # Filtra o DataFrame pela data
    df_dia = df[df['Data_Venda'].dt.date == data_filtro]
    return df_dia['Valor_Total_Venda'].sum()

def get_cliente_maior_gasto(df):
    """Retorna o nome do cliente que mais gastou no total."""
    df['Nome_Completo'] = df['Nome'] + ' ' + df['Sobrenome']
    gastos_por_cliente = df.groupby('Nome_Completo')['Valor_Total_Venda'].sum()
    return gastos_por_cliente.idxmax()

def get_cliente_menor_gasto(df):
    """Retorna o nome do cliente que menos gastou no total."""
    df['Nome_Completo'] = df['Nome'] + ' ' + df['Sobrenome']
    gastos_por_cliente = df.groupby('Nome_Completo')['Valor_Total_Venda'].sum()
    return gastos_por_cliente.idxmin()

def calcular_top_5_clientes(df):
    """Identifica os 5 clientes que mais gastaram."""
    # Criamos uma coluna 'Nome_Completo' para facilitar a visualização
    df['Nome_Completo'] = df['Nome'] + ' ' + df['Sobrenome']
    top_clientes = df.groupby('Nome_Completo')['Valor_Total_Venda'].sum().nlargest(5)
    print("\nTop 5 Clientes (por Faturamento):")
    print(top_clientes)
    return top_clientes

def get_produto_mais_vendido(df, por='faturamento'):
    """
    Retorna o produto mais vendido, seja por faturamento ou por quantidade.
    
    Args:
        df (pd.DataFrame): DataFrame consolidado de vendas.
        por (str): Critério da análise ('faturamento' ou 'quantidade').
        
    Returns:
        str: O nome do produto mais vendido.
    """
    if por == 'faturamento':
        return df.groupby('Nome_Produto')['Valor_Total_Venda'].sum().idxmax()
    elif por == 'quantidade':
        return df.groupby('Nome_Produto')['Quantidade'].sum().idxmax()
    else:
        return "Critério inválido. Use 'faturamento' ou 'quantidade'."

def calcular_top_5_produtos_vendidos(df):
    """Identifica os 5 produtos mais vendidos em termos de faturamento."""
    top_produtos = df.groupby('Nome_Produto')['Valor_Total_Venda'].sum().nlargest(5)
    print("\nTop 5 Produtos Mais Vendidos (por Faturamento):")
    print(top_produtos)
    return top_produtos

def get_vendas_por_estado(df):
    """Retorna uma Série com o faturamento total de vendas por estado."""
    return df.groupby('Estado')['Valor_Total_Venda'].sum().sort_values(ascending=False)

def get_produtos_acabando(df_produtos, limite=25):
    """
    Retorna um DataFrame com produtos com estoque abaixo de um limite.
    
    Args:
        df_produtos (pd.DataFrame): DataFrame original de produtos.
        limite (int): O nível de estoque considerado baixo.
        
    Returns:
        pd.DataFrame: Tabela de produtos com estoque baixo.
    """
    return df_produtos[df_produtos['Estoque'] < limite]

def get_vendas_acima_de(df, valor=2500):
    """Retorna todas as vendas individuais com valor acima do especificado."""
    return df[df['Valor_Total_Venda'] > valor]

def get_itens_vendidos_no_dia(df, dia):
    """
    Calcula a quantidade total de itens (soma das quantidades) vendidos em um dia.
    
    Args:
        df (pd.DataFrame): DataFrame consolidado de vendas.
        dia (str): A data no formato 'YYYY-MM-DD'.
        
    Returns:
        int: O número total de itens vendidos no dia.
    """
    data_filtro = pd.to_datetime(dia).date()
    df_dia = df[df['Data_Venda'].dt.date == data_filtro]
    return df_dia['Quantidade'].sum()