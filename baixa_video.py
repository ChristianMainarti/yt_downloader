import yt_dlp as youtube_dl

# Função para baixar o vídeo de uma URL do YouTube na melhor qualidade
def download_video(yt_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo e áudio disponíveis
        'merge_output_format': 'mp4',  # Mergia vídeo e áudio em MP4
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

# Função principal para ler o arquivo e processar cada link
def main():
    # Abra o arquivo txt com a lista de URLs
    with open("links.txt", "r") as file:
        yt_urls = [line.strip() for line in file.readlines()]
        
    # Faça o download de cada URL contida no arquivo
    for yt_url in yt_urls:
        if yt_url:  # Certifique-se de que a linha não está vazia
            print(f"Baixando vídeo de: {yt_url}")
            download_video(yt_url)

if __name__ == "__main__":
    main()
