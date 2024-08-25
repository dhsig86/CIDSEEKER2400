import pandas as pd

# Definir o caminho dos arquivos CSV
categorias_csv_file = 'C:/Users/drdhs/Downloads/CID10CSV/CID-O-CATEGORIAS.CSV'
subcategorias_csv_file = 'C:/Users/drdhs/Downloads/CID10CSV/CID-10-SUBCATEGORIAS.CSV'

# Carregar os arquivos CSV
cid10_categorias_df = pd.read_csv(categorias_csv_file, sep=';', encoding='latin1')
cid10_subcategorias_df = pd.read_csv(subcategorias_csv_file, sep=';', encoding='latin1')

# Mesclando categorias e subcategorias
# Categorias: usando as colunas CAT e DESCRICAO
# Subcategorias: usando as colunas SUBCAT e DESCRICAO
cid10_categorias_df = cid10_categorias_df[['CAT', 'DESCRICAO']]
cid10_categorias_df.columns = ['Código', 'Descrição']  # Renomeando as colunas para ficar uniforme

cid10_subcategorias_df = cid10_subcategorias_df[['SUBCAT', 'DESCRICAO']]
cid10_subcategorias_df.columns = ['Código', 'Descrição']  # Renomeando as colunas para ficar uniforme

# Combinar categorias e subcategorias em um único DataFrame
cid10_completo_df = pd.concat([cid10_categorias_df, cid10_subcategorias_df], ignore_index=True)

# Salvando o DataFrame combinado como JSON
cid10_completo_df.to_json('CID10_completo.json', orient='records', force_ascii=False)

print("Arquivo JSON gerado com sucesso!")
