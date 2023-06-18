import os

from pytube import Playlist, Stream
from pytube.exceptions import AgeRestrictedError


def sanitize(filename):
    return filename.replace("|", "-").replace(":", "-").replace(" ", "-")


class YoutubeDownloader(object):
    def __init__(self, playlist_url):
        self.playlist_url = playlist_url
        self.playlist = None

    def download_playlist(self):
        self._get_playlist()
        self._create_playlist_directory()
        self._download_videos()

    def _dir(self):
        return f"videos/{sanitize(self.playlist.title)}"

    def _create_playlist_directory(self):
        os.makedirs(self._dir(), exist_ok=True)

    def _get_playlist(self):
        self.playlist = Playlist(self.playlist_url)

    def _download_videos(self):
        for (i, video) in enumerate(self.playlist.videos, start=1):
            try:
                print(f"🔄 {i} starting download")
                self._download_video(i, video)
                print(f"✅ downloaded: {video.title}")
            except AgeRestrictedError:
                print(f"🔞 age restricted️: {video.watch_url}")

    def _download_video(self, i, video):
        video_title = video.title
        video_filename = f"{i}-{sanitize(video_title)}"
        stream: Stream = video.streams.get_highest_resolution()
        orig_progress = stream.on_progress

        def on_progress_callback(chunk, file_handler, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            progress = (bytes_downloaded / total_size) * 100
            print(f"⬇️: {video_title} - {progress:.2f}%")
            orig_progress(chunk, file_handler, bytes_remaining)

        stream.on_progress = on_progress_callback
        stream.download(output_path=self._dir(), filename=f"{video_filename}.mp4")

    def _get_video(self):
        return self.playlist.videos[0]
