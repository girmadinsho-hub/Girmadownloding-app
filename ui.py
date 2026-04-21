
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from engine.downloader import Downloader

class DownloaderUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.engine = Downloader()

        self.label = Label(text="Girma Downloader", size_hint=(1, 0.2))

        self.url_input = TextInput(
            hint_text="Paste video URL",
            size_hint=(1, 0.2)
        )

        self.button = Button(
            text="Download",
            size_hint=(1, 0.2)
        )

        self.status = Label(text="Ready", size_hint=(1, 0.2))

        self.button.bind(on_press=self.start_download)

        self.add_widget(self.label)
        self.add_widget(self.url_input)
        self.add_widget(self.button)
        self.add_widget(self.status)

    def start_download(self, instance):

        url = self.url_input.text

        self.status.text = "Downloading..."

        try:
            self.engine.download_single(url)
            self.status.text = "Download Complete"
        except Exception as e:
            self.status.text = f"Error: {e}"


class GirmaApp(App):

    def build(self):
        return DownloaderUI()

if __name__ == "__main__":
    GirmaApp().run()
