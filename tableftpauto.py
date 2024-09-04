import ftplib

def download_file_from_ftp():
    # Detalhes da conexão FTP
    ftp_server = "ftp2.datasus.gov.br"
    ftp_directory = "/pub/sistemas/tup/downloads/"
    file_name = "TabelaUnificada_202408_v2408091312.zip"
    local_file_path = "TabelaUnificada.zip"  # Caminho onde o arquivo será salvo

    try:
        # Conectando ao servidor FTP
        ftp = ftplib.FTP(ftp_server)
        ftp.login()  # Conectando anonimamente

        # Navegando até o diretório desejado
        ftp.cwd(ftp_directory)

        # Abrindo um arquivo local para gravar o download
        with open(local_file_path, "wb") as local_file:
            # Fazendo o download do arquivo
            ftp.retrbinary(f"RETR {file_name}", local_file.write)
        
        print(f"Download completo: {local_file_path}")

    except ftplib.all_errors as e:
        print(f"Erro de FTP: {e}")

    finally:
        # Fechando a conexão com o servidor FTP
        ftp.quit()

# Executa o download
download_file_from_ftp()
