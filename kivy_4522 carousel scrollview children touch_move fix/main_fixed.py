# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from carousel_modified import Carousel
from kivy.uix.button import Button
from kivy.metrics import cm
        
class NotificationDemoApp(App):
    def build(self):
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=1, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        scroll.add_widget(grid)
        for r in range(0,50):
            bt = Button(text='Smooth '+str(r), size_hint_y=None, height=cm(2))
            grid.add_widget(bt)
        scroll2 = ScrollView()
        grid2 = GridLayout(cols=1, spacing=1, size_hint_y=None)
        grid2.bind(minimum_height=grid2.setter('height'))
        scroll2.add_widget(grid2)
        for r in range(50,100):
            bt = Button(text="Fast scrolling works"+str(r), size_hint_y=None, height=cm(2))
            grid2.add_widget(bt)

            
        carousel = Carousel(do_scroll_y=False)
        carousel.add_widget(scroll)
        carousel.add_widget(scroll2)
        return carousel

if __name__ == '__main__':
    NotificationDemoApp().run()
