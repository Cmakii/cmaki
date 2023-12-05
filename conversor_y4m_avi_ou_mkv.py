import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

# O codec é rawvideo para não aplicar compressão
codec_video = '-c:v rawvideo'
pix_fmt = '-pix_fmt yuv420p'

caminho_origem = "/home/pc-einsten-luis/Downloads/Vídeos y4m"
caminho_destino = "/home/pc-einsten-luis/Downloads/Vídeos y4m/Conversões"

# Escolha entre .avi e .mkv
extensao_saida = input("Escolha a extensão de saída (.avi ou .mkv): ").lower()

# Verifica se o diretório de destino existe (se n existir vai criar)
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.y4m'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{nome_arquivo}.{extensao_saida}'

        try:
            comando = (
                f'{comando_ffmpeg} -i "{caminho_completo}" '
                f'{codec_video} {pix_fmt} "{arquivo_saida}"'
            )

            # Executa o comando e captura a saída
            os.system(comando)
        except Exception as e:
            print(f"Erro ao processar o arquivo {caminho_completo}: {str(e)}")

