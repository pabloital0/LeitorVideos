import os

caminho = r"C:\Users\pablo\Desktop\projetos\LeitorVideos\audios\audio_baixado.mp3"

if os.path.isfile(caminho):
    print("✅ O arquivo existe!")
else:
    print("❌ Arquivo NÃO encontrado!")