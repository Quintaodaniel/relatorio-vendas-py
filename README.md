# 📊 Pipeline de Análise de Vendas para Power BI

![Status](https://img.shields.io/badge/status-ativo-green) ![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-2.x-blue?logo=pandas)

Um projeto de automação para transformar dados brutos de vendas em um dataset limpo e pronto para ser visualizado no Power BI.

---

### 🚀 Objetivo

O objetivo principal é criar uma pipeline de dados reutilizável que processe arquivos CSV de vendas, produtos e clientes, gerando uma tabela consolidada para análise de negócios e criação de dashboards.

### ⚙️ Como Funciona

O projeto é dividido em módulos com responsabilidades claras:
-   **`data_processing.py`**: Cuida do carregamento, limpeza e unificação dos dados.
-   **`analysis.py`**: Contém funções para extrair métricas e KPIs específicos.
-   **`main.py`**: Orquestra todo o processo, chamando as funções na ordem correta.

### ▶️ Como Executar

1.  **Clone este repositório**
    ```bash
    git clone [https://github.com/seu-usuario/relatorio-vendas-py.git](https://github.com/seu-usuario/relatorio-vendas-py.git)
    cd relatorio-vendas-py
    ```
2.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute a pipeline**
    ```bash
    python src/main.py
    ```

Ao final, o arquivo `vendas_consolidadas_powerbi.csv` estará disponível na pasta `data/processed/`.