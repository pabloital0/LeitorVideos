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
        
        # Coleta info primeiro (sem baixar ainda)
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            titulo = info.get("title", "audio").strip()
            # Remove caracteres problemáticos no nome do arquivo
            titulo_limpo = re.sub(r'[\\/*?:"<>|,]', "", titulo)
        
        nome_arquivo = f"{titulo_limpo}.mp3"
        caminho_saida = os.path.join("audios", nome_arquivo)
        
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
            ydl.download([url])

        print(f"Áudio salvo: {nome_arquivo}")
        return caminho_saida

    except Exception as e:
        print("Erro ao tentar baixar o áudio:", e)
        return None
