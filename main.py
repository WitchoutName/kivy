import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import *


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,1,mode="rgba")

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos

    def on_touch_up(self, touch):
        self.btn.opacity = 1


class MyApp(App):
    def build(self):
        return Touch()


MyApp().run()
