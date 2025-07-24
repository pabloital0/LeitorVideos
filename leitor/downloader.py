from pytube import YouTube
import os

def baixar_video(url: str, pasta_destino: str = "videos") -> str:
    """
    Baixa o vídeo do YouTube na pasta_destino e retorna o caminho do arquivo salvo.
    
    Args:
        url (str): URL do vídeo do YouTube.
        pasta_destino (str): Pasta onde o vídeo será salvo (default "videos").
    
    Returns:
        str: Caminho completo do arquivo baixado.
    """
    # Cria a pasta destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    yt = YouTube(url)

    # Seleciona o stream com melhor qualidade progressiva (vídeo + áudio)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    if not stream:
        raise Exception("Nenhum stream mp4 progressivo disponível para este vídeo.")

    print(f"Baixando: {yt.title}")
    caminho_arquivo = stream.download(output_path=pasta_destino)
    
    print(f"Vídeo salvo em: {caminho_arquivo}")
    return caminho_arquivo
