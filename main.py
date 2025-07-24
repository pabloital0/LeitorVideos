from leitor.downloader import baixar_video

def main():
    url = input("cola a url do video para baixar")
    caminho = baixar_video(url)
    print(f"download concluido: {caminho}")

if __name__ == "__main__":
    main()