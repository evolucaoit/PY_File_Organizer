import os
import shutil

# Lista de extensões de arquivo a serem organizadas
extensions = ['.jpeg', '.jpg', '.png', '.pdf', '.mp4', '.mkv', '.exe', '.msi', '.rar', '.epub', '.zip', '.7z', 
              '.iso', '.webm', '.m4a', '.mp3', '.wmv', '.avi', '.txt', '.efu', '.torrent', '.xls', '.ods', 
              '.odt', '.doc', '.docx', '.py', '.html', '.md', '.json', '.yaml', '.csv']

# Pasta para possíveis duplicados
duplicados_folder = 'possiveis-duplicados-validar'

def organize_files():
    # Primeiro, organiza os arquivos normalmente
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_extension = os.path.splitext(file)[1]
            if file_extension in extensions:
                pasta_destino = file_extension[1:]  # Remove o ponto da extensão
                arquivo_destino = os.path.join(pasta_destino, file)
                
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                
                if not os.path.exists(arquivo_destino):  # Verifica se o arquivo já existe no destino
                    shutil.move(file, pasta_destino)
                    print(f"Arquivo {file} movido para a pasta {pasta_destino}")
                else:
                    print(f"Arquivo {file} já existe em {pasta_destino}. Ignorando.")

    # Verifica se existe algum arquivo não movido e organiza em 'possiveis-duplicados-validar'
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_extension = os.path.splitext(file)[1]
            if file_extension in extensions:
                duplicados_destino = os.path.join(duplicados_folder, file_extension[1:])
                
                if not os.path.exists(duplicados_destino):
                    os.makedirs(duplicados_destino)
                
                shutil.move(file, duplicados_destino)
                print(f"Arquivo {file} movido para a pasta {duplicados_destino}")

if __name__ == "__main__":
    organize_files()
