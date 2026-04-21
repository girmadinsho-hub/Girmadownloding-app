
from engine.downloader import Downloader

class App:

    def __init__(self):
        self.engine = Downloader()

    def run(self):

        print("===== GIRMA DOWNLOAD APP =====")
        print("1 Download Video")

        choice = input("Select: ")

        if choice == "1":
            url = input("Paste URL: ")
            self.engine.download_single(url)

if __name__ == "__main__":
    app = App()
    app.run()
