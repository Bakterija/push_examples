import kivy
from kivy.lib import osc
from kivy.clock import Clock, mainthread
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import cm
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty, DictProperty
from kivy.properties import ListProperty, NumericProperty

class ProjectsRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass

class Media_Button(RecycleDataViewBehavior, ButtonBehavior, StackLayout):
    index = None  # stores our index
    bg_default = ListProperty()
    bg_selected = ListProperty()
    text = StringProperty()
    bg_color = ListProperty()
    def __init__(self, **kwargs):
        super(Media_Button, self).__init__(**kwargs)
    
    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(Media_Button, self).refresh_view_attrs(rv, index, data)

    def apply_selection(self, rv, index, is_selected):
        if self.selected:
            self.bg_color = self.bg_selected
        else:
            self.bg_color = self.bg_default

    def press(self, *arg):
        self.gui.recolor(self.index)

class Media_Button2(Media_Button):
    def press(self, *arg):
        self.gui.recolor2(self.index)
        

class NotificationDemo(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayout, self).__init__( **kwargs)
        for x in range(0, 100):
            self.ids.rv.data.append({'text': 'TEXT '+str(x), 'gui': self, 'selected': False})
        for x in range(0, 100):
            self.ids.rv2.data.append({'text': 'TEXT '+str(x), 'gui': self, 'selected': False})
        for x in range(0, 100):
            self.ids.gridr.add_widget(Button(text='TEXT '+str(x),size_hint=(1,None), height=cm(1)))
        for x in range(0, 100):
            self.ids.gridr2.add_widget(Button(text='TEXT '+str(x),size_hint=(1,None), height=cm(1)))

    def recolor(self, index):
        for i,x in enumerate(self.ids.rv.data):
            self.ids.rv.data[i]['selected'] = False
        self.ids.rv.data[index]['selected'] = True
        self.ids.rv.refresh_from_data()

    def recolor2(self, index):
        for i,x in enumerate(self.ids.rv2.data):
            self.ids.rv2.data[i]['selected'] = False
        self.ids.rv2.data[index]['selected'] = True
        self.ids.rv2.refresh_from_data()



class NotificationDemoApp(App):
    def build(self):
        return NotificationDemo()

if __name__ == '__main__':
    NotificationDemoApp().run()
