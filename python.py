from kivy.app import App
from kivy.uix.image import AsyncImage

class GifApp(App):
    def build(self):
        # Установка GIF-анимации с помощью AsyncImage
        gif_image = AsyncImage(source='Poluprised_zamok.gif')
        return gif_image

if __name__ == 'main':
    GifApp().run()