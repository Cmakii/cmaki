import os
import fnmatch
import sys

#############################################################
#Ajuste a resolução e a taxa de quadros conforme necessário #
resolucao = '176x144'                                       #
taxa_quadros = 25                                           #
#############################################################

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v rawvideo' # O codec é rawvideo para não aplicar compressão
pix_fmt = '-pix_fmt yuv420p'

caminho_origem = "/home/pc-einsten-luis/Downloads/Vídeos yuv/176x144"
caminho_destino = "/home/pc-einsten-luis/Downloads/Vídeos yuv/176x144/Conversões"

extensao_saida = input("Escolha a extensão de saída (.avi ou .mkv): ").lower() # Escolhe entre .avi e .mkv

# Verifica se o diretório de destino existe (se n existir vai criar)
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.yuv'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{nome_arquivo}.{extensao_saida}'

        try:
            comando = (
                f'{comando_ffmpeg} -s {resolucao} -r {taxa_quadros} -i "{caminho_completo}" '
                f'{codec_video} {pix_fmt} "{arquivo_saida}"'
            )

            # Executa o comando e captura a saída
            os.system(comando)
        except Exception as e:
            print(f"Erro ao processar o arquivo {caminho_completo}: {str(e)}")

