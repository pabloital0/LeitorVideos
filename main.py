import yt_dlp
import os
from leitor.downloader import baixar_video, baixar_audio

def main():
    escolha = input("Quer baixar vídeo (v) ou áudio (a)? ").strip().lower()
    url = input("Cole a URL do vídeo: ").strip()

    if escolha == "v":
        caminho = baixar_video(url)
        if caminho:
            print(f"Vídeo baixado em: {caminho}")
        else:
            print("Falha no download do vídeo.")
    elif escolha == "a":
        caminho = baixar_audio(url)
        if caminho:
            print(f"Áudio baixado em: {caminho}")
        else:
            print("Falha no download do áudio.")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
