import os
import pandas as pd
from zipfile import ZipFile

# URL do FTP para download (este é o link do Datasus, atualizado para 2024)
ftp_url = 'ftp://ftp2.datasus.gov.br/pub/sistemas/tup/downloads/TabelaUnificada_202408_v2408091312.zip'
local_file = 'TabelaUnificada.zip'

# Baixar e extrair o arquivo ZIP
def download_and_extract(ftp_url, local_file):
    if not os.path.exists(local_file):
        os.system(f"curl -o {local_file} {ftp_url}")
        print("Download concluído.")

    with ZipFile(local_file, 'r') as zip_ref:
        zip_ref.extractall('tabela_unificada')
    print("Extração concluída.")

# Filtrar procedimentos de otorrino e cirurgias de cabeça e pescoço
def filter_procedures(file_path):
    df = pd.read_csv(file_path, delimiter=';', encoding='latin1')

    # Filtrando apenas os procedimentos cirúrgicos de otorrino e cabeça/pescoço
    filtro_grupo = df['Grupo'].str.contains('Procedimentos cirúrgicos', case=False, na=False)
    filtro_subgrupo = df['Subgrupo'].str.contains('vias aéreas superiores|cabeça e pescoço', case=False, na=False)

    procedimentos_filtrados = df[filtro_grupo & filtro_subgrupo]

    # Relacionar com CID-10
    cid_procedimentos = procedimentos_filtrados[['Código', 'Nome', 'CID Principal']]
    return cid_procedimentos

# Função principal
if __name__ == '__main__':
    download_and_extract(ftp_url, local_file)

    # Caminho do arquivo extraído
    arquivo_procedimentos = 'tabela_unificada/arquivo_procedimentos.csv'  # Altere conforme o nome correto do arquivo
    dados_filtrados = filter_procedures(arquivo_procedimentos)
    
    # Exibir os primeiros 10 resultados filtrados
    print(dados_filtrados.head(10))

    # Você pode salvar o resultado em um arquivo CSV, se necessário
    dados_filtrados.to_csv('procedimentos_filtrados_otorrino.csv', index=False)
