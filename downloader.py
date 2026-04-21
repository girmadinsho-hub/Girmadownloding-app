
import yt_dlp
import os
from queue import Queue
import threading

class Downloader:

    def __init__(self):

        self.output = "downloads"
        os.makedirs(self.output, exist_ok=True)

        self.queue = Queue()
        self.running = False

    def download_single(self, url):

        options = {
            "outtmpl": self.output + "/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "concurrent_fragment_downloads": 8,
            "retries": 10,
            "continuedl": True,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("✅ Done:", url)

    def worker(self):

        while self.running:

            if not self.queue.empty():
                url = self.queue.get()
                print("📥 Downloading:", url)

                try:
                    self.download_single(url)
                except Exception as e:
                    print("❌ Error:", e)

    def start(self):

        self.running = True
        t = threading.Thread(target=self.worker)
        t.start()

        print("🚀 Queue system started")

    def add(self, url):

        self.queue.put(url)
        print("➕ Added:", url)

    def stop(self):

        self.running = False
        print("🛑 Queue stopped")
