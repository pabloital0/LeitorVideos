from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import re
import os
import yt_dlp

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
    try:
        # Cria pasta 'audios' se não existir
        os.makedirs("audios", exist_ok=True)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audios/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
            # Informar o caminho do FFmpeg aqui:
            'ffmpeg_location': r'C:\ffmpeg\bin',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Áudio salvo: audios/{info['title']}.mp3")
            return os.path.join("audios", info['title'] + ".mp3")

    except Exception as e:
        print("Erro ao tentar baixar o áudio:", e)
        return None
        
