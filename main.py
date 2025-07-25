import os
import pathlib
from leitor.downloader import baixar_video, baixar_audio
from transcrever import transcrever_audio
import whisper


def transcrever_audio(caminho_audio):
    caminho_audio = str(pathlib.Path(caminho_audio).resolve())

    print(f"transcrevendo audio: {caminho_audio}")

    if not os.path.isfile(caminho_audio):
        print(f"❌ Arquivo não encontrado: {caminho_audio}")
        return

    print("carregando modelo whisper...")
    model = whisper.load_model("base")
    
    try:
        result = model.transcribe(caminho_audio)
        texto = result['text']
        print("✅ Transcrição concluída:\n")
        print(texto[:1000])  # Exibe os primeiros 1000 caracteres
        print("Transcrição concluída!")

        # Salva a transcrição em um arquivo .txt com o mesmo nome
        nome_txt = os.path.splitext(caminho_audio)[0] + ".txt"
        with open(nome_txt, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"📝 Transcrição salva em: {nome_txt}")
    except Exception as e:
        print("❌ Erro ao transcrever o áudio:", e)

def main():
    escolha = input("Quer baixar vídeo (v) ou áudio (a)? ").strip().lower()
    url = input("Cole a URL do vídeo: ").strip()

    if escolha == "v":
        caminho = baixar_video(url)
        if caminho:
            print(f"Vídeo baixado em: {caminho}")
        else:
            print("❌ Falha no download do vídeo.")
    elif escolha == "a":
        caminho = baixar_audio(url)

        if caminho:
            # Corrige caminho absoluto e normaliza extensão
            caminho = pathlib.Path(caminho).resolve()
            caminho_str = str(caminho)

            # Corrige possível .mp3.mp3
            if caminho_str.endswith(".mp3.mp3"):
                novo_caminho = caminho_str.replace(".mp3.mp3", ".mp3")
                os.rename(caminho_str, novo_caminho)
                caminho_str = novo_caminho

            print(f"Áudio baixado em: {caminho_str}")
            transcrever_audio(caminho_str)
        else:
            print("❌ Falha no download do áudio.")
    else:
        print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
