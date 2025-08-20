# Importa as funções que criamos nos outros arquivos
import data_processing as dp
import analysis as an

def main():
    print("--- INICIANDO ANÁLISE DE VENDAS ---")

    # 1. PROCESSAMENTO DE DADOS
    # Carrega os dados brutos
    dados_brutos = dp.carregar_dados()
    
    # Sai do programa se os dados não puderem ser carregados
    if dados_brutos is None:
        print("--- FINALIZANDO DEVIDO A ERRO NO CARREGAMENTO ---")
        return

    # Limpa e transforma os dados
    dados_limpos = dp.limpar_e_transformar_dados(dados_brutos)
    
    # Mescla os dataframes em um só
    df_consolidado = dp.mesclar_dados(dados_limpos)
    
    # 2. ANÁLISE DOS DADOS
    # Agora, usamos o dataframe consolidado e o de produtos para chamar as funções de análise
    print("\n--- INICIANDO ANÁLISES ---")

    # Exemplo: Receita de um dia específico
    receita_dia_especifico = an.get_receita_do_dia(df_consolidado, '2025-02-14')
    print(f"\nA receita do dia 2025-02-14 foi: R$ {receita_dia_especifico:,.2f}")

    # Cliente que mais gastou
    cliente_top = an.get_cliente_maior_gasto(df_consolidado)
    print(f"\nO cliente que mais gastou foi: {cliente_top}")

    # Produto mais vendido por faturamento
    produto_top_faturamento = an.get_produto_mais_vendido(df_consolidado, por='faturamento')
    print(f"\nO produto mais vendido (por faturamento) foi: {produto_top_faturamento}")
    
    # Produto mais vendido por quantidade
    produto_top_quantidade = an.get_produto_mais_vendido(df_consolidado, por='quantidade')
    print(f"\nO produto mais vendido (por quantidade) foi: {produto_top_quantidade}")

    # Vendas por estado
    vendas_estado = an.get_vendas_por_estado(df_consolidado)
    print("\nFaturamento por Estado:")
    print(vendas_estado.to_string())

    # Produtos com estoque baixo (lembre-se de usar o dataframe de produtos original)
    df_produtos_original = dados_limpos['produtos']
    produtos_acabando = an.get_produtos_acabando(df_produtos_original, limite=20)
    print("\nProdutos com estoque baixo (menos de 20 unidades):")
    print(produtos_acabando[['Nome_Produto', 'Estoque']].to_string(index=False))

    # 3. SALVAR RESULTADO FINAL
    # Salva o dataframe consolidado e limpo para ser usado no Power BI
    dp.salvar_dados_processados(df_consolidado, "vendas_consolidadas_powerbi.csv")

    print("\n--- ANÁLISE DE VENDAS CONCLUÍDA ---")

# Este bloco garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()