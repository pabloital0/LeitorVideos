import yt_dlp
import os

def baixar_video(url):
    try:
        os.makedirs("videos", exist_ok=True)

        ydl_opts = {
            'outtmpl': 'videos/%(title)s.%(ext)s',
            'format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Download concluído: {info['title']}")
            return info['title']
    except Exception as e:
        print("Erro ao tentar baixar o vídeo:", e)
        return None

def main():
    url = input("Cole a URL do vídeo para baixar: ").strip()
    titulo = baixar_video(url)
    if titulo:
        print("✅ Download concluído com sucesso!")
    else:
        print("❌ Falha no download.")

if __name__ == "__main__":
    main()
