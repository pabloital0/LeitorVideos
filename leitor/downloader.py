from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import re

def baixar_video(url):
    try:
        # Valida a URL básica do YouTube
        if not re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/', url):
            raise ValueError("URL inválida")

        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if stream is None:
            print("Nenhum stream progressivo MP4 disponível.")
            return None

        print(f"Baixando: {yt.title}")
        caminho = stream.download(output_path="videos")
        return caminho

    except VideoUnavailable:
        print("Vídeo indisponível.")
        return None
    except Exception as e:
        print("Erro ao tentar baixar o vídeo:", e)
        return None
