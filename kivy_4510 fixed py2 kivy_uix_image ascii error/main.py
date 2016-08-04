# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
import image

class NotificationDemoApp(App):
    def build(self):
        sorc = "ØØØØØØØ example.jpg"
        img = image.Image(source=sorc)

        return img

if __name__ == '__main__':
    NotificationDemoApp().run()
