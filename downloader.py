import yt_dlp as youtube_dl

# Função para baixar o áudio de uma URL do YouTube
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Seleciona o melhor formato de áudio disponível
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extrai apenas o áudio
            'preferredcodec': 'mp3',  # Converte o áudio para MP3
            'preferredquality': '192',  # Define a qualidade do áudio (192 kbps)
        }],
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
            print(f"Baixando áudio de: {yt_url}")
            download_audio(yt_url)

if __name__ == "__main__":
    main()
