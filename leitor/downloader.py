from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import re
import os
import yt_dlp
import unicodedata

def limpar_nome_arquivo(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    return "".join(c if c.isalnum() or c in " -_." else "_" for c in nome)


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
    
    
def baixar_audio(url):
    import os
    from yt_dlp import YoutubeDL

    pasta = "audios"
    nome_base = "audio_baixado"
    caminho_base = os.path.join(pasta, nome_base)
    nome_arquivo_final = f"{caminho_base}.mp3"

    os.makedirs(pasta, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': caminho_base + '.%(ext)s',  # salva como .webm
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:/ffmpeg/bin'  # caminho do ffmpeg
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Garante que retorna o nome final corretamente:
    return os.path.abspath(nome_arquivo_final)
    return str(Path(output_path).resolve())