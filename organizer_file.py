import os #interagir com o sistema operacional
import shutil #mover, copiar ou apagar arquivos 

# Caminho da pasta Downloads
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

for file in os.listdir(downloads):
    origem = os.path.join(downloads, file)

    # Ignora pastas
    if os.path.isdir(origem):
        continue

    # Pega a extensão do arquivo (ex: "pdf", "jpg")
    ext = os.path.splitext(file)[1][1:] or "outros"
    destino = os.path.join(downloads, ext)

    # Cria a pasta se não existir
    os.makedirs(destino, exist_ok=True)

    # Move o arquivo
    shutil.move(origem, os.path.join(destino, file))

print("✅ Downloads organizados com sucesso!")