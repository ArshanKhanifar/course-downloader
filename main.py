from youtube_downloader import YoutubeDownloader

if __name__ == '__main__':
    # playlist_url = input("Enter the YouTube playlist URL: ")
    playlist_url = "https://www.youtube.com/playlist?list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2"
    YoutubeDownloader(playlist_url).download_playlist()
