import whisper
import os

def transcrever_audio(caminho_audio):
    print("carregando modelo whisper...")
  
    try:
        
        caminho_audio = caminho_audio.encode('utf-8').decode('utf-8')  # força encoding correto
        model = whisper.load_model("base")
        print(f"transcrevendo audio: {caminho_audio}")
        resultado = model.transcribe(caminho_audio)
        texto = resultado['text']
    
        print("transcrição concluida!\n")
        print(texto)
    
        # Salvar a transcrição em um arquivo .txt
        nome_arquivo = os.path.splitext(os.path.basename(caminho_audio))[0] + "_transcricao.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
             f.write(texto)

        print(f"Transcrição salva em: {nome_arquivo}")

    except Exception as e:
       print("❌ Erro ao transcrever o áudio:", e)